# Locality, failover, and recovery

**RM-TRAFFIC-LOCALITY-0001:** Locality binds region/zone/rack/node/network/edge/provider and data-residency/compliance fault domains with provenance, topology generation, distance/cost, and authority; labels are not assumed trustworthy.

**RM-TRAFFIC-LOCALITY-0002:** Locality preference, strictness, spillover, capacity reservation, cross-zone/region cost, latency, resilience, privacy, and data authority are explicit route policy.

**RM-TRAFFIC-FAILOVER-0001:** Failover binds trigger evidence, source and target service/subset/locality generations, consistency/data readiness, credentials, capacity, traffic ramp, retry/effect safety, DNS/control-plane propagation, objectives, and operator authority.

**RM-TRAFFIC-FAILOVER-0002:** Detection, decision, configuration acceptance, endpoint visibility, new connection/request routing, existing session handling, sink/data readiness, and user-visible recovery are separate milestones.

**RM-TRAFFIC-FAILOVER-0003:** Failback is a new controlled transition with health hold, capacity/data convergence, progressive ramp, affinity/session behavior, rollback, and split-view prevention rather than automatic reversal.

**RM-TRAFFIC-FAILOVER-0004:** Partial partitions and asymmetric reachability can create different endpoint/health views; globally exclusive routing claims require coordination and resource-enforced fencing where effects demand it.

**RM-TRAFFIC-FAILOVER-0005:** Brownout/degraded modes name disabled features, reduced quality, stale/read-only paths, authorization, user disclosure, objectives, and recovery gates.

**RM-TRAFFIC-LOCALITY-0003:** Desktop/mobile/offline clients treat network/location change as a new discovery and connection generation with cache partitioning, privacy, metering, background, and power policy.
