# Caching, freshness, and invalidation

**RM-CONTENT-CACHE-0001:** Cache keys include exact subject generation/digest, operation/purpose, detector/inspector/transformer/provider generations, rule/signature/model/reputation databases, policy, platform/architecture, limits, disclosure mode, and relevant origin/quarantine state.

**RM-CONTENT-CACHE-0002:** Structural findings may be immutable for exact bytes while malware, reputation, trust, policy, registry, parser-vulnerability, and quarantine decisions expire or revoke independently.

**RM-CONTENT-CACHE-0003:** Negative, unknown, unsupported, timeout, crash, resource-exhausted, password-required, partial, and no-finding results have distinct bounded freshness and retry policies; transient failure cannot become durable allow evidence.

**RM-CONTENT-CACHE-0004:** Provider/database/policy updates, new vulnerability intelligence, trust/reputation revocation, subject replacement, quarantine mutation, and privacy/tenant changes invalidate all affected derived decisions and representations.

**RM-CONTENT-CACHE-0005:** Cached previews, extracted text, signatures, metadata, and findings may expose sensitive content. Storage is encrypted where required, least-privilege, partitioned, size/retention bounded, securely removed, and excluded from broad indexing/backups unless selected.

**RM-CONTENT-CACHE-0006:** Request collapse shares work only across equivalent authorities, privacy partitions, disclosure consent, policies, and cancellation semantics. One caller cannot broaden provider submission or retain another caller’s content.
