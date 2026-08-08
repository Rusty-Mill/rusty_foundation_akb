# Revocation, status, and freshness

**RM-PKI-STATUS-0001:** Revoked, good-for-a-named-source/window, unknown, stale, unavailable, malformed, unauthorized responder, policy-disabled, not-applicable, and not-checked MUST remain distinct per certificate.

**RM-PKI-STATUS-0002:** CRL, delta CRL, OCSP, stapled status, provider blocklist, short-lived-certificate policy, transparency/monitor evidence, and proprietary status services are independent evidence sources with provenance and precedence.

**RM-PKI-STATUS-0003:** Every status item MUST bind issuer/responder authority, target certificate identity, production/this/next-update times, signature algorithm/policy, retrieval/cache provenance, validation time, freshness window, and replay/rollback protection.

**RM-PKI-STATUS-0004:** Hard-fail, soft-fail, require-stapled, offline-cache-only, best-effort, or disabled behavior MUST be explicit by purpose, certificate role, network context, and error class. `unknown` MUST NOT be reported as `good`.

**RM-PKI-STATUS-0005:** Status checking MUST bound response/request bytes, object count, recursion, redirects, hosts, elapsed time, concurrency, cache, and signature work. Untrusted distribution and responder locators grant no general network authority.

**RM-PKI-STATUS-0006:** Revocation checking does not prove non-compromise, present private-key control, issuance legitimacy, or status beyond the evidence source and freshness window.

**RM-PKI-STATUS-0007:** Status evidence expiring, trust/policy/store change, clock uncertainty, responder compromise/revocation, or cache rollback invalidates affected cached validation results by dependency and generation.
