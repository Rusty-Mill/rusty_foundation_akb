# Graphics and presentation conformance specification

**Status:** Draft

| ID | Requirements | Method |
|---|---|---|
| GRAPH-DEVICE-001 | DEVICE-0001–0004 | Enumerate/query with missing, unknown, contradictory, and changing features; resolution never publishes a device below required vector |
| GRAPH-DEVICE-002 | DEVICE-0005–0009 | Inject removal/reset/hang at creation, allocation, compile, submit, wait, present, and destroy; verify one lost epoch and terminal outstanding-work classification |
| GRAPH-MEM-001 | MEMORY-0001–0007 | Exercise zero/maximum/alignment/format/coherency/budget/fragmentation vectors plus use-after-destroy and cross-epoch attempts |
| GRAPH-MEM-002 | MEMORY-0003, 0008–0009 | Scan reused allocations/readback/diagnostics; test import/export ownership, synchronization, denial, revocation, and protected-content boundaries |
| GRAPH-SUBMIT-001 | SUBMIT-0001–0007 | Generate dependency DAGs, cycles, cross-queue races, cancellation/deadline, backpressure, and loss; compare declared happens-before and terminal status |
| GRAPH-SUBMIT-002 | SUBMIT-0008–0009 | Calibrate/disrupt timestamp domains and enable instrumentation; no undeclared ordering or content leakage |
| GRAPH-PRESENT-001 | PRESENT-0001–0005 | Acquire/abandon/submit/present every image and result path; distinguish accepted, displayed, dropped, stale, timeout, and unknown |
| GRAPH-PRESENT-002 | PRESENT-0006–0009 | Resize, occlude, minimize, migrate, suspend, saturate frame flight, toggle modes, and recreate during every phase; bounded latency/resources and exact generations |
| GRAPH-PRESENT-003 | PRESENT-0010–0012 | Color/HDR/alpha/damage/protected-path vectors; compare full redraw oracle and prevent strengthened capture/confidentiality claims |
| GRAPH-FRAME-001 | FRAME-0001–0007 | Correlate input/update/submit/accept/display under fixed, variable, occluded, battery, thermal, and remote conditions; preserve unknown milestones |

## Validation layers

1. Backend-neutral state-machine/property tests.
2. Provider validation layers/debug runtime where available.
3. Native trace comparison for ownership, synchronization, and presentation.
4. Visual/color reference patterns under fixed display configurations.
5. Fault-injection and long-duration resource accounting.

Passing a native validation layer is supporting evidence, not proof of Rusty Mill behavioral conformance.

