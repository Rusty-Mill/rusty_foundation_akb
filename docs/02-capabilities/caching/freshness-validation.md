# Freshness and validation

**RM-CACHE-FRESH-0001:** Reuse policy separately evaluates current age, freshness lifetime, validator strength, request directives, origin policy, disconnected state, acceptable-staleness budget, privacy, and invalidation epoch.

**RM-CACHE-FRESH-0002:** Wall-clock-derived freshness handles skew, backward/forward jumps, overflow, suspend, and uncertain time; elapsed local age uses monotonic time where meaningful.

**RM-CACHE-FRESH-0003:** Validation is conditional against an exact origin identity/generation. An unchanged response refreshes only metadata authorized by the validation contract.

**RM-CACHE-FRESH-0004:** Weak validators, timestamps, provider ETags, content digests, database revisions, and application versions remain distinct evidence and are never substituted silently.

**RM-CACHE-FRESH-0005:** Stale-while-revalidate, stale-if-error, disconnected reuse, and offline caches require explicit maximum staleness, eligible error classes, background work authority, user disclosure where material, and recovery behavior.

**RM-CACHE-FRESH-0006:** Partial/range entries combine only when representation identity and strong validation prove a coherent whole; otherwise the operation refetches or fails explicitly.

**RM-CACHE-FRESH-0007:** Authorization or policy changes can revoke reuse independently of data freshness.
