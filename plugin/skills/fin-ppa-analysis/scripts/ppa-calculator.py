#!/usr/bin/env python3
"""PPA Calculator -- fin-ppa-analysis bundled script.

Buyer-side levelized cost comparison of PPA vs self-generation vs grid
for data center operators. Models basis risk, curtailment exposure,
escalation, ITC benefit on self-gen, and sensitivity analysis.

Requires: Python 3.11+ (stdlib only, no external dependencies).

Usage:
    python3 ppa-calculator.py --help
    python3 ppa-calculator.py --input ppa-inputs.json --output ppa-results.json
    python3 ppa-calculator.py --load-mw 30 --grid-tariff 65 --ppa-price 35
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

DEFAULT_GRID_ESCALATION = 0.025     # 2.5% annual grid tariff escalation
DEFAULT_DISCOUNT_RATE = 0.08        # 8% WACC for NPV
DEFAULT_SOLAR_DEGRADATION = 0.005   # 0.5% annual solar panel degradation
ITC_RATE = 0.30                     # 30% ITC with prevailing wage (FEDERAL-TAX-GUIDE.md)
DEFAULT_CURTAILMENT_RATE = 0.03     # 3% average curtailment
DEFAULT_BASIS_RISK = 4.0            # $/MWh default basis risk spread
DEFAULT_ANALYSIS_YEARS = 15         # Standard PPA term
HOURS_PER_YEAR = 8760


# ---------------------------------------------------------------------------
# Data classes
# ---------------------------------------------------------------------------

@dataclass
class PPAInput:
    """Complete input for PPA analysis calculation."""
    # Facility
    load_mw: float = 30.0
    load_factor: float = 0.95            # DC load factor (high, near-constant)
    # Grid baseline
    grid_tariff_mwh: float = 65.0        # Current grid tariff $/MWh
    grid_escalation: float = DEFAULT_GRID_ESCALATION
    grid_demand_charge_kw_month: float = 0.0  # $/kW/month demand charge
    # PPA
    ppa_price_mwh: float = 35.0          # PPA contract price $/MWh
    ppa_escalator: float = 0.02          # 2% annual PPA escalation
    ppa_term_years: int = 15
    ppa_settlement: str = "physical"     # physical or virtual
    ppa_volume_pct: float = 1.0          # % of load covered by PPA
    # Basis risk
    basis_risk_mwh: float = DEFAULT_BASIS_RISK  # $/MWh basis risk spread
    # Curtailment
    curtailment_rate: float = DEFAULT_CURTAILMENT_RATE
    buyer_pays_during_curtailment: bool = True
    # Self-generation
    selfgen_capex_per_kw: float = 1200.0  # $/kW installed cost (solar)
    selfgen_capacity_mw: float = 0.0      # MW of self-gen (0 = auto-size)
    selfgen_capacity_factor: float = 0.22  # Solar capacity factor
    selfgen_om_per_kwh: float = 0.01      # $/kWh O&M
    selfgen_degradation: float = DEFAULT_SOLAR_DEGRADATION
    itc_eligible: bool = True
    itc_rate: float = ITC_RATE
    # Analysis
    analysis_term_years: int = DEFAULT_ANALYSIS_YEARS
    discount_rate: float = DEFAULT_DISCOUNT_RATE


@dataclass
class AnnualComparison:
    """Single year cost comparison across options."""
    year: int
    grid_cost: float
    ppa_cost: float
    ppa_basis_risk: float
    ppa_curtailment_cost: float
    ppa_all_in: float
    selfgen_cost: float
    cheapest: str
    savings_vs_grid: float


@dataclass
class SensitivityCase:
    """Single sensitivity scenario result."""
    variable: str
    scenario: str
    grid_levelized: float
    ppa_levelized: float
    selfgen_levelized: float
    recommendation: str


@dataclass
class PPAResult:
    """Complete PPA analysis output."""
    grid_levelized_cost: float
    ppa_levelized_cost: float
    selfgen_levelized_cost: float
    annual_comparison: list            # list of AnnualComparison dicts
    recommendation: str
    savings_vs_grid_ppa: float
    savings_vs_grid_ppa_pct: float
    savings_vs_grid_selfgen: float
    savings_vs_grid_selfgen_pct: float
    basis_risk_impact_annual: float
    curtailment_cost_annual: float
    additionality_note: str
    sensitivity_results: list          # list of SensitivityCase dicts
    npv_grid: float
    npv_ppa: float
    npv_selfgen: float


# ---------------------------------------------------------------------------
# Core calculation functions
# ---------------------------------------------------------------------------

def calculate_annual_energy(load_mw: float, load_factor: float) -> float:
    """Calculate annual energy consumption in MWh."""
    return load_mw * load_factor * HOURS_PER_YEAR


def calculate_grid_cost(tariff_mwh: float, escalation: float, year: int,
                         annual_energy: float,
                         demand_charge_kw_month: float,
                         load_mw: float) -> float:
    """Calculate grid electricity cost for a given year."""
    energy_cost = annual_energy * tariff_mwh * (1 + escalation) ** year
    demand_cost = load_mw * 1000 * demand_charge_kw_month * 12 * (1 + escalation) ** year
    return energy_cost + demand_cost


def calculate_ppa_cost(ppa_price: float, escalator: float, year: int,
                        annual_energy: float, volume_pct: float,
                        basis_risk_mwh: float, curtailment_rate: float,
                        buyer_pays_curtailment: bool,
                        settlement: str) -> tuple:
    """Calculate PPA cost for a given year.

    Returns (ppa_energy_cost, basis_risk_cost, curtailment_cost, total).
    """
    ppa_price_yr = ppa_price * (1 + escalator) ** year
    ppa_energy = annual_energy * volume_pct

    # Base PPA cost
    ppa_cost = ppa_energy * ppa_price_yr

    # Basis risk (applies to virtual PPAs or any PPA with node mismatch)
    basis_cost = ppa_energy * basis_risk_mwh if basis_risk_mwh > 0 else 0.0

    # Curtailment cost (buyer pays PPA price but gets no energy)
    curtailment_cost = 0.0
    if buyer_pays_curtailment and curtailment_rate > 0:
        curtailment_cost = ppa_energy * curtailment_rate * ppa_price_yr

    total = ppa_cost + basis_cost + curtailment_cost
    return ppa_cost, basis_cost, curtailment_cost, total


def calculate_selfgen_lcoe(capex_per_kw: float, capacity_mw: float,
                            capacity_factor: float, om_per_kwh: float,
                            degradation: float, itc_eligible: bool,
                            itc_rate: float, discount_rate: float,
                            analysis_years: int) -> float:
    """Calculate self-generation LCOE (Levelized Cost of Energy).

    LCOE = (CapEx - ITC + NPV(O&M)) / NPV(Generation)
    """
    if capacity_mw <= 0 or capacity_factor <= 0:
        return float("inf")

    capex = capacity_mw * 1000 * capex_per_kw  # Total CapEx
    itc_benefit = capex * itc_rate if itc_eligible else 0.0
    net_capex = capex - itc_benefit

    # NPV of O&M costs
    om_npv = 0.0
    gen_npv = 0.0
    for yr in range(1, analysis_years + 1):
        # Generation with degradation
        annual_gen = capacity_mw * 1000 * capacity_factor * HOURS_PER_YEAR
        annual_gen *= (1 - degradation) ** yr

        # O&M cost
        annual_om = annual_gen * om_per_kwh

        # Discount
        discount = (1 + discount_rate) ** yr
        om_npv += annual_om / discount
        gen_npv += annual_gen / discount

    if gen_npv <= 0:
        return float("inf")

    lcoe = (net_capex + om_npv) / gen_npv
    return lcoe * 1000  # Convert $/kWh to $/MWh


def calculate_selfgen_annual_cost(capacity_mw: float, capacity_factor: float,
                                   degradation: float, om_per_kwh: float,
                                   year: int) -> float:
    """Calculate self-gen annual cost (O&M only, capex is sunk)."""
    annual_gen = capacity_mw * 1000 * capacity_factor * HOURS_PER_YEAR
    annual_gen *= (1 - degradation) ** year
    return annual_gen * om_per_kwh


def calculate_levelized_cost(annual_costs: List[float], annual_energy: float,
                              discount_rate: float) -> float:
    """Calculate levelized cost from a stream of annual costs."""
    cost_npv = 0.0
    energy_npv = 0.0
    for yr, cost in enumerate(annual_costs, 1):
        discount = (1 + discount_rate) ** yr
        cost_npv += cost / discount
        energy_npv += annual_energy / discount
    if energy_npv <= 0:
        return 0.0
    return cost_npv / energy_npv


def calculate(inputs: PPAInput) -> PPAResult:
    """Orchestrate all PPA analysis calculations."""
    annual_energy = calculate_annual_energy(inputs.load_mw, inputs.load_factor)

    # Auto-size self-gen if not specified
    selfgen_mw = inputs.selfgen_capacity_mw
    if selfgen_mw <= 0:
        # Size to cover ~30% of load (typical rooftop/adjacent solar)
        selfgen_mw = inputs.load_mw * 0.3

    # --- Annual cost comparison ---
    grid_costs = []
    ppa_costs = []
    selfgen_costs = []
    comparisons = []

    for yr in range(1, inputs.analysis_term_years + 1):
        # Grid
        grid_cost = calculate_grid_cost(
            inputs.grid_tariff_mwh, inputs.grid_escalation, yr - 1,
            annual_energy, inputs.grid_demand_charge_kw_month, inputs.load_mw,
        )
        grid_costs.append(grid_cost)

        # PPA
        ppa_energy, basis, curtailment, ppa_total = calculate_ppa_cost(
            inputs.ppa_price_mwh, inputs.ppa_escalator, yr - 1,
            annual_energy, inputs.ppa_volume_pct,
            inputs.basis_risk_mwh, inputs.curtailment_rate,
            inputs.buyer_pays_during_curtailment, inputs.ppa_settlement,
        )
        ppa_costs.append(ppa_total)

        # Self-gen (O&M only for annual comparison; LCOE includes capex)
        sg_cost = calculate_selfgen_annual_cost(
            selfgen_mw, inputs.selfgen_capacity_factor,
            inputs.selfgen_degradation, inputs.selfgen_om_per_kwh, yr,
        )
        selfgen_costs.append(sg_cost)

        # Determine cheapest
        options = {"Grid": grid_cost, "PPA": ppa_total, "Self-gen": sg_cost}
        cheapest = min(options, key=options.get)

        comparisons.append(AnnualComparison(
            year=yr,
            grid_cost=round(grid_cost, 2),
            ppa_cost=round(ppa_energy, 2),
            ppa_basis_risk=round(basis, 2),
            ppa_curtailment_cost=round(curtailment, 2),
            ppa_all_in=round(ppa_total, 2),
            selfgen_cost=round(sg_cost, 2),
            cheapest=cheapest,
            savings_vs_grid=round(grid_cost - min(ppa_total, sg_cost), 2),
        ))

    # --- Levelized costs ---
    grid_levelized = calculate_levelized_cost(grid_costs, annual_energy,
                                               inputs.discount_rate)
    ppa_levelized = calculate_levelized_cost(ppa_costs, annual_energy,
                                              inputs.discount_rate)
    selfgen_lcoe = calculate_selfgen_lcoe(
        inputs.selfgen_capex_per_kw, selfgen_mw,
        inputs.selfgen_capacity_factor, inputs.selfgen_om_per_kwh,
        inputs.selfgen_degradation, inputs.itc_eligible,
        inputs.itc_rate, inputs.discount_rate, inputs.analysis_term_years,
    )

    # --- NPVs ---
    npv_grid = sum(c / (1 + inputs.discount_rate) ** yr
                   for yr, c in enumerate(grid_costs, 1))
    npv_ppa = sum(c / (1 + inputs.discount_rate) ** yr
                  for yr, c in enumerate(ppa_costs, 1))
    npv_selfgen = sum(c / (1 + inputs.discount_rate) ** yr
                      for yr, c in enumerate(selfgen_costs, 1))
    # Add self-gen capex to NPV
    selfgen_capex = selfgen_mw * 1000 * inputs.selfgen_capex_per_kw
    itc_benefit = selfgen_capex * inputs.itc_rate if inputs.itc_eligible else 0.0
    npv_selfgen += selfgen_capex - itc_benefit

    # --- Recommendation ---
    options = {"Grid": grid_levelized, "PPA": ppa_levelized, "Self-gen": selfgen_lcoe}
    recommendation = min(options, key=options.get)

    # --- Savings ---
    savings_ppa = (grid_levelized - ppa_levelized) * annual_energy * inputs.analysis_term_years / 1e6
    savings_ppa_pct = ((grid_levelized - ppa_levelized) / grid_levelized * 100
                       if grid_levelized > 0 else 0.0)
    savings_sg = (grid_levelized - selfgen_lcoe) * annual_energy * inputs.analysis_term_years / 1e6
    savings_sg_pct = ((grid_levelized - selfgen_lcoe) / grid_levelized * 100
                      if grid_levelized > 0 else 0.0)

    # --- Basis risk and curtailment annual impact ---
    basis_annual = annual_energy * inputs.basis_risk_mwh
    curtailment_annual = (annual_energy * inputs.curtailment_rate
                          * inputs.ppa_price_mwh
                          if inputs.buyer_pays_during_curtailment else 0.0)

    # --- Additionality ---
    additionality = (
        "New-build PPA qualifies for additionality under CSRD, SBTi, and RE100 "
        "frameworks (market-based Scope 2 accounting). Existing facility RECs "
        "may not satisfy additionality requirements."
    )

    # --- Sensitivity ---
    sensitivity = []

    # Grid escalation +/-1%
    for label, delta in [("Grid escalation -1%", -0.01), ("Grid escalation +1%", 0.01)]:
        alt_grid_costs = [
            calculate_grid_cost(inputs.grid_tariff_mwh,
                                inputs.grid_escalation + delta, yr - 1,
                                annual_energy, inputs.grid_demand_charge_kw_month,
                                inputs.load_mw)
            for yr in range(1, inputs.analysis_term_years + 1)
        ]
        alt_grid_lev = calculate_levelized_cost(alt_grid_costs, annual_energy,
                                                 inputs.discount_rate)
        alt_opts = {"Grid": alt_grid_lev, "PPA": ppa_levelized, "Self-gen": selfgen_lcoe}
        sensitivity.append(SensitivityCase(
            variable="Grid escalation", scenario=label,
            grid_levelized=round(alt_grid_lev, 2),
            ppa_levelized=round(ppa_levelized, 2),
            selfgen_levelized=round(selfgen_lcoe, 2),
            recommendation=min(alt_opts, key=alt_opts.get),
        ))

    # Curtailment +/-2%
    for label, delta in [("Curtailment -2%", -0.02), ("Curtailment +2%", 0.02)]:
        alt_curt = max(0, inputs.curtailment_rate + delta)
        alt_ppa_costs = [
            calculate_ppa_cost(
                inputs.ppa_price_mwh, inputs.ppa_escalator, yr - 1,
                annual_energy, inputs.ppa_volume_pct,
                inputs.basis_risk_mwh, alt_curt,
                inputs.buyer_pays_during_curtailment, inputs.ppa_settlement,
            )[3]
            for yr in range(1, inputs.analysis_term_years + 1)
        ]
        alt_ppa_lev = calculate_levelized_cost(alt_ppa_costs, annual_energy,
                                                inputs.discount_rate)
        alt_opts = {"Grid": grid_levelized, "PPA": alt_ppa_lev, "Self-gen": selfgen_lcoe}
        sensitivity.append(SensitivityCase(
            variable="Curtailment rate", scenario=label,
            grid_levelized=round(grid_levelized, 2),
            ppa_levelized=round(alt_ppa_lev, 2),
            selfgen_levelized=round(selfgen_lcoe, 2),
            recommendation=min(alt_opts, key=alt_opts.get),
        ))

    # Basis risk +/-$2/MWh
    for label, delta in [("Basis risk -$2/MWh", -2.0), ("Basis risk +$2/MWh", 2.0)]:
        alt_basis = max(0, inputs.basis_risk_mwh + delta)
        alt_ppa_costs = [
            calculate_ppa_cost(
                inputs.ppa_price_mwh, inputs.ppa_escalator, yr - 1,
                annual_energy, inputs.ppa_volume_pct,
                alt_basis, inputs.curtailment_rate,
                inputs.buyer_pays_during_curtailment, inputs.ppa_settlement,
            )[3]
            for yr in range(1, inputs.analysis_term_years + 1)
        ]
        alt_ppa_lev = calculate_levelized_cost(alt_ppa_costs, annual_energy,
                                                inputs.discount_rate)
        alt_opts = {"Grid": grid_levelized, "PPA": alt_ppa_lev, "Self-gen": selfgen_lcoe}
        sensitivity.append(SensitivityCase(
            variable="Basis risk", scenario=label,
            grid_levelized=round(grid_levelized, 2),
            ppa_levelized=round(alt_ppa_lev, 2),
            selfgen_levelized=round(selfgen_lcoe, 2),
            recommendation=min(alt_opts, key=alt_opts.get),
        ))

    return PPAResult(
        grid_levelized_cost=round(grid_levelized, 2),
        ppa_levelized_cost=round(ppa_levelized, 2),
        selfgen_levelized_cost=round(selfgen_lcoe, 2),
        annual_comparison=[asdict(c) for c in comparisons],
        recommendation=recommendation,
        savings_vs_grid_ppa=round(savings_ppa, 2),
        savings_vs_grid_ppa_pct=round(savings_ppa_pct, 2),
        savings_vs_grid_selfgen=round(savings_sg, 2),
        savings_vs_grid_selfgen_pct=round(savings_sg_pct, 2),
        basis_risk_impact_annual=round(basis_annual, 2),
        curtailment_cost_annual=round(curtailment_annual, 2),
        additionality_note=additionality,
        sensitivity_results=[asdict(s) for s in sensitivity],
        npv_grid=round(npv_grid, 2),
        npv_ppa=round(npv_ppa, 2),
        npv_selfgen=round(npv_selfgen, 2),
    )


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------

def parse_args() -> argparse.Namespace:
    """Parse command-line arguments."""
    parser = argparse.ArgumentParser(
        description=(
            "Data center PPA analysis calculator with buyer-side levelized "
            "cost comparison of PPA vs self-generation vs grid. Models basis "
            "risk, curtailment exposure, ITC benefit, and sensitivity."
        ),
        epilog=(
            "Examples:\n"
            "  python3 ppa-calculator.py --input ppa-inputs.json\n"
            "  python3 ppa-calculator.py --load-mw 30 --grid-tariff 65 --ppa-price 35\n"
            "  python3 ppa-calculator.py --load-mw 50 --grid-tariff 80 --ppa-price 55 "
            "--basis-risk 6\n"
            "\nDISCLAIMER: Not investment advice. For planning purposes only.\n"
            "\nPart of fin-ppa-analysis skill (stellenium/dc-skills)."
        ),
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )

    parser.add_argument("--input", metavar="FILE",
                        help="JSON input file with PPAInput fields")
    parser.add_argument("--output", metavar="FILE",
                        help="JSON output file (default: stdout)")

    # Quick-run CLI args
    parser.add_argument("--load-mw", type=float, default=30.0,
                        help="Facility load in MW (default: 30)")
    parser.add_argument("--grid-tariff", type=float, default=65.0,
                        help="Current grid tariff in $/MWh (default: 65)")
    parser.add_argument("--grid-escalation", type=float,
                        default=DEFAULT_GRID_ESCALATION,
                        help=f"Annual grid escalation rate (default: {DEFAULT_GRID_ESCALATION})")
    parser.add_argument("--ppa-price", type=float, default=35.0,
                        help="PPA contract price in $/MWh (default: 35)")
    parser.add_argument("--ppa-escalator", type=float, default=0.02,
                        help="PPA annual escalation rate (default: 0.02)")
    parser.add_argument("--ppa-term", type=int, default=15,
                        help="PPA term in years (default: 15)")
    parser.add_argument("--basis-risk", type=float, default=DEFAULT_BASIS_RISK,
                        help=f"Basis risk in $/MWh (default: {DEFAULT_BASIS_RISK})")
    parser.add_argument("--curtailment-rate", type=float,
                        default=DEFAULT_CURTAILMENT_RATE,
                        help=f"Curtailment rate (default: {DEFAULT_CURTAILMENT_RATE})")
    parser.add_argument("--selfgen-capex", type=float, default=1200.0,
                        help="Self-gen installed cost in $/kW (default: 1200)")
    parser.add_argument("--selfgen-cf", type=float, default=0.22,
                        help="Self-gen capacity factor (default: 0.22)")
    parser.add_argument("--no-itc", action="store_true",
                        help="Self-gen not eligible for ITC")
    parser.add_argument("--analysis-years", type=int,
                        default=DEFAULT_ANALYSIS_YEARS,
                        help=f"Analysis term in years (default: {DEFAULT_ANALYSIS_YEARS})")
    parser.add_argument("--discount-rate", type=float,
                        default=DEFAULT_DISCOUNT_RATE,
                        help=f"Discount rate for NPV (default: {DEFAULT_DISCOUNT_RATE})")

    return parser.parse_args()


def main():
    """Entry point."""
    args = parse_args()

    if args.input:
        with open(args.input) as f:
            data = json.load(f)
        inputs = PPAInput(**{
            k: v for k, v in data.items()
            if k in PPAInput.__dataclass_fields__
        })
    else:
        inputs = PPAInput(
            load_mw=args.load_mw,
            grid_tariff_mwh=args.grid_tariff,
            grid_escalation=args.grid_escalation,
            ppa_price_mwh=args.ppa_price,
            ppa_escalator=args.ppa_escalator,
            ppa_term_years=args.ppa_term,
            basis_risk_mwh=args.basis_risk,
            curtailment_rate=args.curtailment_rate,
            selfgen_capex_per_kw=args.selfgen_capex,
            selfgen_capacity_factor=args.selfgen_cf,
            itc_eligible=not args.no_itc,
            analysis_term_years=args.analysis_years,
            discount_rate=args.discount_rate,
        )

    result = calculate(inputs)
    output_json = json.dumps(asdict(result), indent=2)

    if args.output:
        with open(args.output, "w") as f:
            f.write(output_json + "\n")
        print(f"PPA analysis results written to {args.output}", file=sys.stderr)
    else:
        print(output_json)


if __name__ == "__main__":
    main()
