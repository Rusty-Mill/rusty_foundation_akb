# Mutation, invalidation, and coherence

**RM-CACHE-INVALIDATE-0001:** Mutation policy selects versioned immutable names, write-through update, delete, tag/dependency purge, namespace epoch, targeted revalidation, or bounded expiry; these mechanisms are not equivalent.

**RM-CACHE-INVALIDATE-0002:** Invalidation binds issuer authority, exact scope/key/tag/dependency, generation or epoch, reason, deadline, provider topology, and audit identity.

**RM-CACHE-INVALIDATE-0003:** Outcomes distinguish accepted, scheduled, locally applied, provider-reported complete, sampled/observed propagation, partial, rejected, expired, and reconciled.

**RM-CACHE-INVALIDATE-0004:** A purge does not retract copies already served, browser or third-party caches outside its scope, offline clients, backups, logs, or derived artifacts.

**RM-CACHE-INVALIDATE-0005:** Dependency invalidation uses versioned bounded graphs with cycle, fanout, cardinality, missing-edge, and partial-failure handling.

**RM-CACHE-INVALIDATE-0006:** Namespace epochs reject old entries without requiring synchronous physical deletion; reclamation is separate bounded work.

**RM-CACHE-INVALIDATE-0007:** Coherence claims name writers, readers, tiers, operations, ordering, maximum staleness, partitions, failure assumptions, and tested histories.

**RM-CACHE-INVALIDATE-0008:** Security or legal emergency removal favors origin denial, authorization revocation, short freshness, immutable replacement, and scoped purge together; purge alone is not a guaranteed recall mechanism.
