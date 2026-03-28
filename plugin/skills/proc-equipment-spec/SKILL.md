---
name: proc-equipment-spec
description: "Generate detailed equipment specifications for data center procurement with performance requirements, compliance standards, and acceptance criteria. Use when writing equipment specs, specifying DC hardware requirements, preparing procurement specifications, or defining acceptance criteria for data center equipment. Trigger with \"equipment spec\", \"hardware specification\", \"procurement spec\", \"equipment requirements\", \"DC equipment\", or \"specify data center hardware\"."
argument-hint: "<equipment-category>"
---

# Equipment Specification Generator

Generate vendor-neutral performance specifications for data center equipment categories.
Produces specification documents suitable for competitive procurement -- quantitative
performance targets replace brand-specific language to ensure fair bidding.

## Phase 1: Critical Discovery

> Answer these questions first. They determine the entire specification scope.

**Project Context:**

1. Which equipment categories need specifications? Select all that apply:
   - **Power distribution:** Switchgear, UPS, PDU/RPP, Generator, ATS
   - **Cooling:** Chiller, CRAH/CRAC, CDU (liquid cooling), Cooling tower, Dry cooler
   - **Infrastructure:** Racks/cabinets, Structured cabling, Raised floor/cable tray
   - **Life safety:** Fire detection, Fire suppression (clean agent, pre-action)
   - **Security:** Access control, CCTV/video surveillance, Intrusion detection
   - **Monitoring:** BMS, DCIM, Environmental sensors, Power metering

2. What facility type?
   - Traditional enterprise (single-tenant, 2-20MW)
   - Hyperscale (cloud provider, 20-500MW+)
   - Sovereign (government/national security)
   - Colocation (multi-tenant, retail or wholesale)
   - Modular/prefab (factory-built, rapid deployment)
   - Edge (1-5MW, distributed)

3. What facility tier (redundancy level)?
   - Tier I (basic, no redundancy)
   - Tier II (redundant components, N+1)
   - Tier III (concurrently maintainable, N+1 minimum)
   - Tier IV (fault tolerant, 2N or 2N+1)

4. What is the target IT capacity (MW)?

5. What cooling technology is planned?
   - Air-cooled (CRAH/CRAC with raised floor or in-row)
   - Liquid-cooled (direct-to-chip, immersion, rear-door HEX)
   - Hybrid (air for general compute, liquid for high density)

6. What target rack density range (kW per rack)?
   - Standard density (4-10 kW/rack)
   - Medium density (10-25 kW/rack)
   - High density (25-50 kW/rack)
   - Ultra-high density (50-100+ kW/rack)

7. What specification format is preferred?
   - **Performance-based:** Define outcomes and let vendors propose solutions
   - **Prescriptive:** Define exact requirements and configurations
   - **Hybrid:** Performance-based with prescriptive minimums

## Phase 2: Context Refinement

> Based on Phase 1 answers, gather additional detail.

### Power Equipment Path

If power distribution equipment is selected:

1. What utility voltage and configuration? (13.8kV, 34.5kV, single/dual feed)
2. UPS topology preference? (static double-conversion, rotary, modular scalable)
3. Generator fuel type? (diesel, natural gas, bi-fuel)
4. Altitude of installation site? (affects generator derating above 1,000ft)

### Cooling Equipment Path

If cooling equipment is selected:

1. Climate zone per ASHRAE classification? (A1-A4, H1)
2. Design wet-bulb and dry-bulb temperatures?
3. Water availability and quality? (municipal, reclaimed, well, no water)
4. Noise restrictions at property boundary? (dBA limit)

### Infrastructure/Security Path

If racks, cabling, or security equipment is selected:

1. Seismic zone? (Zone 0-4 -- affects rack bracing and anchoring requirements)
2. Floor loading capacity? (psf -- determines rack weight limits)
3. Security clearance level? (unclassified, CUI, classified, SCIF)

## What I Need from Upstream

**From power-capacity-model (eng-power-model):**
- Utility feed voltage and capacity
- UPS configuration and capacity per module
- PDU/RPP distribution architecture
- Redundancy tier and configuration (N, N+1, 2N)
- Generator sizing and runtime requirements

**From cooling-design-report (eng-cooling-design):**
- Cooling technology selection and capacity
- Equipment list with sizing (chillers, CRAHs, CDUs)
- Water consumption requirements
- Design temperatures (supply/return)

If upstream artifacts are not available, I will ask you for the technical
requirements or generate specifications with [TO BE CONFIRMED] placeholders.

## Facility Type Parameters

| Parameter | Traditional | Hyperscale | Sovereign | Colo | Modular | Edge |
|-----------|-------------|------------|-----------|------|---------|------|
| Spec format | Hybrid | Performance | Prescriptive | Performance | Prescriptive | Performance |
| Testing rigor | Standard | Extended | Maximum | Standard | Factory + field | Minimal |
| Warranty typical | 1 year | 3-5 years | 5 years | 1-2 years | 2 years | 1 year |
| Domestic sourcing | Optional | Optional | Required | Optional | Preferred | N/A |
| Documentation depth | Standard | Detailed | Comprehensive | Standard | Pre-packaged | Minimal |

## Specification Assembly Process

For each selected equipment category, generate a specification sheet containing:

### 1. Performance Requirements
- Quantitative capacity targets (kW, kVA, BTU/hr, CFM, GPM)
- Efficiency requirements at specified load points (25%, 50%, 75%, 100%)
- Operating range (temperature, humidity, altitude)
- Response time and transfer time requirements (where applicable)

### 2. Environmental Requirements
- Operating temperature range per ASHRAE TC 9.9 (if applicable)
- Humidity tolerance range
- Altitude derating factors (generators, cooling equipment)
- Acoustic limits (dBA at specified distance)
- Ingress protection rating (IP rating for outdoor equipment)

### 3. Compliance Requirements
- UL/cUL listing or CE marking
- NEMA ratings (enclosures, motor types)
- ASHRAE standards (90.4, TC 9.9 -- as applicable)
- NFPA compliance (75, 76, 855 -- as applicable)
- Seismic certification (OSHPD, IBC -- if seismic zone 2+)
- BICSI 002-2024 (structured cabling)

### 4. Interface Requirements
- Electrical connections (voltage, phase, amperage, connector type)
- Communication protocols (Modbus TCP/IP, BACnet, SNMP v3)
- Physical dimensions and weight constraints
- Piping connections (size, material, pressure rating -- cooling)
- Integration with BMS/DCIM platform

### 5. Warranty and Support Requirements
- Minimum warranty period
- On-site spare parts inventory
- Response time for warranty service (2hr/4hr/next business day)
- Preventive maintenance requirements and intervals
- End-of-life and spare parts availability commitment (10 years minimum)

### 6. Testing and Acceptance
- Factory acceptance test (FAT) requirements and witness provisions
- Site acceptance test (SAT) procedures
- Performance verification testing methodology
- Commissioning requirements and duration
- Integrated systems testing with adjacent equipment

## Reference Data

Load on demand -- do not read upfront:

- [Cost benchmarks](../../references/COST-BENCHMARKS.md) -- Regional equipment cost ranges for specification reasonableness check

## Output Template

This skill produces two files:

### Markdown Report: `<project-name>-equipment-specifications.md`

**Project:** [Project Name]
**Date:** [Date]
**Prepared by:** [Skill: proc-equipment-spec v1.0]

For each equipment category, a specification sheet with all 6 sections above.
Each specification uses "or approved equal" language to maintain vendor neutrality.
Performance targets are quantitative and testable.

### JSON Sidecar: `<project-name>-equipment-specifications.json`

```json
{
  "artifact_type": "equipment-specifications",
  "skill_version": "1.0",
  "project_name": "...",
  "facility_type": "traditional | hyperscale | sovereign | colo | modular | edge",
  "tier": "I | II | III | IV",
  "it_capacity_mw": 0,
  "spec_format": "performance | prescriptive | hybrid",
  "equipment_categories": [
    {
      "category": "UPS",
      "capacity": "2000 kVA",
      "redundancy": "N+1",
      "key_requirements": ["double-conversion", "lithium iron phosphate", ">96% efficiency at 50% load"],
      "compliance": ["UL 1778", "NFPA 855"]
    }
  ],
  "upstream_sources": {
    "power": "power-capacity-model | manual | placeholder",
    "cooling": "cooling-design-report | manual | placeholder"
  }
}
```

## Gotchas

- **Vendor-neutral specs must avoid brand-specific terminology.** Write "lithium iron phosphate UPS with double-conversion topology" not "Vertiv Liebert EXL S1." Specify chemistry, topology, and performance. Include "or approved equal" on every specification line item.

- **Generator specs must include altitude derating.** A 2MW generator at 5,000ft elevation delivers only ~1.7MW (3.5% derating per 1,000ft above 1,000ft). Sea-level rated capacity is meaningless without altitude context. Always specify site altitude and derated capacity.

- **"Or approved equal" language is mandatory for competitive procurement.** Without it, the specification becomes a sole-source document even with vendor-neutral performance language. Define the criteria for "approved equal" (meet or exceed all performance requirements in the specification).

- **UPS efficiency specs must state the load point.** A UPS claiming 96% efficiency at 100% load may only achieve 90% at 25% load. In 2N configurations where each UPS runs at ~25% load, the part-load efficiency dominates operating cost. Always specify efficiency at 25%, 50%, 75%, and 100% load points.

- **Cooling equipment specs must specify both sensible and total cooling capacity.** Data center loads are almost entirely sensible heat. A CRAH rated at 200kW total capacity may only deliver 160kW sensible. Sensible Heat Ratio (SHR > 0.95) should be specified for DC cooling equipment.

## Evaluations

See `evals/evals.json` for test scenarios covering full facility, liquid cooling retrofit, and high-altitude specifications.
