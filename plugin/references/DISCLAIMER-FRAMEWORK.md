# Disclaimer Framework

> Source of truth for all disclaimer language in Stellenium DC Skills.
> Financial skills (fin-*) and compliance skills (comp-*) MUST include
> the relevant verbatim paragraphs below in their output.

**As-of:** 2026-03-27
**Next review:** 2026-06-27
**Staleness warning:** 90 days

---

## Financial Disclaimer

For all fin-* skills. Include in full in every financial skill output.

FINANCIAL DISCLAIMER: The financial projections, cost estimates, and economic
analyses produced by this skill are for preliminary planning and evaluation
purposes only. This is not investment advice, financial advice, or
a recommendation to proceed with any transaction. Actual costs, revenues, and
returns will vary based on market conditions, vendor negotiations, site-specific
factors, and regulatory changes not modeled here.

All financial outputs are presented as ranges where possible. Point estimates
should be treated as order-of-magnitude guidance, not bankable figures. Users
must engage qualified financial advisors, tax professionals, and legal counsel
before making investment decisions based on these outputs.

Sensitivity analyses are provided to illustrate the impact of key variable
changes. They do not represent probabilistic forecasts or guarantee that
outcomes will fall within the stated ranges.

---

## Regulatory and Compliance Disclaimer

For all comp-* skills. Include in full in every compliance skill output.

REGULATORY DISCLAIMER: The regulatory analysis, compliance guidance, and
jurisdiction-specific information produced by this skill reflect the regulatory
landscape as of the skill's publication date. Regulations change frequently --
new legislation, executive orders, court decisions, and regulatory guidance can
alter requirements without notice.

This output does not constitute legal advice. Users must verify all regulatory
requirements with qualified local counsel in each relevant jurisdiction before
relying on this analysis for compliance decisions, permit applications, or
contractual obligations.

Where jurisdiction-specific caveats are noted, they highlight known areas of
regulatory complexity or recent change. Absence of a caveat does not imply
regulatory simplicity or stability.

---

## Tax Disclaimer

For skills referencing FEDERAL-TAX-GUIDE.md. Include alongside the Financial
Disclaimer when tax incentive calculations are part of the output.

TAX DISCLAIMER: Tax incentive calculations (ITC, PTC, MACRS, Section 179D,
Opportunity Zones, cost segregation, bonus depreciation) are estimates based
on current tax law as of the reference data publication date. Tax law is
subject to legislative change, IRS guidance updates, and judicial
interpretation.

Tax benefits modeled here assume qualification criteria are met. Actual
qualification depends on project-specific facts reviewed by a qualified tax
advisor. Do not rely on these estimates for tax planning, tax filing, or
investment structuring without professional tax counsel.

---

## How to Use This Framework

### For fin-* skills:
Include the Financial Disclaimer in full in your skill's output.
If the skill references FEDERAL-TAX-GUIDE.md, also include the Tax Disclaimer.

### For comp-* skills:
Include the Regulatory and Compliance Disclaimer in full in your skill's output.

### Formatting:
Place disclaimers at the END of skill output, after all analysis sections.
Use a horizontal rule (---) to visually separate disclaimers from analysis.

### CI Enforcement:
The validation pipeline checks that fin-* and comp-* skills reference
DISCLAIMER-FRAMEWORK.md. The verbatim text must appear in the skill's
output template or be loaded from this file at runtime.
