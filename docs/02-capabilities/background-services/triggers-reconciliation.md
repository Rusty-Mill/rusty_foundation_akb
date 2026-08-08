# Triggers and state reconciliation

**RM-BACKGROUND-TRIGGER-0001:** Time, boot/login/session, device, network, power, filesystem, IPC/socket, notification/push, and provider-specific triggers MUST identify source, scope, subscription generation, predicate, payload reliability, coalescing/loss behavior, and authority.

**RM-BACKGROUND-TRIGGER-0002:** Trigger occurrence is at-least-once invalidation evidence unless a stronger provider contract is proven. It MUST NOT be treated as an exactly-once durable event journal or as authority to act.

**RM-BACKGROUND-TRIGGER-0003:** An attempt MUST re-observe authoritative domain state and revalidate definition, principal, policy, resources, freshness, and work eligibility before claiming work.

**RM-BACKGROUND-TRIGGER-0004:** Trigger payloads are bounded untrusted hints. Identifiers, paths, device data, network state, account data, and event metadata require current generation and ordinary boundary validation.

**RM-BACKGROUND-TRIGGER-0005:** Registration races, duplicate/coalesced/out-of-order delivery, overflow, broker restart, suspend/resume, and definition replacement MUST converge through snapshot-plus-generation reconciliation.

**RM-BACKGROUND-TRIGGER-0006:** Wake and background-start side effects require explicit authority and provider support. Observation or schedule possession does not authorize waking a device or bypassing user energy policy.

**RM-BACKGROUND-TRIGGER-0007:** Trigger removal or definition disablement MUST close new admission before draining or invalidating already admitted attempts according to declared policy.
