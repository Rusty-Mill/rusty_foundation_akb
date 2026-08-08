# Hash, MAC, and derivation

**RM-CRYPTO-DERIVE-0001:** Hash operations MUST name algorithm, output length, input segmentation semantics, finalization, and canonical expected digest encoding. A digest alone provides neither authenticity nor safe password storage.

**RM-CRYPTO-DERIVE-0002:** MAC operations MUST bind key generation, exact MAC algorithm/parameters, full semantic message, protocol/domain context, tag length, and comparison policy. Truncation is explicit and policy-validated.

**RM-CRYPTO-DERIVE-0003:** Security-sensitive digest, MAC, tag, and key-confirmation comparisons MUST use a provider-evidenced value-independent comparison for equal-length inputs; length and parse rejection remain explicit.

**RM-CRYPTO-DERIVE-0004:** General KDF operations MUST specify source-key type, KDF identity, salt, label/info/context encoding, domain separation, output length, multi-output indexing, strength bound, and whether source/output material is exportable.

**RM-CRYPTO-DERIVE-0005:** Password-based derivation is a separate contract with password encoding, salt generation/length, memory/time/parallelism cost, output purpose, resource limits, policy version, upgrade detection, denial-of-service bounds, and secret-value handling.

**RM-CRYPTO-DERIVE-0006:** Salt, nonce, IV, personalization, label, and associated data MUST remain typed by role. Randomness requirements and reuse consequences are specified per algorithm; fields cannot be interchanged because their byte lengths match.

**RM-CRYPTO-DERIVE-0007:** Streaming and one-shot operations MUST produce identical results for the same semantic input where the algorithm permits; update-after-finalize, duplicate finalize, cloning, cancellation, and partial-output behavior are explicit.
