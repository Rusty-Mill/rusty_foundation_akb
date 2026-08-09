# Cross-cutting qualities

**RM-APP-AUTH-XCUT-0001:** Security defaults prohibit implicit method downgrade, password grant, wildcard redirect, bearer artifacts in URLs, reusable challenge acceptance, unsigned or algorithm-confused assertions, ambient token access, cross-tenant session reuse, and recovery based solely on a compromised channel.

**RM-APP-AUTH-XCUT-0002:** Privacy minimizes identifiers, claims, attestation, device signals, account discovery, federation correlation, authentication telemetry, and recovery disclosure; pairwise identifiers and selective claims are supported where provider semantics allow.

**RM-APP-AUTH-XCUT-0003:** Accessibility supplies adequate time, multiple usable verification options where policy permits, screen-reader and keyboard support, non-biometric alternatives, clear device/transaction context, safe cancellation, recovery, localization, and no reliance on color, memory, or rapid transcription alone.

**RM-APP-AUTH-XCUT-0004:** Internationalization treats identifiers and names under provider-declared comparison rules, supports localized prompts/errors/notifications without signing ambiguous localized strings, and protects bidirectional and confusable transaction presentation.

**RM-APP-AUTH-XCUT-0005:** Observability separates plan/challenge/interaction/verification/policy/session/resource milestones, records generations and latency without secrets or reusable artifacts, applies anti-enumeration to external errors, and exposes revocation/recovery propagation and residuals.

**RM-APP-AUTH-XCUT-0006:** Async-first APIs support cancellation, deadlines, external-browser/device handoff, resumable correlation, and bounded queues; sync completeness covers locally bounded provider calls but does not create runtimes or block indefinitely on human interaction.

**RM-APP-AUTH-XCUT-0007:** Native performance preserves platform brokers, secure hardware, zero-copy token parsing where safe, connection reuse, and cached verified metadata while generation/freshness keys prevent security-relevant stale reuse.
