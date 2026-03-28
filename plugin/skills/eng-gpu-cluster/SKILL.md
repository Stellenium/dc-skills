---
name: eng-gpu-cluster
description: "Design AI and HPC GPU cluster facility infrastructure including accelerator selection, rack layout, power delivery, and cooling at chip level. Use when planning GPU cluster infrastructure, designing AI training facilities, sizing racks for H100/B200/MI300X, or planning high-density compute deployments. Trigger with \"GPU cluster\", \"AI cluster design\", \"HPC facility\", \"GPU rack layout\", \"H100 infrastructure\", \"B200 deployment\", or \"AI training facility\"."
argument-hint: "<gpu-model or workload>"
---

# GPU Cluster Facility Design

Design AI/HPC GPU cluster facility infrastructure covering accelerator selection,
rack layout, power and cooling per rack, interconnect topology, and training vs
inference optimization. Produces a complete cluster facility plan with rack layout,
cooling distribution, and network fabric design.

## What I Need from Upstream

**From power-capacity-model (eng-power-model):**
- Total IT load budget (kW)
- Per-rack power budget (kW/rack)
- Utility capacity and redundancy tier
- Phased deployment schedule (if multi-phase)

If upstream data is not available, I will ask you for total power budget
and redundancy requirements.

## Phase 1: Critical Discovery

> Answer these questions first. They determine the entire approach.

**Project Context:**

1. Is this a greenfield site or brownfield conversion?
   - **Greenfield:** New construction -- proceed to Greenfield Path below
   - **Brownfield:** Adding GPU compute to existing facility -- proceed to Brownfield Path below

2. What facility type?
   - Traditional enterprise (single-tenant, 2-20MW)
   - Hyperscale (cloud provider, 20-500MW+)
   - Sovereign (government/national security)
   - Colocation (multi-tenant, retail or wholesale)
   - Modular/prefab (factory-built, rapid deployment)
   - Edge (1-5MW, distributed)

3. What is the primary workload?
   - AI training (large model training, distributed across many GPUs)
   - AI inference (model serving, latency-sensitive)
   - HPC simulation (traditional scientific computing)
   - Mixed (training + inference or multi-tenant)

4. What is the target GPU/accelerator?
   - NVIDIA H100 SXM5 (700W, 80GB HBM3)
   - NVIDIA H200 SXM (700W, 141GB HBM3e)
   - NVIDIA B200 SXM (1000W, 192GB HBM3e)
   - NVIDIA GB200 NVL72 (120kW/rack, 72 GPUs, liquid mandatory)
   - AMD MI300X (750W, 192GB HBM3)
   - AMD MI350X (~750W, 288GB HBM3e)
   - Intel Gaudi 3 (600-900W)
   - Undecided (will evaluate options)

5. What is the total compute scale?
   - Number of GPUs (e.g., 1000, 10000, 100000)
   - Or target compute capacity (PFLOPS FP8/FP16)

6. What are the interconnect requirements?
   - Single-node (no GPU-to-GPU across nodes)
   - Multi-node NVLink domain (GB200 NVL72: 72 GPUs per domain)
   - InfiniBand fabric (NDR 400G or XDR 800G)
   - Ethernet-based (RoCEv2, 400G or 800G)

7. What is the deployment timeline?
   - Immediate (0-6 months)
   - Near-term (6-12 months)
   - Phased multi-year

## Phase 2: Context Refinement

> Based on Phase 1 answers, gather additional detail.

### Training Path

If workload is **AI training**:
1. Maximum model size (parameters) and target parallelism strategy?
2. Cluster topology preference? (fat-tree, rail-optimized, dragonfly)
3. NVLink domain sizing requirements? (8 GPU for H100, 72 GPU for GB200)
4. Checkpoint storage requirements? (capacity and throughput for model checkpoints)
5. Job scheduler and orchestration platform? (Slurm, Kubernetes, custom)

### Inference Path

If workload is **AI inference**:
1. Target latency SLA? (time to first token, inter-token latency)
2. Request routing strategy? (load balancer, model routing, A/B testing)
3. Model parallelism approach? (tensor parallel, pipeline parallel, data parallel)
4. Autoscaling requirements? (burst capacity, minimum always-on)
5. Multi-model serving? (single large model vs. many smaller models)

### High-Density Path (>50 kW/rack)

If rack density exceeds 50 kW:
1. CDU (Coolant Distribution Unit) placement strategy?
2. Piping manifold design: overhead or underfloor?
3. Secondary cooling loop temperature and flow rate requirements?
4. Facility water loop integration with building cooling plant?

### Brownfield Path

If Phase 1 answer is **Brownfield**:
1. Existing rack infrastructure and power density per rack?
2. Structural floor loading capacity? (40kW air rack ~800kg; 120kW liquid rack ~2000kg+)
3. Existing cooling type and available cooling capacity?
4. Available power capacity beyond current IT load?
5. Network infrastructure (fiber, conduit, MDF/IDF locations)?

### Multi-Generation Path

If deploying mixed GPU generations:
1. Network segmentation strategy? (separate fabrics or shared)
2. Cooling zone separation? (air-cooled H100 zone vs liquid-cooled B200 zone)
3. Power density zoning? (different kW/rack by GPU generation)

## Facility Type Parameters

| Parameter | Traditional | Hyperscale | Sovereign | Colo | Modular | Edge |
|-----------|-------------|------------|-----------|------|---------|------|
| Typical GPU count | 100-1,000 | 10,000-100,000+ | 1,000-10,000 | 100-5,000 | 100-2,000 | 10-200 |
| Rack density (kW) | 20-40 | 40-120 | 30-80 | 20-50 | 30-80 | 10-30 |
| Network fabric | IB or Ethernet | InfiniBand | InfiniBand | Ethernet | InfiniBand | Ethernet |
| Cooling | Air/hybrid | Liquid | Liquid | Air/hybrid | Liquid | Air/packaged |
| Interconnect tier | NDR 400G | XDR 800G | NDR/XDR | NDR 400G | NDR 400G | Ethernet 400G |

## GPU Selection Matrix

Load detailed specifications on demand from [GPU Reference](../../references/GPU-REFERENCE.md).

| GPU | TDP | Memory | Interconnect | Cooling | Training | Inference |
|-----|-----|--------|--------------|---------|----------|-----------|
| H100 SXM5 | 700W | 80GB HBM3 | 900 GB/s NVLink | Air or liquid | Strong | Strong |
| H200 SXM | 700W | 141GB HBM3e | 900 GB/s NVLink | Air or liquid | Strong (larger models) | Strong |
| B200 SXM | 1,000W | 192GB HBM3e | 1.8 TB/s NVLink | Air/liquid | Best-in-class | Strong |
| GB200 NVL72 | 120kW/rack | 13.5TB aggregate | 130 TB/s NVLink domain | Liquid mandatory | Best (72-GPU domain) | Optimal for large models |
| MI300X | 750W | 192GB HBM3 | Infinity Fabric | Air or liquid | Competitive | Strong (memory advantage) |
| MI350X | ~750W | 288GB HBM3e | Infinity Fabric | TBD | Competitive | Strong |
| Gaudi 3 PCIe | 600W | 128GB HBM2e | 24x200G RoCE | Air | Cost-optimized | Cost-optimized |
| Gaudi 3 OAM | 900W | 128GB HBM2e | 24x200G RoCE | Air or liquid | Cost-optimized | Cost-optimized |

## Analysis & Output

### Rack Layout Design Process

1. **Determine per-rack power** from GPU count x TDP + networking overhead (10-15% of GPU power) + storage overhead (5-10%)
2. **Calculate total racks** = total GPU count / GPUs per rack
3. **Map rack rows** to network fabric topology:
   - NVLink domains = physical adjacency (H100: 8-GPU node; GB200: 72-GPU rack)
   - InfiniBand leaf switches serve one or two racks; spine switches aggregate rows
4. **Plan cooling zones:**
   - Air-cooled racks: hot/cold aisle containment, 20-35 kW/rack
   - Liquid-cooled racks: CDU placement at 1 CDU per 8-16 racks typical
5. **Determine floor loading:** 40kW air-cooled rack ~800kg; 120kW liquid-cooled rack ~2000kg+
   - Standard raised floor: 1000-1200 kg capacity -- structural reinforcement or slab-on-grade for liquid-cooled
6. **Calculate cable density:** GB200 NVL72 = 72x 400G external connections per rack = 28.8 Tbps
7. **Size storage tier:** checkpoint storage for training (typically 2-5x model size, NVMe or parallel filesystem)

### Reference Data

Load these files on demand -- do not read upfront:

- [GPU specifications](../../references/GPU-REFERENCE.md) -- All sections: accelerator specs, interconnect bandwidth, cooling requirements, rack density ranges

### Validation Loop

1. Verify per-rack power does not exceed facility power budget per rack
2. Cross-check GPU TDP against GPU-REFERENCE.md specifications
3. Validate cooling technology matches rack density (>35kW requires liquid or RDHx; >80kW requires DLC/immersion; GB200 NVL72 mandates liquid at 25C max inlet)
4. Verify interconnect topology supports required NVLink domain size
5. Check floor loading capacity against rack weight estimates
6. Validate total power does not exceed utility capacity (including redundancy overhead)
7. If any constraint violated: flag the error, adjust layout, recompute from step 1

## Output

This skill produces two files:
1. `<project-name>-gpu-cluster-design.md` -- Full report
2. `<project-name>-gpu-cluster-design.json` -- Structured data for downstream skills

### GPU Cluster Design Report

**Project:** [Project Name]
**Date:** [Date]
**Prepared by:** [Skill: eng-gpu-cluster v1.0]

#### 1. Executive Summary
- Workload type: [training / inference / mixed]
- Accelerator: [GPU model]
- Total GPUs: [count]
- Total racks: [count] at [X-Y kW/rack]
- Total IT load: [X-Y MW] (range reflecting configuration options)
- Cooling type: [air / liquid / hybrid]
- Interconnect: [InfiniBand NDR/XDR / Ethernet RoCEv2]

#### 2. Accelerator Selection
- Selected: [GPU model] -- justification based on workload, budget, timeline
- Alternatives evaluated: [list with brief rationale for rejection]

#### 3. Cluster Topology
```
[Text-based topology diagram]
Row 1: [racks] -- Leaf Switch -- Spine
Row 2: [racks] -- Leaf Switch -- Spine
...
NVLink Domain: [size] GPUs per domain
```

#### 4. Rack Layout
| Row | Racks | GPU/Rack | kW/Rack | Cooling | Network |
|-----|-------|----------|---------|---------|---------|
| Row 1 | [N] | [M] | [X-Y] | [type] | [ports] |

#### 5. Per-Rack Power/Cooling Budget
| Component | Power (kW) | % of Rack | Notes |
|-----------|-----------|-----------|-------|
| GPUs | [X] | [Y%] | [count] x [TDP] |
| Networking | [X] | [Y%] | Switches + NICs |
| Storage | [X] | [Y%] | NVMe + controllers |
| Overhead | [X] | [Y%] | BMC, fans, misc |
| **Total** | **[X-Y]** | **100%** | |

#### 6. Interconnect Fabric Design
- Intra-node: [NVLink generation, bandwidth]
- Inter-node: [InfiniBand/Ethernet, per-port bandwidth]
- Topology: [fat-tree / rail-optimized / dragonfly]
- Total fabric ports: [count]
- Optics: [SR4/DR4 for intra-row, FR4 for inter-row]

#### 7. Cooling Distribution Plan
- Primary cooling: [technology]
- CDU count and placement: [N CDUs, 1 per X racks]
- Piping manifold: [overhead / underfloor]
- Inlet temperature: [X C max]

#### 8. Phased Deployment Plan
| Phase | GPUs | Racks | IT Load (MW) | Timeline | Cost Estimate |
|-------|------|-------|-------------|----------|---------------|
| Phase 1 | [N] | [N] | [X-Y] | [date] | [$X-YM] |

### JSON Sidecar

```json
{
  "artifact_type": "gpu-cluster-design",
  "skill_version": "1.0",
  "project_name": "<project-name>",
  "gpu_model": "nvidia-b200",
  "total_gpus": 10000,
  "total_racks": 250,
  "per_rack_kw": 50,
  "total_it_load_kw": 12500,
  "cooling_type": "direct-liquid-cooling",
  "interconnect_type": "infiniband-ndr",
  "topology": "fat-tree",
  "nvlink_domain_size": 8,
  "workload_type": "training",
  "phases": [
    {"phase": 1, "gpus": 5000, "racks": 125, "it_load_kw": 6250, "timeline": "2025-Q4"}
  ]
}
```

## Gotchas

- GB200 NVL72 is a RACK-SCALE system -- 72 GPUs + 36 Grace CPUs per rack at ~120kW. You cannot put fewer GPUs in a rack or mix with other GPU types in the same rack. The entire rack is one NVLink domain.
- NVLink domain size determines the maximum model parallel width. H100 NVLink domain is 8 GPUs (one node); GB200 NVL72 domain is 72 GPUs (one rack). This fundamentally changes training topology and the models you can efficiently train.
- InfiniBand fabric pricing scales non-linearly. At 10,000+ GPUs, the network (switches, optics, cables) can cost 30-50% of the GPU cost itself due to spine switch density.
- Floor loading for liquid-cooled GPU racks (2000kg+) exceeds standard raised-floor capacity (typically rated for 1000-1200kg). Structural reinforcement or slab-on-grade is required for any deployment above ~50kW/rack.
- Training cluster utilization rarely exceeds 70-80% due to collective communication overhead (AllReduce, AllGather). Do not size power/cooling for 100% simultaneous GPU utilization -- use 75-85% as the design point.

## Evaluations

See `evals/evals.json` for test scenarios.
