# Authenticated encryption

An `AeadPlan` binds exact algorithm/parameters, key generation, nonce construction and uniqueness owner, tag length, associated-data schema, plaintext/ciphertext length limits, record framing, rekey limits, overlap/in-place policy, provider, and output format generation.

**RM-CRYPTO-AEAD-0001:** Authenticated encryption is the base symmetric confidentiality/integrity contract. Unauthenticated encryption modes require a separate legacy contract and MUST NOT be offered as an equivalent fallback.

**RM-CRYPTO-AEAD-0002:** Nonce generation/allocation MUST have a single declared owner and uniqueness strategy bound to key generation, concurrency, crash/restart, rollback/snapshot/restore, counter exhaustion, and multi-process/device coordination.

**RM-CRYPTO-AEAD-0003:** Ciphertext format MUST bind version, suite/parameters, key identifier/generation policy, nonce, tag, associated-data schema/version, framing, and length limits without exposing sensitive metadata unnecessarily.

**RM-CRYPTO-AEAD-0004:** Decryption MUST authenticate before releasing plaintext to ordinary consumers. Streaming/provisional plaintext, if selected for specialized protocols, is separately typed as untrusted and cannot escape before final authentication.

**RM-CRYPTO-AEAD-0005:** Authentication failure MUST return no plaintext and MUST avoid diagnostic distinctions that create a protocol oracle. Parse, policy, key, provider, and resource failures remain internally attributable under redaction policy.

**RM-CRYPTO-AEAD-0006:** In-place and overlapping-buffer operations require exact provider support and failure atomicity. Output length, initialization, retained partial data, and zeroization behavior are specified for every failure/cancellation path.

**RM-CRYPTO-AEAD-0007:** Message/byte/time limits and rekey thresholds are enforced per key generation. Exhaustion prevents further encryption while separately governed decryption may remain available.
