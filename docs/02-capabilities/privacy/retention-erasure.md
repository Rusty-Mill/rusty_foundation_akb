# Retention, restriction, holds, and erasure

**RM-PRIVACY-RETENTION-0001:** Retention rules bind data/subject/purpose/record class, start event, duration or review schedule, authoritative clock, extensions, holds/exceptions, action at expiry, destruction method, recipients/processors, backup/archive behavior, and policy generation.

**RM-PRIVACY-RETENTION-0002:** Retention starts from a named event such as collection, last interaction, contract/account closure, case completion, consent withdrawal, model generation, publication, supersession, or hold release; “N days” without its event is incomplete.

**RM-PRIVACY-RESTRICT-0001:** Restriction is a versioned state that blocks selected access/use/disclosure/automation while preserving required storage, integrity, audit, correction, review, and eventual release/erase authority. It is not merely a UI flag.

**RM-PRIVACY-HOLD-0001:** Holds bind issuer/authority, scope/query and matched inventory snapshot, purpose/legal-policy reference, start/expiry/review, allowed processing, custodians, conflicts, notifications, release, and immutable audit. Portable code does not decide whether a hold is legally valid.

**RM-PRIVACY-ERASE-0001:** An erasure plan enumerates authoritative live records, object versions, replicas, indexes/search, caches/CDNs, queues/events, exports/shares/recipients, derived data, logs/audit, backups/archives, models/features, keys/tokens, tombstones, holds, and unknown frontiers.

**RM-PRIVACY-ERASE-0002:** Logical deletion, access revocation, cryptographic erasure, overwrite, physical reclamation, backup expiry, recipient notification/deletion, model retraining/unlearning, aggregate retention, and proof destruction are distinct methods and milestones.

**RM-PRIVACY-ERASE-0003:** Erasure results report per-system generation and outcome, excluded/held/required retained data, anonymized/aggregated derivatives, recipient status, backup restoration guards, propagation objective, failures/retries, unverifiable residuals, and completion boundary.

**RM-PRIVACY-ERASE-0004:** Tombstones retain only the minimum identity/fencing/policy evidence needed to prevent resurrection and replay. They are classified, purpose-limited, bounded, and themselves subject to review.
