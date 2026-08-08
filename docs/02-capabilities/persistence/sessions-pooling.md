# Connections, sessions, statements, and pooling

**RM-PERSISTENCE-SESSION-0001:** A connection/session binds database identity and generation, authenticated principal/tenant, endpoint/topology/provider, secure channel, default catalog/schema, locale/time zone, encoding, transaction defaults, statement/resource limits, and session-state policy.

**RM-PERSISTENCE-SESSION-0002:** Connection establishment, authentication, session initialization, topology discovery, transaction readiness, liveness, draining, closing, and invalidation are separate. A successful socket or login is not database readiness.

**RM-PERSISTENCE-SESSION-0003:** Session state—transactions, temporary objects, prepared statements, variables, role, search path, isolation, time zone, advisory locks, cursors, and notifications—is explicit and reset/verified before pool reuse. Failed reset destroys the session.

**RM-PERSISTENCE-POOL-0001:** Pool partition keys include database/generation, principal/tenant/role, credential generation, security/topology policy, session-state profile, read/write/consistency role, provider, and network privacy scope. Pooling cannot broaden identity or consistency.

**RM-PERSISTENCE-POOL-0002:** Pools bound open/idle/in-use/waiting connections, queue time/count, lifetime/idle/request count, validation, leak detection, fairness, burst, warmup, draining, credential rotation, topology change, and shutdown. Acquisition has its own deadline/cancellation evidence.

**RM-PERSISTENCE-STATEMENT-0001:** Prepared statements bind session or portable plan scope, exact query/dialect digest, parameter/result schema, schema/catalog generation, role/settings, provider plan identity, and invalidation policy. Cached plans are revalidated after material changes.

**RM-PERSISTENCE-SESSION-0004:** Cancellation requests provider interruption but may race execution/commit and can leave a transaction aborted, active, uncertain, or reusable only after protocol reconciliation. No connection returns to a pool until state is known and clean.

