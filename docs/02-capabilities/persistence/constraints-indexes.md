# Constraints, indexes, and concurrency

**RM-PERSISTENCE-CONSTRAINT-0001:** Constraints bind stable identity/generation, object/columns/expression, null/collation/type semantics, immediate/deferred/not-valid/validated state, conflict behavior, provider enforcement, and domain meaning. Application-only validation is not a database constraint.

**RM-PERSISTENCE-CONSTRAINT-0002:** Primary/unique, foreign/reference, check, exclusion, not-null, generated/default, row/tenant security, and domain constraints remain distinct. Deferrability, cascades, cycles, partial predicates, and validation scope are explicit.

**RM-PERSISTENCE-CONSTRAINT-0003:** Constraint violation returns exact constraint identity and safe typed conflict evidence without leaking unrelated records, secrets, internal query text, or provider topology. A uniqueness error can still be a serialization/retry race under the selected isolation.

**RM-PERSISTENCE-INDEX-0001:** Index definitions bind object/schema generation, key/include fields/expressions, ordering/collation/null semantics, uniqueness, predicate, method/provider options, partition, visibility/build state, maintenance and storage policy.

**RM-PERSISTENCE-INDEX-0002:** Planned/building/backfilling/validating/ready/degraded/invalid/dropping are separate. Concurrent/online build guarantees and write/read visibility are provider-specific; an index cannot be selected until its readiness evidence satisfies policy.

**RM-PERSISTENCE-CONCURRENCY-0001:** Optimistic version checks, compare-and-swap, row/range/predicate/advisory locks, MVCC snapshots, and provider conflict detection are different mechanisms with exact scope, lifetime, fairness, deadlock, fencing, and external-resource limits.

**RM-PERSISTENCE-CONCURRENCY-0002:** Lock wait/held/released/deadlock/timeout/cancel/session-loss and victim evidence are explicit. Transaction locks end at the provider boundary and do not fence external resources or stale restored/cloned database generations.

