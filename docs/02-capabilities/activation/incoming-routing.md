# Incoming activation and instance routing

Incoming native events adapt to [`rm.lifecycle.activation`](../lifecycle/activation.md) and retain activation-specific handler and reference evidence.

**RM-ACTIVATION-IN-0001:** An incoming request MUST carry activation identity/generation, kind/verb, target references and claimed types, native provenance, association/handler role evidence, source/origin disclosure quality, user-interaction/foreground token, delivery time, instance-routing evidence, and unknown fields.

**RM-ACTIVATION-IN-0002:** Every request is untrusted and at-least-once. The application validates schema, freshness, target generation, content/scheme policy, authority, replay/idempotency, current state, and domain preconditions before acting.

**RM-ACTIVATION-IN-0003:** Initial process launch, activation delivery, instance selection, redirection to an existing instance, readiness, window routing, focus/foreground, content open, and domain completion are distinct milestones.

**RM-ACTIVATION-IN-0004:** Single-/multi-instance policy is a platform service. Routing keys are explicit product scope and MUST NOT be derived solely from process name, target path, URI host, or untrusted payload.

**RM-ACTIVATION-IN-0005:** Concurrent and duplicate requests have bounded ordered queues and deduplication keyed to native/request identity plus product policy. Deduplication cannot merge distinct user actions or extend stale authority.

**RM-ACTIVATION-IN-0006:** Activation arriving before initialization is retained under bounded startup policy; readiness distinguishes runtime/provider initialization, activation intake, UI availability, target validation, and app-defined handled/failed acknowledgment where supported.

**RM-ACTIVATION-IN-0007:** Reopen, ordinary launch, document/URI, notification action, share, restoration, and platform extension remain distinguishable even when routed to the same window or domain command.
