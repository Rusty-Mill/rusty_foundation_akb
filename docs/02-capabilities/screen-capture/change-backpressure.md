# Change, delivery, and backpressure

**RM-SCREEN-CAPTURE-DELIVERY-0001:** Frame, cursor, audio, state, and error delivery MUST use bounded queues or pools with declared capacity, ownership, wake policy, and behavior at saturation.

**RM-SCREEN-CAPTURE-DELIVERY-0002:** Drop-oldest, drop-newest, coalesce, block-provider, copy, reduce-rate, reduce-resolution, or terminate policies MUST be explicit, measurable, and compatible with native callback constraints.

**RM-SCREEN-CAPTURE-DELIVERY-0003:** Native delivery callbacks MUST NOT execute arbitrary product, UI, encoder, network, storage, plugin, or exporter work and MUST have an enforced time and allocation budget.

**RM-SCREEN-CAPTURE-DELIVERY-0004:** Held buffers MUST be counted against a stated budget. Exhaustion MUST produce observable pressure and MUST NOT permit unbounded allocation or overwrite a live consumer lease.

**RM-SCREEN-CAPTURE-DELIVERY-0005:** Source resize, crop, mode, color, cursor, audio, or provider change MUST be transactional or generation-changing; frames from incompatible configurations cannot share an interpretation.

**RM-SCREEN-CAPTURE-DELIVERY-0006:** Lossy change notification MUST trigger coherent re-observation. Overflow, device loss, sleep/resume, session switch, and provider restart retire unverifiable generations.

**RM-SCREEN-CAPTURE-DELIVERY-0007:** Stop and teardown MUST bound new delivery, drain or invalidate queued items by policy, release native buffers and devices, and report residual ambiguity.

Slow consumers cannot force the compositor or UI to wait indefinitely. A sync convenience surface may wait on the same async state machine under an explicit deadline; it does not create different lifecycle or cancellation semantics.
