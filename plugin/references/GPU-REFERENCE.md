# GPU Reference Data

> TDP, cooling requirements, memory, bandwidth, interconnect, and density
> specifications for data center AI/HPC accelerators.
> Skills load individual sections by H2 header -- do not load the entire file.

**As-of:** 2026-03-27
**Next review:** 2026-06-27
**Staleness warning:** 90 days

---

## NVIDIA Hopper (H100, H200)

The Hopper generation remains widely deployed in production AI/HPC data centers. H100 SXM5 is the canonical data center variant; H200 adds higher-capacity HBM3e memory on the same architecture.

| Accelerator | TDP | Memory | Mem BW | Interconnect BW | Cooling | Form Factor | Confidence | Source |
|-------------|-----|--------|--------|-----------------|---------|-------------|------------|--------|
| H100 SXM5 | 700W | 80 GB HBM3 | 3.35 TB/s | 900 GB/s NVLink | Air or liquid | SXM5 | confirmed | [NVIDIA H100](https://www.nvidia.com/en-us/data-center/h100/) |
| H100 PCIe | 350W | 80 GB HBM3 | 2.0 TB/s | PCIe Gen5 x16 | Air | PCIe | confirmed | [NVIDIA H100](https://www.nvidia.com/en-us/data-center/h100/) |
| H200 SXM | 700W | 141 GB HBM3e | 4.8 TB/s | 900 GB/s NVLink | Air or liquid | SXM5 | confirmed | [NVIDIA H200](https://www.nvidia.com/en-us/data-center/h200/) |

**Rack density ranges (H100/H200 SXM5):**
- Air-cooled: 20-35 kW/rack (4-8 GPUs per node, 4-8 nodes per rack)
- Rear-door heat exchanger (RDHx): up to 45 kW/rack
- Direct liquid cooling (DLC): up to 60 kW/rack

**Compute performance:**
- H100 SXM5: 3,958 TFLOPS FP8, 1,979 TFLOPS FP16
- H200: Same compute as H100, but 1.76x memory capacity enables larger models without recomputation

> Note: H100 NVL (dual-GPU module, 94 GB HBM3 per GPU) exists but is less common in large-scale deployments. Specs follow SXM5 baseline with dual-GPU NVLink bridge.

---

## NVIDIA Blackwell (B200, GB200)

Blackwell represents a generational leap in per-GPU power and density. B200 is the discrete accelerator; GB200 NVL72 is a rack-scale system with mandatory liquid cooling.

| Accelerator | TDP | Memory | Mem BW | Interconnect BW | Cooling | Form Factor | Confidence | Source |
|-------------|-----|--------|--------|-----------------|---------|-------------|------------|--------|
| B200 | 1,000W | 192 GB HBM3e | 8 TB/s | 1.8 TB/s NVLink | Air/liquid (see notes) | SXM | confirmed | [NVIDIA B200](https://www.nvidia.com/en-us/data-center/b200/) |
| GB200 NVL72 | 120 kW/rack | 13.5 TB aggregate (72 GPUs) | N/A (rack-level) | 130 TB/s NVLink domain | Liquid mandatory | Rack-scale | confirmed | [NVIDIA GB200 NVL72](https://www.nvidia.com/en-us/data-center/gb200-nvl72/) |

**Cooling notes by density tier:**
- B200 air-cooled: viable up to ~35 kW/rack
- B200 rear-door heat exchanger (RDHx): up to ~50 kW/rack
- B200 direct liquid cooling (DLC): up to ~70 kW/rack
- GB200 NVL72: **mandatory** liquid cooling -- 25C max inlet temperature, 45C outlet, minimum 20 L/min flow rate per rack

**GB200 NVL72 rack specifications:**
- 72 Blackwell GPUs + 36 Grace CPUs per rack
- Total rack power: 120 kW (some reports cite 125-130 kW)
- Dimensions: standard 52U rack with custom liquid cooling manifolds
- Networking: 72x 400G ConnectX-8 per rack (external fabric)

> Source: [Introl B200 vs GB200 Deployment Guide](https://introl.com/blog/nvidia-b200-vs-gb200-deployment-guide) | [TrendForce rack power analysis](https://x.com/trendforce/status/1900050272568926560)

**Compute performance:**
- B200: 9,000 TFLOPS FP4, 4,500 TFLOPS FP8
- GB200 NVL72: Up to 1.4 ExaFLOPS FP4 per rack (72 GPUs)

---

## AMD Instinct (MI300X, MI350X)

AMD Instinct accelerators use the OAM (OCP Accelerator Module) form factor and compete on memory capacity and bandwidth. MI300X is shipping; MI350X launched mid-2025 with higher memory capacity.

| Accelerator | TDP | Memory | Mem BW | Interconnect BW | Cooling | Form Factor | Confidence | Source |
|-------------|-----|--------|--------|-----------------|---------|-------------|------------|--------|
| MI300X | 750W | 192 GB HBM3 | 5.3 TB/s | PCIe Gen5 / Infinity Fabric | Air or liquid | OAM | confirmed | [AMD MI300X Datasheet](https://www.amd.com/content/dam/amd/en/documents/instinct-tech-docs/data-sheets/amd-instinct-mi300x-data-sheet.pdf) |
| MI350X | ~750W | 288 GB HBM3e | ~8 TB/s (estimated) | Infinity Fabric | TBD | OAM | estimated | [AMD MI350 Product Page](https://www.amd.com/en/products/accelerators/instinct/mi350.html) |

**Notes:**
- MI300X uses 8 XCDs (Accelerator Complex Dies) on a single package with 12 HBM3 stacks
- MI350X TDP is **not vendor-confirmed** as of March 2026. The ~750W estimate is based on the MI300X baseline and industry analyst expectations. Actual TDP may range 750-1,000W.
- MI350X memory bandwidth estimated from HBM3e specifications; official figures pending AMD datasheet publication
- OAM form factor requires compatible baseboard (e.g., AMD OAM UBB or OCP-compliant third-party)

**Rack density:**
- MI300X air-cooled: 20-35 kW/rack (similar to H100)
- MI300X liquid-cooled: up to 60 kW/rack
- MI350X density guidance not yet published

---

## Intel Gaudi

Intel Gaudi 3 targets cost-optimized AI training and inference. Available in both PCIe and OAM form factors with significantly different power envelopes.

| Accelerator | TDP | Memory | Mem BW | Interconnect BW | Cooling | Form Factor | Confidence | Source |
|-------------|-----|--------|--------|-----------------|---------|-------------|------------|--------|
| Gaudi 3 PCIe | 600W | 128 GB HBM2e | 3.67 TB/s | PCIe Gen5 x16 + 24x 200G RoCE | Air | PCIe | confirmed | [Intel Gaudi 3 White Paper](https://www.intel.com/content/www/us/en/content-details/817486/intel-gaudi-3-ai-accelerator-white-paper.html) |
| Gaudi 3 OAM | 900W | 128 GB HBM2e | 3.67 TB/s | 24x 200G RoCE | Air or liquid | OAM | confirmed | [Intel Gaudi 3 White Paper](https://www.intel.com/content/www/us/en/content-details/817486/intel-gaudi-3-ai-accelerator-white-paper.html) |

**Notes:**
- Gaudi 3 uses integrated Ethernet (RoCE v2) for scale-out rather than proprietary interconnect
- 24x 200G ports provide 4.8 Tb/s aggregate network bandwidth per accelerator
- OAM variant supports higher-density deployments requiring liquid cooling
- Intel has announced Gaudi architecture transition to Falcon Shores; Gaudi 3 is the current shipping product
- Gaudi 3 positioning: ~40% lower cost than equivalent NVIDIA systems (Intel claim, not independently verified)

**Rack density:**
- Gaudi 3 PCIe: 15-25 kW/rack (lower density due to PCIe form factor)
- Gaudi 3 OAM: 25-40 kW/rack air-cooled, up to 55 kW/rack liquid-cooled

---

## Google TPU

Google TPUs are **cloud-only** accelerators available exclusively through Google Cloud. They are included for comparison context when evaluating on-premise GPU clusters against cloud alternatives.

| Accelerator | TDP | Memory | Mem BW | Interconnect BW | Cooling | Availability | Confidence | Source |
|-------------|-----|--------|--------|-----------------|---------|--------------|------------|--------|
| TPU v5p | 450W | 95 GB HBM | 2.76 TB/s | 4,800 Gbps ICI | Liquid (Google infrastructure) | Cloud-only | confirmed | [Google TPU v5p Docs](https://docs.cloud.google.com/tpu/docs/v5p) |
| TPU v6e (Trillium) | ~250W (estimated) | 32 GB HBM | N/A | ICI (improved) | Google infrastructure | Cloud-only | estimated | [Google TPU v6e Docs](https://docs.cloud.google.com/tpu/docs/v6e) |

**Notes:**
- TPU v5p deploys in pods of up to 8,960 chips connected via Inter-Chip Interconnect (ICI)
- TPU v6e (Trillium): Google claims 67% more energy-efficient than v5e and 4.7x peak compute performance
- TPU v6e TDP of ~250W is **estimated** from the efficiency improvement claim relative to v5e. Google does not publish per-chip TDP for cloud-only hardware.
- TPUs are not available for on-premise deployment; data center planners use TPU pricing/performance for build-vs-buy analysis
- TPU v5p supports 3D torus topology for large-scale training interconnect

**Relevance to DC planning:**
- Use TPU pricing (on-demand and committed use) as a cloud comparison baseline
- TPU pod power is managed entirely by Google; no facility-level cooling design needed
- Cost comparison: TPU v5p on-demand ~$4.20/chip/hour vs GPU on-premise amortized cost

---

## Interconnect & Networking

High-bandwidth, low-latency interconnect is critical for distributed AI training. This section covers GPU-to-GPU and rack-to-rack networking technologies relevant to data center fabric design.

**NVLink generations:**

| Generation | Bandwidth (bidirectional) | GPUs Connected | Used By | Source |
|------------|--------------------------|----------------|---------|--------|
| NVLink 4th gen | 900 GB/s | Up to 8 (via NVSwitch) | H100, H200 | [NVIDIA NVLink](https://www.nvidia.com/en-us/data-center/nvlink/) |
| NVLink 5th gen | 1.8 TB/s | Up to 72 (via NVSwitch) | B200, GB200 | [NVIDIA NVLink](https://www.nvidia.com/en-us/data-center/nvlink/) |

**NVSwitch:**
- NVSwitch 3rd gen (Hopper): Connects 8 GPUs in a fully-connected topology within a node
- NVSwitch 4th gen (Blackwell): Connects up to 72 GPUs in GB200 NVL72 with 130 TB/s aggregate bisection bandwidth

**Data center fabric (rack-to-rack):**

| Technology | Per-Port BW | Typical Use | Notes | Source |
|------------|-------------|-------------|-------|--------|
| InfiniBand NDR | 400 Gbps | AI training clusters | NVIDIA-ecosystem standard; lowest latency | [NVIDIA InfiniBand](https://www.nvidia.com/en-us/networking/products/infiniband/) |
| InfiniBand XDR | 800 Gbps | Next-gen AI clusters | Shipping 2025+; doubles NDR bandwidth | [NVIDIA InfiniBand](https://www.nvidia.com/en-us/networking/products/infiniband/) |
| Ethernet RoCEv2 | 400/800 Gbps | Cost-optimized clusters | Higher latency than IB; improving with RDMA | Industry standard |
| Ultra Ethernet | 800 Gbps+ | Future standard | UEC consortium; AI-optimized Ethernet | [Ultra Ethernet Consortium](https://ultraethernet.org/) |

**Network design considerations for DC planners:**
- InfiniBand requires dedicated fabric (separate from management/storage networks)
- Typical AI cluster: 1-2 InfiniBand ports per GPU (400-800 Gbps each)
- Cable density: GB200 NVL72 rack has 72x 400G external connections = 28.8 Tbps per rack
- Optics: 400G SR4/DR4 for intra-row (<100m), 400G FR4 for inter-row (<2km)

---

## Cooling Requirements by GPU

Thermal matrix for data center cooling design. Maps each accelerator to recommended cooling method, maximum rack density per cooling type, and inlet temperature requirements. This section serves the eng-cooling-design skill directly.

| Accelerator | TDP | Air Cooling Max | RDHx Max | DLC Max | Liquid Mandatory | Max Inlet Temp | Confidence |
|-------------|-----|-----------------|----------|---------|------------------|----------------|------------|
| H100 SXM5 | 700W | 35 kW/rack | 45 kW/rack | 60 kW/rack | No | 35C (ASHRAE A1) | confirmed |
| H200 SXM | 700W | 35 kW/rack | 45 kW/rack | 60 kW/rack | No | 35C (ASHRAE A1) | confirmed |
| B200 SXM | 1,000W | 35 kW/rack | 50 kW/rack | 70 kW/rack | No (below 35kW) | 35C (ASHRAE A1) | confirmed |
| GB200 NVL72 | 120 kW/rack | N/A | N/A | 120 kW/rack | **Yes** | 25C | confirmed |
| MI300X OAM | 750W | 35 kW/rack | 45 kW/rack | 60 kW/rack | No | 35C (ASHRAE A1) | confirmed |
| MI350X OAM | ~750W | ~35 kW/rack | ~45 kW/rack | ~60 kW/rack | No (estimated) | 35C (estimated) | estimated |
| Gaudi 3 PCIe | 600W | 25 kW/rack | 35 kW/rack | 45 kW/rack | No | 35C (ASHRAE A1) | confirmed |
| Gaudi 3 OAM | 900W | 40 kW/rack | 50 kW/rack | 55 kW/rack | No | 35C (ASHRAE A1) | confirmed |
| TPU v5p | 450W | N/A | N/A | N/A | Google-managed | Google-managed | confirmed |
| TPU v6e | ~250W | N/A | N/A | N/A | Google-managed | Google-managed | estimated |

**Cooling method definitions:**
- **Air cooling:** Hot/cold aisle containment with CRAC/CRAH units. Viable for densities up to ~35 kW/rack.
- **RDHx (Rear-Door Heat Exchanger):** Water-cooled rear door removes heat at the rack. Extends air-cooled facilities to ~50 kW/rack without raised floor changes.
- **DLC (Direct Liquid Cooling):** Cold plates on CPUs/GPUs with facility water loop. Enables 60-70 kW/rack. Requires piping infrastructure.
- **Immersion:** Single-phase or two-phase immersion. Alternative to DLC for highest densities. Not yet mainstream for GPU workloads.

**ASHRAE thermal guidelines (TC 9.9):**
- A1 class: 15-32C recommended, 15-35C allowable inlet temperature
- A2 class: 10-35C recommended (for higher-density facilities)
- Liquid cooling inlet: Typically 25-45C depending on system; GB200 NVL72 requires 25C max

> Sources: [NVIDIA Thermal Design Guides](https://www.nvidia.com/en-us/data-center/), [ASHRAE TC 9.9 Thermal Guidelines](https://tc0909.ashraetcs.org/), [Introl Deployment Guide](https://introl.com/blog/nvidia-b200-vs-gb200-deployment-guide)
