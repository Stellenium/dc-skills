#!/usr/bin/env python3
"""Debt Sizing -- fin-debt-sizing bundled script.

Calculates DSCR-based debt capacity for data center projects with construction
facility modeling, term loan amortization schedules, covenant testing (DSCR,
debt yield, LTV), cash trap provisions, and sensitivity analysis.

Requires: Python 3.11+ (stdlib only, no external dependencies).

Usage:
    python3 debt-sizing.py --help
    python3 debt-sizing.py --input debt-inputs.json --output debt-results.json
    python3 debt-sizing.py --project-cost 200000000 --annual-ebitda 30000000
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

DEFAULT_MIN_DSCR = 1.30
CASH_TRAP_DSCR = 1.15
DEFAULT_TRIGGER_DSCR = 1.05
DEFAULT_AMORT_YEARS = 15
DEFAULT_TERM_YEARS = 7
DEFAULT_CONSTRUCTION_MONTHS = 24
DEFAULT_INTEREST_RATE = 0.06
DEFAULT_MIN_DEBT_YIELD = 0.08
DEFAULT_MAX_LTV = 0.75


# ---------------------------------------------------------------------------
# Data classes
# ---------------------------------------------------------------------------

@dataclass
class DebtSizingInput:
    """Complete input for debt sizing calculation."""
    project_cost: float = 200_000_000.0
    annual_ebitda: float = 30_000_000.0
    ebitda_growth_rate: float = 0.03
    maintenance_capex_pct: float = 0.03     # 3% of revenue as maintenance capex
    tax_rate: float = 0.21
    working_capital_pct: float = 0.02       # 2% of revenue as working capital
    interest_rate: float = DEFAULT_INTEREST_RATE
    amortization_years: int = DEFAULT_AMORT_YEARS
    term_years: int = DEFAULT_TERM_YEARS
    min_dscr: float = DEFAULT_MIN_DSCR
    cash_trap_dscr: float = CASH_TRAP_DSCR
    default_dscr: float = DEFAULT_TRIGGER_DSCR
    max_ltv: float = DEFAULT_MAX_LTV
    min_debt_yield: float = DEFAULT_MIN_DEBT_YIELD
    construction_months: int = DEFAULT_CONSTRUCTION_MONTHS
    construction_rate: float = 0.065        # Construction loan rate (SOFR + spread)
    draw_schedule: list = field(default_factory=lambda: [])  # Monthly draw %
    projection_years: int = 10
    occupancy_schedule: list = field(default_factory=lambda: [
        0.40, 0.65, 0.80, 0.90, 0.95, 0.95, 0.95, 0.95, 0.95, 0.95
    ])


@dataclass
class AnnualDebtSchedule:
    """Single year of amortization schedule with covenant testing."""
    year: int
    beginning_balance: float
    payment: float
    principal: float
    interest: float
    ending_balance: float
    ebitda: float
    cfads: float
    dscr: float
    debt_yield: float
    ltv: float
    covenant_status: str      # Pass, Cash Trap, Default


@dataclass
class ConstructionDraw:
    """Construction facility draw schedule."""
    month: int
    draw_amount: float
    cumulative_drawn: float
    interest_accrued: float
    cumulative_interest: float


@dataclass
class SensitivityResult:
    """Sensitivity analysis result for one scenario."""
    scenario: str
    dscr_year1: float
    dscr_min: float
    covenant_status: str
    max_debt_capacity: float


@dataclass
class DebtSizingResult:
    """Complete debt sizing output."""
    max_debt_capacity: float
    ltv: float
    debt_yield: float
    interest_rate: float
    amortization_years: int
    term_years: int
    min_dscr_achieved: float
    avg_dscr: float
    annual_schedule: list           # list of AnnualDebtSchedule dicts
    construction_draws: list        # list of ConstructionDraw dicts
    construction_interest: float
    total_debt_service: float
    balloon_balance: float
    sensitivity: list               # list of SensitivityResult dicts
    covenant_summary: dict


# ---------------------------------------------------------------------------
# Core calculation functions
# ---------------------------------------------------------------------------

def calculate_cfads(ebitda: float, tax_rate: float,
                     maintenance_capex_pct: float,
                     working_capital_pct: float) -> float:
    """Calculate Cash Flow Available for Debt Service.

    CFADS = EBITDA - taxes - maintenance CapEx - working capital changes.
    NOT raw EBITDA (common mistake in DC project finance).
    """
    taxes = max(0, ebitda * tax_rate * 0.6)  # Effective rate after depreciation shield
    maintenance = ebitda * maintenance_capex_pct
    working_capital = ebitda * working_capital_pct
    return ebitda - taxes - maintenance - working_capital


def calculate_annual_payment(principal: float, rate: float,
                              amortization_years: int) -> float:
    """Calculate constant annual payment (mortgage-style amortization)."""
    if rate <= 0 or amortization_years <= 0:
        return principal / max(1, amortization_years)
    r = rate
    n = amortization_years
    return principal * (r * (1 + r) ** n) / ((1 + r) ** n - 1)


def size_debt_from_dscr(cfads: float, min_dscr: float, rate: float,
                         amortization_years: int) -> float:
    """Size maximum debt capacity from CFADS and minimum DSCR.

    Max annual debt service = CFADS / min DSCR
    Solve for loan principal given rate and amortization.
    """
    max_annual_ds = cfads / min_dscr
    if rate <= 0 or amortization_years <= 0:
        return max_annual_ds * amortization_years
    r = rate
    n = amortization_years
    # PV of annuity: P = PMT * [(1+r)^n - 1] / [r * (1+r)^n]
    pv_factor = ((1 + r) ** n - 1) / (r * (1 + r) ** n)
    return max_annual_ds * pv_factor


def build_construction_schedule(project_cost: float, debt_pct: float,
                                 construction_months: int,
                                 construction_rate: float,
                                 draw_schedule: list) -> tuple:
    """Build construction facility draw schedule.

    Returns (list of ConstructionDraw, total capitalized interest).
    """
    total_draw = project_cost * debt_pct
    draws = []
    cumulative = 0.0
    cumulative_interest = 0.0
    monthly_rate = construction_rate / 12

    # Default even draw if no schedule provided
    if not draw_schedule or len(draw_schedule) < construction_months:
        draw_schedule = [1.0 / construction_months] * construction_months

    for month in range(1, construction_months + 1):
        idx = month - 1
        pct = draw_schedule[idx] if idx < len(draw_schedule) else 0.0
        draw_amount = total_draw * pct
        cumulative += draw_amount

        # Interest on cumulative drawn balance
        interest = cumulative * monthly_rate
        cumulative_interest += interest

        draws.append(ConstructionDraw(
            month=month,
            draw_amount=round(draw_amount, 2),
            cumulative_drawn=round(cumulative, 2),
            interest_accrued=round(interest, 2),
            cumulative_interest=round(cumulative_interest, 2),
        ))

    return draws, round(cumulative_interest, 2)


def build_amortization_schedule(inputs: DebtSizingInput,
                                 loan_amount: float) -> List[AnnualDebtSchedule]:
    """Build full amortization schedule with covenant testing."""
    annual_payment = calculate_annual_payment(
        loan_amount, inputs.interest_rate, inputs.amortization_years
    )
    balance = loan_amount
    schedule = []

    for yr in range(1, inputs.projection_years + 1):
        # EBITDA with growth and occupancy
        occupancy = (inputs.occupancy_schedule[yr - 1]
                     if yr - 1 < len(inputs.occupancy_schedule) else 0.95)
        base_ebitda = inputs.annual_ebitda * (1 + inputs.ebitda_growth_rate) ** (yr - 1)
        ebitda = base_ebitda * occupancy

        # CFADS
        cfads = calculate_cfads(
            ebitda, inputs.tax_rate,
            inputs.maintenance_capex_pct, inputs.working_capital_pct,
        )

        # Debt service
        if yr <= inputs.term_years and balance > 0:
            interest = balance * inputs.interest_rate
            principal = min(balance, annual_payment - interest)
            if principal < 0:
                principal = 0
            payment = interest + principal
            ending_balance = max(0, balance - principal)
        else:
            interest = principal = payment = 0.0
            ending_balance = 0.0

        # Covenant tests
        dscr = cfads / payment if payment > 0 else float("inf")
        debt_yield = ebitda / loan_amount if loan_amount > 0 else 0.0
        ltv = ending_balance / inputs.project_cost if inputs.project_cost > 0 else 0.0

        # Covenant status
        if dscr != float("inf"):
            if dscr < inputs.default_dscr:
                status = "Default"
            elif dscr < inputs.cash_trap_dscr:
                status = "Cash Trap"
            else:
                status = "Pass"
        else:
            status = "Pass (no debt service)"

        schedule.append(AnnualDebtSchedule(
            year=yr,
            beginning_balance=round(balance, 2),
            payment=round(payment, 2),
            principal=round(principal, 2),
            interest=round(interest, 2),
            ending_balance=round(ending_balance, 2),
            ebitda=round(ebitda, 2),
            cfads=round(cfads, 2),
            dscr=round(dscr, 4) if dscr != float("inf") else 0.0,
            debt_yield=round(debt_yield, 4),
            ltv=round(ltv, 4),
            covenant_status=status,
        ))

        balance = ending_balance

    return schedule


def run_sensitivity(inputs: DebtSizingInput, loan_amount: float) -> List[SensitivityResult]:
    """Run sensitivity analysis across key variables."""
    scenarios = []

    # Base case
    base_schedule = build_amortization_schedule(inputs, loan_amount)
    dscrs = [s.dscr for s in base_schedule if s.dscr > 0]
    scenarios.append(SensitivityResult(
        scenario="Base case",
        dscr_year1=base_schedule[0].dscr if base_schedule else 0.0,
        dscr_min=min(dscrs) if dscrs else 0.0,
        covenant_status="Pass" if all(s.covenant_status == "Pass" or "no debt" in s.covenant_status for s in base_schedule) else "Breach",
        max_debt_capacity=round(loan_amount, 2),
    ))

    # NOI -10%
    low_inputs = DebtSizingInput(**{
        k: v for k, v in asdict(inputs).items()
        if k in DebtSizingInput.__dataclass_fields__
    })
    low_inputs.annual_ebitda = inputs.annual_ebitda * 0.90
    low_schedule = build_amortization_schedule(low_inputs, loan_amount)
    low_dscrs = [s.dscr for s in low_schedule if s.dscr > 0]
    worst_low = min(low_dscrs) if low_dscrs else 0.0
    scenarios.append(SensitivityResult(
        scenario="NOI -10%",
        dscr_year1=low_schedule[0].dscr if low_schedule else 0.0,
        dscr_min=worst_low,
        covenant_status="Pass" if worst_low >= inputs.min_dscr else "Breach",
        max_debt_capacity=round(loan_amount, 2),
    ))

    # NOI +10%
    high_inputs = DebtSizingInput(**{
        k: v for k, v in asdict(inputs).items()
        if k in DebtSizingInput.__dataclass_fields__
    })
    high_inputs.annual_ebitda = inputs.annual_ebitda * 1.10
    high_schedule = build_amortization_schedule(high_inputs, loan_amount)
    high_dscrs = [s.dscr for s in high_schedule if s.dscr > 0]
    scenarios.append(SensitivityResult(
        scenario="NOI +10%",
        dscr_year1=high_schedule[0].dscr if high_schedule else 0.0,
        dscr_min=min(high_dscrs) if high_dscrs else 0.0,
        covenant_status="Pass",
        max_debt_capacity=round(loan_amount, 2),
    ))

    # Rate +100bps
    rate_up = DebtSizingInput(**{
        k: v for k, v in asdict(inputs).items()
        if k in DebtSizingInput.__dataclass_fields__
    })
    rate_up.interest_rate = inputs.interest_rate + 0.01
    up_schedule = build_amortization_schedule(rate_up, loan_amount)
    up_dscrs = [s.dscr for s in up_schedule if s.dscr > 0]
    worst_up = min(up_dscrs) if up_dscrs else 0.0
    scenarios.append(SensitivityResult(
        scenario="Rate +100bps",
        dscr_year1=up_schedule[0].dscr if up_schedule else 0.0,
        dscr_min=worst_up,
        covenant_status="Pass" if worst_up >= inputs.min_dscr else "Breach",
        max_debt_capacity=round(loan_amount, 2),
    ))

    # Rate -100bps
    rate_down = DebtSizingInput(**{
        k: v for k, v in asdict(inputs).items()
        if k in DebtSizingInput.__dataclass_fields__
    })
    rate_down.interest_rate = max(0.01, inputs.interest_rate - 0.01)
    down_schedule = build_amortization_schedule(rate_down, loan_amount)
    down_dscrs = [s.dscr for s in down_schedule if s.dscr > 0]
    scenarios.append(SensitivityResult(
        scenario="Rate -100bps",
        dscr_year1=down_schedule[0].dscr if down_schedule else 0.0,
        dscr_min=min(down_dscrs) if down_dscrs else 0.0,
        covenant_status="Pass",
        max_debt_capacity=round(loan_amount, 2),
    ))

    return scenarios


def calculate(inputs: DebtSizingInput) -> DebtSizingResult:
    """Orchestrate all debt sizing calculations."""
    # Step 1: Calculate CFADS at stabilization
    stabilized_ebitda = inputs.annual_ebitda
    cfads = calculate_cfads(
        stabilized_ebitda, inputs.tax_rate,
        inputs.maintenance_capex_pct, inputs.working_capital_pct,
    )

    # Step 2: Size debt from DSCR
    dscr_capacity = size_debt_from_dscr(
        cfads, inputs.min_dscr, inputs.interest_rate, inputs.amortization_years,
    )

    # Step 3: Check LTV constraint
    ltv_capacity = inputs.project_cost * inputs.max_ltv

    # Step 4: Check debt yield constraint
    dy_capacity = stabilized_ebitda / inputs.min_debt_yield if inputs.min_debt_yield > 0 else float("inf")

    # Final debt capacity is the minimum of all constraints
    max_debt = min(dscr_capacity, ltv_capacity, dy_capacity)
    max_debt = round(max_debt, 2)

    # LTV and debt yield at max debt
    ltv = max_debt / inputs.project_cost if inputs.project_cost > 0 else 0.0
    debt_yield = stabilized_ebitda / max_debt if max_debt > 0 else 0.0

    # Step 5: Construction schedule
    debt_pct = max_debt / inputs.project_cost if inputs.project_cost > 0 else 0.0
    construction_draws, construction_interest = build_construction_schedule(
        inputs.project_cost, debt_pct,
        inputs.construction_months, inputs.construction_rate,
        inputs.draw_schedule,
    )

    # Term loan balance = max_debt + capitalized construction interest
    term_loan_balance = max_debt + construction_interest

    # Step 6: Amortization schedule
    schedule = build_amortization_schedule(inputs, term_loan_balance)

    # Summary statistics
    dscrs = [s.dscr for s in schedule if s.dscr > 0 and s.year <= inputs.term_years]
    min_dscr_achieved = min(dscrs) if dscrs else 0.0
    avg_dscr = sum(dscrs) / len(dscrs) if dscrs else 0.0

    total_ds = sum(s.payment for s in schedule if s.year <= inputs.term_years)

    # Balloon balance at term maturity
    term_end = [s for s in schedule if s.year == inputs.term_years]
    balloon = term_end[0].ending_balance if term_end else 0.0

    # Step 7: Sensitivity analysis
    sensitivity = run_sensitivity(inputs, term_loan_balance)

    # Covenant summary
    breaches = [s for s in schedule if s.covenant_status == "Default"]
    traps = [s for s in schedule if s.covenant_status == "Cash Trap"]
    covenant_summary = {
        "total_years_tested": len([s for s in schedule if s.year <= inputs.term_years]),
        "years_pass": len([s for s in schedule if s.covenant_status == "Pass" and s.year <= inputs.term_years]),
        "years_cash_trap": len(traps),
        "years_default": len(breaches),
        "first_trap_year": traps[0].year if traps else None,
        "first_default_year": breaches[0].year if breaches else None,
    }

    return DebtSizingResult(
        max_debt_capacity=max_debt,
        ltv=round(ltv, 4),
        debt_yield=round(debt_yield, 4),
        interest_rate=inputs.interest_rate,
        amortization_years=inputs.amortization_years,
        term_years=inputs.term_years,
        min_dscr_achieved=round(min_dscr_achieved, 4),
        avg_dscr=round(avg_dscr, 4),
        annual_schedule=[asdict(s) for s in schedule],
        construction_draws=[asdict(d) for d in construction_draws],
        construction_interest=construction_interest,
        total_debt_service=round(total_ds, 2),
        balloon_balance=round(balloon, 2),
        sensitivity=[asdict(s) for s in sensitivity],
        covenant_summary=covenant_summary,
    )


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------

def parse_args() -> argparse.Namespace:
    """Parse command-line arguments."""
    parser = argparse.ArgumentParser(
        description=(
            "Data center debt sizing calculator with DSCR-based capacity, "
            "construction facility modeling, term loan amortization, covenant "
            "testing (DSCR, debt yield, LTV), and sensitivity analysis."
        ),
        epilog=(
            "Examples:\n"
            "  python3 debt-sizing.py --input debt-inputs.json\n"
            "  python3 debt-sizing.py --project-cost 200000000 --annual-ebitda 30000000\n"
            "  python3 debt-sizing.py --project-cost 800000000 --annual-ebitda 120000000 --min-dscr 1.25\n"
            "\nDISCLAIMER: Not investment advice. For planning purposes only.\n"
            "\nPart of fin-debt-sizing skill (stellenium/dc-skills)."
        ),
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )

    parser.add_argument("--input", metavar="FILE",
                        help="JSON input file with DebtSizingInput fields")
    parser.add_argument("--output", metavar="FILE",
                        help="JSON output file (default: stdout)")

    # Quick-run CLI args
    parser.add_argument("--project-cost", type=float, default=200_000_000,
                        help="Total project cost in USD (default: 200000000)")
    parser.add_argument("--annual-ebitda", type=float, default=30_000_000,
                        help="Annual stabilized EBITDA in USD (default: 30000000)")
    parser.add_argument("--interest-rate", type=float, default=DEFAULT_INTEREST_RATE,
                        help=f"Interest rate (default: {DEFAULT_INTEREST_RATE})")
    parser.add_argument("--min-dscr", type=float, default=DEFAULT_MIN_DSCR,
                        help=f"Minimum DSCR requirement (default: {DEFAULT_MIN_DSCR})")
    parser.add_argument("--max-ltv", type=float, default=DEFAULT_MAX_LTV,
                        help=f"Maximum LTV (default: {DEFAULT_MAX_LTV})")
    parser.add_argument("--amortization-years", type=int, default=DEFAULT_AMORT_YEARS,
                        help=f"Amortization period in years (default: {DEFAULT_AMORT_YEARS})")
    parser.add_argument("--term-years", type=int, default=DEFAULT_TERM_YEARS,
                        help=f"Loan term in years (default: {DEFAULT_TERM_YEARS})")
    parser.add_argument("--construction-months", type=int,
                        default=DEFAULT_CONSTRUCTION_MONTHS,
                        help=f"Construction period in months (default: {DEFAULT_CONSTRUCTION_MONTHS})")
    parser.add_argument("--projection-years", type=int, default=10,
                        help="Projection period in years (default: 10)")

    return parser.parse_args()


def main():
    """Entry point."""
    args = parse_args()

    if args.input:
        with open(args.input) as f:
            data = json.load(f)
        inputs = DebtSizingInput(**{
            k: v for k, v in data.items()
            if k in DebtSizingInput.__dataclass_fields__
        })
    else:
        inputs = DebtSizingInput(
            project_cost=args.project_cost,
            annual_ebitda=args.annual_ebitda,
            interest_rate=args.interest_rate,
            min_dscr=args.min_dscr,
            max_ltv=args.max_ltv,
            amortization_years=args.amortization_years,
            term_years=args.term_years,
            construction_months=args.construction_months,
            projection_years=args.projection_years,
        )

    result = calculate(inputs)
    output_json = json.dumps(asdict(result), indent=2)

    if args.output:
        with open(args.output, "w") as f:
            f.write(output_json + "\n")
        print(f"Debt sizing results written to {args.output}", file=sys.stderr)
    else:
        print(output_json)


if __name__ == "__main__":
    main()
