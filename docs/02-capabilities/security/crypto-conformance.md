# Cryptographic operations and key-management conformance specification

| Area | Required evidence |
|---|---|
| Policy/resolution | stable suite identities, exact parameters/encodings, prohibited/legacy modes, provider mismatch/fallback denial, policy update and transition |
| Keys/authority | generate/import/open/use/export/rotate/revoke/destroy separation, purpose/principal/use limits, non-exportability, state races, lineage and deletion nonclaims |
| Hash/MAC/KDF | official and independent vectors, segmentation/finalization, truncation/comparison, domain separation, salt/context/output bounds, password cost/DoS |
| AEAD | vectors and negative cases, nonce uniqueness across concurrency/crash/snapshot, AAD/tag/length, no unauthenticated plaintext, in-place/overlap/failure atomicity |
| Public key | signature/verification encodings and malleability, wrong context/algorithm/key, agreement validation/KDF, hybrid composition, malformed/adversarial inputs |
| Transfer | bounded canonical parse, public/private/wrapped forms, policy preservation, wrong-provider/tenant/context/replay, backup/migration nonclaims |
| Provider/evidence | software/OS/hardware/remote providers, provenance/version/self-tests, removal/update/fallback, attestation replay/trust, certification-boundary accuracy |
| Operations/quality | buffer arithmetic/aliasing, secret copies/zeroization, concurrency/affinity, async cancellation, prompt denial, fault injection, oracle and timing tests |

Corpora include published standards vectors, independently generated cross-provider vectors, Wycheproof-style malformed/edge cases where license and scope permit, boundary sizes, empty/maximum inputs, noncanonical encodings, invalid points/keys/tags/signatures, nonce/counter exhaustion, corrupted wrapped/imported keys, provider faults, concurrency races, and policy transitions. Reports bind OS/build/CPU/microcode, provider/module/version/configuration/mode, algorithm/parameters/encoding, key origin/storage/protection/export/usage, policy generation, random source, interaction/session state, test corpus version, and every hardware/certification/side-channel/destruction nonclaim.
