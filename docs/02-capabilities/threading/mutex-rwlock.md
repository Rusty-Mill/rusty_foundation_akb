# Mutexes and reader/writer locks

**RM-THREAD-MUTEX-0001:** Successful unlock synchronizes-with a later successful acquisition according to the Rust/native memory model. Ownership, recursion, process scope, and poisoning policy are explicit.

**RM-THREAD-MUTEX-0002:** Acquisition supports blocking, try, and monotonic-deadline forms where selected. Timeout/cancellation does not imply acquisition and leaves no owned guard.

**RM-THREAD-MUTEX-0003:** Fairness, FIFO order, priority inheritance, adaptive spinning, and starvation bounds are independent qualities; none are inferred from the name `mutex`.

**RM-THREAD-MUTEX-0004:** Panic/abnormal-owner detection is an advisory consistency signal. Recovery requires application validation; automatic poisoning is a policy, not a universal native behavior.

**RM-THREAD-RWLOCK-0001:** Reader/writer locks define reader concurrency, exclusive writer ownership, upgrade/downgrade support, preference/fairness, recursion, and starvation behavior. Upgrade is unsupported unless atomicity is proven.

**RM-THREAD-RWLOCK-0002:** Guards are nontransferable unless the exact contract permits transfer, and safe APIs prevent protected data from escaping the guard lifetime.

**RM-THREAD-MUTEX-0005:** Cross-process synchronization is a separate capability with robust-owner, shared-memory-layout, namespace, and crash-recovery evidence.

