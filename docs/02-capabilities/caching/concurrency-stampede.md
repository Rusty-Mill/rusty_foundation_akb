# Concurrency and stampede control

**RM-CACHE-CONCURRENCY-0001:** Per-key request collapse shares only a compatible origin operation whose key, partition, authority class, representation, deadline policy, and result visibility are safe for every waiter.

**RM-CACHE-CONCURRENCY-0002:** One waiter's cancellation or deadline does not cancel shared work still authorized and needed by others; the final waiter may cancel according to explicit background-fill policy.

**RM-CACHE-CONCURRENCY-0003:** Collapse never transfers credentials, tracing baggage, locale, privacy choices, response mutation, or error disclosure across callers.

**RM-CACHE-CONCURRENCY-0004:** Stampede control bounds concurrent fills globally, per origin, tenant, key, and tier using queue limits, jitter, admission, early refresh, and overload behavior.

**RM-CACHE-CONCURRENCY-0005:** Failed and slow fills have bounded negative/backoff policy that cannot create permanent poison entries or hide origin recovery.

**RM-CACHE-CONCURRENCY-0006:** Conditional publish prevents an older fill, refresh, or retry from overwriting a newer entry or invalidation epoch.

**RM-CACHE-CONCURRENCY-0007:** Hot-key replication and local shielding preserve privacy and invalidation scope while exposing increased staleness and memory cost.
