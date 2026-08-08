# Condition, semaphore, event, and wait primitives

**RM-THREAD-COND-0001:** Condition wait atomically releases the associated lock and begins waiting under provider semantics, then reacquires before return. Consumers loop on a protected predicate because wakeups may be spurious or obsolete.

**RM-THREAD-COND-0002:** Notify-one does not promise which waiter wakes; notify-all does not promise simultaneous progress. Predicate state, not notification count, determines correctness.

**RM-THREAD-SEMAPHORE-0001:** A counting semaphore declares maximum count, initial count, overflow behavior, process scope, fairness, and whether release/acquire establishes synchronization.

**RM-THREAD-EVENT-0001:** One-shot, auto-reset, and manual-reset events are different contracts. Signal state, consumed wake, reset races, and waiter arrival ordering are explicit.

**RM-THREAD-WAIT-0001:** Wait-one, wait-any, and wait-all distinguish readiness observation from resource acquisition. Native multiwait limitations, handle count, message/APC dispatch, and false-ready races are disclosed.

**RM-THREAD-WAIT-0002:** Deadlines use the selected monotonic clock. Cancellation, timeout, signal, object destruction, abandoned owner, and provider failure are distinct terminal outcomes.

**RM-THREAD-WAIT-0003:** Blocking a UI/COM/apartment or runtime worker thread may require message/reentrancy integration; generic waits never silently pump messages or execute callbacks.

