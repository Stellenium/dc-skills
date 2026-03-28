# Solar & Wind Resource Data

> Solar irradiance (GHI), wind speed, and capacity factor data by global region
> for behind-the-meter power generation analysis and renewable energy procurement.
> Skills load individual sections by H2 header -- do not load the entire file.

**As-of:** 2026-03-27
**Next review:** 2027-03-27
**Staleness warning:** 365 days

---

## North America

Solar and wind resource data for major data center markets in the United States and Canada. GHI values represent annual horizontal plane irradiance; wind speeds are hub-height averages at 80-100m.

| Location/Zone | GHI (kWh/m2/yr) | Avg Wind Speed (m/s) | Solar CF (%) | Wind CF (%) | Notes | Confidence | Source |
|---------------|-----------------|---------------------|-------------|------------|-------|------------|--------|
| Phoenix, AZ | 2,350 | 4.5 | 27-29 | 15-20 | Top US solar market; limited wind | confirmed | [NREL NSRDB](https://nsrdb.nrel.gov/) |
| Dallas/Fort Worth, TX | 1,850 | 7.5 | 22-25 | 35-40 | Strong wind corridor; good solar | confirmed | [NREL NSRDB](https://nsrdb.nrel.gov/) |
| Ashburn, VA | 1,500 | 5.5 | 17-20 | 22-28 | Moderate solar; offshore wind potential | confirmed | [NREL NSRDB](https://nsrdb.nrel.gov/) |
| Des Moines, IA | 1,450 | 8.0 | 17-19 | 38-45 | Premier US wind market; MidAmerican territory | confirmed | [NREL NSRDB](https://nsrdb.nrel.gov/) |
| Hillsboro, OR | 1,250 | 5.0 | 15-18 | 25-30 | Lower solar; Columbia Gorge wind access | confirmed | [NREL NSRDB](https://nsrdb.nrel.gov/) |
| Montreal, QC | 1,350 | 6.0 | 15-17 | 28-33 | Short solar season; strong winter wind | confirmed | [IRENA Global Atlas](https://globalatlas.irena.org/) |

**DC-relevant implications:**
- Texas and Iowa offer the best combined solar+wind resources in North America, enabling hybrid BTM configurations with 60-80% self-generation ratios
- Northern Virginia's moderate solar resource still supports BTM PV at 17-20% capacity factor, competitive with grid at current Dominion Energy rates when paired with ITC
- Pacific Northwest hydro baseload reduces the economic case for BTM renewables despite adequate wind resources

---

## Europe

Solar and wind resource data for European data center markets. Northern Europe favors wind; Southern Europe and Mediterranean favor solar. Seasonal variation is more pronounced than in North American markets.

| Location/Zone | GHI (kWh/m2/yr) | Avg Wind Speed (m/s) | Solar CF (%) | Wind CF (%) | Notes | Confidence | Source |
|---------------|-----------------|---------------------|-------------|------------|-------|------------|--------|
| Stockholm, SE | 1,000 | 6.5 | 11-14 | 30-35 | Low solar; excellent onshore wind | confirmed | [IRENA Global Atlas](https://globalatlas.irena.org/) |
| Amsterdam, NL | 1,050 | 7.0 | 12-14 | 32-38 | Offshore wind hub; limited land solar | confirmed | [IRENA Global Atlas](https://globalatlas.irena.org/) |
| Frankfurt, DE | 1,100 | 5.5 | 12-15 | 25-30 | Moderate resources; grid constrained | confirmed | [IRENA Global Atlas](https://globalatlas.irena.org/) |
| Dublin, IE | 950 | 8.5 | 10-13 | 35-42 | Premier European wind market | confirmed | [IRENA Global Atlas](https://globalatlas.irena.org/) |
| Madrid, ES | 1,900 | 5.5 | 22-25 | 25-30 | Top European solar market; growing DC hub | confirmed | [IRENA Global Atlas](https://globalatlas.irena.org/) |
| Milan, IT | 1,500 | 4.5 | 17-20 | 18-22 | Good solar; limited wind onshore | confirmed | [IRENA Global Atlas](https://globalatlas.irena.org/) |

**DC-relevant implications:**
- Nordic and Irish wind capacity factors (35-42%) rival the best US wind sites, making PPAs extremely competitive at 2.0-3.5 cents/kWh
- Southern European solar (Madrid, Milan) achieves 20-25% capacity factor, enabling competitive BTM solar for emerging DC markets in Spain and Italy
- EU additionality requirements increasingly favor new-build BTM generation over REC-only procurement

---

## Middle East & North Africa

Exceptional solar resources across the region with limited but growing wind potential. Water scarcity constrains panel cleaning for ground-mount solar.

| Location/Zone | GHI (kWh/m2/yr) | Avg Wind Speed (m/s) | Solar CF (%) | Wind CF (%) | Notes | Confidence | Source |
|---------------|-----------------|---------------------|-------------|------------|-------|------------|--------|
| Riyadh, SA | 2,400 | 5.0 | 25-28 | 18-22 | NEOM project driving data center + renewables | confirmed | [World Bank ESMAP](https://globalsolaratlas.info/) |
| Dubai, AE | 2,200 | 4.5 | 24-27 | 15-18 | DEWA utility-scale solar at record-low PPAs | confirmed | [World Bank ESMAP](https://globalsolaratlas.info/) |
| Cairo, EG | 2,100 | 6.5 | 23-26 | 28-33 | Gulf of Suez wind corridor; strong solar | confirmed | [World Bank ESMAP](https://globalsolaratlas.info/) |
| Casablanca, MA | 1,900 | 7.0 | 21-24 | 30-35 | Morocco leads African renewable deployment | confirmed | [IRENA Global Atlas](https://globalatlas.irena.org/) |

**DC-relevant implications:**
- Solar PV in MENA achieves 24-28% capacity factor, enabling competitive BTM solar for hyperscale facilities with LCOE below 2 cents/kWh in best locations
- Dust soiling reduces panel output 15-25% without regular cleaning; water-scarce sites should budget for robotic dry-cleaning systems
- Gulf states offer sovereign wealth fund co-investment for DC+renewable packages aligned with Vision 2030 and similar diversification strategies

---

## Sub-Saharan Africa

Excellent solar resource across most of the continent with growing wind potential in East Africa and coastal regions. Grid unreliability makes BTM generation critical rather than optional.

| Location/Zone | GHI (kWh/m2/yr) | Avg Wind Speed (m/s) | Solar CF (%) | Wind CF (%) | Notes | Confidence | Source |
|---------------|-----------------|---------------------|-------------|------------|-------|------------|--------|
| Lagos, NG | 1,750 | 3.5 | 18-21 | 12-15 | Limited wind; solar viable; grid unreliable | estimated | [World Bank ESMAP](https://globalsolaratlas.info/) |
| Nairobi, KE | 2,000 | 6.0 | 21-24 | 28-32 | Lake Turkana wind farm corridor nearby | confirmed | [World Bank ESMAP](https://globalsolaratlas.info/) |
| Johannesburg, ZA | 2,100 | 5.5 | 22-25 | 25-28 | Best African DC market; REIPPP procurement | confirmed | [World Bank ESMAP](https://globalsolaratlas.info/) |
| Accra, GH | 1,800 | 5.0 | 19-22 | 18-22 | Emerging West African DC hub | estimated | [World Bank ESMAP](https://globalsolaratlas.info/) |

**DC-relevant implications:**
- Grid unreliability (frequent outages, voltage fluctuations) in most Sub-Saharan markets makes BTM solar+BESS an operational necessity, not just a cost optimization
- South Africa's REIPPP program provides a proven BTM procurement framework for DC developers; 22-25% solar capacity factors are bankable
- DFI funding (IFC, AfDB, Power Africa) is available for DC projects with integrated renewable energy components -- see DFI-FUNDING.md

---

## Southeast Asia

Strong solar resource year-round due to equatorial positioning but monsoon seasonality affects output. Wind resources are generally limited except in specific coastal corridors.

| Location/Zone | GHI (kWh/m2/yr) | Avg Wind Speed (m/s) | Solar CF (%) | Wind CF (%) | Notes | Confidence | Source |
|---------------|-----------------|---------------------|-------------|------------|-------|------------|--------|
| Singapore | 1,600 | 3.0 | 16-18 | 8-12 | Land-constrained; rooftop solar only for BTM | confirmed | [World Bank ESMAP](https://globalsolaratlas.info/) |
| Jakarta, ID | 1,700 | 3.5 | 17-19 | 10-14 | Tropical monsoon reduces consistency | estimated | [World Bank ESMAP](https://globalsolaratlas.info/) |
| Johor Bahru, MY | 1,650 | 3.5 | 16-18 | 10-14 | Singapore overflow market; more land for solar | estimated | [World Bank ESMAP](https://globalsolaratlas.info/) |
| Ho Chi Minh City, VN | 1,750 | 5.0 | 18-20 | 20-25 | South Vietnam wind potential; growing market | estimated | [World Bank ESMAP](https://globalsolaratlas.info/) |
| Bangkok, TH | 1,700 | 4.0 | 17-19 | 14-18 | Moderate solar; limited wind | estimated | [World Bank ESMAP](https://globalsolaratlas.info/) |

**DC-relevant implications:**
- Singapore's land scarcity limits BTM solar to rooftop installations on DC buildings, typically covering only 5-10% of facility load
- Johor Bahru and Jakarta offer larger land parcels for meaningful ground-mount BTM solar installations (1 MW per ~5 acres)
- Monsoon seasonality creates 20-30% output variation between wet and dry seasons -- BESS pairing is recommended for consistent BTM contribution

---

## Latin America

Strong solar resource in Mexico and the Andes corridor; growing wind resources in Brazil, Mexico, and Colombia. DC market is nascent but expanding rapidly.

| Location/Zone | GHI (kWh/m2/yr) | Avg Wind Speed (m/s) | Solar CF (%) | Wind CF (%) | Notes | Confidence | Source |
|---------------|-----------------|---------------------|-------------|------------|-------|------------|--------|
| Queretaro, MX | 2,050 | 5.0 | 22-25 | 20-25 | Growing DC hub; nearshoring demand | confirmed | [World Bank ESMAP](https://globalsolaratlas.info/) |
| Sao Paulo, BR | 1,600 | 4.5 | 17-19 | 15-20 | Largest LATAM DC market; hydro-dependent grid | estimated | [World Bank ESMAP](https://globalsolaratlas.info/) |
| Santiago, CL | 2,000 | 6.0 | 22-25 | 28-32 | Atacama solar resource world-class; growing DC | confirmed | [World Bank ESMAP](https://globalsolaratlas.info/) |
| Bogota, CO | 1,650 | 5.5 | 17-20 | 25-28 | La Guajira wind corridor; stable grid | estimated | [World Bank ESMAP](https://globalsolaratlas.info/) |

**DC-relevant implications:**
- Chile's Atacama Desert offers world-class solar (GHI >2,500 in best spots) with record-breaking PPA prices; Santiago DC market benefits from nearby solar + Andean wind
- Mexico's nearshoring trend is driving DC demand in Queretaro and Monterrey, where excellent solar resources enable competitive BTM generation
- Brazil's hydro-dependent grid faces drought risk, making BTM solar+BESS increasingly attractive as a reliability hedge for DC operators

---

## Australia & Oceania

Strong solar resource across most of Australia with excellent wind in southern coastal regions. New Zealand offers wind but limited solar compared to Australia.

| Location/Zone | GHI (kWh/m2/yr) | Avg Wind Speed (m/s) | Solar CF (%) | Wind CF (%) | Notes | Confidence | Source |
|---------------|-----------------|---------------------|-------------|------------|-------|------------|--------|
| Sydney, AU | 1,800 | 6.5 | 20-23 | 28-33 | Western Sydney DC corridor; good solar+wind | confirmed | [World Bank ESMAP](https://globalsolaratlas.info/) |
| Melbourne, AU | 1,550 | 7.0 | 17-20 | 32-38 | Excellent wind; cooler climate reduces cooling load | confirmed | [World Bank ESMAP](https://globalsolaratlas.info/) |
| Perth, AU | 2,100 | 6.0 | 23-26 | 28-32 | Emerging DC market; strong solar resource | confirmed | [World Bank ESMAP](https://globalsolaratlas.info/) |
| Auckland, NZ | 1,400 | 6.5 | 15-17 | 30-35 | Wind-favored; sovereign DC market | estimated | [IRENA Global Atlas](https://globalatlas.irena.org/) |

**DC-relevant implications:**
- Australia's NEM grid is transitioning from coal to renewables, creating both opportunity (cheap PPAs) and risk (grid instability during transition)
- Melbourne's combination of strong wind resources and cooler climate makes it attractive for BTM wind + free cooling combinations
- Large-scale solar PPAs in Australia have been volatile due to policy uncertainty; BTM generation provides more price certainty than grid-purchased renewables

> Sources: [NREL NSRDB](https://nsrdb.nrel.gov/), [IRENA Global Atlas](https://globalatlas.irena.org/), [World Bank ESMAP Global Solar Atlas](https://globalsolaratlas.info/), [World Bank ESMAP Global Wind Atlas](https://globalwindatlas.info/). GHI values are multi-year annual averages. Wind speeds are estimated at 80-100m hub height. Capacity factors are typical ranges for utility-scale installations in each region and will vary based on specific site conditions, equipment selection, and tracking configuration.
