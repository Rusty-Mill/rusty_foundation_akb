# Selective synchronization and queries

**RM-APP-SYNC-SELECT-0001:** A selection is an immutable, versioned predicate/projection over dataset/schema/security context with stable identity, parameters, completeness semantics, limits, and dependency closure.

**RM-APP-SYNC-SELECT-0002:** Selection changes distinguish expansion, contraction, reclassification, tenant/account movement, and policy revocation. Contraction removes or quarantines out-of-scope local state under explicit retention and pending-change rules.

**RM-APP-SYNC-SELECT-0003:** Referential, authorization, merge, tombstone, and schema dependencies cross selection boundaries only through defined stubs, redacted projections, on-demand fetch, or rejection; absence does not imply deletion.

**RM-APP-SYNC-SELECT-0004:** Pagination and incremental queries bind a stable snapshot/frontier or disclose drift, duplicates, omissions, and restart rules. Tokens are opaque scoped progress evidence.

**RM-APP-SYNC-SELECT-0005:** Server-side filtering is enforced at the authoritative boundary and rechecked as policy changes. Client filtering is presentation behavior, never a confidentiality control.

**RM-APP-SYNC-SELECT-0006:** Priority, prefetch, metered-network, battery, storage-pressure, and user-control policy may schedule transfer but cannot reorder semantic dependencies or starve deletion/revocation indefinitely.
