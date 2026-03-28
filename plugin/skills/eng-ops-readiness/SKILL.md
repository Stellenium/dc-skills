---
name: eng-ops-readiness
description: "Generate an operations readiness and handover plan for data center facilities with staffing models, SOPs, training programs, and Day 1 checklists. Use when preparing to operate a new DC, planning staffing for a data center, writing SOPs, or transitioning from construction to operations. Trigger with \"ops readiness\", \"operations handover\", \"DC staffing\", \"SOPs\", \"Day 1 checklist\", \"operations plan\", or \"ready to operate\"."
---

# Operations Readiness Plan

Generate an operations readiness and handover plan for data center facilities.
Covers staffing, SOPs, spare parts, incident response, vendor management, and
phased operational milestones. The output is an actionable handover document
aligned to commissioning completion.

## What I Need from Upstream

**From commissioning-plan (eng-commissioning):**
- Level 4 IST completion date (handover gate)
- Systems commissioned and their configurations
- Deficiency punch list status
- Vendor O&M manuals collected during commissioning
- BMS/DCIM configuration and alarm setpoints

If upstream artifact is not available, I will gather facility parameters
directly through discovery questions.

## Phase 1: Critical Discovery

> Answer these questions first. They determine the operations scope.

**Project Context:**

1. What facility type?
   - Hyperscale (large operations team, specialized roles)
   - Colocation (customer-facing operations, NOC + facility engineering)
   - Enterprise (single-tenant, may share staff with corporate facilities)
   - Modular/prefab (minimal on-site staff, remote monitoring emphasis)
   - Edge (unmanned, remote operations only)
   - Sovereign (enhanced staffing for security and compliance)

2. What Tier level?
   - Tier I/II (business-hours operations possible)
   - Tier III (24/7 staffing required for concurrent maintainability)
   - Tier IV (24/7 staffing with redundant shift coverage)

3. What is the MW capacity?
   - Phase 1 IT load
   - Total build-out capacity
   - Number of buildings/halls

4. Self-operated or managed services?
   - Self-operated (developer/owner builds operations team)
   - Managed services provider (third-party operations contractor)
   - Hybrid (owner manages critical systems, MSP handles routine)

5. What staffing model?
   - 24/7 on-site staffing (all shifts)
   - Business-hours on-site with 24/7 remote monitoring (NOC)
   - Remote-only with emergency response dispatch

6. Is this an existing operations team (brownfield) or new team build?
   - New team build (recruiting and training from scratch)
   - Existing team expansion (adding staff for new facility)
   - Team transition (from construction/commissioning to operations)

7. How many IT customers/tenants?
   - Single tenant (enterprise or hyperscale)
   - Multiple tenants (colo, 5-50+)
   - Government (special access and reporting requirements)

## Phase 2: Context Refinement

> Based on Phase 1, gather operations-specific detail.

### Managed Services Path

If managed services:

1. What is the MSP contract scope? (full operations, facilities only, NOC only)
2. What SLAs govern the MSP? (response time, resolution time, availability)
3. What is the owner's retained role? (asset management, capital decisions, tenant relations)
4. What handover documentation does the MSP require?

### Colo Path

If colocation:

1. What customer-facing operations are required? (provisioning, moves/adds/changes, tours)
2. What SLA reporting cadence? (monthly, quarterly, real-time portal)
3. What tenant escalation path exists? (account manager -> facility manager -> VP)
4. What is the customer onboarding process?

## Staffing Model

### FTE Sizing by Facility Type and Tier

| Role | 10MW Tier III | 25MW Tier III | 50MW Tier III | 100MW+ Tier IV | Colo 20MW | Edge Fleet (10 sites) |
|------|--------------|--------------|--------------|----------------|-----------|----------------------|
| Facility Manager | 1 | 1 | 1 | 1-2 | 1 | 1 (regional) |
| Critical Facility Engineer (CFE) | 4 (24/7 shifts) | 6 (24/7 + relief) | 8-10 | 12-16 | 6 | 2 (mobile) |
| Electrical Technician | 1 | 2 | 3-4 | 6-8 | 2 | 1 (mobile) |
| Mechanical Technician | 1 | 2 | 3-4 | 6-8 | 2 | 1 (mobile) |
| NOC Operator | 2 (24/7) | 4 (24/7) | 4-6 | 8-12 | 4 (24/7) | 2 (24/7) |
| Security Officer | 2 (24/7) | 2 (24/7) | 4 (24/7) | 6-8 | 4 (24/7) | 0 (remote) |
| Administrative | 1 | 1-2 | 2-3 | 4-6 | 2-3 | 1 |
| **Total FTE** | **12-14** | **18-22** | **28-36** | **50-70** | **22-28** | **8-10** |

### Shift Coverage Model (24/7)

| Shift | Hours | CFE | NOC | Security | Total Per Shift |
|-------|-------|-----|-----|----------|----------------|
| Day (A) | 0600-1800 | 2 | 1 | 1 | 4 |
| Night (B) | 1800-0600 | 1 | 1 | 1 | 3 |
| Relief | Rotating | 1 (covers PTO/sick) | 0 | 0 | 1 |

4 shifts rotating for 24/7 coverage: A, B, C, D shift pattern (12-hour shifts, 3-on/3-off or 4-on/4-off).

## SOP Development

### Priority Classification

| Priority | Category | Examples | Target Completion |
|----------|----------|---------|-------------------|
| P1 -- Safety critical | Emergency procedures | EPO procedure, fire response, electrical arc flash, confined space entry | Day 1 |
| P1 -- Safety critical | Electrical switching | Medium-voltage switching, UPS bypass, generator manual start | Day 1 |
| P2 -- Operational critical | Mechanical procedures | Chiller start/stop, cooling tower operation, economizer transition | Day 1 |
| P2 -- Operational critical | Monitoring | Alarm response procedures, escalation matrix, event logging | Day 1 |
| P3 -- Routine operational | Change management | Work permit process, LOTO, hot work permit, visitor management | Day 30 |
| P3 -- Routine operational | Maintenance | PM schedules, vendor coordination, parts ordering | Day 30 |
| P4 -- Administrative | Business processes | Shipping/receiving, inventory management, procurement, reporting | Day 90 |

### SOP Count Estimation

| Facility Size | P1 SOPs | P2 SOPs | P3 SOPs | P4 SOPs | Total |
|---------------|---------|---------|---------|---------|-------|
| 10MW Tier III | 15-20 | 15-20 | 20-30 | 10-15 | 60-85 |
| 50MW Tier III | 25-35 | 25-35 | 35-50 | 15-25 | 100-145 |
| 100MW+ Tier IV | 40-50 | 40-50 | 50-70 | 25-40 | 155-210 |

## Spare Parts Strategy

### Critical Spares by System

| System | Critical Spare | Recommended Stock | Lead Time (New) | Classification |
|--------|---------------|-------------------|-----------------|----------------|
| UPS | Power module | 1 per UPS type (N+1 in spares) | 12-16 weeks | Capital |
| UPS | Battery string/module | 1 string per UPS | 4-8 weeks | Capital |
| Generator | Starter motor | 1 per generator type | 8-12 weeks | Expense |
| Generator | Governor/AVR | 1 per generator type | 12-16 weeks | Capital |
| Generator | Fuel injector set | 1 set per generator type | 4-8 weeks | Expense |
| ATS/STS | Control board | 1 per ATS type | 8-12 weeks | Capital |
| Cooling | Compressor | 1 per chiller type | 26-52 weeks | Capital |
| Cooling | VFD (variable frequency drive) | 1 per VFD size | 8-16 weeks | Capital |
| Cooling | Fan motor/assembly | 1 per CRAH type | 4-8 weeks | Expense |
| Electrical | Protective relay | 1 per relay type | 4-8 weeks | Expense |
| Electrical | Circuit breaker (MV) | 1 per breaker type | 26-52 weeks | Capital |
| BMS | Controller module | 1 per controller type | 4-8 weeks | Expense |
| Fire | Clean agent cylinder | 1 reserve per zone type | 4-8 weeks | Expense |
| PDU | Breaker | 2 per breaker size (common sizes) | 2-4 weeks | Expense |

### Spare Parts Inventory Sizing

| Facility Size | Estimated Items | Estimated Value | Warehouse Space |
|---------------|----------------|----------------|-----------------|
| 10MW | 50-80 items | $500K-1M | 200-400 sqft |
| 50MW | 120-180 items | $2-4M | 500-1,000 sqft |
| 100MW+ | 200-350 items | $5-10M | 1,000-2,000 sqft |

## Incident Response

### Severity Classification

| Severity | Definition | Response Time | Resolution Target | Notification |
|----------|-----------|--------------|------------------|-------------|
| Sev 1 -- Critical | Active IT load impact or imminent risk | Immediate (on-site within 5 min) | Stabilize within 1 hour | CEO, CTO, VP Ops, all customers |
| Sev 2 -- Major | Redundancy loss, single point of failure active | 15 minutes | Restore redundancy within 4 hours | VP Ops, facility manager, affected customers |
| Sev 3 -- Minor | Degraded performance, no redundancy loss | 1 hour | Resolve within 24 hours | Facility manager, NOC supervisor |
| Sev 4 -- Informational | Monitoring alert, no operational impact | Next business day | Resolve within 1 week | NOC log only |

### Escalation Matrix

| Time Elapsed | Sev 1 | Sev 2 | Sev 3 | Sev 4 |
|-------------|-------|-------|-------|-------|
| 0 min | CFE + NOC | CFE + NOC | NOC | NOC log |
| 5 min | Facility manager | -- | -- | -- |
| 15 min | VP Operations | Facility manager | -- | -- |
| 30 min | CTO/CEO | -- | Facility manager | -- |
| 1 hour | Customer notification | VP Operations | -- | -- |
| 4 hours | Executive war room | Customer notification | -- | -- |

### Post-Incident Review

- Sev 1 and Sev 2: post-incident review within 48 hours
- Root cause analysis document within 5 business days
- Corrective action plan with owner and due dates
- Customer-facing incident report within 72 hours (colo)
- Regulatory notification if required (financial services, healthcare data)

## Vendor Management

### OEM Service Contract Framework

| Contract Level | Response Time | Parts Coverage | Labor | Annual Cost (% of equipment value) |
|----------------|-------------|---------------|-------|--------------------------------------|
| Premium (24/7 emergency) | 2-4 hours | All parts included | Included | 8-12% |
| Standard (business hours) | Next business day | Major components | Included | 4-6% |
| Basic (parts only) | 1-2 weeks | Parts at list price | Time & materials | 1-2% |

### Vendor SLA Requirements

- Response time SLA with liquidated damages for non-compliance
- Parts availability commitment (critical spares stocked at regional depot)
- Training requirements (vendor trains owner's staff on equipment maintenance)
- Remote monitoring and diagnostics capability
- Firmware/software update schedule and compatibility testing

## Operational Milestones

### Day 1 Checklist

- [ ] All P1 and P2 SOPs published and accessible
- [ ] Emergency contact list posted in NOC, electrical rooms, and mechanical rooms
- [ ] Security active (access control, CCTV recording, perimeter secured)
- [ ] BMS monitoring live with alarm setpoints configured
- [ ] Fire/life safety systems active and tested
- [ ] Emergency power tested (generator start, transfer, retransfer)
- [ ] Communication systems operational (radio, phone, paging)
- [ ] First aid supplies and AED locations identified and stocked
- [ ] LOTO equipment and arc flash PPE staged at all electrical rooms
- [ ] Vendor emergency contact numbers verified and tested

### Day 30 Checklist

- [ ] All staff trained on P1 (safety critical) procedures with documented sign-off
- [ ] First emergency drill completed (fire evacuation or utility loss simulation)
- [ ] All P3 SOPs published
- [ ] Preventive maintenance schedule published and first cycle initiated
- [ ] Spare parts inventory complete and cataloged
- [ ] Vendor service contracts executed for all critical systems
- [ ] Shift handover process operational and documented
- [ ] BMS alarm fine-tuning complete (nuisance alarms suppressed, thresholds adjusted)

### Day 90 Checklist

- [ ] First quarterly maintenance cycle complete for all systems
- [ ] PUE baseline established (3-month average)
- [ ] All P4 SOPs published
- [ ] Second emergency drill completed (different scenario from Day 30)
- [ ] Incident response procedure validated through tabletop exercise
- [ ] Operations team performance review (staffing adequacy, training gaps)
- [ ] Vendor performance review (response time, parts availability, satisfaction)
- [ ] Capacity management baseline established (power, cooling, space)

## Output

This skill produces two files:
1. `<project-name>-ops-readiness-plan.md` -- Operations readiness plan
2. `<project-name>-ops-readiness-plan.json` -- Structured data

### JSON Sidecar

```json
{
  "artifact_type": "ops-readiness-plan",
  "skill_version": "1.0",
  "project_name": "...",
  "staffing": {
    "total_fte": 0,
    "roles": [
      {"title": "Critical Facility Engineer", "count": 0, "shift_pattern": "24/7 rotating"}
    ],
    "annual_cost_estimate": 0
  },
  "sops": {
    "total_count": 0,
    "critical_count": 0,
    "categories": ["emergency", "electrical-switching", "mechanical", "monitoring", "change-management", "maintenance", "administrative"]
  },
  "spare_parts": {
    "items": [],
    "estimated_inventory_value": 0
  },
  "incident_response": {
    "severity_levels": 4,
    "escalation_matrix": {}
  },
  "milestones": {
    "day_1": ["SOPs published", "security active", "BMS live", "emergency contacts posted"],
    "day_30": ["staff trained", "first drill completed", "PM schedule initiated", "spares cataloged"],
    "day_90": ["first quarterly PM complete", "PUE baseline", "tabletop exercise", "vendor review"]
  }
}
```

## Gotchas

- **Industry average time-to-fill for critical facility engineers is 90-120 days -- start recruiting before commissioning begins.** CFE candidates with Tier III+ experience are scarce and in high demand. Waiting until IST completion to begin recruiting means the facility sits idle for 3-4 months. Begin recruiting when construction reaches 70% completion.

- **Spare parts for custom switchgear can have 26-52 week lead times.** A failed medium-voltage breaker with a 52-week replacement lead time means a year of operating without redundancy. Stock critical spares for all custom-engineered equipment BEFORE the facility goes live. The $200K cost of spare MV breakers is trivial compared to the risk of operating without redundancy.

- **Most data center incidents occur during planned maintenance, not equipment failure.** Human error during maintenance switching operations is the leading cause of DC outages (Uptime Institute annual report). Invest heavily in SOP quality and procedure compliance enforcement. Require two-person verification for all MV switching operations.

- **Managed services provider handovers fail when the MSP lacks facility-specific knowledge.** A generic MSP operations manual does not replace facility-specific SOPs. Require a 30-60 day overlap period where the construction/commissioning team operates alongside the MSP team with formal knowledge transfer and procedure validation.

- **Colo operators underestimate the customer-facing operations burden.** For every 10 tenants, budget 1 additional FTE for customer operations (provisioning, moves/adds/changes, tours, incident communication). A 50-tenant facility needs 5 customer operations staff beyond the engineering team.

## Evaluations

See `evals/evals.json` for test scenarios covering hyperscale self-operated, colo MSP handover, and modular minimal-staff operations.
