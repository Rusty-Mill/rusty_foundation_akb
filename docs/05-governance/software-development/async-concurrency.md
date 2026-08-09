# Async, sync, concurrency, cancellation, and resources

**RM-DEV-ASYNC-0001:** Async is used only where the contract can exploit genuine I/O concurrency, waiting, multiplexing, or cancellation. CPU-bound and trivially sequential work remains synchronous unless explicitly scheduled.

**RM-DEV-ASYNC-0002:** Potentially blocking portable capabilities provide async paths that do not dedicate a worker solely to waiting when native completion/readiness exists. Blocking adapters disclose their threads, queues, saturation, and shutdown behavior.

**RM-DEV-ASYNC-0003:** Sync APIs MUST NOT create, enter, or block an undisclosed async runtime. Sync completeness has an independent execution path or requires an explicit caller-supplied runtime/service.

**RM-DEV-ASYNC-0004:** Futures/tasks are cancellation-safe only when documented and tested. Dropping a future is not assumed to cancel native work, release operation-owned state, or roll back partial effects.

**RM-DEV-CONC-0001:** Shared mutable state declares synchronization, ordering, fairness, poisoning/failure, reentrancy, and shutdown invariants. Locks are not held across arbitrary callbacks, `.await`, blocking I/O, or FFI calls without explicit proof.

**RM-DEV-CONC-0002:** Atomics document the protected invariant, memory ordering, linearization point, ABA/generation handling, and model/test evidence. `SeqCst` cannot substitute for an unstated invariant.

**RM-DEV-CONC-0003:** Channels, queues, task sets, caches, registries, and callback lists are bounded or have enforced budgets/backpressure and overload evidence.

**RM-DEV-CONC-0004:** Thread affinity, executor affinity, and callback context are explicit semantic properties and verified on every supported provider.

**RM-DEV-RES-0001:** Resources use deterministic ownership and idempotent close/release semantics. Destructors perform bounded infallible local cleanup only; required durable/network effects have explicit operations.

**RM-DEV-RES-0002:** Shutdown joins or accounts for tasks, native operations, threads, handles, callbacks, and buffers. Detached work requires owner, lifetime, failure reporting, and process-exit policy.
