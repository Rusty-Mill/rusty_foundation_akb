# Trust stores, anchors, and distrust

A `TrustSnapshot` is immutable and identifies provider/version, scope, generation/digest, observation time, ordered policy sources, anchors, explicit distrust/blocklist entries, purpose/name/policy constraints, user/admin/enterprise/application overrides, and unavailable/hidden evidence.

**RM-PKI-TRUST-0001:** Trust anchors, trusted leafs, intermediate caches, ordinary certificate stores, identities/private keys, distrust entries, purpose constraints, and user exceptions MUST remain distinct.

**RM-PKI-TRUST-0002:** System, enterprise, administrator, user, application-private, pinned, and supplied trust sources MUST retain provenance and precedence. Merging is policy resolution, not certificate concatenation.

**RM-PKI-TRUST-0003:** An anchor is trust-policy input and need not be a self-signed certificate. Self-signature validity does not make a certificate trusted, and a trusted anchor's self-signature need not be part of path validation.

**RM-PKI-TRUST-0004:** Explicit distrust and constraints MUST override a lower-priority allow according to resolved policy. Extracting only anchor certificates MUST NOT claim to preserve blocklists or rich trust metadata.

**RM-PKI-TRUST-0005:** Enumeration/observation MUST be side-effect-free, privacy-minimized, bounded, and generation-aware. It MUST NOT prompt, import, fetch, unlock private keys, or infer trust from store membership.

**RM-PKI-TRUST-0006:** Trust-store mutation is a separately authorized transactional administration service with exact scope, expected generation, source ownership, policy validation, audit, commit/rollback, and accessible user/admin disclosure.

**RM-PKI-TRUST-0007:** Store/provider updates, enterprise policy, user changes, distrust distribution, application pinset changes, and clock/policy revisions invalidate cached results by generation rather than relying solely on certificate expiry.
