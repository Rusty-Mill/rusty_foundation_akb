# Cancellation and operation lifetime

Cancellation requests a provider to stop an operation if possible. It is neither rollback nor proof that the native subsystem has stopped touching operation memory.

**RM-ASYNC-CANCEL-0001:** Cancellation MUST race with ordinary completion and yield one terminal result: completed normally, failed, or cancelled, with exact progress.

**RM-ASYNC-CANCEL-0002:** Buffer memory, native control structures, registrations, and resource-generation references MUST remain alive and unmodified until terminal completion is observed.

**RM-ASYNC-CANCEL-0003:** A timeout is policy that requests cancellation at a monotonic deadline. Timeout-requested, cancellation-acknowledged, and terminal outcome MUST remain distinguishable.

**RM-ASYNC-CANCEL-0004:** Closing a resource MUST define whether operations are drained, cancelled, detached under supervision, or invalidated; close MUST NOT imply synchronous cancellation acknowledgement.

**RM-ASYNC-CANCEL-0005:** Cancellation safety MUST state whether progress mutates buffers, stream position, message queues, filesystem state, or remote-visible state before the terminal outcome.

**RM-ASYNC-CANCEL-0006:** Operation state MUST prevent ABA reuse: a late completion for an older generation cannot complete or corrupt a newer operation occupying reused storage.

See [ADR-0053](../../adr/0053-cancellation-does-not-end-operation-lifetime.md).
