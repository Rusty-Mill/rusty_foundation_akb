# Realtime audio processing

The device-driven callback is a restricted execution domain with a finite frame budget. Its data plane is preallocated and bounded; construction, graph mutation, diagnostics export, permission UI, device enumeration, and recovery live on a control plane.

**RM-AUDIO-RT-0001:** A realtime callback MUST NOT allocate, block, perform file/network I/O, acquire an ordinary contended lock, wait on another executor, invoke user-interface APIs, or emit synchronous logs.

**RM-AUDIO-RT-0002:** Callback inputs, outputs, scratch memory, command queues, and telemetry counters MUST be preallocated or proven bounded and realtime-safe.

**RM-AUDIO-RT-0003:** Control-plane changes become visible through a bounded lock-free or equivalent proven handoff at a declared frame boundary. Destruction waits outside the callback for generation retirement.

**RM-AUDIO-RT-0004:** Callback panic/unwind MUST NOT cross FFI or platform callback boundaries. Failure policy is declared and may silence, bypass, stop, or invalidate with deferred diagnostics.

**RM-AUDIO-RT-0005:** Realtime quality claims require measured deadline misses, callback duration distribution, XRUNs, page faults, allocations, priority/QoS state, CPU/power conditions, and interference workload.

**RM-AUDIO-RT-0006:** “Lock-free” alone is insufficient: algorithms MUST prove bounded work, memory lifetime, ordering, overflow behavior, and absence of reclamation stalls on the callback path.

See [ADR-0049](../../adr/0049-realtime-audio-callbacks-are-a-restricted-execution-domain.md).
