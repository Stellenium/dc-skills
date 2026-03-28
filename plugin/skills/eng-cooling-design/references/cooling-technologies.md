# Cooling Technologies Reference

> Detailed specifications for all 14 data center cooling technologies.
> Loaded on demand by eng-cooling-design skill. Do not load upfront.

## Air-Based Technologies

### Raised-Floor Air Cooling
Pressurized underfloor plenum delivers cold air through perforated tiles to server inlets.
Classic approach for legacy data centers. Limited to low-density deployments.
- **Density range:** 3-10 kW/rack
- **PUE contribution:** 0.4-0.6
- **WUE:** 0 (no water, unless paired with chilled water plant)
- **Pros:** Simple design, well-understood, low capital cost
- **Cons:** Poor at high densities, hot spots from uneven airflow, raised floor limits structural load
- **Best for:** Legacy facilities, low-density enterprise, brownfield with existing raised floor

### In-Row Cooling
Cooling units placed between server racks in the row, drawing hot air from hot aisle
and delivering cold air directly to adjacent racks. Eliminates long air paths.
- **Density range:** 5-25 kW/rack
- **PUE contribution:** 0.3-0.5
- **WUE:** 0 (DX) or low (chilled water)
- **Pros:** Close-coupled to heat source, no raised floor needed, scalable per row
- **Cons:** Occupies rack positions, requires chilled water or refrigerant piping per row
- **Best for:** Medium-density deployments, retrofits, colocation halls

### Hot/Cold Aisle Containment
Physical barriers (curtains, panels, or hard enclosures) separate hot exhaust air
from cold supply air. Dramatically improves air-cooling efficiency.
- **Density range:** 5-30 kW/rack (with in-row or overhead cooling)
- **PUE contribution:** 0.2-0.4
- **WUE:** 0 (inherits from cooling source)
- **Pros:** 20-40% cooling efficiency improvement over open aisle, works with existing CRAC/CRAH
- **Cons:** Fire suppression complexity, containment breaches degrade performance
- **Best for:** Any air-cooled facility seeking efficiency gains, colocation environments

### Rear-Door Heat Exchanger (RDHx)
Water-cooled coil replaces or supplements the rear rack door. Removes 50-100% of
rack heat at the point of generation before it enters the room.
- **Density range:** 10-50 kW/rack
- **PUE contribution:** 0.1-0.3
- **WUE:** 0-0.5 (depends on heat rejection method)
- **Pros:** Retrofittable, rack-level granularity, extends air-cooled facilities to higher densities
- **Cons:** Water in the rack row (leak risk), pressure drop affects server fans, piping per rack
- **Best for:** Brownfield density upgrades, mixed-density environments, extending air-cooled life

## Liquid-Based Technologies

### Direct-to-Chip Liquid Cooling (DLC)
Cold plates mounted directly on CPUs/GPUs with facility water loop circulating
coolant. Removes 70-80% of heat at the chip level; residual air cooling for remaining.
- **Density range:** 30-120+ kW/rack
- **PUE contribution:** 0.05-0.15
- **WUE:** 0 (closed-loop, no evaporation)
- **Pros:** Highest efficiency for GPU workloads, enables highest densities, closed-loop water
- **Cons:** Requires piping infrastructure, CDU placement, server-level plumbing modifications
- **Best for:** AI/HPC with B200, GB200, MI300X at high density; new hyperscale builds

### Single-Phase Immersion
Servers submerged in dielectric fluid (mineral oil or engineered fluids). Heat
transferred to fluid, then to facility water loop via heat exchangers.
- **Density range:** 40-100+ kW/rack (tank)
- **PUE contribution:** 0.03-0.10
- **WUE:** 0 (closed-loop dielectric fluid)
- **Pros:** Near-silent operation, no fans needed, excellent heat transfer, dust elimination
- **Cons:** Server form factor changes, fluid cost ($15-30/liter), maintenance complexity, limited vendor support
- **Best for:** Extreme density, noise-sensitive locations, edge with harsh environments

### Two-Phase Immersion
Servers submerged in low-boiling-point dielectric fluid that boils on contact with
hot components. Vapor condenses on overhead coil, returning fluid by gravity.
- **Density range:** 50-200+ kW/rack (theoretical)
- **PUE contribution:** 0.02-0.08
- **WUE:** 0 (closed system)
- **Pros:** Lowest possible PUE contribution, passive circulation (no pumps), extreme density support
- **Cons:** Very high fluid cost ($50-200/liter), limited commercial deployments, GWP concerns for some fluids, specialized enclosures
- **Best for:** Research facilities, extreme density future deployments, not yet mainstream

## Heat Rejection Technologies

### Adiabatic / Evaporative Cooling
Uses water evaporation to pre-cool air or reject heat. Includes direct evaporative
(wetted media) and indirect evaporative (plate heat exchanger with water spray).
- **Density range:** Support technology for any density
- **PUE contribution:** 0.1-0.3 (as heat rejection)
- **WUE:** 0.5-1.5 L/kWh
- **Pros:** Low energy consumption, effective in hot-dry climates, lower cost than mechanical chillers
- **Cons:** Water consumption, less effective in humid climates, Legionella risk management required
- **Best for:** Hot-dry climates (Phoenix, Middle East), hyperscale heat rejection

### Dry Coolers
Finned coil heat exchangers rejecting heat to ambient air without water. Similar to
a car radiator at industrial scale.
- **Density range:** Support technology for any density
- **PUE contribution:** 0.15-0.35
- **WUE:** 0 (completely waterless)
- **Pros:** Zero water consumption, low maintenance, simple operation
- **Cons:** Performance degrades at high ambient temperatures, larger footprint than wet cooling, fan energy
- **Best for:** Water-scarce regions, sovereign facilities requiring water independence, cold/temperate climates

### Cooling Towers
Evaporative heat rejection using water cascading over fill media with airflow.
The most common heat rejection method for large data centers.
- **Density range:** Support technology for any density
- **PUE contribution:** 0.1-0.25
- **WUE:** 1.8-2.5 L/kWh
- **Pros:** Most efficient heat rejection per dollar, proven technology, handles large loads
- **Cons:** High water consumption (7-10M gal/year per MW IT), Legionella risk, chemical treatment required, permitting challenges in water-scarce areas
- **Best for:** Large facilities with abundant water supply, cost-optimized hyperscale

## Advanced Technologies

### Free Cooling / Economizer
Uses cold outdoor air (air-side) or cold outdoor water temperatures (water-side) to
cool the data center without mechanical refrigeration. Hours of availability depend
on climate.
- **Density range:** Support technology for any density
- **PUE contribution:** 0.05-0.20 (averaged annually; varies seasonally)
- **WUE:** 0 (air-side) or low (water-side)
- **Pros:** Dramatically reduces energy in cold climates, 4000-8000+ hours/year in Nordic/cold regions
- **Cons:** Climate-dependent, filtration required for air-side, humidity control complexity
- **Best for:** Cold and temperate climates (Stockholm, Montreal, Dublin), any facility seeking PUE reduction

### Geothermal Cooling
Uses stable underground temperatures (10-15C year-round) via ground-source heat
exchangers (closed-loop boreholes or open-loop groundwater).
- **Density range:** Support technology for any density
- **PUE contribution:** 0.05-0.15
- **WUE:** 0 (closed-loop) or varies (open-loop)
- **Pros:** Consistent year-round performance regardless of ambient conditions, very low operating cost
- **Cons:** High upfront cost (borehole drilling), geological survey required, land area for borehole field, permitting
- **Best for:** Facilities with suitable geology, long-term builds where CapEx is amortized, Nordic/volcanic regions

### Absorption Cooling
Uses waste heat or natural gas to drive a cooling cycle (typically lithium bromide
absorption chiller) instead of electric compressors.
- **Density range:** Support technology for any density
- **PUE contribution:** 0.15-0.30 (depends on heat source)
- **WUE:** 0.5-1.5 L/kWh (with cooling tower rejection)
- **Pros:** Converts waste heat to cooling, reduces electrical load, can use generator waste heat
- **Cons:** Lower COP than electric chillers (0.7-1.4 vs 5-7), larger equipment footprint, water consumption
- **Best for:** Facilities with waste heat source (gas turbines, fuel cells), combined heat and power (CHP) installations

### Heat Reuse
Captures waste heat from the data center cooling loop and delivers it to external
consumers (district heating, greenhouses, industrial processes).
- **Density range:** Support technology for any density
- **PUE contribution:** 0 (does not reduce PUE but offsets external energy use)
- **WUE:** 0 (may reduce overall facility water use if replacing boilers)
- **Pros:** Revenue or cost offset, sustainability reporting benefit, community relations, ERE/ERF improvement
- **Cons:** Requires nearby heat consumer, seasonal demand mismatch, temperature may be too low for some uses (DLC return at 40-50C)
- **Best for:** Nordic countries with district heating networks, facilities near industrial/agricultural heat consumers
