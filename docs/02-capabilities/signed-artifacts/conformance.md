# Signed-artifact conformance

Every report identifies artifact/envelope/signed-view profiles, policy/trust/algorithm generations, providers, OS/architecture, network/cache/time mode, fixtures, and result-evidence digest.

**RM-SIGNED-CONFORMANCE-0001:** The corpus covers valid native and portable signatures; embedded/detached/multiple/countersignatures; exact covered/excluded bytes; malformed, truncated, overlapping, duplicate, trailing, recursive, compressed, Unicode/case/path, symlink, archive, and polyglot attacks.

**RM-SIGNED-CONFORMANCE-0002:** Tests mutate every covered and permitted/excluded region and prove the declared effect. Verifiers reject ambiguity between authenticated bytes and executable, installed, rendered, or interpreted content.

**RM-SIGNED-CONFORMANCE-0003:** Signer tests cover wrong purpose/role, untrusted/expired/not-yet-valid/revoked/rotated credentials, ambiguous chains, weak algorithms, hardware/remote-provider outage, unauthorized requests, approval substitution, batch confusion, retries, cancellation, and ambiguous completion.

**RM-SIGNED-CONFORMANCE-0004:** Timestamp tests cover imprint mismatch, local versus trusted time, wrong TSA purpose/root/policy, nonce behavior, weak/expired/revoked evidence, before/after/unknown compromise, clock uncertainty, renewal, offline verification, and network failure.

**RM-SIGNED-CONFORMANCE-0005:** Transparency tests cover missing/wrong inclusion proofs, log-key rotation, stale/invalid checkpoints, consistency/witness policy, split-view simulations, duplicate submission, privacy policy, unavailable logs, and self-contained bundles.

**RM-SIGNED-CONFORMANCE-0006:** Provenance tests cover subject/material mismatch, false/missing/unknown claims, builder/workflow changes, mutable references, hostile SBOM fields, redaction, reproducible match/mismatch, and independent signer/build trust.

**RM-SIGNED-CONFORMANCE-0007:** Policy tests exercise signer thresholds/roles, channel/target/version/downgrade, platform assessment, freshness, offline modes, cache invalidation, emergency distrust, overrides, TOCTOU substitution, and every typed result/nonclaim.

**RM-SIGNED-CONFORMANCE-0008:** Cross-platform fixtures preserve native semantics and document intentional differences; no adapter may pass by discarding unsupported security-relevant evidence.

