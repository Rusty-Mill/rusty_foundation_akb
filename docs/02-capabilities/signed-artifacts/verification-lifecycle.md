# Verification policy and lifecycle

**RM-SIGNED-VERIFY-0001:** Artifact acceptance policy is immutable and versioned. It binds artifact kind/purpose/target/channel, allowed signed-view and envelope profiles, signer roles/thresholds, trust roots/pins, algorithms, timestamp/transparency/provenance/SBOM/reproducibility requirements, freshness, network mode, and resource bounds.

**RM-SIGNED-VERIFY-0002:** Verification evaluates independently: structural validity, exact digest coverage, signature cryptography, signer key/certificate trust and purpose, timestamp, transparency, provenance, platform notarization/reputation, version/downgrade rules, and product authorization.

**RM-SIGNED-VERIFY-0003:** The result records every input digest, evidence item, policy/trust/algorithm/log generation, provider/version, time/clock and network/cache mode, successful and failed checks, warnings, unknowns, expiry, and nonclaims.

**RM-SIGNED-VERIFY-0004:** `valid`, `invalid`, `indeterminate`, `unsupported`, `policy-rejected`, and `resource-limit` remain distinct. A convenience boolean cannot erase the evidence-bearing result.

**RM-SIGNED-VERIFY-0005:** Installation, execution, publication, loading, or document trust requires separate action authority and a fresh result whose subject exactly matches the bytes acted upon. Time-of-check/time-of-use substitution is prevented.

**RM-SIGNED-VERIFY-0006:** Cache keys include all material evidence and policy generations. Trust-store, distrust, algorithm policy, log key/checkpoint, artifact bytes, clock-quality, status, or product-policy changes invalidate affected cached conclusions.

**RM-SIGNED-LIFECYCLE-0001:** Signer/key/certificate/log/timestamp-authority rotation permits explicit overlap and quorum transitions. New artifacts cannot silently use retired generations.

**RM-SIGNED-LIFECYCLE-0002:** Compromise and revocation policy distinguishes signatures made before evidenced compromise, after compromise, at unknown time, and under emergency distrust. Trusted timestamps inform but do not dictate acceptance.

**RM-SIGNED-LIFECYCLE-0003:** Emergency policy updates are authenticated, generation-monotonic, rollback-protected, auditable, locally recoverable, and testable offline. Failure to refresh yields a declared fail-open, fail-closed, or degraded result by artifact risk class.

