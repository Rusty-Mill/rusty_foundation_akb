# `rm.graphics.submission`

| Field | Value |
|---|---|
| Status | Draft |
| Contract version | 0.1.0 |

**RM-GRAPHICS-SUBMIT-0001:** A submission names one device epoch, queue class, immutable work batch, resource accesses/transitions, wait dependencies, signal milestones, priority class, and diagnostic correlation.

**RM-GRAPHICS-SUBMIT-0002:** Submission acceptance means ownership transferred to the provider; it does not mean execution, completion, or visibility. Each milestone has a separate observable result.

**RM-GRAPHICS-SUBMIT-0003:** Synchronization edges form an acyclic happens-before graph under the portable contract. Cycles and unsatisfied external waits fail validation or terminate with a bounded diagnostic rather than hanging silently.

**RM-GRAPHICS-SUBMIT-0004:** A completion value is monotonic within its synchronization timeline and scoped to one device epoch. Waiting supports async and sync paths, deadlines, and cancellation without cancelling already accepted GPU work by implication.

**RM-GRAPHICS-SUBMIT-0005:** Frames/work in flight are bounded by explicit policy. Backpressure occurs before unbounded CPU work, command storage, presentation images, or latency accumulates.

**RM-GRAPHICS-SUBMIT-0006:** Queue order is guaranteed only within a declared queue/timeline and explicit dependencies. Independent queues may overlap; accidental native serialization is not a portable guarantee.

**RM-GRAPHICS-SUBMIT-0007:** On device loss, every accepted submission receives a terminal status: proven complete, not executed, or indeterminate. Resource reuse/destruction rules treat indeterminate work conservatively.

**RM-GRAPHICS-SUBMIT-0008:** Timestamp/query results identify clock domain, valid bits/range, calibration quality, availability, and discontinuities. They never masquerade as the runtime monotonic clock without an explicit correlation.

**RM-GRAPHICS-SUBMIT-0009:** Validation and observability are bounded, optional by contract, and content-safe. Instrumentation cannot insert undeclared synchronization that changes correctness.

