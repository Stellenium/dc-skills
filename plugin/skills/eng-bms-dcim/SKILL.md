---
name: eng-bms-dcim
description: "Design BMS and DCIM architecture covering sensor strategy, alarm hierarchy, integration points, and capacity management dashboards. Use when planning building management systems, selecting DCIM platforms, designing monitoring infrastructure, or integrating BMS with DCIM for a data center. Trigger with \"BMS\", \"DCIM\", \"building management\", \"monitoring\", \"sensor strategy\", \"capacity management\", or \"data center infrastructure management\"."
---

# BMS/DCIM Architecture

Design BMS and DCIM architecture for data center facilities with sensor strategy,
alarm hierarchy, protocol selection, network architecture, and digital twin
readiness assessment. Produces a comprehensive monitoring and management
architecture covering mechanical, electrical, environmental, and capacity systems.

## What I Need from Upstream

**From power-capacity-model (eng-power-model):**
- Total IT load and facility load
- Power chain architecture (for power metering placement)
- Cooling system architecture (for sensor placement strategy)
- Redundancy tier (affects monitoring redundancy requirements)

If upstream data is not available, I will ask for facility parameters
directly or use industry-standard defaults.

## Phase 1: Critical Discovery

> Answer these questions first. They determine the architecture scope.

**Project Context:**

1. What facility type?
   - Hyperscale (campus, 10,000+ sensor points, centralized monitoring)
   - Colocation (multi-tenant DCIM with tenant portal requirements)
   - Enterprise (single-tenant, integrated with corporate IT)
   - Edge (fleet management, centralized DCIM, remote BMS)
   - Sovereign (enhanced security, air-gapped options)

2. What is the scale?
   - Number of IT rooms/halls
   - Total white space (sqft)
   - Total facility (sqft including support spaces)
   - Number of buildings (campus)

3. What Tier level?
   - Tier I/II (basic monitoring)
   - Tier III (redundant monitoring paths, no single point of failure)
   - Tier IV (fully redundant monitoring infrastructure)

4. Is there existing BMS? (brownfield)
   - No existing BMS (greenfield)
   - Existing BMS -- specify vendor and protocol
   - Existing BMS to be replaced
   - Existing BMS to be integrated/expanded

5. What is the preferred vendor ecosystem?
   - Open protocol (vendor-agnostic, BACnet/Modbus/SNMP)
   - Proprietary platform (specify: Schneider EcoStruxure, Vertiv Liebert, Honeywell, Siemens)
   - Hybrid (open protocol with preferred DCIM platform)

6. Is digital twin capability required?
   - Yes -- full 3D digital twin with real-time data overlay
   - Partial -- 2D floor plan with real-time sensor data
   - No -- standard dashboard and reporting
   - Future consideration (design for readiness)

7. What enterprise IT integration is needed?
   - ServiceNow (ITSM/CMDB integration)
   - BMC Helix / Remedy
   - PagerDuty / Opsgenie (alerting)
   - Custom API integration
   - None (standalone system)

## Phase 2: Context Refinement

> Based on Phase 1, gather architecture-specific detail.

### Multi-Tenant Path (Colo)

1. What tenant data is exposed through the portal?
2. Do tenants require API access to their monitoring data?
3. What tenant billing data comes from DCIM? (power, cooling, space)
4. How are tenant SLA metrics calculated and reported?

### Edge Fleet Path

1. How many edge sites in the fleet?
2. What WAN connectivity is available? (bandwidth, latency, reliability)
3. What local BMS capability is needed at each site? (standalone vs dependent)
4. What are the remote management requirements? (restart, firmware update, configuration)

## BMS Architecture

### BMS Scope

| System | Monitoring Points | Control Points | Protocol | Priority |
|--------|------------------|----------------|----------|----------|
| Mechanical (HVAC) | Temperature, humidity, pressure, flow, valve position | Setpoints, valve actuators, VFD speed | BACnet IP | Critical |
| Electrical (EPMS) | Voltage, current, power, energy, power factor | Breaker status (monitor only for most) | Modbus TCP | Critical |
| Fire/life safety | Alarm status, zone status, trouble | Integration only (no control from BMS) | Hardwired + BACnet | Critical |
| Access control | Door status, badge events, alarm | Integration only (separate security system) | API/REST | High |
| Generators | Run status, fuel level, output, coolant temp | Start/stop (emergency only) | Modbus RTU/TCP | Critical |
| UPS | Input/output voltage, load %, battery status, runtime | Bypass (maintenance only) | SNMP/Modbus | Critical |
| Leak detection | Zone status, leak location | Integration only | Contact closure/Modbus | High |
| Lighting | On/off status, dimming level | Schedule, occupancy override | BACnet/DALI | Low |

### Sensor Strategy (ASHRAE TC 9.9 Alignment)

**Temperature sensors:**
- Rack inlet: one sensor per rack at top, middle, and bottom (3 per rack for high-density)
- Rack exhaust: one sensor per rack at top (minimum)
- CRAH/CRAC return and supply: differential temperature monitoring
- Outside air temperature: for economizer control
- Under-floor plenum: one per 100 sqft (where applicable)
- Above-ceiling return plenum: one per 200 sqft

**Humidity sensors:**
- One per CRAH/CRAC unit (return air)
- One per 2,000 sqft of white space (supplemental)
- Outside air humidity (for economizer dew point control)

**Differential pressure:**
- Under-floor to room (raised floor facilities)
- Room to corridor (containment effectiveness)
- Filter differential pressure (all air handling units)
- Building positive pressure (exterior vs interior)

**Power metering:**
- Utility service entrance (revenue-grade metering, +/- 0.5%)
- Main switchgear bus (per bus section)
- UPS input and output (per module)
- PDU/RPP (per panel)
- Branch circuit monitoring (per circuit, for capacity management)
- Outlet-level monitoring (optional, for tenant billing in colo)

### Sensor Count Estimation

| Facility Size | Temperature | Humidity | Pressure | Power | Total Approx |
|---------------|-------------|---------|----------|-------|-------------|
| 10MW / 30K sqft | 300-500 | 30-50 | 20-30 | 100-200 | 500-800 |
| 50MW / 150K sqft | 1,500-2,500 | 150-250 | 80-120 | 500-800 | 2,500-4,000 |
| 200MW / 500K sqft | 5,000-10,000 | 500-1,000 | 300-500 | 2,000-3,000 | 8,000-15,000 |

## DCIM Architecture

### DCIM Modules

| Module | Function | Data Sources | Key Outputs |
|--------|----------|-------------|-------------|
| Capacity management | Track power, cooling, space utilization | Power metering, BMS sensors, asset database | Utilization %, available capacity, stranded capacity alerts |
| Power chain visualization | Real-time power flow from utility to rack | EPMS meters, UPS monitoring, PDU data | Single-line diagram with live data, power path redundancy view |
| Environmental monitoring | Temperature, humidity, airflow mapping | BMS temperature/humidity/pressure sensors | Heat maps, ASHRAE compliance alerts, hotspot detection |
| Asset lifecycle | Track equipment install, warranty, maintenance | Manual entry, barcode/RFID, procurement | Asset register, warranty expiration, replacement planning |
| Change management | Coordinate infrastructure changes | Ticket system integration, approval workflow | Change requests, impact analysis, rollback procedures |
| Reporting/analytics | Historical trends, SLA reporting, PUE | All data sources via historian | PUE trending, SLA compliance, capacity forecasting |

### Capacity Management

- Track three dimensions: power (kW per rack/row/hall), cooling (kW rejection per zone), space (rack units, floor tiles)
- Alert on stranded capacity (power available but cooling insufficient, or vice versa)
- Forecast capacity exhaustion based on deployment rate trending
- Reserve management for committed but not yet deployed capacity (critical for colo)

## Alarm Hierarchy

### 4-Tier Alarm Model

| Tier | Name | Response | Escalation | Auto-Remediation |
|------|------|----------|-----------|------------------|
| 1 | Informational | Log only, no action | None | None |
| 2 | Warning | NOC acknowledges within 30 min | To facility manager after 2 hours | Optional (e.g., increase cooling setpoint) |
| 3 | Critical | NOC responds within 5 min | To director after 15 min; VP after 30 min | Yes (e.g., start standby cooling, transfer to backup) |
| 4 | Emergency | Immediate response, all hands | CEO/CTO within 5 min; customer notification | Yes (e.g., EPO, generator start, emergency cooling) |

### Alarm Examples by Tier

- **Tier 1:** UPS battery nearing end-of-life (6 months), filter differential pressure approaching limit
- **Tier 2:** Room temperature above warning threshold (>80F), UPS module on bypass, coolant leak detected (minor)
- **Tier 3:** Room temperature above critical threshold (>95F), UPS fault (redundant module), cooling plant failure (standby activated)
- **Tier 4:** Fire alarm activation, complete utility loss, multiple simultaneous failures, EPO activation

## Protocol Selection

| Protocol | Layer | Best For | Limitations |
|----------|-------|----------|-------------|
| BACnet IP | Mechanical/HVAC | Industry standard for building automation; rich object model | Complex to configure; vendor implementations vary |
| Modbus TCP | Electrical/power | Simple, reliable for power metering and generator monitoring | No built-in discovery; flat namespace |
| SNMP v2c/v3 | IT equipment/UPS | Standard for IT infrastructure monitoring | Security concerns (v2c); limited for non-IT devices |
| OPC-UA | Unified/gateway | Cross-protocol aggregation; information model; security | Complex to deploy; overkill for simple installations |
| REST/API | DCIM integration | Modern IT integration; cloud connectivity | Not real-time; depends on vendor API availability |

## Network Architecture

### OT/IT Segmentation (IEC 62443)

- Dedicated BMS VLAN (isolated from corporate IT and tenant networks)
- Firewall between OT and IT networks with whitelisted protocols only
- BMS controllers on dedicated switches (no shared infrastructure with IT)
- Historian/time-series database in DMZ between OT and IT
- Remote access via jump host with MFA (no direct OT network access)
- For sovereign/classified: physically separate OT network (no IP path to IT)

## Digital Twin Readiness

### Readiness Assessment Criteria

| Criterion | Score 1-5 | Requirements |
|-----------|-----------|-------------|
| 3D model | Is BIM model available and current? | IFC format, LOD 300+ |
| Real-time data feeds | Are sensor APIs available? | BACnet/Modbus/SNMP with <30s latency |
| Network bandwidth | Can OT network support data volume? | 100Mbps+ dedicated for digital twin |
| Vendor maturity | Is selected DCIM vendor digital twin-capable? | Evaluate Nlyte, Sunbird, Vertiv, Schneider |
| Use case definition | Are digital twin use cases justified? | CFD simulation, what-if capacity, training |
| Cost justification | Does ROI justify investment? | Typically viable above 50MW facilities |

## Output

This skill produces two files:
1. `<project-name>-bms-dcim-architecture.md` -- Architecture report
2. `<project-name>-bms-dcim-architecture.json` -- Structured data

### JSON Sidecar

```json
{
  "artifact_type": "bms-dcim-architecture",
  "skill_version": "1.0",
  "project_name": "...",
  "bms": {
    "scope": ["mechanical", "electrical", "fire", "access-control"],
    "protocols": ["BACnet-IP", "Modbus-TCP", "SNMP"],
    "sensor_count_estimate": 0,
    "alarm_tiers": 4
  },
  "dcim": {
    "modules": ["capacity-management", "power-chain", "environmental", "asset-lifecycle"],
    "capacity_management": true,
    "power_chain_visualization": true
  },
  "network": {
    "architecture": "segmented | air-gapped",
    "segmentation": "logical | physical | air-gapped",
    "protocols": ["BACnet-IP", "Modbus-TCP", "SNMP", "OPC-UA"]
  },
  "digital_twin": {
    "readiness_score": 0,
    "requirements": ["..."],
    "estimated_cost": 0
  },
  "integration_points": ["ServiceNow", "PagerDuty"]
}
```

## Gotchas

- **BMS vendors often propose proprietary protocols that create 10-year vendor lock-in.** Once a proprietary BMS platform is deployed across a campus, migration costs $500K-2M+ due to controller replacement and re-programming. Specify open protocols (BACnet IP, Modbus TCP) in the design basis and require the vendor to demonstrate interoperability with third-party systems before contract award.

- **DCIM "capacity management" features rarely work accurately above 80% utilization without manual calibration.** As facilities approach full capacity, stranded capacity identification requires granular branch-circuit-level metering data and manual validation of nameplate vs actual load. Budget for quarterly capacity audits supplementing DCIM automated tracking.

- **OT/IT network segmentation is often an afterthought that becomes a $500K+ retrofit.** Designing BMS on the corporate IT network saves money during construction but creates a security vulnerability and a compliance failure for SOC 2, ISO 27001, and NIST 800-53. Design dedicated OT network infrastructure from day one -- retrofitting segregation into a running facility requires outage windows for network migration.

- **Sensor drift in temperature and humidity sensors can reach 2-3F and 5% RH within 2 years without calibration.** ASHRAE TC 9.9 A1 envelope allows only 5F of headroom (64.4-80.6F inlet). A 3F sensor drift can mask a real temperature excursion or trigger false alarms. Budget for annual sensor calibration in the operations plan.

- **Digital twin projects fail most often due to stale 3D models, not technology limitations.** The BIM model used for construction diverges from as-built within months as modifications occur. Without a process to update the 3D model with every change order, the digital twin becomes a misleading fiction. Budget for as-built model maintenance or do not invest in digital twin.

## Evaluations

See `evals/evals.json` for test scenarios covering hyperscale campus, colo multi-tenant, and edge fleet BMS/DCIM design.
