# Diagnostic bundles

A diagnostic-bundle service gathers an explicitly selected, reviewable set of artifacts for support or incident analysis.

**RM-DIAGNOSTICS-BUNDLE-0001:** A bundle manifest records schema version, collection reason, consent/policy basis, product/build identity, collection times, included artifact identities, omissions, truncation, redaction policy version, and integrity hashes.

**RM-DIAGNOSTICS-BUNDLE-0002:** Collection uses least authority and an allowlist. It cannot recursively harvest arbitrary user directories, environment blocks, clipboard content, secrets, raw credentials, or unrelated process data.

**RM-DIAGNOSTICS-BUNDLE-0003:** Each artifact has a sensitivity classification, size/time budget, producer provenance, retention recommendation, and separate preview/consent presentation where user interaction is required.

**RM-DIAGNOSTICS-BUNDLE-0004:** Redaction is schema aware and occurs before export. When safe redaction cannot be established, the artifact is omitted or retained only in a more restricted local tier.

**RM-DIAGNOSTICS-BUNDLE-0005:** Bundle creation is cancellable, bounded, and atomic at publication. Partial collection remains temporary and is deleted according to explicit cleanup evidence.

**RM-DIAGNOSTICS-BUNDLE-0006:** Integrity proves artifact bytes have not changed since packaging; it does not establish truth, authorship, or authorization unless a separate signing/attestation contract applies.

