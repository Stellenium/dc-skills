---
name: eng-fire-life-safety
description: "Design fire detection, suppression, and life safety systems for data centers covering NFPA 75, NFPA 76, and NFPA 2001 compliance. Use when designing fire suppression for a DC, selecting clean agent systems, planning fire detection, or ensuring NFPA compliance for data center facilities. Trigger with \"fire suppression\", \"life safety\", \"NFPA\", \"fire detection\", \"clean agent\", \"fire protection for data center\", or \"FM-200\"."
---

# Fire & Life Safety Design

Design fire detection, suppression, and life safety systems for data center
facilities. Covers NFPA 75 (IT equipment), NFPA 76 (telecom), and NFPA 855
(energy storage) with clean agent, pre-action sprinkler, and VESDA systems.
Produces a comprehensive fire/life safety design with zone mapping, system
selection, code compliance, and cost estimation.

## What I Need from Upstream

**From power-capacity-model (eng-power-model):**
- Total IT load and facility layout (number of IT rooms, power density)
- UPS and battery configuration (BESS presence triggers NFPA 855)
- Generator type and fuel storage (diesel, natural gas)
- Redundancy tier (affects suppression zone redundancy)

If upstream data is not available, I will ask for facility parameters
directly or use industry-standard defaults.

## Phase 1: Critical Discovery

> Answer these questions first. They determine the entire fire/life safety approach.

**Project Context:**

1. What facility type?
   - Hyperscale (campus with multiple buildings, dedicated fire pump house)
   - Colocation (multi-tenant, tenant-demarcated suppression zones)
   - Enterprise (single-tenant, single building)
   - Modular/prefab (factory-integrated suppression)
   - Edge (simplified systems, remote monitoring)
   - Sovereign (enhanced requirements per government standards)

2. What Tier level?
   - Tier I/II (basic protection, single suppression path)
   - Tier III (concurrently maintainable, suppression must not interrupt operations)
   - Tier IV (fault tolerant, redundant suppression systems)

3. Is battery energy storage (BESS) on-site?
   - Yes -- lithium-ion (triggers NFPA 855 compliance)
   - Yes -- other chemistry (specify)
   - No BESS

4. What is the suppression preference for IT spaces?
   - Clean agent (FM-200/HFC-227ea or Novec 1230/FK-5-1-12)
   - Inert gas (IG-541 Inergen, IG-55 Argonite)
   - Pre-action sprinkler (double interlock)
   - Water mist
   - No preference (recommend based on facility type)

5. Who is the authority having jurisdiction (AHJ)?
   - Local fire marshal (specify jurisdiction)
   - State fire marshal
   - Federal (DoD, GSA)
   - International (specify country/standard)

6. Is the facility occupied or unmanned?
   - 24/7 occupied (staffed NOC and operations)
   - Business-hours occupied with after-hours remote monitoring
   - Unmanned with remote monitoring only

7. How many floors?
   - Single story
   - Multi-story (specify count)

8. What is the total IT room area (sqft)?
   - Approximate total white space area
   - Number of discrete IT rooms/halls

## Phase 2: Context Refinement

> Based on Phase 1 answers, gather system-specific detail.

### BESS Path (if BESS present)

1. What is the BESS capacity (MWh) and chemistry?
2. Is the BESS indoor or outdoor?
3. What is the BESS rack configuration and spacing?
4. Has a thermal runaway propagation study been completed?

### Colo Path (if multi-tenant)

1. How are tenant cages/suites arranged?
2. Do tenants require independent suppression zones?
3. What is the tenant notification protocol for suppression activation?
4. Who controls suppression system impairment during tenant work?

### Facility Type Parameters

| Parameter | Hyperscale | Colo | Enterprise | Modular | Edge |
|-----------|------------|------|------------|---------|------|
| Fire water supply | Campus loop, dedicated pump | Building riser, city main | City main or on-site tank | Integrated tank/agent | Agent cylinder |
| IT room suppression | Clean agent or pre-action | Clean agent per zone | Clean agent | Factory-integrated clean agent | Agent cylinder |
| Detection | VESDA + spot-type | VESDA per tenant zone | VESDA or spot-type | VESDA | Spot-type |
| BESS suppression | Dedicated NFPA 855 | Per tenant BESS | Dedicated zone | Integrated | Rarely applicable |
| Cost range ($/sqft) | $8-15 IT, $3-6 non-IT | $10-18 IT | $8-15 IT | Factory-included | $15-25 |

## Detection Systems

### Detection Technology Comparison

| Technology | Detection Speed | False Alarm Rate | Coverage | Best Use | NFPA Reference |
|------------|----------------|------------------|----------|----------|----------------|
| VESDA (aspirating smoke detection) | Very early (pre-combustion) | Very low | Air-sampling network, 1 detector per 1,500-5,000 sqft | IT rooms, under-floor, above-ceiling | NFPA 76 Sec 6.5 |
| Spot-type smoke (photoelectric) | Early | Moderate | 1 per 900 sqft (30ft spacing) | Offices, corridors, support rooms | NFPA 72 |
| Spot-type smoke (ionization) | Very early for flaming fires | Higher | 1 per 900 sqft | NOT recommended for DCs (false alarms from dust) | NFPA 72 |
| Linear heat detection | Late (only for heat events) | Very low | Cable run length | Cable trays, generator rooms | NFPA 72 |
| Flame detection (IR/UV) | Fast for open flame | Low | Line-of-sight, 50-100ft range | Generator rooms, fuel storage | NFPA 72 |

### VESDA Zone Design

- Install VESDA in all IT rooms, under-floor plenums, and above-ceiling plenums
- Air-sampling pipe network with capillary tubes at rack-level
- Four alarm thresholds: Alert (0.005% obs/ft), Action (0.05%), Fire 1 (0.1%), Fire 2 (0.15%)
- Integration with BMS for HVAC shutdown on Fire 1 alarm
- VESDA per-zone: each IT room is an independent VESDA zone

## Suppression Systems

### Clean Agent Systems (IT Spaces)

**FM-200 (HFC-227ea):**
- Design concentration: 7.0-7.9% (NFPA 2001)
- Discharge time: 10 seconds maximum
- Room integrity required (door fan test per NFPA 2001 Annex C)
- Pressure relief venting required to prevent structural damage
- GWP: 3,220 (high -- regulatory phase-down risk in EU and some US states)

**Novec 1230 (FK-5-1-12):**
- Design concentration: 4.2-5.9% (NFPA 2001)
- Discharge time: 10 seconds maximum
- Room integrity required (same door fan test)
- Pressure relief venting required
- GWP: 1 (preferred for sustainability-focused projects)

**Inert Gas (IG-541 Inergen):**
- Design concentration: 36.5-43.0% (reduces O2 to 12.5%)
- Discharge time: 60 seconds maximum
- Large cylinder storage (3x volume of clean agent for same coverage)
- No room integrity requirement (gas dissipates naturally)
- GWP: 0 (best environmental profile)

### Pre-Action Sprinkler (General Areas and Belt-and-Suspenders)

- Double interlock pre-action: requires both detection alarm AND sprinkler head activation
- Prevents water discharge from accidental pipe damage (critical for IT spaces)
- Used as secondary system over clean agent in AHJ-required jurisdictions
- NFPA 13 design density: Ordinary Hazard Group 1 (0.15 gpm/sqft over 1,500 sqft)

### BESS Fire Protection (NFPA 855)

- Thermal runaway detection: off-gas sensors (CO, H2, VOC) and cell temperature monitoring
- Suppression: water-based (sprinkler or deluge) is NFPA 855 preferred for lithium-ion
- Deflagration venting: explosion relief panels for enclosed BESS rooms
- Spacing: minimum 3ft between battery racks, 10ft from walls (NFPA 855 Table 11.1.2)
- Ventilation: mechanical exhaust to prevent flammable gas accumulation
- Thermal barrier: 2-hour fire-rated separation between BESS and IT spaces

## Life Safety

### Egress Design

- Maximum travel distance: 200ft (unsprinklered) / 250ft (sprinklered) per IBC
- Minimum 2 exits per IT room >1,000 sqft
- Emergency lighting: 90-minute battery backup on all egress paths
- Exit signage: illuminated, on emergency power circuit
- Knox box at main entrance for fire department access
- Fire command center: required for buildings >75ft or with fire alarm > 50 devices

### Fire Department Access

- Fire department connection (FDC) within 100ft of fire lane
- Fire lane: 20ft minimum width, 13ft-6in vertical clearance
- Fire hydrant spacing: 300ft maximum along fire lane
- Key box (Knox) at all secured entries
- Fire department pre-plan document (updated annually)

## Output

This skill produces two files:
1. `<project-name>-fire-life-safety-design.md` -- Full report
2. `<project-name>-fire-life-safety-design.json` -- Structured data

### JSON Sidecar

```json
{
  "artifact_type": "fire-life-safety-design",
  "skill_version": "1.0",
  "project_name": "...",
  "detection_systems": [
    {"zone": "...", "type": "VESDA | spot-smoke | linear-heat | flame", "coverage_sqft": 0}
  ],
  "suppression_systems": [
    {"zone": "...", "type": "clean-agent | pre-action | inert-gas | water-mist | deluge", "agent": "...", "discharge_time_sec": 0, "concentration_pct": 0}
  ],
  "nfpa_compliance": {
    "nfpa_75": true,
    "nfpa_76": false,
    "nfpa_855": false
  },
  "egress": {
    "exits": 0,
    "travel_distance_ft": 0,
    "emergency_lighting": true
  },
  "estimated_cost_range": "$X-Y per sqft"
}
```

## Gotchas

- **NFPA 855 spacing requirements for lithium-ion BESS can consume 40% more floor area than electrical design alone.** Battery rack spacing (3ft minimum between racks, 10ft from walls), deflagration venting, and 2-hour fire-rated separation from IT spaces dramatically increase BESS room footprint. Coordinate BESS layout with structural and electrical teams BEFORE finalizing building dimensions.

- **Clean agent systems require room integrity testing (door fan test) that fails if cable penetrations are not properly firestopped.** Every cable tray, conduit, and pipe penetration through IT room walls and floors must be firestopped with rated materials. A single un-firestopped penetration can cause the door fan test to fail, requiring costly remediation after construction.

- **Some AHJs require sprinklers OVER clean agent systems (belt-and-suspenders).** This doubles the installed cost and adds water piping into IT spaces. Negotiate early with the AHJ -- present UL-listed clean agent system data and NFPA 75 provisions that explicitly allow clean agent as the sole suppression in IT rooms.

- **VESDA air-sampling systems must be commissioned with the HVAC system running at design airflow.** Aspirating smoke detection sensitivity is calibrated to specific airflow patterns. If VESDA is commissioned with HVAC off or at reduced flow, detection thresholds will be wrong when the facility operates at full load. Commission VESDA AFTER HVAC commissioning.

- **FM-200 (HFC-227ea) faces regulatory phase-down under the Kigali Amendment and EU F-Gas Regulation** due to its GWP of 3,220. New installations should prefer Novec 1230 (GWP 1) or inert gas (GWP 0) to avoid mid-lifecycle agent replacement costs. Some European AHJs already restrict new FM-200 installations.

## Evaluations

See `evals/evals.json` for test scenarios covering BESS, hyperscale campus, and colo suppression design.
