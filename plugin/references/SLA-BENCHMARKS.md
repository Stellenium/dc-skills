# SLA Benchmarks & Availability Standards

> Tier I-IV availability targets, component MTTR/MTBF benchmarks, credit structure
> templates, and measurement methodology for data center SLA design and negotiation.
> Skills load individual sections by H2 header -- do not load the entire file.

**As-of:** 2026-03-27
**Next review:** 2026-09-27
**Staleness warning:** 180 days

---

## Tier Availability Targets

Industry-standard availability targets by Uptime Institute Tier classification. These represent design targets -- contractual SLAs are typically negotiated at or slightly below these levels to account for operational variance.

| Tier | Annual Availability (%) | Allowed Downtime (hrs/yr) | Typical SLA Guarantee | Redundancy Level | Concurrent Maintainability | Fault Tolerant | Confidence | Source |
|------|------------------------|--------------------------|----------------------|-----------------|---------------------------|----------------|------------|--------|
| Tier I | 99.671% | 28.8 | 99.5% - 99.67% | N (no redundancy) | No | No | confirmed | [Uptime Institute Tier Standard](https://uptimeinstitute.com/tiers) |
| Tier II | 99.741% | 22.7 | 99.67% - 99.74% | N+1 (component) | No | No | confirmed | [Uptime Institute Tier Standard](https://uptimeinstitute.com/tiers) |
| Tier III | 99.982% | 1.6 | 99.95% - 99.98% | N+1 (system) | Yes | No | confirmed | [Uptime Institute Tier Standard](https://uptimeinstitute.com/tiers) |
| Tier IV | 99.995% | 0.4 | 99.99% - 99.995% | 2N or 2N+1 | Yes | Yes | confirmed | [Uptime Institute Tier Standard](https://uptimeinstitute.com/tiers) |

**Availability math reference:**

| Target | "Nines" | Downtime/Year | Downtime/Month | Downtime/Week |
|--------|---------|---------------|----------------|---------------|
| 99.9% | Three nines | 8 hrs 46 min | 43.8 min | 10.1 min |
| 99.95% | Three and a half nines | 4 hrs 23 min | 21.9 min | 5.0 min |
| 99.99% | Four nines | 52.6 min | 4.4 min | 1.0 min |
| 99.995% | Four and a half nines | 26.3 min | 2.2 min | 0.5 min |
| 99.999% | Five nines | 5.3 min | 0.4 min | 0.1 min |

**Key distinctions:**
- Tier classification describes the design and topology of the facility, not the SLA itself
- Contractual SLAs are typically 0.01-0.05% below the Tier design target to account for human error and unprecedented events
- "Five nines" (99.999%) is not formally part of the Uptime Tier standard but is sometimes offered as a premium SLA by hyperscale operators

---

## Component MTTR/MTBF

Mean Time to Repair (MTTR) and Mean Time Between Failures (MTBF) for critical data center infrastructure components. These values are used for availability modeling and spare parts planning.

| Component | MTBF (hours) | MTTR (hours) | Availability (%) | Failure Mode | Notes | Confidence | Source |
|-----------|-------------|-------------|------------------|-------------|-------|------------|--------|
| UPS (static, single module) | 200,000 | 4-8 | 99.997% | Module failure, capacitor degradation | Battery MTBF separate; module MTBF for rotary UPS is higher (~500K hrs) | confirmed | [IEEE 493 Gold Book](https://standards.ieee.org/ieee/493/3598/) |
| UPS Battery (VRLA) | 40,000-60,000 | 2-4 | 99.993% | Thermal runaway, cell dry-out, connection failure | Li-ion MTBF higher (~100K hrs) but thermal management critical | confirmed | IEEE 493 / Vendor data |
| Diesel Generator | 150,000 | 4-12 | 99.995% | Start failure, fuel system, coolant, governor | Start reliability: 95-99% depending on maintenance; fail-to-start is distinct from MTBF | confirmed | [IEEE 493 Gold Book](https://standards.ieee.org/ieee/493/3598/) |
| ATS (Automatic Transfer Switch) | 500,000 | 1-2 | 99.9997% | Mechanical failure, control board | Transfer time: 100-500ms for open transition; <4ms for static transfer | confirmed | IEEE 493 / ASCO data |
| STS (Static Transfer Switch) | 750,000 | 2-4 | 99.9997% | Thyristor failure, control electronics | Transfer time: <4ms; higher MTBF than ATS but more complex repair | confirmed | Vendor data |
| PDU (Power Distribution Unit) | 300,000 | 2-4 | 99.999% | Breaker trip, transformer failure, monitoring | Rack PDU MTBF higher (~1M hrs); floor PDU figures shown | confirmed | Vendor data |
| CRAH/CRAC Unit | 80,000-120,000 | 4-8 | 99.994% | Compressor failure, fan motor, refrigerant leak | N+1 configuration critical; single unit failure should not impact cooling | confirmed | IEEE 493 / ASHRAE data |
| Chiller (centrifugal) | 60,000-100,000 | 8-24 | 99.98% | Compressor failure, tube fouling, bearing wear | Longest MTTR in cooling chain; spare compressor stocking recommended | confirmed | [ASHRAE Equipment Life](https://www.ashrae.org/) |
| Network Switch (core) | 300,000-500,000 | 0.5-2 | 99.9997% | Software crash, power supply, fan failure | Dual-supervisor configs reduce MTTR to <1 min (automatic failover) | confirmed | Vendor data (Cisco, Arista, Juniper) |

**Modeling notes:**
- Series components multiply availability: A_total = A1 x A2 x A3 (single path)
- Parallel (redundant) components: A_parallel = 1 - (1-A1) x (1-A2) (two-path)
- MTBF values represent field experience across vendor fleet; individual unit performance varies by environment (temperature, loading, maintenance quality)
- Generator start failure is a separate reliability metric from operational MTBF -- model both in availability calculations

---

## Credit Structure Templates

Standard SLA credit structures for colocation and wholesale data center contracts. Credits compensate tenants for availability failures and incentivize operator performance.

### Tiered Credit Model (Tier III Target: 99.982%)

| Downtime Range (per month) | Cumulative Downtime | Credit (% of MRC) | Escalation |
|---------------------------|--------------------|--------------------|------------|
| 0 - 1 min | Within SLA target | 0% | None |
| 1 min - 15 min | Minor breach | 5% | Notification to tenant |
| 15 min - 1 hr | Moderate breach | 10% | Root cause analysis required |
| 1 hr - 4 hrs | Significant breach | 20% | Executive review + remediation plan |
| 4 hrs - 8 hrs | Major breach | 30% | Remediation plan + penalty escalation |
| > 8 hrs | Critical breach | 50% (cap) | Tenant termination right triggered |

### Tiered Credit Model (Tier IV Target: 99.995%)

| Downtime Range (per month) | Cumulative Downtime | Credit (% of MRC) | Escalation |
|---------------------------|--------------------|--------------------|------------|
| 0 - 30 sec | Within SLA target | 0% | None |
| 30 sec - 5 min | Minor breach | 5% | Notification to tenant |
| 5 min - 30 min | Moderate breach | 15% | Root cause analysis required |
| 30 min - 2 hrs | Significant breach | 25% | Executive review + remediation plan |
| 2 hrs - 4 hrs | Major breach | 40% | Remediation plan + penalty escalation |
| > 4 hrs | Critical breach | 50% (cap) | Tenant termination right triggered |

### Credit Structure Design Principles

- **Cap at 50% of MRC:** Industry standard; uncapped credits create existential risk for operators
- **Escalation ladder:** Each tier triggers increasing operational response requirements
- **Termination right:** Typically activated after 2-3 consecutive months exceeding the major breach threshold or any single critical breach
- **Carve-outs:** Force majeure, scheduled maintenance (with advance notice), and tenant-caused outages are excluded from credit calculations
- **Measurement granularity:** Credits calculated monthly against monthly recurring charges (MRC)

---

## Measurement Methodology

How availability is measured, what counts as downtime, and standard exclusions in data center SLAs.

### Availability Formula

```
Availability (%) = ((Total Minutes - Downtime Minutes) / Total Minutes) x 100
```

Where:
- **Total Minutes** = calendar minutes in the measurement period (month: 43,200 avg; year: 525,600)
- **Downtime Minutes** = minutes where power, cooling, or connectivity to the tenant's contracted space is unavailable

### What Counts as Downtime

| Event | Counts as Downtime | Notes |
|-------|-------------------|-------|
| Utility power loss beyond UPS runtime | Yes | Includes generator fail-to-start scenarios |
| UPS failure causing power interruption | Yes | Even if utility power is available |
| Cooling failure causing thermal shutdown | Yes | Measured from shutdown, not from cooling loss |
| Network switch failure (operator-provided) | Yes | Only for operator-managed network; tenant gear excluded |
| Fire suppression activation (non-test) | Yes | Includes VESDA-triggered shutdowns |
| Planned maintenance with advance notice | No | Typically requires 72 hours minimum notice; some contracts require 30 days |
| Force majeure events | No | Must be defined in contract; typically: natural disaster, war, government action |
| Tenant-caused outage | No | Includes tenant overloading circuits beyond contracted capacity |
| Partial facility outage (unaffected tenants) | No | Only affected tenants count downtime against their SLA |

### Measurement Intervals

| Approach | Interval | Pros | Cons | Typical Use |
|----------|----------|------|------|-------------|
| Monthly rolling | Calendar month | Simple; aligns with billing | Short window hides annual trends | Colo SLAs |
| Annual rolling | Trailing 12 months | Captures seasonal patterns | Slow to detect degradation | Enterprise/hyperscale |
| Continuous (real-time) | Per-minute | Most accurate; supports 24/7 CFE | Complex; requires monitoring investment | Premium SLAs |

### Exclusion Windows

Standard scheduled maintenance windows negotiated in SLAs:

- **Planned maintenance:** 4-8 hours/quarter typical allowance; larger windows for Tier I/II facilities
- **Emergency maintenance:** 2-4 hours/month allowance with 4-hour advance notice minimum
- **Firmware/software updates:** Often bundled into planned maintenance; should be explicit in contract
- **Utility-scheduled outages:** Typically excluded if notice provided; contested for facilities with redundant utility feeds

> Sources: [Uptime Institute Tier Standard](https://uptimeinstitute.com/tiers), [IEEE 493 Gold Book](https://standards.ieee.org/ieee/493/3598/), ASHRAE TC 9.9 reliability data, vendor reliability publications. MTBF/MTTR values are industry composites -- individual equipment performance varies by manufacturer, model, environment, and maintenance program. SLA credit structures are representative templates; actual contracts are negotiated between parties.
