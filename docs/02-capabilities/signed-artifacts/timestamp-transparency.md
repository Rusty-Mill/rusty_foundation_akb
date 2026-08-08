# Timestamping and transparency

**RM-SIGNED-TIME-0001:** A signer-claimed local time, file modification time, build time, repository commit time, transparency integrated time, and trusted timestamp are distinct typed evidence.

**RM-SIGNED-TIME-0002:** A trusted timestamp binds the exact signature or content imprint, timestamp authority identity and trust policy, algorithm, serial/policy identifier, nonce behavior, asserted time/accuracy/ordering, token bytes, and verification evidence.

**RM-SIGNED-TIME-0003:** Timestamp verification applies a dedicated trust purpose and historical validation policy. It reports whether the signature was evidenced before signer credential expiry or revocation; it does not invent signing authority or prove when content was created.

**RM-SIGNED-TIME-0004:** Missing, untrusted, malformed, mismatched, weak, expired, unavailable, or indeterminate timestamp evidence remains distinguishable. Local signing time cannot satisfy a trusted-time requirement.

**RM-SIGNED-TRANSPARENCY-0001:** Transparency evidence identifies log/operator, entry/body digest, inclusion proof, signed checkpoint/tree size, integrated time, log-key generation, consistency/witness evidence where required, and retrieval source.

**RM-SIGNED-TRANSPARENCY-0002:** Inclusion proves only that a value was incorporated under the verified log state. It does not prove signer authority, claim truth, artifact safety, global consistency, or confidentiality.

**RM-SIGNED-TRANSPARENCY-0003:** Online submission is an explicit privacy and availability boundary. Policy defines permitted claim disclosure, log set/quorum, witness requirements, retry/idempotency, split-view handling, and offline-bundle acceptance.

**RM-SIGNED-TRANSPARENCY-0004:** Verification can consume a self-contained bundle without silently contacting a network. Fresh online evidence and cached/offline evidence retain provenance and freshness.

## Renewal

Long-lived artifacts can acquire new timestamps, archive evidence, or transparency checkpoints without rewriting the original signed claims. Renewal signatures explicitly bind the prior evidence digest and policy; they do not retroactively repair an invalid original signature.

