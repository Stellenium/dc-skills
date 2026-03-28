#!/usr/bin/env python3
"""Waterfall Model -- fin-project-model bundled script.

Calculates IRR, NPV, MOIC, and multi-tranche equity waterfall distribution
for data center project finance. Supports senior debt, mezzanine, and equity
tranches with configurable hurdle rates, catch-up, and carried interest.

Requires: Python 3.11+ (stdlib only, no external dependencies).

Usage:
    python3 waterfall-model.py --help
    python3 waterfall-model.py --input model-inputs.json --output model-results.json
    python3 waterfall-model.py --capex 110000000 --revenue 30000000 --projection-years 10
"""
import argparse
import json
import math
import sys
from dataclasses import dataclass, field, asdict
from typing import List, Optional


# ---------------------------------------------------------------------------
# Constants
# ---------------------------------------------------------------------------

# MACRS 5-year depreciation schedule (year 1-6 percentages)
MACRS_5YR = [0.20, 0.32, 0.192, 0.1152, 0.1152, 0.0576]
# MACRS 7-year depreciation schedule (year 1-8)
MACRS_7YR = [0.1429, 0.2449, 0.1749, 0.1249, 0.0893, 0.0892, 0.0893, 0.0446]

MAX_IRR_ITERATIONS = 200
IRR_TOLERANCE = 1e-8


# ---------------------------------------------------------------------------
# Data classes
# ---------------------------------------------------------------------------

@dataclass
class DebtTranche:
    """A single debt tranche (senior or mezzanine)."""
    name: str = "Senior"
    amount: float = 0.0
    interest_rate: float = 0.06
    tenor_years: int = 10
    amortization_years: int = 10    # for amortization schedule
    interest_only_years: int = 0    # IO period before amortization starts


@dataclass
class FinancialModelInput:
    """Complete input for a financial model calculation."""
    project_capacity_mw: float = 10.0
    capex_total: float = 110_000_000.0
    revenue_year1: float = 0.0              # annual revenue (or computed below)
    revenue_per_kw_month: float = 150.0     # $/kW/month (colo pricing)
    occupancy_schedule: list = field(default_factory=lambda: [
        0.30, 0.50, 0.70, 0.85, 0.90, 0.95, 0.95, 0.95, 0.95, 0.95
    ])
    annual_opex_year1: float = 0.0          # if 0, computed as % of revenue
    opex_pct_of_revenue: float = 0.55       # 55% OpEx ratio if opex not given
    opex_escalation_rate: float = 0.03      # 3% annual escalation
    revenue_escalation_rate: float = 0.025  # 2.5% annual revenue escalation
    projection_years: int = 10
    # Debt
    debt_tranches: list = field(default_factory=list)  # list of DebtTranche dicts
    # Equity
    equity_amount: float = 0.0              # if 0, computed as capex - debt
    preferred_return_rate: float = 0.10     # 10% preferred return (hurdle)
    catch_up_rate: float = 1.00             # GP gets 100% until caught up
    carried_interest_rate: float = 0.20     # 20% GP carry above hurdle
    lp_share: float = 0.80                  # 80% LP / 20% GP split
    # Tax
    discount_rate: float = 0.08
    tax_rate: float = 0.21
    itc_rate: float = 0.0                   # ITC as % of qualifying CapEx
    itc_qualifying_capex: float = 0.0
    macrs_schedule: str = "5yr"             # "5yr" or "7yr"
    depreciable_pct: float = 0.50           # % of CapEx eligible for accel depreciation
    bonus_depreciation_pct: float = 1.00    # 100% post-OBBBA
    escalation_rate: float = 0.03


@dataclass
class AnnualCashFlow:
    """Single year cash flow detail."""
    year: int; revenue: float; opex: float; ebitda: float
    debt_service: float; interest: float; principal: float
    depreciation_benefit: float; taxes: float; fcfe: float
    dscr: float; occupancy: float


@dataclass
class WaterfallDistribution:
    """Equity waterfall distribution for a single year."""
    year: int; available_cash: float; preferred_return: float; catch_up: float
    carried_interest_lp: float; carried_interest_gp: float
    total_lp: float; total_gp: float


@dataclass
class FinancialModelResult:
    """Complete financial model result."""
    annual_cash_flows: list             # list of AnnualCashFlow dicts
    project_irr: float
    equity_irr: float
    npv: float
    moic: float
    dscr_min: float
    dscr_avg: float
    total_capex: float
    total_equity: float
    total_debt: float
    total_revenue: float
    total_distributions: float
    equity_waterfall: list              # list of WaterfallDistribution dicts
    sensitivity: dict
    tax_benefits: dict
    confidence_range_low: float
    confidence_range_high: float


# ---------------------------------------------------------------------------
# Core calculation functions
# ---------------------------------------------------------------------------

def calculate_irr(cash_flows: List[float], guess: float = 0.10) -> float:
    """Calculate IRR using Newton-Raphson method on a cash flow stream.

    Args:
        cash_flows: List of cash flows, starting with initial investment (negative).
        guess: Initial guess for IRR.

    Returns:
        IRR as a decimal (e.g., 0.12 for 12%). Returns 0.0 if no convergence.
    """
    rate = guess
    for _ in range(MAX_IRR_ITERATIONS):
        npv_val = sum(cf / (1 + rate) ** i for i, cf in enumerate(cash_flows))
        # Derivative of NPV with respect to rate
        dnpv = sum(
            -i * cf / (1 + rate) ** (i + 1)
            for i, cf in enumerate(cash_flows)
        )
        if abs(dnpv) < 1e-14:
            break
        new_rate = rate - npv_val / dnpv
        if abs(new_rate - rate) < IRR_TOLERANCE:
            return round(new_rate, 6)
        rate = new_rate
        # Guard against divergence
        if rate < -0.99 or rate > 10.0:
            break
    return round(rate, 6) if abs(rate) < 10.0 else 0.0


def calculate_npv(cash_flows: List[float], discount_rate: float) -> float:
    """Calculate Net Present Value of a cash flow stream."""
    return round(
        sum(cf / (1 + discount_rate) ** i for i, cf in enumerate(cash_flows)),
        2,
    )


def calculate_moic(total_distributions: float, total_invested: float) -> float:
    """Multiple on Invested Capital: total out / total in."""
    if total_invested <= 0:
        return 0.0
    return round(total_distributions / total_invested, 2)


def calculate_debt_service(tranche: DebtTranche, year: int) -> tuple:
    """Return (interest, principal, total_debt_service) for one year."""
    if tranche.amount <= 0 or year > tranche.tenor_years:
        return 0.0, 0.0, 0.0
    if year <= tranche.interest_only_years:
        i = round(tranche.amount * tranche.interest_rate, 2)
        return i, 0.0, i
    amort_yrs = max(1, tranche.amortization_years - tranche.interest_only_years)
    principal = tranche.amount / amort_yrs
    paid = year - tranche.interest_only_years - 1
    balance = max(0, tranche.amount - principal * paid)
    interest = balance * tranche.interest_rate
    return round(interest, 2), round(principal, 2), round(interest + principal, 2)


def calculate_depreciation_benefit(capex: float, depreciable_pct: float,
                                   macrs_schedule: str, bonus_pct: float,
                                   tax_rate: float, year: int) -> float:
    """Tax benefit from MACRS/bonus depreciation in a given year."""
    dep_amt = capex * depreciable_pct
    if bonus_pct >= 1.0:
        return round(dep_amt * tax_rate, 2) if year == 1 else 0.0
    schedule = MACRS_5YR if macrs_schedule == "5yr" else MACRS_7YR
    idx = year - 1
    if idx >= len(schedule):
        return 0.0
    deduction = dep_amt * (1 - bonus_pct) * schedule[idx]
    if year == 1:
        deduction += dep_amt * bonus_pct
    return round(deduction * tax_rate, 2)


def run_waterfall(annual_fcfe: List[float], equity_invested: float,
                  preferred_return_rate: float, catch_up_rate: float,
                  carried_interest_rate: float, lp_share: float,
                  ) -> List[WaterfallDistribution]:
    """Equity waterfall: return of capital -> pref return -> catch-up -> carry."""
    gp_share = 1 - lp_share
    capital_returned = pref_paid = cumulative_pref_owed = gp_catch_up_paid = 0.0
    distributions = []
    for i, fcfe in enumerate(annual_fcfe):
        available = max(0, fcfe)
        remaining = available
        pref_return = catch_up = carry_lp = carry_gp = 0.0
        cumulative_pref_owed += equity_invested * preferred_return_rate
        # Tier 1: Return of capital
        if capital_returned < equity_invested and remaining > 0:
            t1 = min(remaining, equity_invested - capital_returned)
            capital_returned += t1; remaining -= t1; carry_lp += t1
        # Tier 2: Preferred return
        pref_deficit = cumulative_pref_owed - pref_paid
        if pref_deficit > 0 and remaining > 0:
            t2 = min(remaining, pref_deficit)
            pref_return = t2; pref_paid += t2; remaining -= t2; carry_lp += t2
        # Tier 3: GP catch-up
        if remaining > 0 and catch_up_rate > 0:
            gp_target = (capital_returned + pref_paid + gp_catch_up_paid) * gp_share
            gp_deficit = gp_target - gp_catch_up_paid
            if gp_deficit > 0:
                t3 = min(remaining, gp_deficit)
                catch_up = t3; gp_catch_up_paid += t3; remaining -= t3
        # Tier 4: Carried interest split
        if remaining > 0:
            carry_lp += remaining * lp_share
            carry_gp = catch_up + remaining * gp_share
        else:
            carry_gp = catch_up
        distributions.append(WaterfallDistribution(
            year=i + 1, available_cash=round(available, 2),
            preferred_return=round(pref_return, 2), catch_up=round(catch_up, 2),
            carried_interest_lp=round(carry_lp, 2), carried_interest_gp=round(carry_gp, 2),
            total_lp=round(carry_lp, 2), total_gp=round(carry_gp, 2)))
    return distributions


def _clone_inputs(inputs: FinancialModelInput) -> FinancialModelInput:
    """Create a shallow copy of inputs for sensitivity variation."""
    return FinancialModelInput(**{
        k: v for k, v in asdict(inputs).items()
        if k in FinancialModelInput.__dataclass_fields__
    })


def run_sensitivity(inputs: FinancialModelInput, variable: str,
                    range_pct: float = 0.20) -> dict:
    """Vary one parameter and compute IRR impact."""
    base_irr = build_financial_model(inputs).equity_irr
    lo, hi = _clone_inputs(inputs), _clone_inputs(inputs)
    if variable == "occupancy":
        lo.occupancy_schedule = [max(0, o - range_pct) for o in inputs.occupancy_schedule]
        hi.occupancy_schedule = [min(1.0, o + range_pct) for o in inputs.occupancy_schedule]
    elif variable == "power_cost":
        lo.opex_pct_of_revenue = inputs.opex_pct_of_revenue * (1 - range_pct)
        hi.opex_pct_of_revenue = inputs.opex_pct_of_revenue * (1 + range_pct)
    elif variable == "construction_cost":
        lo.capex_total = inputs.capex_total * (1 - range_pct)
        hi.capex_total = inputs.capex_total * (1 + range_pct)
    elif variable == "interest_rate":
        for dt in lo.debt_tranches:
            if isinstance(dt, dict):
                dt["interest_rate"] = dt.get("interest_rate", 0.06) - 0.02
        for dt in hi.debt_tranches:
            if isinstance(dt, dict):
                dt["interest_rate"] = dt.get("interest_rate", 0.06) + 0.02
    lo_irr = build_financial_model(lo).equity_irr
    hi_irr = build_financial_model(hi).equity_irr
    return {"variable": variable, "base_irr": base_irr, "low_irr": lo_irr,
            "high_irr": hi_irr,
            "irr_impact": round(max(abs(lo_irr - base_irr), abs(hi_irr - base_irr)) * 100, 2)}


def build_financial_model(inputs: FinancialModelInput) -> FinancialModelResult:
    """Build the complete financial model."""
    # Parse debt tranches
    debt_tranches = []
    total_debt = 0.0
    for dt in inputs.debt_tranches:
        if isinstance(dt, dict):
            tranche = DebtTranche(**{
                k: v for k, v in dt.items()
                if k in DebtTranche.__dataclass_fields__
            })
        else:
            tranche = dt
        debt_tranches.append(tranche)
        total_debt += tranche.amount

    # Equity amount
    equity = inputs.equity_amount
    if equity <= 0:
        equity = inputs.capex_total - total_debt
        equity = max(0, equity)

    # Revenue calculation
    capacity_kw = inputs.project_capacity_mw * 1000

    # Extend occupancy schedule to cover full projection period
    occ = list(inputs.occupancy_schedule)
    while len(occ) < inputs.projection_years:
        occ.append(occ[-1] if occ else 0.90)

    # Build year-by-year cash flows
    cash_flows = []
    project_cash_flows = [-inputs.capex_total]  # year 0 for project IRR
    equity_cash_flows = [-equity]                 # year 0 for equity IRR

    itc_benefit = 0.0
    if inputs.itc_rate > 0 and inputs.itc_qualifying_capex > 0:
        itc_benefit = inputs.itc_qualifying_capex * inputs.itc_rate

    total_revenue = 0.0
    total_distributions = 0.0
    dscr_values = []

    for yr in range(1, inputs.projection_years + 1):
        occupancy = occ[yr - 1] if yr - 1 < len(occ) else occ[-1]
        rev_escalation = (1 + inputs.revenue_escalation_rate) ** (yr - 1)
        opex_escalation = (1 + inputs.opex_escalation_rate) ** (yr - 1)

        # Revenue
        if inputs.revenue_year1 > 0:
            revenue = inputs.revenue_year1 * occupancy * rev_escalation
        else:
            revenue = (
                capacity_kw * inputs.revenue_per_kw_month * 12
                * occupancy * rev_escalation
            )

        # OpEx
        if inputs.annual_opex_year1 > 0:
            opex = inputs.annual_opex_year1 * opex_escalation
        else:
            opex = revenue * inputs.opex_pct_of_revenue

        ebitda = revenue - opex

        # Debt service (sum across tranches)
        total_interest = 0.0
        total_principal = 0.0
        total_ds = 0.0
        for tranche in debt_tranches:
            interest, principal, ds = calculate_debt_service(tranche, yr)
            total_interest += interest
            total_principal += principal
            total_ds += ds

        # Depreciation tax benefit
        dep_benefit = calculate_depreciation_benefit(
            inputs.capex_total,
            inputs.depreciable_pct,
            inputs.macrs_schedule,
            inputs.bonus_depreciation_pct,
            inputs.tax_rate,
            yr,
        )

        # ITC in year 1
        if yr == 1:
            dep_benefit += itc_benefit

        # Taxes (simplified: on EBITDA - interest - depreciation)
        taxable = ebitda - total_interest - dep_benefit
        taxes = max(0, taxable * inputs.tax_rate) if taxable > 0 else 0.0

        # Free cash flow to equity
        fcfe = ebitda - total_ds - taxes + dep_benefit

        # DSCR
        dscr = ebitda / total_ds if total_ds > 0 else float("inf")
        if dscr != float("inf"):
            dscr_values.append(dscr)

        total_revenue += revenue
        total_distributions += max(0, fcfe)

        cash_flows.append(AnnualCashFlow(
            year=yr,
            revenue=round(revenue, 2),
            opex=round(opex, 2),
            ebitda=round(ebitda, 2),
            debt_service=round(total_ds, 2),
            interest=round(total_interest, 2),
            principal=round(total_principal, 2),
            depreciation_benefit=round(dep_benefit, 2),
            taxes=round(taxes, 2),
            fcfe=round(fcfe, 2),
            dscr=round(dscr, 4) if dscr != float("inf") else 0.0,
            occupancy=round(occupancy, 3),
        ))

        project_cash_flows.append(ebitda - taxes)
        equity_cash_flows.append(fcfe)

    # IRR calculations
    project_irr = calculate_irr(project_cash_flows)
    equity_irr = calculate_irr(equity_cash_flows)

    # NPV
    npv = calculate_npv(equity_cash_flows, inputs.discount_rate)

    # MOIC
    moic = calculate_moic(total_distributions, equity)

    # DSCR stats
    dscr_min = round(min(dscr_values), 2) if dscr_values else 0.0
    dscr_avg = round(sum(dscr_values) / len(dscr_values), 2) if dscr_values else 0.0

    # Equity waterfall
    fcfe_list = [cf.fcfe for cf in cash_flows]
    waterfall = run_waterfall(
        fcfe_list, equity,
        inputs.preferred_return_rate,
        inputs.catch_up_rate,
        inputs.carried_interest_rate,
        inputs.lp_share,
    )

    # Tax benefits summary
    tax_benefits = {
        "macrs_schedule": inputs.macrs_schedule,
        "depreciable_amount": round(inputs.capex_total * inputs.depreciable_pct, 2),
        "bonus_depreciation": round(
            inputs.capex_total * inputs.depreciable_pct * inputs.bonus_depreciation_pct
            * inputs.tax_rate, 2
        ),
        "itc_benefit": round(itc_benefit, 2),
    }

    # Sensitivity (skip recursive sensitivity in nested calls)
    sensitivity = {}

    # Confidence range
    uncertainty = 0.15
    conf_low = round(equity_irr * (1 - uncertainty), 4)
    conf_high = round(equity_irr * (1 + uncertainty), 4)

    return FinancialModelResult(
        annual_cash_flows=[asdict(cf) for cf in cash_flows],
        project_irr=round(project_irr * 100, 2),
        equity_irr=round(equity_irr * 100, 2),
        npv=npv,
        moic=moic,
        dscr_min=dscr_min,
        dscr_avg=dscr_avg,
        total_capex=round(inputs.capex_total, 2),
        total_equity=round(equity, 2),
        total_debt=round(total_debt, 2),
        total_revenue=round(total_revenue, 2),
        total_distributions=round(total_distributions, 2),
        equity_waterfall=[asdict(w) for w in waterfall],
        sensitivity=sensitivity,
        tax_benefits=tax_benefits,
        confidence_range_low=round(conf_low * 100, 2),
        confidence_range_high=round(conf_high * 100, 2),
    )


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------

def parse_args() -> argparse.Namespace:
    """Parse command-line arguments."""
    parser = argparse.ArgumentParser(
        description=(
            "Data center project finance model with IRR/NPV/MOIC calculation "
            "and multi-tranche equity waterfall distribution. Supports senior "
            "debt, mezzanine, and equity with configurable hurdle rates."
        ),
        epilog=(
            "Examples:\n"
            "  python3 waterfall-model.py --input model-inputs.json\n"
            "  python3 waterfall-model.py --capex 110000000 --revenue 30000000\n"
            "\nDISCLAIMER: Not investment advice. For planning purposes only.\n"
            "\nPart of fin-project-model skill (stellenium/dc-skills)."
        ),
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )

    parser.add_argument(
        "--input", metavar="FILE",
        help="JSON input file with FinancialModelInput fields",
    )
    parser.add_argument(
        "--output", metavar="FILE",
        help="JSON output file (default: stdout)",
    )

    # Quick-run CLI args
    parser.add_argument(
        "--capex", type=float, default=110_000_000,
        help="Total CapEx in USD (default: 110000000)",
    )
    parser.add_argument(
        "--revenue", type=float, default=0,
        help="Annual revenue Year 1 in USD (default: computed from capacity)",
    )
    parser.add_argument(
        "--capacity-mw", type=float, default=10.0,
        help="Project capacity in MW (default: 10)",
    )
    parser.add_argument(
        "--projection-years", type=int, default=10,
        help="Projection period in years (default: 10)",
    )
    parser.add_argument(
        "--debt-pct", type=float, default=0.70,
        help="Debt as percentage of CapEx (default: 0.70)",
    )
    parser.add_argument(
        "--interest-rate", type=float, default=0.06,
        help="Senior debt interest rate (default: 0.06)",
    )
    parser.add_argument(
        "--equity-irr-target", type=float, default=0.10,
        help="Equity IRR hurdle / preferred return (default: 0.10)",
    )
    parser.add_argument(
        "--discount-rate", type=float, default=0.08,
        help="Discount rate for NPV (default: 0.08)",
    )

    return parser.parse_args()


def main():
    """Entry point."""
    args = parse_args()

    if args.input:
        with open(args.input) as f:
            data = json.load(f)
        inputs = FinancialModelInput(**{
            k: v for k, v in data.items()
            if k in FinancialModelInput.__dataclass_fields__
        })
    else:
        debt_amount = args.capex * args.debt_pct
        equity_amount = args.capex * (1 - args.debt_pct)

        inputs = FinancialModelInput(
            project_capacity_mw=args.capacity_mw,
            capex_total=args.capex,
            revenue_year1=args.revenue,
            projection_years=args.projection_years,
            debt_tranches=[{
                "name": "Senior",
                "amount": debt_amount,
                "interest_rate": args.interest_rate,
                "tenor_years": args.projection_years,
                "amortization_years": args.projection_years,
                "interest_only_years": 0,
            }],
            equity_amount=equity_amount,
            preferred_return_rate=args.equity_irr_target,
            discount_rate=args.discount_rate,
        )

    result = build_financial_model(inputs)

    # Run sensitivity if this is a direct (non-recursive) call
    if not result.sensitivity:
        sens_results = {}
        for var in ["occupancy", "power_cost", "construction_cost", "interest_rate"]:
            try:
                sens_results[var] = run_sensitivity(inputs, var)
            except Exception:
                sens_results[var] = {"variable": var, "error": "computation failed"}
        result.sensitivity = sens_results

    output_json = json.dumps(asdict(result), indent=2)

    if args.output:
        with open(args.output, "w") as f:
            f.write(output_json + "\n")
        print(f"Financial model results written to {args.output}", file=sys.stderr)
    else:
        print(output_json)


if __name__ == "__main__":
    main()
