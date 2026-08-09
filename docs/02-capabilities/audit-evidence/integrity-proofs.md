# Integrity, signatures, timestamps, and transparency

**RM-AUDIT-INTEGRITY-0001:** Integrity profiles declare canonical bytes, digest/signature/MAC algorithms and parameters, signer/key/certificate generation, trust policy, sequence/chain/Merkle structure, anchor, verification interval, and expiry/rotation.

**RM-AUDIT-INTEGRITY-0002:** Hashes prove byte equality only; MACs add shared-key origin claims; signatures add holder-of-key origin evidence; trusted timestamps add bounded external time claims; WORM/retention locks add provider-enforced mutation constraints. None are interchangeable.

**RM-AUDIT-INTEGRITY-0003:** Chaining declares genesis/restart, fork, missing segment, backfill, reordering, key rotation, algorithm migration, checkpoint/anchor, and partial-range verification behavior.

**RM-AUDIT-INTEGRITY-0004:** Verification produces an immutable report of exact artifacts/ranges, canonicalization, key/trust/time inputs, valid/invalid/missing/unknown results, forks/gaps, tool generation, and nonclaims.

**RM-AUDIT-INTEGRITY-0005:** Keys are isolated from event producers/storage administrators where threat policy requires. Key compromise, loss, expiry, revocation, unauthorized signing, and signer rollback have explicit incident/recovery semantics.

**RM-AUDIT-INTEGRITY-0006:** External anchoring/transparency discloses public metadata, batching delay, inclusion/consistency proofs, monitor assumptions, privacy leakage, and availability. Publication is not validation of event truth.

**RM-AUDIT-INTEGRITY-0007:** Enabling an integrity feature is not verification; conformance and operations regularly validate representative and complete required ranges against independent trust material.
