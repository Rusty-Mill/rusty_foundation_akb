# Privacy, security, and governance

**RM-OBSERVE-PRIVACY-0001:** Every field and artifact is classified at definition as public, operational, pseudonymous, personal, secret, or prohibited. Unknown classification defaults to prohibited export.

**RM-OBSERVE-PRIVACY-0002:** Redaction, hashing, tokenization, sampling, retention, and access control are distinct controls. Hashing low-entropy or identifying data does not automatically anonymize it.

**RM-OBSERVE-PRIVACY-0003:** Collection and export authority are separate. Local operational telemetry does not imply network transmission, cross-account correlation, or third-party processing permission.

**RM-OBSERVE-PRIVACY-0004:** Telemetry cannot contain secret values, authentication material, private keys, raw protected configuration, secure-text content, or unrestricted memory unless a narrowly scoped crash-artifact policy explicitly authorizes the latter.

**RM-OBSERVE-PRIVACY-0005:** Diagnostic endpoints, dynamic tracing controls, bundle generation, dump access, and exporter configuration require explicit authority and are auditable without disclosing captured content.

**RM-OBSERVE-PRIVACY-0006:** Retention and deletion policy applies independently to buffers, spools, native stores, bundles, crash artifacts, derived symbols, and remote copies. Failed upload does not authorize indefinite retention.

**RM-OBSERVE-PRIVACY-0007:** Event volume, attribute cardinality, recursive instrumentation, and attacker-controlled error paths are resource-exhaustion surfaces with enforced budgets.

## Governance gate

New event schemas require owner, purpose, operational consumer, sensitivity review, cardinality/volume budget, compatibility policy, retention class, and conformance evidence. “Useful someday” is not sufficient justification for collection.

