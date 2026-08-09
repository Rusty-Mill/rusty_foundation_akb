# Mobile and web push binding

**RM-COMMS-PUSH-0001:** A push subscription/token binds application/bundle/origin, environment, device/app-installation generation, provider/project/topic, endpoint, cryptographic material where applicable, authorization state, locale, capabilities, and last validation.

**RM-COMMS-PUSH-0002:** Tokens/endpoints are opaque secrets or sensitive identifiers, rotate without notice, and are not user identity. Registration, refresh, sign-out, reinstall, restore, account switch, provider invalidation, and deletion reconcile mappings.

**RM-COMMS-PUSH-0003:** Payload bindings state notification versus data intent, size, priority, TTL/expiry, collapse/replacement key, topic/channel, mutable-content/background behavior, encryption, actions, and provider-specific transformations.

**RM-COMMS-PUSH-0004:** Provider acceptance, persistent storage, device transport, OS receipt, app callback, native presentation, user interaction, and application synchronization/effect are separate milestones.

**RM-COMMS-PUSH-0005:** Collapse and expiry intentionally permit loss and replacement. Ordering, retention, background execution, promptness, and notification presentation are not assumed; authoritative data is fetched and reconciled through application APIs where needed.

**RM-COMMS-PUSH-0006:** Web Push uses endpoint authorization, VAPID/application-server identity where selected, and payload encryption profiles without claiming that push-service-visible metadata, timing, or length is confidential.

**RM-COMMS-PUSH-0007:** Permission denial/revocation, focus/quiet hours, power/data-saving, force-stop, background restrictions, offline devices, provider throttling, and uninstall are distinct observable or unknown outcomes.
