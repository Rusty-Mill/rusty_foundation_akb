# Cross-cutting qualities

**RM-SECRETS-XCUT-0001:** Security uses least broker/target authority, explicit purpose/audience, protected channels, workload attestation, conditional mutation, short leases, non-reveal operations, controlled delivery, target-side revocation, dual control, and fail-closed stale/unknown handling.

**RM-SECRETS-XCUT-0002:** Privacy treats secret names, paths, owners, targets, access timing, lease metadata, operator sessions, and leak findings as sensitive; it minimizes correlation, disclosure, cloud scanning, session recording, retention, and cross-tenant visibility.

**RM-SECRETS-XCUT-0003:** Accessibility and internationalization apply to unlock, consent, checkout, approval, break-glass, rotation failure, recovery, and leak response without displaying secrets, depending on color, imposing transcription-only tasks, or localizing stable identifiers.

**RM-SECRETS-XCUT-0004:** Observability records descriptor/generation/operation/provider/target/dependent correlation, lifecycle milestones, lease horizon, adoption/revocation residuals, and sanitized reasons while prohibiting plaintext, secret-derived hashes, tokens, credential payloads, and unsafe target responses.

**RM-SECRETS-XCUT-0005:** Async-first APIs support cancellation/deadlines/streamed generation updates/backpressure and expose ambiguous external effects; sync completeness covers bounded local broker/provider operations without hidden runtimes or indefinite human/network waits.

**RM-SECRETS-XCUT-0006:** Native performance preserves opaque provider operations, hardware keys, connection/session pooling, local agents, streaming updates, conditional reads, bounded caches, and batched rotation while never weakening isolation, generation checks, or cleanup evidence.
