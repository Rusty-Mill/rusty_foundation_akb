# Runtime and executor integration

The I/O engine owns native registration, submission, polling/dequeue, cancellation forwarding, and terminalization. The executor owns task queues, scheduling policy, worker lifecycle, and consumer polling. A narrow wake interface connects them.

**RM-ASYNC-RUNTIME-0001:** An I/O engine MUST NOT require one global executor or create a hidden runtime. Engine construction receives explicit clock, cancellation, wake, limits, and shutdown dependencies.

**RM-ASYNC-RUNTIME-0002:** Completion delivery MUST tolerate a consumer being concurrently polled, cancelled, dropped, migrated when allowed, or already completed; wakes are hints and MAY be coalesced.

**RM-ASYNC-RUNTIME-0003:** Provider callbacks/pollers MUST perform bounded bookkeeping and wake publication, not arbitrary consumer code.

**RM-ASYNC-RUNTIME-0004:** Engine shutdown MUST stop admission, request/coordinate cancellation, continue draining terminal completions, reject late generation mismatches, and report bounded/unbounded survivors.

**RM-ASYNC-RUNTIME-0005:** Synchronous domain operations use genuine platform synchronous behavior or a disclosed blocking service. They MUST NOT nest an event loop, block an executor worker indefinitely, or depend on polling an unrelated async future.

**RM-ASYNC-RUNTIME-0006:** UI/run-loop, apartment, signal-mask, thread-affinity, and fork constraints MUST be declared per provider. Generic waits MUST NOT silently pump callbacks.

An engine may support dedicated poll threads, caller-driven polling, or safe run-loop integration as selectable qualities. None changes operation semantics.
