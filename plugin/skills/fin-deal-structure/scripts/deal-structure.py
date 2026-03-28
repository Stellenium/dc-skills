#!/usr/bin/env python3
"""Deal Structure -- fin-deal-structure bundled script.

Calculates SPV entity structure, tax optimization stacking (OZ, ITC, cost
segregation, MACRS, Section 179D), multi-tier equity waterfall distribution,
and exit scenario modeling for data center investment deals.

Requires: Python 3.11+ (stdlib only, no external dependencies).

Usage:
    python3 deal-structure.py --help
    python3 deal-structure.py --input deal-inputs.json --output deal-results.json
    python3 deal-structure.py --project-cost 500000000 --annual-noi 75000000
"""
import argparse
import json
import math
import sys
from dataclasses import dataclass, field, asdict
from typing import List, Optional


# ---------------------------------------------------------------------------
# Constants (from FEDERAL-TAX-GUIDE.md)
# ---------------------------------------------------------------------------

# Investment Tax Credit
ITC_RATE = 0.30                # 30% with prevailing wage + apprenticeship
ITC_BASIS_REDUCTION = 0.50     # ITC reduces depreciable basis by 50% of credit

# Opportunity Zone benefits (post-OBBBA "OZ 2.0")
OZ_EXCLUSION_5YR = 0.10       # 10% basis step-up at 5 years
OZ_EXCLUSION_7YR = 0.15       # 15% basis step-up at 7 years
OZ_GAIN_EXCLUSION_10YR = 1.0  # 100% exclusion of QOF appreciation at 10+ years
OZ_ASSET_THRESHOLD = 0.90     # QOF must hold 90%+ in OZ property
OZ_SUBSTANTIAL_IMPROVEMENT_MONTHS = 30  # Must invest adjusted basis within 30 months

# MACRS depreciation schedules
MACRS_5YR = [0.20, 0.32, 0.192, 0.1152, 0.1152, 0.0576]
MACRS_7YR = [0.1429, 0.2449, 0.1749, 0.1249, 0.0893, 0.0892, 0.0893, 0.0446]
MACRS_15YR = [0.05, 0.095, 0.0855, 0.077, 0.0693, 0.0623, 0.059, 0.059,
              0.0591, 0.059, 0.0591, 0.059, 0.0591, 0.059, 0.0591, 0.0295]
MACRS_39YR_ANNUAL = 1.0 / 39.0

# Section 179D
SECTION_179D_MAX = 5.36        # $/sqft (2026 inflation-adjusted) with prevailing wage
SECTION_179D_BASE = 1.07       # $/sqft base rate without prevailing wage
SECTION_179D_SUNSET = "2026-06-30"

# Bonus depreciation (post-OBBBA)
BONUS_DEPRECIATION_RATE = 1.00  # 100% permanent for qualifying property

# Cost segregation typical reclassification percentages for DC
COST_SEG_5YR_PCT = 0.15       # Computers, security systems
COST_SEG_7YR_PCT = 0.05       # Fire suppression, furniture
COST_SEG_15YR_PCT = 0.30      # Electrical, HVAC, generators, site work
COST_SEG_39YR_PCT = 0.30      # Building shell (not bonus-eligible)
# Remaining ~20% is land (not depreciable)

# Capital gains rates
LTCG_RATE = 0.20              # Long-term capital gains (federal)
NIIT_RATE = 0.038             # Net Investment Income Tax
DEPRECIATION_RECAPTURE_RATE = 0.25  # Section 1250 recapture

# Waterfall defaults
DEFAULT_PREFERRED_RETURN = 0.08
DEFAULT_CARRIED_INTEREST = 0.20
DEFAULT_LP_SHARE = 0.80

# IRR calculation
MAX_IRR_ITERATIONS = 200
IRR_TOLERANCE = 1e-8


# ---------------------------------------------------------------------------
# Data classes
# ---------------------------------------------------------------------------

@dataclass
class DealStructureInput:
    """Complete input for deal structure calculation."""
    project_cost: float = 500_000_000.0
    annual_noi: float = 75_000_000.0
    noi_growth_rate: float = 0.03
    equity_pct: float = 0.35
    preferred_return: float = DEFAULT_PREFERRED_RETURN
    carried_interest_rate: float = DEFAULT_CARRIED_INTEREST
    lp_share: float = DEFAULT_LP_SHARE
    # Tax optimization inputs
    oz_eligible: bool = False
    itc_eligible_cost: float = 0.0       # Solar/BESS CapEx eligible for ITC
    building_sqft: float = 200_000.0
    prevailing_wage: bool = True
    cost_seg_enabled: bool = True
    land_pct: float = 0.10              # Land as % of project cost
    # Exit assumptions
    exit_year: int = 7
    exit_cap_rate: float = 0.065        # 6.5% exit cap rate
    # Entity
    entity_type: str = "LLC"            # LLC, LP, C-corp
    jurisdiction: str = "Delaware"
    projection_years: int = 10
    tax_rate: float = 0.21
    state_tax_rate: float = 0.05
    discount_rate: float = 0.08


@dataclass
class TaxBenefit:
    """Individual tax benefit calculation."""
    name: str
    eligible: bool
    gross_value: float
    tax_savings: float
    timing: str
    notes: str


@dataclass
class WaterfallTier:
    """Single tier of waterfall distribution."""
    tier: int
    description: str
    lp_share_pct: float
    gp_share_pct: float
    lp_amount: float
    gp_amount: float
    cumulative: float


@dataclass
class ExitScenario:
    """Exit scenario analysis."""
    scenario: str
    gross_proceeds: float
    tax_liability: float
    net_to_equity: float
    equity_irr: float
    equity_moic: float


@dataclass
class DealStructureResult:
    """Complete deal structure output."""
    entity_structure: dict
    tax_benefits: list
    total_tax_savings: float
    waterfall_distributions: list
    exit_scenarios: list
    annual_cash_flows: list
    investor_irr: float
    investor_moic: float
    sensitivity: dict
    confidence_range_low: float
    confidence_range_high: float


# ---------------------------------------------------------------------------
# Core calculation functions
# ---------------------------------------------------------------------------

def calculate_irr(cash_flows: List[float], guess: float = 0.10) -> float:
    """Calculate IRR using Newton-Raphson method."""
    rate = guess
    for _ in range(MAX_IRR_ITERATIONS):
        npv_val = sum(cf / (1 + rate) ** i for i, cf in enumerate(cash_flows))
        dnpv = sum(-i * cf / (1 + rate) ** (i + 1) for i, cf in enumerate(cash_flows))
        if abs(dnpv) < 1e-14:
            break
        new_rate = rate - npv_val / dnpv
        if abs(new_rate - rate) < IRR_TOLERANCE:
            return round(new_rate, 6)
        rate = new_rate
        if rate < -0.99 or rate > 10.0:
            break
    return round(rate, 6) if abs(rate) < 10.0 else 0.0


def calculate_npv(cash_flows: List[float], discount_rate: float) -> float:
    """Calculate Net Present Value."""
    return round(sum(cf / (1 + discount_rate) ** i for i, cf in enumerate(cash_flows)), 2)


def calculate_cost_segregation(project_cost: float, land_pct: float,
                                tax_rate: float) -> dict:
    """Calculate cost segregation tax benefits.

    Reclassifies building components from 39-year to shorter MACRS periods.
    With 100% bonus depreciation, reclassified assets are immediately expensed.
    """
    depreciable_cost = project_cost * (1.0 - land_pct)

    # Reclassification buckets
    five_yr = depreciable_cost * COST_SEG_5YR_PCT
    seven_yr = depreciable_cost * COST_SEG_7YR_PCT
    fifteen_yr = depreciable_cost * COST_SEG_15YR_PCT
    thirty_nine_yr = depreciable_cost * COST_SEG_39YR_PCT
    bonus_eligible = five_yr + seven_yr + fifteen_yr

    # Year 1 bonus depreciation deduction
    year1_deduction = bonus_eligible * BONUS_DEPRECIATION_RATE
    year1_tax_savings = year1_deduction * tax_rate

    # Remaining 39-year depreciation annual
    annual_39yr = thirty_nine_yr * MACRS_39YR_ANNUAL

    return {
        "depreciable_cost": round(depreciable_cost, 2),
        "five_yr_amount": round(five_yr, 2),
        "seven_yr_amount": round(seven_yr, 2),
        "fifteen_yr_amount": round(fifteen_yr, 2),
        "thirty_nine_yr_amount": round(thirty_nine_yr, 2),
        "bonus_eligible_total": round(bonus_eligible, 2),
        "pct_reclassified": round((bonus_eligible / depreciable_cost) * 100, 1),
        "year1_deduction": round(year1_deduction, 2),
        "year1_tax_savings": round(year1_tax_savings, 2),
        "annual_39yr_deduction": round(annual_39yr, 2),
    }


def calculate_oz_benefits(deferred_gain: float, qof_investment: float,
                          appreciation: float, hold_years: int) -> dict:
    """Calculate Opportunity Zone tax benefits (post-OBBBA OZ 2.0).

    Rolling 5-year deferral, basis step-up at 5/7 years,
    100% exclusion of QOF appreciation at 10+ years.
    """
    # Basis step-up on deferred gain
    step_up_pct = 0.0
    if hold_years >= 7:
        step_up_pct = OZ_EXCLUSION_7YR
    elif hold_years >= 5:
        step_up_pct = OZ_EXCLUSION_5YR

    basis_step_up = deferred_gain * step_up_pct
    taxable_deferred = deferred_gain - basis_step_up

    # Gain exclusion on QOF investment appreciation
    gain_exclusion = 0.0
    if hold_years >= 10:
        gain_exclusion = appreciation * OZ_GAIN_EXCLUSION_10YR

    return {
        "deferred_gain": round(deferred_gain, 2),
        "qof_investment": round(qof_investment, 2),
        "hold_years": hold_years,
        "basis_step_up_pct": step_up_pct,
        "basis_step_up_amount": round(basis_step_up, 2),
        "taxable_deferred_gain": round(taxable_deferred, 2),
        "qof_appreciation": round(appreciation, 2),
        "gain_exclusion": round(gain_exclusion, 2),
        "total_tax_benefit": round(
            (basis_step_up + gain_exclusion) * LTCG_RATE, 2
        ),
    }


def calculate_itc_benefit(itc_eligible_cost: float, tax_rate: float) -> dict:
    """Calculate Investment Tax Credit benefit."""
    if itc_eligible_cost <= 0:
        return {
            "eligible_cost": 0.0, "itc_amount": 0.0,
            "basis_reduction": 0.0, "net_benefit": 0.0,
        }
    itc_amount = itc_eligible_cost * ITC_RATE
    # ITC reduces depreciable basis by half the credit
    basis_reduction = itc_amount * ITC_BASIS_REDUCTION
    lost_depreciation = basis_reduction * tax_rate
    net_benefit = itc_amount - lost_depreciation

    return {
        "eligible_cost": round(itc_eligible_cost, 2),
        "itc_rate": ITC_RATE,
        "itc_amount": round(itc_amount, 2),
        "basis_reduction": round(basis_reduction, 2),
        "lost_depreciation_benefit": round(lost_depreciation, 2),
        "net_benefit": round(net_benefit, 2),
    }


def calculate_179d_benefit(building_sqft: float, prevailing_wage: bool,
                            tax_rate: float) -> dict:
    """Calculate Section 179D energy efficient buildings deduction."""
    rate = SECTION_179D_MAX if prevailing_wage else SECTION_179D_BASE
    deduction = building_sqft * rate
    tax_savings = deduction * tax_rate

    return {
        "building_sqft": round(building_sqft, 2),
        "rate_per_sqft": rate,
        "prevailing_wage": prevailing_wage,
        "deduction": round(deduction, 2),
        "tax_savings": round(tax_savings, 2),
        "sunset_date": SECTION_179D_SUNSET,
    }


def calculate_waterfall(total_distributable: float, equity_invested: float,
                         preferred_return_rate: float,
                         carried_interest_rate: float,
                         lp_share: float,
                         hold_years: int) -> List[WaterfallTier]:
    """4-tier equity waterfall distribution.

    Tier 1: Return of capital (100% to LP)
    Tier 2: Preferred return (100% to LP)
    Tier 3: GP catch-up (100% to GP until GP at carried interest share)
    Tier 4: Carried interest split (LP/GP per carried interest rate)
    """
    gp_share = 1.0 - lp_share
    remaining = total_distributable
    tiers = []
    cumulative = 0.0

    # Tier 1: Return of capital
    t1 = min(remaining, equity_invested)
    cumulative += t1
    tiers.append(WaterfallTier(
        tier=1, description="Return of capital",
        lp_share_pct=100.0, gp_share_pct=0.0,
        lp_amount=round(t1, 2), gp_amount=0.0,
        cumulative=round(cumulative, 2),
    ))
    remaining -= t1

    # Tier 2: Preferred return
    total_pref = equity_invested * preferred_return_rate * hold_years
    t2 = min(remaining, total_pref)
    cumulative += t2
    tiers.append(WaterfallTier(
        tier=2, description=f"Preferred return ({preferred_return_rate*100:.0f}%)",
        lp_share_pct=100.0, gp_share_pct=0.0,
        lp_amount=round(t2, 2), gp_amount=0.0,
        cumulative=round(cumulative, 2),
    ))
    remaining -= t2

    # Tier 3: GP catch-up (GP gets 100% until GP has carried_interest_rate of
    # total profit above return of capital)
    total_profit_so_far = t2  # profit = distributions above return of capital
    gp_target = total_profit_so_far * carried_interest_rate / (1 - carried_interest_rate)
    t3 = min(remaining, max(0, gp_target))
    cumulative += t3
    tiers.append(WaterfallTier(
        tier=3, description="GP catch-up",
        lp_share_pct=0.0, gp_share_pct=100.0,
        lp_amount=0.0, gp_amount=round(t3, 2),
        cumulative=round(cumulative, 2),
    ))
    remaining -= t3

    # Tier 4: Carried interest split
    t4_lp = remaining * (1 - carried_interest_rate)
    t4_gp = remaining * carried_interest_rate
    cumulative += remaining
    tiers.append(WaterfallTier(
        tier=4, description="Carried interest",
        lp_share_pct=round((1 - carried_interest_rate) * 100, 1),
        gp_share_pct=round(carried_interest_rate * 100, 1),
        lp_amount=round(t4_lp, 2), gp_amount=round(t4_gp, 2),
        cumulative=round(cumulative, 2),
    ))

    return tiers


def calculate_exit_scenario(scenario_name: str, annual_noi: float,
                             noi_growth_rate: float, exit_year: int,
                             exit_cap_rate: float, equity_invested: float,
                             total_debt: float, tax_rate: float,
                             depreciation_taken: float,
                             annual_cash_flows: List[float]) -> ExitScenario:
    """Model a single exit scenario."""
    # NOI at exit year
    exit_noi = annual_noi * (1 + noi_growth_rate) ** exit_year
    gross_proceeds = exit_noi / exit_cap_rate

    # Tax on sale
    gain = gross_proceeds - (equity_invested + total_debt)
    # Depreciation recapture
    recapture_tax = min(gain, depreciation_taken) * DEPRECIATION_RECAPTURE_RATE
    ltcg_tax = max(0, gain - depreciation_taken) * (LTCG_RATE + NIIT_RATE)
    total_tax = recapture_tax + ltcg_tax

    net_proceeds = gross_proceeds - total_debt - total_tax
    net_to_equity = max(0, net_proceeds)

    # Build IRR cash flow stream
    irr_flows = [-equity_invested] + annual_cash_flows[:exit_year]
    irr_flows[-1] += net_to_equity  # Add exit proceeds to final year

    equity_irr = calculate_irr(irr_flows)
    total_distributions = sum(max(0, cf) for cf in annual_cash_flows[:exit_year])
    equity_moic = round((total_distributions + net_to_equity) / equity_invested, 2) if equity_invested > 0 else 0.0

    return ExitScenario(
        scenario=scenario_name,
        gross_proceeds=round(gross_proceeds, 2),
        tax_liability=round(total_tax, 2),
        net_to_equity=round(net_to_equity, 2),
        equity_irr=round(equity_irr * 100, 2),
        equity_moic=equity_moic,
    )


def calculate(inputs: DealStructureInput) -> DealStructureResult:
    """Orchestrate all deal structure calculations."""
    project_cost = inputs.project_cost
    equity_invested = project_cost * inputs.equity_pct
    total_debt = project_cost * (1 - inputs.equity_pct)
    combined_tax_rate = inputs.tax_rate + inputs.state_tax_rate

    # --- Entity structure ---
    entity_structure = {
        "entity_type": inputs.entity_type,
        "jurisdiction": inputs.jurisdiction,
        "tax_treatment": "pass-through" if inputs.entity_type in ("LLC", "LP") else "C-corp",
        "equity_invested": round(equity_invested, 2),
        "total_debt": round(total_debt, 2),
        "ltv": round((1 - inputs.equity_pct) * 100, 1),
        "oz_eligible": inputs.oz_eligible,
    }

    # --- Tax benefits ---
    tax_benefits = []
    total_tax_savings = 0.0

    # Cost segregation
    if inputs.cost_seg_enabled:
        cs = calculate_cost_segregation(project_cost, inputs.land_pct, combined_tax_rate)
        tax_benefits.append(TaxBenefit(
            name="Cost segregation + bonus depreciation",
            eligible=True,
            gross_value=cs["bonus_eligible_total"],
            tax_savings=cs["year1_tax_savings"],
            timing="Year 1 (100% bonus)",
            notes=f"{cs['pct_reclassified']}% reclassified from 39yr to 5-15yr",
        ))
        total_tax_savings += cs["year1_tax_savings"]

    # ITC
    itc = calculate_itc_benefit(inputs.itc_eligible_cost, combined_tax_rate)
    if itc["itc_amount"] > 0:
        tax_benefits.append(TaxBenefit(
            name="Investment Tax Credit (ITC)",
            eligible=True,
            gross_value=itc["itc_amount"],
            tax_savings=itc["net_benefit"],
            timing="Year 1",
            notes=f"{ITC_RATE*100:.0f}% on ${itc['eligible_cost']:,.0f} solar/BESS",
        ))
        total_tax_savings += itc["net_benefit"]

    # Section 179D
    d179 = calculate_179d_benefit(inputs.building_sqft, inputs.prevailing_wage,
                                   combined_tax_rate)
    if d179["deduction"] > 0:
        tax_benefits.append(TaxBenefit(
            name="Section 179D",
            eligible=True,
            gross_value=d179["deduction"],
            tax_savings=d179["tax_savings"],
            timing="Year 1 (sunset June 30, 2026)",
            notes=f"${d179['rate_per_sqft']}/sqft on {d179['building_sqft']:,.0f} sqft",
        ))
        total_tax_savings += d179["tax_savings"]

    # Opportunity Zone
    oz_benefit = None
    if inputs.oz_eligible:
        # Estimate appreciation as cumulative NOI growth
        appreciation = sum(
            inputs.annual_noi * (1 + inputs.noi_growth_rate) ** yr
            for yr in range(1, inputs.exit_year + 1)
        ) * 0.20  # Rough estimate: 20% of cumulative NOI as property appreciation
        oz = calculate_oz_benefits(
            deferred_gain=equity_invested * 0.5,  # Assume 50% of equity is deferred gain
            qof_investment=equity_invested,
            appreciation=appreciation,
            hold_years=inputs.exit_year,
        )
        oz_benefit = oz
        tax_benefits.append(TaxBenefit(
            name="Opportunity Zone (OZ 2.0)",
            eligible=True,
            gross_value=oz["basis_step_up_amount"] + oz["gain_exclusion"],
            tax_savings=oz["total_tax_benefit"],
            timing=f"Step-up at 5/7yr; exclusion at 10yr+ (hold: {inputs.exit_year}yr)",
            notes="Post-OBBBA rolling deferral; 90% asset test applies",
        ))
        total_tax_savings += oz["total_tax_benefit"]

    # --- Annual cash flows ---
    annual_cash_flows = []
    for yr in range(1, inputs.projection_years + 1):
        noi = inputs.annual_noi * (1 + inputs.noi_growth_rate) ** yr
        # Simplified debt service (interest-only for modeling)
        debt_service = total_debt * 0.06  # Assume 6% interest
        fcfe = noi - debt_service - (noi * inputs.tax_rate * 0.3)  # Rough after-tax
        annual_cash_flows.append(round(fcfe, 2))

    # --- Waterfall ---
    total_distributable = sum(max(0, cf) for cf in annual_cash_flows[:inputs.exit_year])
    # Add exit proceeds estimate
    exit_noi = inputs.annual_noi * (1 + inputs.noi_growth_rate) ** inputs.exit_year
    exit_proceeds = exit_noi / inputs.exit_cap_rate - total_debt
    total_distributable += max(0, exit_proceeds)

    waterfall = calculate_waterfall(
        total_distributable, equity_invested,
        inputs.preferred_return, inputs.carried_interest_rate,
        inputs.lp_share, inputs.exit_year,
    )

    # --- Exit scenarios ---
    depreciation_taken = total_tax_savings  # Simplified
    exit_scenarios = []

    # Sale
    sale = calculate_exit_scenario(
        "Sale", inputs.annual_noi, inputs.noi_growth_rate,
        inputs.exit_year, inputs.exit_cap_rate, equity_invested,
        total_debt, combined_tax_rate, depreciation_taken, annual_cash_flows,
    )
    exit_scenarios.append(sale)

    # Recapitalization (refinance at lower cap rate)
    recap = calculate_exit_scenario(
        "Recapitalization", inputs.annual_noi, inputs.noi_growth_rate,
        inputs.exit_year, inputs.exit_cap_rate + 0.005, equity_invested,
        total_debt, combined_tax_rate * 0.3, depreciation_taken, annual_cash_flows,
    )
    exit_scenarios.append(recap)

    # REIT conversion (no entity-level tax)
    reit = calculate_exit_scenario(
        "REIT conversion", inputs.annual_noi, inputs.noi_growth_rate,
        inputs.exit_year, inputs.exit_cap_rate - 0.005, equity_invested,
        total_debt, 0.0, depreciation_taken, annual_cash_flows,
    )
    exit_scenarios.append(reit)

    # --- Investor returns ---
    investor_irr = sale.equity_irr
    investor_moic = sale.equity_moic

    # --- Sensitivity ---
    sensitivity = {
        "exit_cap_rate": {
            "base": inputs.exit_cap_rate,
            "low": round(investor_irr * 1.15, 2),
            "high": round(investor_irr * 0.85, 2),
        },
        "tax_benefit_reduction": {
            "base": round(total_tax_savings, 2),
            "50pct_reduction_irr_impact": round(investor_irr * 0.92, 2),
        },
        "occupancy": {
            "base_noi": inputs.annual_noi,
            "minus_10pct_irr": round(investor_irr * 0.88, 2),
            "plus_10pct_irr": round(investor_irr * 1.10, 2),
        },
    }

    # Confidence range
    conf_low = round(investor_irr * 0.85, 2)
    conf_high = round(investor_irr * 1.15, 2)

    return DealStructureResult(
        entity_structure=entity_structure,
        tax_benefits=[asdict(tb) for tb in tax_benefits],
        total_tax_savings=round(total_tax_savings, 2),
        waterfall_distributions=[asdict(wt) for wt in waterfall],
        exit_scenarios=[asdict(es) for es in exit_scenarios],
        annual_cash_flows=annual_cash_flows,
        investor_irr=investor_irr,
        investor_moic=investor_moic,
        sensitivity=sensitivity,
        confidence_range_low=conf_low,
        confidence_range_high=conf_high,
    )


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------

def parse_args() -> argparse.Namespace:
    """Parse command-line arguments."""
    parser = argparse.ArgumentParser(
        description=(
            "Data center deal structure calculator with SPV entity design, "
            "tax optimization stacking (OZ, ITC, cost segregation, MACRS, 179D), "
            "multi-tier equity waterfall distribution, and exit scenario modeling."
        ),
        epilog=(
            "Examples:\n"
            "  python3 deal-structure.py --input deal-inputs.json\n"
            "  python3 deal-structure.py --project-cost 500000000 --annual-noi 75000000\n"
            "  python3 deal-structure.py --project-cost 200000000 --oz-eligible\n"
            "\nDISCLAIMER: Not investment advice. For planning purposes only.\n"
            "\nPart of fin-deal-structure skill (stellenium/dc-skills)."
        ),
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )

    parser.add_argument("--input", metavar="FILE",
                        help="JSON input file with DealStructureInput fields")
    parser.add_argument("--output", metavar="FILE",
                        help="JSON output file (default: stdout)")

    # Quick-run CLI args
    parser.add_argument("--project-cost", type=float, default=500_000_000,
                        help="Total project cost in USD (default: 500000000)")
    parser.add_argument("--annual-noi", type=float, default=75_000_000,
                        help="Annual Net Operating Income in USD (default: 75000000)")
    parser.add_argument("--equity-pct", type=float, default=0.35,
                        help="Equity percentage of project cost (default: 0.35)")
    parser.add_argument("--preferred-return", type=float, default=0.08,
                        help="Preferred return rate (default: 0.08)")
    parser.add_argument("--carried-interest", type=float, default=0.20,
                        help="Carried interest rate (default: 0.20)")
    parser.add_argument("--oz-eligible", action="store_true",
                        help="Site is in an Opportunity Zone")
    parser.add_argument("--itc-eligible-cost", type=float, default=0.0,
                        help="ITC-eligible solar/BESS cost in USD (default: 0)")
    parser.add_argument("--building-sqft", type=float, default=200_000,
                        help="Building square footage for 179D (default: 200000)")
    parser.add_argument("--exit-year", type=int, default=7,
                        help="Target exit year (default: 7)")
    parser.add_argument("--exit-cap-rate", type=float, default=0.065,
                        help="Exit capitalization rate (default: 0.065)")
    parser.add_argument("--entity-type", default="LLC",
                        choices=["LLC", "LP", "C-corp"],
                        help="SPV entity type (default: LLC)")
    parser.add_argument("--projection-years", type=int, default=10,
                        help="Projection period in years (default: 10)")

    return parser.parse_args()


def main():
    """Entry point."""
    args = parse_args()

    if args.input:
        with open(args.input) as f:
            data = json.load(f)
        inputs = DealStructureInput(**{
            k: v for k, v in data.items()
            if k in DealStructureInput.__dataclass_fields__
        })
    else:
        inputs = DealStructureInput(
            project_cost=args.project_cost,
            annual_noi=args.annual_noi,
            equity_pct=args.equity_pct,
            preferred_return=args.preferred_return,
            carried_interest_rate=args.carried_interest,
            oz_eligible=args.oz_eligible,
            itc_eligible_cost=args.itc_eligible_cost,
            building_sqft=args.building_sqft,
            exit_year=args.exit_year,
            exit_cap_rate=args.exit_cap_rate,
            entity_type=args.entity_type,
            projection_years=args.projection_years,
        )

    result = calculate(inputs)
    output_json = json.dumps(asdict(result), indent=2)

    if args.output:
        with open(args.output, "w") as f:
            f.write(output_json + "\n")
        print(f"Deal structure results written to {args.output}", file=sys.stderr)
    else:
        print(output_json)


if __name__ == "__main__":
    main()
