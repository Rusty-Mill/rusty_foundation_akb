# Thread lifecycle

## Capability identity

`rm.thread.spawn` creates an owned native thread under explicit requirements.

**RM-THREAD-SPAWN-0001:** Inputs specify entry ownership, name, stack policy, scheduling/affinity requests, initialization context, shutdown participation, and platform apartment/event-loop constraints. Effective qualities are reported.

**RM-THREAD-SPAWN-0002:** Creation returns an owned join capability or fails without an unowned running thread. Detached behavior is separate explicit policy.

**RM-THREAD-SPAWN-0003:** Entry completion records returned value/status, panic containment result, provider failure, and cleanup outcome. Unwinding never crosses an unsupported native/FFI boundary.

**RM-THREAD-SPAWN-0004:** Join establishes completion synchronization and is idempotently observable, but joining self fails explicitly. Join deadlines do not terminate the thread.

**RM-THREAD-SPAWN-0005:** Cancellation is cooperative through the runtime cancellation contract. Forced suspension/termination and arbitrary signal injection are prohibited from safe portable APIs.

**RM-THREAD-SPAWN-0006:** Stack size is a provider-rounded reservation/commit/guard quality, not guaranteed resident memory. Stack exhaustion remains fatal or provider-specific unless separately contained.

**RM-THREAD-SPAWN-0007:** Thread identifiers include an execution epoch and may be reused after exit. Display names are diagnostic, not identity or authority.

