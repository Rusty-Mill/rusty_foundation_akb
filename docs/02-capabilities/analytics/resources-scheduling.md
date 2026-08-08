# Resources, scheduling, and spill

**RM-ANALYTICS-RESOURCE-0001:** Jobs declare principal/tenant, priority/class, deadline, parallelism bounds, CPU/memory/disk/network/GPU/accelerator, spill/shuffle/state/checkpoint, source/sink rate, monetary/energy/carbon, and locality budgets.

**RM-ANALYTICS-RESOURCE-0002:** Admission and scheduling provide quota, fairness, reservation, preemption, gang/placement, affinity/anti-affinity, fault-domain, data locality, accelerator compatibility, and starvation policy without implying execution guarantees.

**RM-ANALYTICS-RESOURCE-0003:** Memory accounts operator, input/output, hash/sort/join/aggregate, decoding, network, native/GPU, cache, state, checkpoint, and allocator overhead with cooperative revocation and bounded failure.

**RM-ANALYTICS-SPILL-0001:** Spill files bind job/stage/task/attempt/partition, schema/encoding, ordering, integrity, encryption, quota, storage identity/generation, cleanup, and recovery; sensitive data remains protected outside memory.

**RM-ANALYTICS-RESOURCE-0004:** Backpressure flows from sinks/exchanges/operators to sources with bounded queues and observable throttling; buffering cannot convert sustained overload into hidden unbounded latency/state.

**RM-ANALYTICS-RESOURCE-0005:** Skew detection and mitigation record sampling/threshold, split/salt/repartition/broadcast changes, semantic equivalence, resource amplification, and realized-plan evidence.

**RM-ANALYTICS-RESOURCE-0006:** Preemption/cancellation/checkpoint/savepoint behavior names lost/reusable work, state/effect boundary, priority inversion, cleanup, and resumption authority.

**RM-ANALYTICS-RESOURCE-0007:** Multitenant workers isolate memory, CPU, spill/shuffle/state, credentials, catalogs, code/functions, caches, diagnostics, and network egress according to risk.
