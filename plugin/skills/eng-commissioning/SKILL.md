---
name: eng-commissioning
description: "Generate Level 1-5 commissioning and Integrated Systems Testing (IST) plans for data centers with test scripts, acceptance criteria, and punch list tracking. Use when planning DC commissioning, writing test procedures, preparing for IST, or developing acceptance criteria for data center handover. Trigger with \"commissioning\", \"IST\", \"integrated systems testing\", \"commissioning plan\", \"Level 5 testing\", or \"data center handover testing\"."
---

# Commissioning & Integrated Systems Testing

Generate Level 1-5 commissioning plans and Integrated Systems Testing (IST) procedures
for data center facilities. This skill produces structured test procedure documents
with checklists and acceptance criteria -- NOT a typical analytical report. The output
is the commissioning plan a CxA (Commissioning Authority) uses to execute testing.

## What I Need from Upstream

**From power-capacity-model (eng-power-model):**
- Total IT load and redundancy tier
- Power chain architecture (utility, ATS/STS, switchgear, UPS, PDU)
- Generator count and configuration
- Cooling system architecture and redundancy

If upstream data is not available, I will ask for facility parameters
directly or use industry-standard defaults.

## Phase 1: Critical Discovery

> Answer these questions first. They determine the commissioning scope.

**Project Context:**

1. What facility type?
   - Hyperscale (campus, multiple power trains and cooling plants)
   - Colocation (multi-tenant, tenant witness requirements)
   - Enterprise (single-tenant, single building)
   - Modular/prefab (factory-integrated, Level 1 at factory)
   - Edge (simplified commissioning)
   - Sovereign (enhanced documentation and witness requirements)

2. What Tier level?
   - Tier I/II (basic commissioning, no IST)
   - Tier III (full IST with concurrent maintainability verification)
   - Tier IV (full IST with fault tolerance verification, redundant path testing)

3. Greenfield or brownfield?
   - **Greenfield:** Full Level 1-5 commissioning
   - **Brownfield:** Re-commissioning with existing systems assessment

4. How many systems?
   - Number of power trains (utility feeds, generators, UPS modules)
   - Number of cooling plants (chillers, cooling towers, CRAH/CRAC units)
   - Number of ATS/STS transfer switches

5. Who is the commissioning authority?
   - Independent third-party CxA (recommended for Tier III+)
   - Owner's representative/team
   - EPC contractor's commissioning team (less independent)

6. What is the target completion date?
   - Construction completion date
   - IT load deployment date
   - Lease commencement date (colo)

## Phase 2: Context Refinement

> Based on Phase 1, gather system-specific detail.

1. What specific systems require commissioning? (list all major equipment)
2. Are vendor O&M manuals available for all major equipment?
3. What redundancy configuration? (N, N+1, 2N, 2N+1 per system)
4. What utility coordination is required for IST utility disconnection?
5. What is the CxA's DC-specific experience? (number of prior DC commissioning projects)

## Level 1 -- Factory Witness Test (FWT)

Pre-shipment testing at manufacturer's facility before equipment ships to site.

### Purpose
Verify equipment meets specifications before delivery. Identify defects that would be costly to fix on-site.

### Checklist

- [ ] Electrical performance test (voltage regulation, efficiency at 25/50/75/100% load)
- [ ] Thermal performance test (heat rejection capacity at rated conditions)
- [ ] Vibration analysis (baseline readings for future trending)
- [ ] Control system I/O verification (all inputs/outputs functional)
- [ ] Nameplate verification (matches purchase order specifications)
- [ ] Paint and finish inspection (corrosion protection)
- [ ] Dimensional verification (matches foundation and rigging plans)
- [ ] Alarm and fault simulation (verify all alarms annunciate correctly)
- [ ] Communication protocol test (BACnet/Modbus/SNMP connectivity)

### Systems Requiring FWT

| System | FWT Priority | Key Tests | Witness Required |
|--------|-------------|-----------|-----------------|
| UPS (>500kVA) | Critical | Load bank, battery simulation, transfer | CxA + owner |
| Generators | Critical | Full-load run (2-4 hours), governor response | CxA + owner |
| Medium-voltage switchgear | Critical | Dielectric, relay calibration | CxA + owner |
| Chillers | High | Capacity, efficiency at design conditions | CxA |
| Cooling towers | High | Thermal performance, fan balance | CxA |
| ATS/STS | Critical | Transfer time, make-before-break | CxA + owner |
| PDU/RPP | Moderate | Voltage regulation, metering accuracy | CxA |

### Acceptance Criteria
- Manufacturer test report signed by CxA representative
- All tested parameters within specified tolerance
- Punch list items documented and resolved before shipment
- Photographs of nameplate, configuration, and test setup

## Level 2 -- Installation Verification (Pre-Functional)

On-site verification of installation quality before energization.

### Purpose
Verify equipment is installed per design documents and manufacturer requirements. Identify installation defects before power is applied.

### Checklist

- [ ] Equipment installed per approved drawings (location, orientation, clearances)
- [ ] Mechanical alignment verified (shafts, couplings, belt tension)
- [ ] Electrical connections torqued to specification (documented with calibrated torque wrench)
- [ ] Cable termination verified (correct phasing, proper lug crimping)
- [ ] Grounding system tested (resistance per NETA standards, typically < 5 ohms)
- [ ] Megger testing on all power cables (insulation resistance per NETA ATS Table 100.14)
- [ ] Labeling complete and matches as-built drawings
- [ ] Fire stopping of all penetrations verified (UL-listed systems)
- [ ] Seismic restraints installed per design (if applicable)
- [ ] Equipment pads/foundations level and properly grouted
- [ ] Oil/coolant levels verified
- [ ] Control wiring landed and labeled per point list

### NETA Acceptance Testing

| Test | Standard | Pass Criteria | Equipment |
|------|----------|---------------|-----------|
| Insulation resistance (Megger) | NETA ATS 7.15 | >100 megohms at 1,000V (cable) | All power cables |
| Contact resistance | NETA ATS 7.6 | <50 micro-ohms (bolted connections) | Switchgear, bus |
| Protective relay calibration | NETA ATS 7.9 | Within 5% of settings | All protective relays |
| Circuit breaker timing | NETA ATS 7.6 | Within manufacturer spec | MV and LV breakers |
| Ground resistance | NETA ATS 7.13 | <5 ohms (facility ground) | Ground grid |
| Power transformer turns ratio | NETA ATS 7.2 | Within 0.5% of nameplate | All transformers |

### Acceptance Criteria
- All NETA tests pass per ATS tables
- Punch list documented with severity classification (A: safety, B: functional, C: cosmetic)
- Category A items resolved before energization
- Installation photos for as-built documentation

## Level 3 -- Functional Performance Test (FPT)

Individual system testing under load after energization.

### Purpose
Verify each system operates as designed under actual or simulated load conditions.

### Test Procedures

**UPS Functional Tests:**
- [ ] Load bank test at 25%, 50%, 75%, 100% of rated capacity (4-hour test at 100%)
- [ ] Input power failure simulation (utility disconnect, verify battery transfer)
- [ ] Battery discharge test to low-voltage disconnect threshold
- [ ] Bypass transfer (manual and automatic) and retransfer
- [ ] Parallel operation (for modular UPS systems)
- [ ] Efficiency measurement at each load step

**Generator Functional Tests:**
- [ ] Start sequence: auto-start on utility loss within 10 seconds
- [ ] Transfer: ATS/STS transfer within specified time (100-500ms open, <4ms static)
- [ ] Load acceptance: full-load pickup without voltage/frequency excursion beyond limits
- [ ] Retransfer: automatic retransfer to utility after stable utility return (5-30 min delay)
- [ ] Full-load run: minimum 4 hours at 100% rated load
- [ ] Fuel consumption measurement vs design estimate
- [ ] Exhaust emissions measurement (if required by air quality permit)

**Cooling System Functional Tests:**
- [ ] Chiller capacity verification at design conditions (tonnage, GPM, delta-T)
- [ ] Cooling tower thermal performance (approach temperature)
- [ ] CRAH/CRAC unit airflow and cooling capacity per unit
- [ ] Variable speed drive operation across full range
- [ ] Economizer switchover (free cooling transition temperature verification)
- [ ] Redundancy failover: N+1 cooling unit failure with load redistribution

**BMS Point-to-Point Verification:**
- [ ] Every BMS sensor reads within calibration tolerance
- [ ] Every BMS alarm triggers at correct setpoint
- [ ] Every BMS control output actuates correct device
- [ ] Trend logging active for all critical points
- [ ] Graphics display correct real-time values

### Acceptance Criteria
- All systems meet specified performance at each load step
- UPS efficiency >= manufacturer specification at 50-100% load
- Generator start-to-load time within specification
- Cooling systems maintain supply temperature within +/- 1F of setpoint
- All BMS points verified (100% point-to-point, no sampling)

## Level 4 -- Integrated Systems Test (IST)

Full-facility failure simulation testing all systems operating together.

### Purpose
Verify the entire facility responds correctly to realistic failure scenarios. This is the most critical commissioning level -- it proves the facility can protect IT load through all credible failure modes.

### IST Scenarios

| Scenario | Failure Mode | Expected Response | Pass Criteria |
|----------|-------------|-------------------|---------------|
| Utility loss (single feed) | One utility feed interrupted | ATS transfers to generator within 10s; UPS bridges gap; zero IT load impact | No IT load drops; all alarms annunciate; transfer time within SLA |
| Utility loss (complete) | All utility feeds interrupted | All generators start and accept load; all ATS units transfer; UPS bridges gap | No IT load drops; generator start-to-load < 10s; stable voltage/frequency |
| Generator failure during outage | Generator trips while powering facility | Remaining generators accept redistributed load (N+1 verified) | No IT load drops; load sharing rebalances within 5 seconds |
| Cooling plant failure | One chiller or cooling tower trips | Standby unit starts automatically; temperature maintained | Room temperature stays within ASHRAE A1 envelope; < 5F rise |
| Cascade failure | Generator failure followed by cooling failure | Independent systems handle concurrent failures per tier level | No IT load drops; temperature within ASHRAE A1 envelope |
| Fire/EPO | Emergency power off activation in one zone | Affected zone de-energizes; adjacent zones unaffected | Only the targeted zone shuts down; no cascade to other zones |
| Redundant path transfer | Maintenance transfer from A to B path | Seamless transfer via static transfer switch | No IT load interruption; transfer time < 4ms |
| BMS failure | BMS server/controller failure | Systems continue on last-known-good settings; alarms escalate | No operational impact; BMS failover to redundant controller |

### IST Execution Requirements
- All systems at design load (use load banks if IT load not yet deployed)
- Independent CxA witnesses and documents all scenarios
- Building owner/operator representatives present
- Utility coordination for actual utility disconnection (48-72 hours advance notice)
- Licensed electrician operates utility disconnects
- Medical/safety personnel on standby for utility disconnection tests
- Video recording of all IST scenarios

### Acceptance Criteria
- Zero IT load drops across all scenarios
- All transfers within specified time limits
- All alarms annunciate correctly within 30 seconds
- BMS records complete event timeline
- No Category A deficiencies at IST completion

## Level 5 -- Seasonal / Ongoing Commissioning

Post-occupancy performance verification over the first operating year and beyond.

### Purpose
Verify facility performance under actual seasonal conditions and real IT load. Establish performance baselines for ongoing operations.

### Test Schedule

| Test | Season | Frequency | Key Metrics |
|------|--------|-----------|-------------|
| Summer peak cooling | Summer (peak heat) | Annual | Cooling capacity at peak ambient; PUE at peak |
| Winter economizer | Winter (coldest period) | Annual | Free cooling hours; economizer transition temperature |
| Generator reliability run | Any | Quarterly Year 1; semi-annual thereafter | Start reliability; load acceptance; runtime |
| PUE measurement | All seasons | Monthly Year 1; quarterly thereafter | PUE vs design target; seasonal variation |
| Battery capacity | Any | Semi-annual | UPS battery runtime at rated load vs design |
| Fire system test | Any | Annual | Detection and suppression system functional test |

### Acceptance Criteria
- PUE within 10% of design target by end of Year 1
- Generator start reliability > 98% (Tier III) or > 99% (Tier IV)
- Cooling system maintains ASHRAE A1 envelope at summer peak
- Economizer provides expected free cooling hours for climate zone
- All Level 4 IST scenarios re-executable annually

## Output

This skill produces two files:
1. `<project-name>-commissioning-plan.md` -- Structured test procedures per level
2. `<project-name>-commissioning-plan.json` -- Structured data

### JSON Sidecar

```json
{
  "artifact_type": "commissioning-plan",
  "skill_version": "1.0",
  "project_name": "...",
  "levels": [
    {
      "level": 1,
      "name": "Factory Witness Test",
      "test_count": 0,
      "systems": ["UPS", "generators", "switchgear"],
      "acceptance_criteria": ["..."],
      "witness_required": ["CxA", "owner"]
    }
  ],
  "ist_scenarios": [
    {
      "name": "Utility loss (complete)",
      "failure_mode": "All utility feeds interrupted",
      "expected_response": "Generators start, ATS transfers, UPS bridges",
      "pass_criteria": "Zero IT load drops"
    }
  ],
  "schedule": {
    "start_date": "...",
    "l1_complete": "...",
    "l2_complete": "...",
    "l3_complete": "...",
    "l4_complete": "...",
    "l5_start": "..."
  },
  "deficiency_tracking": {
    "open": 0,
    "closed": 0,
    "critical": 0
  }
}
```

## Gotchas

- **Level 4 IST with actual utility disconnection requires 48-72 hours advance coordination with the utility and may require a licensed electrician to operate utility disconnects.** Never simulate utility loss using the ATS test button for IST -- this tests the ATS, not the actual utility transfer chain. True IST requires opening the utility main breaker under load to verify the complete transfer sequence including utility protective relaying.

- **Commissioning costs typically run 1-3% of total construction cost but prevent 10-15x in operational failures.** A $500M facility should budget $5-15M for comprehensive commissioning. Cutting commissioning budget is the most common source of Day 1 operational failures in data centers.

- **Many CxA firms lack DC-specific IST experience -- telecom and office building commissioning does NOT transfer.** A CxA with 100 office building projects but zero DC IST projects will miss critical scenarios (cascade failures, concurrent maintainability, static transfer timing). Require DC-specific references and verify the CxA has performed IST with utility disconnection on Tier III+ facilities.

- **Modular/prefab data centers complete Level 1 at the factory and Levels 2-4 on-site** -- but the factory Level 1 scope is much broader than traditional FWT. Factory commissioning includes full system integration testing that would be Level 3 in stick-built construction. Ensure the factory commissioning protocol is reviewed and accepted by the independent CxA before factory dispatch.

- **Brownfield re-commissioning must include a Level 0 assessment** of existing systems before Levels 2-5 can be scoped. Existing equipment may have undocumented modifications, failed components, or out-of-calibration protection devices that create safety risks during IST.

## Evaluations

See `evals/evals.json` for test scenarios covering Tier IV IST, modular factory commissioning, and brownfield re-commissioning.
