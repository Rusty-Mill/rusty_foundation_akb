# Results, overrides, and lifecycle

A `TrustResult` is immutable evidence containing input digests, selected candidate/path and anchor, policy/purpose/reference identity, time/clock, trust snapshot, algorithm policy, per-certificate checks, status sources/freshness, network/cache behavior, pins/overrides, provider/version, terminal category, warnings, unknowns, and expiration/dependency set.

**RM-PKI-RESULT-0001:** Trusted, untrusted, policy-rejected, identity-mismatch, expired/not-yet-valid, revoked, status-unknown/unavailable/stale, malformed, unsupported, resource-limited, canceled, and provider-failed MUST remain distinct terminal categories.

**RM-PKI-RESULT-0002:** A result MUST expose every material policy input and evidence generation needed to reproduce or explain it; a boolean is only a convenience projection and cannot erase warnings, unknowns, override, or freshness.

**RM-PKI-RESULT-0003:** User/admin exceptions and application pins MUST be typed, scope/purpose/identity/leaf-or-key-bound, provenance-bearing, time-bounded, revocable, auditable, and inaccessible as raw bearer authority. Overrides MUST NOT suppress unrelated failures silently.

**RM-PKI-RESULT-0004:** Trust results are cacheable only until the earliest certificate/status/pin/override/policy expiry and while trust, algorithm, provider, clock-quality, network-mode, and input generations remain compatible.

**RM-PKI-RESULT-0005:** Trust-store/policy/status/provider updates trigger dependency-aware invalidation or revalidation. Absence of a change notification is not proof that a result remains current.

**RM-PKI-RESULT-0006:** Diagnostics MUST be structured and privacy-minimized: certificate/input digests, generalized failure categories, and provider codes by policy; subjects, SANs, URLs, serials, enterprise anchors, and user exceptions are sensitive.

**RM-PKI-RESULT-0007:** Product authentication/authorization consumes the result with protocol proof-of-possession, transcript, account mapping, freshness, and domain policy. It MUST NOT authorize solely because `trusted=true`.
