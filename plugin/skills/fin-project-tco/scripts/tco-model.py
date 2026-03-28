#!/usr/bin/env python3
"""TCO Model -- fin-project-tco bundled script.

Calculates Total Cost of Ownership for data center projects with CapEx/OpEx
breakdown, NPV, tax incentive modeling, and sensitivity analysis.

Requires: Python 3.11+ (stdlib only, no external dependencies).

Usage:
    python3 tco-model.py --help
    python3 tco-model.py --input tco-inputs.json --output tco-results.json
    python3 tco-model.py --it-load-kw 10000 --pue 1.35 --power-cost 0.065 --state VA
"""
import argparse
import json
import math
import sys
from dataclasses import dataclass, field, asdict
from typing import List, Optional


# ---------------------------------------------------------------------------
# Data classes
# ---------------------------------------------------------------------------

@dataclass
class TCOInputs:
    """All inputs required for a TCO calculation."""
    it_load_kw: float = 10000.0
    total_facility_kw: float = 0.0  # computed from it_load_kw * pue if 0
    pue: float = 1.35
    capex_per_mw: float = 11_000_000.0  # USD per MW of IT load
    power_cost_kwh: float = 0.065  # USD per kWh
    annual_escalation_pct: float = 3.0  # percent per year
    discount_rate: float = 0.08  # WACC / hurdle rate
    analysis_years: int = 10
    state: str = "VA"
    staffing_per_mw: float = 4.0  # FTEs per MW of IT load
    loaded_cost_per_fte: float = 120_000.0  # annual loaded cost per FTE
    maintenance_pct_of_capex: float = 0.03  # 3% of M&E CapEx
    insurance_pct: float = 0.0075  # 0.75% of replacement value
    property_tax_rate: float = 0.012  # 1.2% of assessed value
    sales_tax_exempt: bool = True
    sales_tax_rate: float = 0.06  # state + local sales tax rate
    property_tax_abatement_years: int = 0
    itc_pct: float = 0.0  # ITC as % of qualifying renewable CapEx
    qualifying_renewable_capex: float = 0.0  # USD
    bonus_depreciation_pct: float = 1.0  # 100% post-OBBBA
    depreciable_pct_of_capex: float = 0.50  # % reclassified via cost seg
    corporate_tax_rate: float = 0.21
    section_179d_sqft: float = 0.0  # building square footage
    section_179d_rate: float = 5.36  # USD per sqft (2026 inflation-adjusted)
    oz_eligible: bool = False


@dataclass
class AnnualOpEx:
    """Single year operating expenditure breakdown."""
    year: int
    power_cost: float
    staffing: float
    maintenance: float
    insurance: float
    property_tax: float
    software_misc: float
    total: float
    escalation_factor: float


@dataclass
class TaxIncentive:
    """A single tax incentive line item."""
    name: str
    value: float
    eligible: bool
    notes: str = ""


@dataclass
class SensitivityResult:
    """Result of varying one input parameter."""
    variable: str
    base_npv: float
    low_npv: float
    high_npv: float
    impact_pct: float  # max absolute % change from base


@dataclass
class TCOResult:
    """Complete TCO calculation result."""
    total_capex: float
    annual_opex: List[dict]
    total_opex: float
    total_tco: float
    npv: float
    tax_incentive_total: float
    tax_incentives: List[dict]
    sensitivity: List[dict]
    inputs_summary: dict


# ---------------------------------------------------------------------------
# Core calculation functions
# ---------------------------------------------------------------------------

def calculate_capex(inputs: TCOInputs) -> float:
    """Calculate total capital expenditure."""
    it_load_mw = inputs.it_load_kw / 1000.0
    return it_load_mw * inputs.capex_per_mw


def calculate_annual_opex(inputs: TCOInputs, capex: float) -> List[AnnualOpEx]:
    """Calculate year-by-year operating expenditure with escalation."""
    if inputs.total_facility_kw <= 0:
        total_facility_kw = inputs.it_load_kw * inputs.pue
    else:
        total_facility_kw = inputs.total_facility_kw

    it_load_mw = inputs.it_load_kw / 1000.0
    escalation = 1.0 + (inputs.annual_escalation_pct / 100.0)
    me_capex = capex * 0.65  # M&E is typically 65% of total CapEx

    results = []
    for yr in range(1, inputs.analysis_years + 1):
        esc = escalation ** (yr - 1)

        power = total_facility_kw * inputs.power_cost_kwh * 8760 * esc
        staff = it_load_mw * inputs.staffing_per_mw * inputs.loaded_cost_per_fte * esc
        maint = me_capex * inputs.maintenance_pct_of_capex * esc
        ins = capex * inputs.insurance_pct * esc

        # Property tax: zero during abatement period
        if yr <= inputs.property_tax_abatement_years:
            prop_tax = 0.0
        else:
            prop_tax = capex * inputs.property_tax_rate * esc

        software = it_load_mw * 50_000 * esc  # ~$50K/MW for DCIM, BMS, etc.

        total = power + staff + maint + ins + prop_tax + software

        results.append(AnnualOpEx(
            year=yr,
            power_cost=round(power, 2),
            staffing=round(staff, 2),
            maintenance=round(maint, 2),
            insurance=round(ins, 2),
            property_tax=round(prop_tax, 2),
            software_misc=round(software, 2),
            total=round(total, 2),
            escalation_factor=round(esc, 4),
        ))
    return results


def calculate_npv(capex: float, annual_opex: List[AnnualOpEx],
                  discount_rate: float, tax_savings: float = 0.0) -> float:
    """Calculate Net Present Value of all costs (negative = cost)."""
    npv = capex - tax_savings  # year 0 CapEx minus tax savings
    for opex in annual_opex:
        npv += opex.total / ((1 + discount_rate) ** opex.year)
    return round(npv, 2)


def calculate_tax_incentives(inputs: TCOInputs, capex: float) -> List[TaxIncentive]:
    """Calculate all applicable tax incentive line items."""
    incentives = []

    # Sales tax exemption
    if inputs.sales_tax_exempt:
        # Equipment + materials typically 70-80% of CapEx
        taxable_portion = capex * 0.75
        savings = taxable_portion * inputs.sales_tax_rate
        incentives.append(TaxIncentive(
            name="Sales Tax Exemption",
            value=round(savings, 2),
            eligible=True,
            notes=f"Exemption on equipment and materials ({inputs.state})"
        ))
    else:
        incentives.append(TaxIncentive(
            name="Sales Tax Exemption",
            value=0.0,
            eligible=False,
            notes="Not exempt in this jurisdiction"
        ))

    # Property tax abatement
    if inputs.property_tax_abatement_years > 0:
        annual_tax = capex * inputs.property_tax_rate
        savings = annual_tax * inputs.property_tax_abatement_years
        incentives.append(TaxIncentive(
            name="Property Tax Abatement",
            value=round(savings, 2),
            eligible=True,
            notes=f"{inputs.property_tax_abatement_years}-year abatement"
        ))

    # Federal ITC on qualifying renewable CapEx
    if inputs.itc_pct > 0 and inputs.qualifying_renewable_capex > 0:
        itc_value = inputs.qualifying_renewable_capex * inputs.itc_pct
        incentives.append(TaxIncentive(
            name="Federal ITC",
            value=round(itc_value, 2),
            eligible=True,
            notes=f"{inputs.itc_pct * 100:.0f}% on ${inputs.qualifying_renewable_capex:,.0f} qualifying renewable CapEx"
        ))

    # Bonus depreciation (100% post-OBBBA)
    if inputs.bonus_depreciation_pct > 0:
        depreciable_amount = capex * inputs.depreciable_pct_of_capex
        year1_deduction = depreciable_amount * inputs.bonus_depreciation_pct
        tax_savings = year1_deduction * inputs.corporate_tax_rate
        incentives.append(TaxIncentive(
            name="Bonus Depreciation (100% Post-OBBBA)",
            value=round(tax_savings, 2),
            eligible=True,
            notes=f"100% on ${depreciable_amount:,.0f} reclassified via cost segregation"
        ))

    # Section 179D
    if inputs.section_179d_sqft > 0:
        deduction = inputs.section_179d_sqft * inputs.section_179d_rate
        tax_savings_179d = deduction * inputs.corporate_tax_rate
        incentives.append(TaxIncentive(
            name="Section 179D Deduction",
            value=round(tax_savings_179d, 2),
            eligible=True,
            notes=f"${inputs.section_179d_rate}/sqft on {inputs.section_179d_sqft:,.0f} sqft (sunset June 30, 2026)"
        ))

    # Opportunity Zone
    if inputs.oz_eligible:
        # Model assumes capital gains equal to 20% of CapEx invested via QOF
        assumed_gains = capex * 0.20
        # 10-year hold: full exclusion of appreciation on QOF investment
        # Plus basis step-up: 15% at 7 years
        basis_step_up_savings = assumed_gains * 0.15 * inputs.corporate_tax_rate
        incentives.append(TaxIncentive(
            name="Opportunity Zone Benefits",
            value=round(basis_step_up_savings, 2),
            eligible=True,
            notes="Capital gains deferral + 15% basis step-up (7yr hold); full exclusion at 10yr"
        ))

    return incentives


def run_sensitivity(inputs: TCOInputs, variable: str,
                    range_pct: float = 0.20) -> SensitivityResult:
    """Vary one input parameter and return NPV impact."""
    # Base case
    capex_base = calculate_capex(inputs)
    opex_base = calculate_annual_opex(inputs, capex_base)
    incentives_base = calculate_tax_incentives(inputs, capex_base)
    tax_savings_base = sum(i.value for i in incentives_base if i.eligible)
    npv_base = calculate_npv(capex_base, opex_base, inputs.discount_rate, tax_savings_base)

    # Create modified inputs for low and high scenarios
    def _modify(inp: TCOInputs, var: str, factor: float) -> TCOInputs:
        """Return a copy of inputs with one variable modified."""
        d = {
            "it_load_kw": inp.it_load_kw,
            "total_facility_kw": inp.total_facility_kw,
            "pue": inp.pue,
            "capex_per_mw": inp.capex_per_mw,
            "power_cost_kwh": inp.power_cost_kwh,
            "annual_escalation_pct": inp.annual_escalation_pct,
            "discount_rate": inp.discount_rate,
            "analysis_years": inp.analysis_years,
            "state": inp.state,
            "staffing_per_mw": inp.staffing_per_mw,
            "loaded_cost_per_fte": inp.loaded_cost_per_fte,
            "maintenance_pct_of_capex": inp.maintenance_pct_of_capex,
            "insurance_pct": inp.insurance_pct,
            "property_tax_rate": inp.property_tax_rate,
            "sales_tax_exempt": inp.sales_tax_exempt,
            "sales_tax_rate": inp.sales_tax_rate,
            "property_tax_abatement_years": inp.property_tax_abatement_years,
            "itc_pct": inp.itc_pct,
            "qualifying_renewable_capex": inp.qualifying_renewable_capex,
            "bonus_depreciation_pct": inp.bonus_depreciation_pct,
            "depreciable_pct_of_capex": inp.depreciable_pct_of_capex,
            "corporate_tax_rate": inp.corporate_tax_rate,
            "section_179d_sqft": inp.section_179d_sqft,
            "section_179d_rate": inp.section_179d_rate,
            "oz_eligible": inp.oz_eligible,
        }
        if var == "power_cost":
            d["power_cost_kwh"] = inp.power_cost_kwh * factor
        elif var == "pue":
            d["pue"] = inp.pue + (0.1 if factor > 1 else -0.1)
            d["total_facility_kw"] = inp.it_load_kw * d["pue"]
        elif var == "construction_cost":
            d["capex_per_mw"] = inp.capex_per_mw * factor
        elif var == "discount_rate":
            d["discount_rate"] = inp.discount_rate + (0.02 if factor > 1 else -0.02)
        elif var == "utilization":
            d["it_load_kw"] = inp.it_load_kw * factor
            d["total_facility_kw"] = d["it_load_kw"] * inp.pue
        return TCOInputs(**d)

    def _npv_for(modified: TCOInputs) -> float:
        c = calculate_capex(modified)
        o = calculate_annual_opex(modified, c)
        i = calculate_tax_incentives(modified, c)
        ts = sum(x.value for x in i if x.eligible)
        return calculate_npv(c, o, modified.discount_rate, ts)

    low_inputs = _modify(inputs, variable, 1 - range_pct)
    high_inputs = _modify(inputs, variable, 1 + range_pct)
    npv_low = _npv_for(low_inputs)
    npv_high = _npv_for(high_inputs)

    max_delta = max(abs(npv_low - npv_base), abs(npv_high - npv_base))
    impact_pct = (max_delta / abs(npv_base) * 100) if npv_base != 0 else 0.0

    return SensitivityResult(
        variable=variable,
        base_npv=npv_base,
        low_npv=npv_low,
        high_npv=npv_high,
        impact_pct=round(impact_pct, 2),
    )


def calculate_tco(inputs: TCOInputs) -> TCOResult:
    """Run the full TCO calculation."""
    # Derive total facility load if not provided
    if inputs.total_facility_kw <= 0:
        inputs.total_facility_kw = inputs.it_load_kw * inputs.pue

    capex = calculate_capex(inputs)
    annual_opex = calculate_annual_opex(inputs, capex)
    total_opex = sum(yr.total for yr in annual_opex)
    total_tco = capex + total_opex

    tax_incentives = calculate_tax_incentives(inputs, capex)
    tax_savings = sum(i.value for i in tax_incentives if i.eligible)

    npv = calculate_npv(capex, annual_opex, inputs.discount_rate, tax_savings)

    # Sensitivity analysis
    sensitivity_vars = [
        "power_cost", "pue", "construction_cost",
        "discount_rate", "utilization",
    ]
    sensitivity = [run_sensitivity(inputs, v) for v in sensitivity_vars]

    return TCOResult(
        total_capex=round(capex, 2),
        annual_opex=[asdict(yr) for yr in annual_opex],
        total_opex=round(total_opex, 2),
        total_tco=round(total_tco, 2),
        npv=round(npv, 2),
        tax_incentive_total=round(tax_savings, 2),
        tax_incentives=[asdict(i) for i in tax_incentives],
        sensitivity=[asdict(s) for s in sensitivity],
        inputs_summary={
            "it_load_kw": inputs.it_load_kw,
            "it_load_mw": inputs.it_load_kw / 1000.0,
            "total_facility_kw": inputs.total_facility_kw,
            "pue": inputs.pue,
            "capex_per_mw": inputs.capex_per_mw,
            "power_cost_kwh": inputs.power_cost_kwh,
            "discount_rate": inputs.discount_rate,
            "analysis_years": inputs.analysis_years,
            "state": inputs.state,
        },
    )


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------

def parse_args() -> argparse.Namespace:
    """Parse command-line arguments."""
    parser = argparse.ArgumentParser(
        description="Calculate Total Cost of Ownership for data center projects",
        epilog="Example: python3 tco-model.py --it-load-kw 10000 --pue 1.35 --power-cost 0.065 --state VA",
    )

    parser.add_argument("--input", metavar="FILE",
                        help="JSON input file with TCOInputs fields")
    parser.add_argument("--output", metavar="FILE",
                        help="JSON output file (default: stdout)")

    # Quick-run CLI args (alternative to --input)
    parser.add_argument("--it-load-kw", type=float, default=10000,
                        help="IT load in kW (default: 10000)")
    parser.add_argument("--pue", type=float, default=1.35,
                        help="Power Usage Effectiveness (default: 1.35)")
    parser.add_argument("--power-cost", type=float, default=0.065,
                        help="Power cost in USD/kWh (default: 0.065)")
    parser.add_argument("--capex-per-mw", type=float, default=11_000_000,
                        help="CapEx per MW of IT load in USD (default: 11000000)")
    parser.add_argument("--discount-rate", type=float, default=0.08,
                        help="Discount rate / WACC (default: 0.08)")
    parser.add_argument("--years", type=int, default=10,
                        help="Analysis horizon in years (default: 10)")
    parser.add_argument("--state", type=str, default="VA",
                        help="US state for tax incentive context (default: VA)")
    parser.add_argument("--escalation", type=float, default=3.0,
                        help="Annual cost escalation percent (default: 3.0)")
    parser.add_argument("--no-sales-tax-exempt", action="store_true",
                        help="Disable sales tax exemption")
    parser.add_argument("--property-tax-abatement-years", type=int, default=0,
                        help="Years of property tax abatement (default: 0)")
    parser.add_argument("--itc-pct", type=float, default=0.0,
                        help="ITC percentage on qualifying renewable CapEx (default: 0)")
    parser.add_argument("--renewable-capex", type=float, default=0.0,
                        help="Qualifying renewable CapEx in USD (default: 0)")
    parser.add_argument("--section-179d-sqft", type=float, default=0.0,
                        help="Building sqft for Section 179D deduction (default: 0)")
    parser.add_argument("--oz", action="store_true",
                        help="Site is in a designated Opportunity Zone")

    return parser.parse_args()


def main():
    """Entry point."""
    args = parse_args()

    if args.input:
        with open(args.input) as f:
            data = json.load(f)
        inputs = TCOInputs(**{k: v for k, v in data.items()
                              if k in TCOInputs.__dataclass_fields__})
    else:
        inputs = TCOInputs(
            it_load_kw=args.it_load_kw,
            pue=args.pue,
            power_cost_kwh=args.power_cost,
            capex_per_mw=args.capex_per_mw,
            discount_rate=args.discount_rate,
            analysis_years=args.years,
            state=args.state,
            annual_escalation_pct=args.escalation,
            sales_tax_exempt=not args.no_sales_tax_exempt,
            property_tax_abatement_years=args.property_tax_abatement_years,
            itc_pct=args.itc_pct,
            qualifying_renewable_capex=args.renewable_capex,
            section_179d_sqft=args.section_179d_sqft,
            oz_eligible=args.oz,
        )

    result = calculate_tco(inputs)
    output_json = json.dumps(asdict(result), indent=2)

    if args.output:
        with open(args.output, "w") as f:
            f.write(output_json)
            f.write("\n")
        print(f"TCO results written to {args.output}", file=sys.stderr)
    else:
        print(output_json)


if __name__ == "__main__":
    main()
