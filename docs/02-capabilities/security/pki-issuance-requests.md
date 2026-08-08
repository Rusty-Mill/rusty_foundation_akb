# Requests, proof-of-possession, and attestation

**RM-PKI-REQUEST-0001:** A certificate request is immutable bounded evidence containing request/profile format and version, subject/public key, signature/POP mechanism, requested attributes/extensions/identifiers, challenge/transaction bindings, signer/requester identity where defined, exact bytes, and parser diagnostics.

**RM-PKI-REQUEST-0002:** Request parsing rejects malformed, noncanonical where required, duplicate/conflicting, unknown critical, ambiguous string/name, oversized, recursive, weak-algorithm, invalid-key, and signature/POP-invalid inputs before policy evaluation.

**RM-PKI-REQUEST-0003:** Proof-of-possession proves control or authorized use of the private key corresponding to the requested public key under the exact challenge/request context. It does not prove identity, device integrity, key non-exportability, uniqueness, or issuance authority.

**RM-PKI-REQUEST-0004:** POP method identifies signature/key-agreement/indirect mechanism, algorithms/parameters, challenge/nonce/channel binding, verifier, time, replay state, and result. A bare public key or self-signature outside the request context is insufficient where replay/substitution matters.

**RM-PKI-REQUEST-0005:** Key generation uses an approved cryptographic plan and returns an opaque key-generation handle plus public-key/protection/provider evidence. The request builder cannot export private material merely to encode a CSR.

**RM-PKI-REQUEST-0006:** Key attestation is separately verified against attestation trust/policy and binds public key, hardware/provider/device/workload, security properties, freshness/challenge, firmware/module state, certification scope, privacy, and unknowns. It never becomes general subject identity or future non-exportability proof.

**RM-PKI-REQUEST-0007:** Requested extensions and names are untrusted proposals. The CA copies, modifies, rejects, or constructs them only under explicit profile policy and records requested-versus-issued differences.

**RM-PKI-REQUEST-0008:** Server-side key generation, archival, escrow, recovery, or key transport is disabled by default and requires a separate profile specifying generation trust, confidential delivery, recipient authentication, exportability, wrapping, split knowledge, retention, access, audit, destruction, and compromise response.

