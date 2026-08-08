# Atomics and memory ordering

**RM-THREAD-ATOMIC-0001:** Portable atomic operations follow the current supported Rust atomic memory model and expose only target-supported widths/alignment or a separately disclosed lock-based emulation.

**RM-THREAD-ATOMIC-0002:** Relaxed, acquire, release, acquire-release, and sequentially consistent orderings retain their Rust meanings. Invalid operation/order combinations are rejected.

**RM-THREAD-ATOMIC-0003:** Data races involving non-atomic conflicting access are undefined behavior. Volatile access, scheduler priority, single-core affinity, and OS interlocked naming do not replace synchronization.

**RM-THREAD-ATOMIC-0004:** Compare-exchange distinguishes success/failure orderings and permits weak spurious failure only where requested. ABA avoidance, reclamation, progress, and compound invariants are protocol responsibilities.

**RM-THREAD-ATOMIC-0005:** Lock-free, wait-free, obstruction-free, and merely atomic are distinct implementation qualities reported per type/operation/target.

**RM-THREAD-ATOMIC-0006:** Cross-process or device-shared atomics require separate cache-coherence, representation, mapping, and lifetime evidence; ordinary process atomics do not imply them.

