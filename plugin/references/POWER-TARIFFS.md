# Industrial Power Tariffs & Grid Data

> Industrial grid tariffs by country and state, renewable energy costs (LCOE),
> PPA pricing trends, and grid carbon intensity for data center site selection.
> Skills load individual sections by H2 header -- do not load the entire file.

**As-of:** 2026-03-27
**Next review:** 2026-09-27
**Staleness warning:** 180 days

---

## North America Industrial Tariffs

Industrial electricity rates for top data center markets in the US and Canada. Rates reflect large industrial/commercial tariff schedules (typically 1 MW+ demand). Excludes demand charges unless noted.

**United States -- Top 15 DC Markets:**

| State | Utility | Rate (cents/kWh) | Rate Type | Min Load | Confidence | Source |
|-------|---------|-------------------|-----------|----------|------------|--------|
| Virginia | Dominion Energy | 6.0-7.0 | Schedule GS-3/GS-4 | 500 kW+ | confirmed | [Dominion Rate Schedules](https://www.dominionenergy.com/virginia/rates-and-tariffs) |
| Texas | Various (ERCOT) | 4.7-8.0 | Deregulated wholesale | N/A | confirmed | [ERCOT Market Prices](http://www.ercot.com/mktinfo/prices) |
| Ohio | AEP Ohio | 5.5-7.0 | GS-4 Large General Service | 1 MW+ | confirmed | [AEP Ohio Tariffs](https://www.aepohio.com/business/account/rates/) |
| Georgia | Georgia Power | 6.5-7.5 | PL-1 Power and Light | 500 kW+ | confirmed | [Georgia Power Rates](https://www.georgiapower.com/business/billing-and-rate-plans/business-rates.html) |
| Iowa | MidAmerican Energy | 5.0-6.0 | Large General Service | 1 MW+ | confirmed | [MidAmerican Tariffs](https://www.midamericanenergy.com/tariffs-ia) |
| Oregon | PGE / PacifiCorp | 5.0-6.5 | Schedule 83/89 | 1 MW+ | confirmed | [PGE Rate Schedules](https://portlandgeneral.com/about/rates-tariffs) |
| Illinois | ComEd | 6.5-8.0 | Large Load Delivery | 400 kW+ | confirmed | [ComEd Rate Information](https://www.comed.com/rates-billing/rates-tariffs) |
| Nevada | NV Energy | 5.5-7.5 | LGS-2 | 1 MW+ | confirmed | [NV Energy Tariffs](https://www.nvenergy.com/account-services/energy-pricing-plans/rate-schedules) |
| Arizona | APS / SRP | 5.5-7.0 | E-36 / Large General | 500 kW+ | confirmed | [APS Rate Schedules](https://www.aps.com/residential/account-services/service-plans-rates-and-regulations/service-plans) |
| Washington | Various | 4.0-6.0 | Large Industrial | 1 MW+ | confirmed | [EIA State Profiles](https://www.eia.gov/electricity/state/) |
| Indiana | Duke Energy IN | 6.0-7.5 | Rate HLF | 1 MW+ | confirmed | [Duke Energy IN Rates](https://www.duke-energy.com/business/billing/rates) |
| North Carolina | Duke Energy Carolinas | 6.0-7.5 | OPT-V | 1 MW+ | confirmed | [Duke Energy NC Rates](https://www.duke-energy.com/business/billing/rates) |
| Utah | Rocky Mountain Power | 5.0-6.5 | Schedule 9 | 1 MW+ | confirmed | [Rocky Mountain Power](https://www.rockymountainpower.net/savings-energy-choices/rates.html) |
| New York | Various | 8.0-12.0 | SC-7/SC-13 | 500 kW+ | confirmed | [NYISO Market Data](https://www.nyiso.com/energy-market-operational-data) |
| California | PG&E / SCE | 10.0-16.0 | E-20 / TOU-8 | 500 kW+ | confirmed | [CPUC Rate Data](https://www.cpuc.ca.gov/industries-and-topics/electrical-energy/electric-rates) |

**Canada:**

| Province | Utility | Rate (cents/kWh USD) | Rate Type | Notes | Confidence | Source |
|----------|---------|---------------------|-----------|-------|------------|--------|
| Quebec | Hydro-Quebec | 3.5-5.0 | Rate L (Large Industrial) | Cheapest in North America; 99% hydro | confirmed | [Hydro-Quebec Rates](https://www.hydroquebec.com/business/customer-space/rates/) |
| Ontario | IESO | 7.0-10.0 | Class A Industrial | Global adjustment applies; nuclear/hydro mix | confirmed | [IESO Rates](https://www.ieso.ca/en/Power-Data/Data-Directory) |
| Alberta | AESO | 5.0-8.0 | Deregulated | Wholesale market; volatile; growing renewables | confirmed | [AESO Market Data](https://www.aeso.ca/market/market-and-system-reporting/) |
| British Columbia | BC Hydro | 4.5-6.0 | Rate 1823 (Large General) | Hydro baseload; competitive rates | confirmed | [BC Hydro Rates](https://www.bchydro.com/accounts-billing/rates-energy-use/electricity-rates.html) |

**Mexico (emerging):**

| Region | Rate (cents/kWh USD) | Notes | Confidence | Source |
|--------|---------------------|-------|------------|--------|
| Queretaro | 6.0-9.0 | Industrial tariff GDMTH; growing DC market | estimated | [CFE Tariffs](https://app.cfe.mx/Aplicaciones/CCFE/Tarifas/TarifasCRENegocio/Tarifas/GranDemandaMTH.aspx) |
| Monterrey | 5.5-8.5 | Nearshoring driving demand | estimated | [CFE Tariffs](https://app.cfe.mx/Aplicaciones/CCFE/Tarifas/TarifasCRENegocio/Tarifas/GranDemandaMTH.aspx) |

---

## Europe Industrial Tariffs

European industrial electricity rates for data center markets. Rates include energy component, network charges, and applicable taxes/levies. Renewable energy surcharges noted where they significantly impact total cost.

| Country | Rate (cents/kWh USD) | Key Levy/Surcharge | Market Type | Confidence | Source |
|---------|---------------------|-------------------|-------------|------------|--------|
| UK | 12.0-18.0 | Climate Change Levy (CCL) | Deregulated | confirmed | [Ofgem Energy Data](https://www.ofgem.gov.uk/energy-data-and-research) |
| Netherlands | 8.0-14.0 | Energy tax (energiebelasting); ODE surcharge | Deregulated | confirmed | [Eurostat Energy](https://ec.europa.eu/eurostat/web/energy/database) |
| Germany | 10.0-16.0 | EEG surcharge (reduced for large consumers since 2024) | Deregulated | confirmed | [Eurostat Energy](https://ec.europa.eu/eurostat/web/energy/database) |
| Ireland | 10.0-15.0 | PSO levy; grid capacity constraints | SEM (Single Electricity Market) | confirmed | [CRU Market Data](https://www.cru.ie/professional/energy/) |
| France | 7.0-11.0 | CSPE/TICFE (capped for intensive users) | Regulated + market | confirmed | [CRE Energy Data](https://www.cre.fr/en/) |
| Sweden | 3.0-6.0 | Minimal levies; electricity tax reduced for DCs | Deregulated (Nord Pool) | confirmed | [Nord Pool Market Data](https://www.nordpoolgroup.com/en/Market-data/) |
| Finland | 4.0-7.0 | Electricity tax (reduced rate for industry) | Deregulated (Nord Pool) | confirmed | [Nord Pool Market Data](https://www.nordpoolgroup.com/en/Market-data/) |
| Norway | 3.0-5.5 | Minimal levies; 98% hydro generation | Deregulated (Nord Pool) | confirmed | [Nord Pool Market Data](https://www.nordpoolgroup.com/en/Market-data/) |
| Denmark | 6.0-10.0 | Energy taxes (partially refundable for industry) | Deregulated (Nord Pool) | confirmed | [Nord Pool Market Data](https://www.nordpoolgroup.com/en/Market-data/) |
| Spain | 7.0-12.0 | Electric tax + generation charges | Deregulated (OMIE) | estimated | [OMIE Market Data](https://www.omie.es/en) |
| Poland | 8.0-13.0 | Capacity market charges; coal transition costs | Deregulated | estimated | [Eurostat Energy](https://ec.europa.eu/eurostat/web/energy/database) |

**European power market notes:**
- Nordics advantage: Abundant hydro (Norway, Sweden) and wind (Denmark) provide some of Europe's cheapest and cleanest power
- EU Energy Efficiency Directive (EED): Data centers > 500 kW must report energy data from 2024; future efficiency mandates expected
- Additionality: Large DCs increasingly required to demonstrate renewable energy additionality (new generation, not just RECs)
- Grid capacity: Dublin, Amsterdam moratoriums partially lifted but long interconnection queues persist (12-36 months)

---

## Asia-Pacific Industrial Tariffs

Industrial electricity rates for APAC data center markets. Markets are categorized as regulated (government-set tariffs) or deregulated (wholesale + retail competition).

| Country/Region | Rate (cents/kWh USD) | Market Structure | DC-Specific Rate | Confidence | Source |
|----------------|---------------------|------------------|------------------|------------|--------|
| Singapore | 12.0-18.0 | Deregulated (EMA) | No special DC rate | confirmed | [EMA Market Data](https://www.ema.gov.sg/statistic.aspx?sta_sid=20140826Y84sgBebjwKV) |
| Japan (Tokyo) | 12.0-18.0 | Partially deregulated | High-voltage industrial discounts | confirmed | [TEPCO Rate Plans](https://www.tepco.co.jp/en/hd/index-e.html) |
| Japan (Osaka) | 10.0-15.0 | Partially deregulated | Kansai Electric rates slightly lower | confirmed | Industry reports |
| Australia (Sydney) | 8.0-14.0 | Deregulated (NEM) | Large user agreements common | confirmed | [AEMO Market Data](https://aemo.com.au/energy-systems/electricity/national-electricity-market-nem/data-nem) |
| India (Maharashtra) | 7.0-11.0 | Regulated (state tariff) | Some states offer DC incentives | estimated | [CERC/SERC Tariff Orders](https://cercind.gov.in/) |
| India (Tamil Nadu) | 6.0-10.0 | Regulated (state tariff) | Industrial HT tariff | estimated | [TNERC Tariff Orders](https://www.tnerc.gov.in/) |
| Indonesia (Jakarta) | 7.0-10.0 | Regulated (PLN) | Industrial tariff I-3/I-4 | estimated | [PLN Tariff Schedule](https://web.pln.co.id/pelanggan/tarif-tenaga-listrik) |
| Malaysia (Johor) | 6.0-9.0 | Regulated (TNB/SESB) | Industrial tariff E2/E3 | estimated | [TNB Tariff Schedule](https://www.tnb.com.my/business/tariff-rates) |
| South Korea | 8.0-12.0 | Regulated (KEPCO) | Industrial tariff B | confirmed | [KEPCO Rate Schedule](https://home.kepco.co.kr/kepco/EN/main.do) |

**APAC power market notes:**
- Singapore: Moratorium on new DC construction partially lifted (2024); green energy requirements for new approvals
- Japan: Post-Fukushima energy mix shifting; renewable targets but still heavily fossil-dependent
- India: Interstate wheeling of renewable power possible; open access regulations vary by state
- Southeast Asia: Growing DC demand outpacing grid upgrades; captive power generation (gas, solar) increasingly common

---

## Renewable Energy Costs

Levelized Cost of Energy (LCOE) and PPA pricing for renewable energy technologies relevant to data center power procurement. LCOE represents the lifetime cost of generation; PPA rates represent contracted purchase prices available in the market.

**LCOE by Technology (Global, 2025-2026):**

| Technology | LCOE Range (cents/kWh) | Capacity Factor | Key Markets for DC | Confidence | Source |
|------------|----------------------|-----------------|-------------------|------------|--------|
| Utility-scale Solar PV | 2.5-5.0 | 20-30% | TX, AZ, NV, India, Australia, Spain | confirmed | [IRENA Renewable Cost Database](https://www.irena.org/costs) |
| Onshore Wind | 3.0-6.0 | 25-45% | TX, IA, Nordics, UK, India | confirmed | [IRENA Renewable Cost Database](https://www.irena.org/costs) |
| Offshore Wind | 5.5-11.0 | 35-55% | UK, Netherlands, Denmark, US East Coast | confirmed | [IRENA Renewable Cost Database](https://www.irena.org/costs) |
| BESS (4-hr Li-ion) | 8.0-15.0 (storage only) | N/A | All markets (paired with solar/wind) | confirmed | [BNEF Energy Storage Outlook](https://about.bnef.com/energy-storage/) |
| Solar + BESS (hybrid) | 4.0-7.0 | 40-70% (with storage) | TX, AZ, India, Australia | confirmed | [Lazard LCOE+ 2025](https://www.lazard.com/research-insights/levelized-cost-of-energyplus/) |

**PPA Pricing for DC-Scale Deals (50-500 MW):**

| Region | Solar PPA (cents/kWh) | Wind PPA (cents/kWh) | Trend | Confidence | Source |
|--------|----------------------|---------------------|-------|------------|--------|
| US (ERCOT/SPP) | 2.5-4.0 | 2.5-4.5 | Stable to declining | confirmed | [LevelTen PPA Index](https://www.leveltenenergy.com/ppa) |
| US (PJM) | 3.5-5.5 | 4.0-6.0 | Rising (interconnection delays) | confirmed | [LevelTen PPA Index](https://www.leveltenenergy.com/ppa) |
| Nordics | 2.5-4.0 | 2.0-3.5 | Stable | confirmed | Industry reports |
| India | 2.5-3.5 | 3.0-4.0 | Declining | estimated | [CERC/SECI Auction Data](https://seci.co.in/) |
| Australia | 3.5-5.0 | 4.0-6.0 | Volatile (policy dependent) | estimated | [AEMO/CER Data](https://aemo.com.au/) |

**DC-specific renewable considerations:**
- 24/7 carbon-free energy (CFE): Emerging standard beyond annual REC matching; requires time-matched local generation
- Additionality requirements: Google, Microsoft require new-build renewables, not existing facility RECs
- Virtual PPA (VPPA): Financial settlement only; no physical power delivery. Common for multi-state DC operators
- Sleeved PPA: Physical power delivery through utility; requires compatible utility territory
- Behind-the-meter (BTM): On-site solar/BESS reduces grid dependence; limited by site area (1 MW solar needs ~5 acres)

---

## Grid Carbon Intensity

Grid-average carbon intensity by country and US region in grams CO2 equivalent per kilowatt-hour (gCO2e/kWh). Used for Scope 2 emissions calculations and sustainability reporting. Trend indicates direction of change over the past 3 years.

| Country/Region | gCO2e/kWh | Trend | Primary Generation Mix | Confidence | Source |
|----------------|-----------|-------|----------------------|------------|--------|
| Norway | 10-30 | Stable (already very low) | 98% hydro | confirmed | [Electricity Maps](https://app.electricitymaps.com/) |
| Sweden | 20-50 | Declining | Hydro + nuclear + wind | confirmed | [Electricity Maps](https://app.electricitymaps.com/) |
| France | 50-80 | Stable | 70% nuclear | confirmed | [Electricity Maps](https://app.electricitymaps.com/) |
| Quebec (Canada) | 5-15 | Stable (very low) | 99% hydro | confirmed | [Hydro-Quebec Sustainability](https://www.hydroquebec.com/sustainable-development/) |
| Ontario (Canada) | 30-60 | Declining | Nuclear + hydro | confirmed | [IESO Generator Output](https://www.ieso.ca/) |
| UK | 150-250 | Declining rapidly | Gas + wind + nuclear | confirmed | [National Grid ESO](https://www.nationalgrideso.com/) |
| US - PJM (VA, OH, PA) | 350-500 | Declining slowly | Gas + coal + nuclear | confirmed | [EPA eGRID](https://www.epa.gov/egrid) |
| US - ERCOT (TX) | 350-450 | Declining | Gas + wind + solar | confirmed | [EPA eGRID](https://www.epa.gov/egrid) |
| US - MISO (IA, IL, IN) | 400-550 | Declining slowly | Coal + gas + wind | confirmed | [EPA eGRID](https://www.epa.gov/egrid) |
| US - CAISO (CA) | 200-300 | Declining | Gas + solar + hydro | confirmed | [EPA eGRID](https://www.epa.gov/egrid) |
| US - Northwest (OR, WA) | 100-200 | Stable | Hydro + wind + gas | confirmed | [EPA eGRID](https://www.epa.gov/egrid) |
| Germany | 300-450 | Declining (post-coal phase) | Gas + renewables + coal | confirmed | [Electricity Maps](https://app.electricitymaps.com/) |
| Netherlands | 300-450 | Declining | Gas + wind + solar | confirmed | [Electricity Maps](https://app.electricitymaps.com/) |
| Ireland | 250-400 | Declining | Gas + wind | confirmed | [EirGrid System Data](https://www.eirgridgroup.com/) |
| Singapore | 350-450 | Declining slowly | Gas (95%+) | confirmed | [EMA Singapore](https://www.ema.gov.sg/) |
| Japan | 400-550 | Declining slowly | Gas + coal + nuclear (restarting) | confirmed | [ISEP Japan Energy Data](https://www.isep.or.jp/en/) |
| India | 650-800 | Declining (solar growth) | Coal + renewables | confirmed | [CEA Carbon Emission Reports](https://cea.nic.in/) |
| Australia (NEM) | 500-700 | Declining | Coal + gas + solar + wind | confirmed | [AEMO Carbon Intensity](https://aemo.com.au/) |

**Carbon intensity considerations for DC planning:**
- Location-based vs market-based Scope 2: GHG Protocol allows either method; location-based uses grid average, market-based uses contracted energy
- Marginal vs average emissions: Grid average understates impact of new DC load; marginal emission rates are higher (typically 1.5-2x average in coal/gas grids)
- 24/7 CFE matching: More meaningful than annual REC matching; penalizes nighttime consumption in solar-dominant grids
- Science Based Targets (SBTi): Requires absolute emission reductions, not just intensity improvements
- CSRD (EU): Mandatory sustainability reporting for large companies including DC operators from 2025

> Sources: [EPA eGRID](https://www.epa.gov/egrid), [Electricity Maps](https://app.electricitymaps.com/), [IRENA](https://www.irena.org/), [IEA Electricity Data](https://www.iea.org/data-and-statistics). Carbon intensity figures are annual averages; hourly variation can be significant (2-5x range in renewable-heavy grids).
