# Encryption, signatures, and trust

**RM-ARCHIVE-CRYPTO-0001:** Container encryption selects an exact authenticated profile, KDF and parameters, key source/generation, nonce allocation, covered fields, header/metadata confidentiality, chunking, padding, and failure-release policy.

**RM-ARCHIVE-CRYPTO-0002:** Passwords are credentials mediated by the secret/interaction boundary; they are not keys, command arguments, environment defaults, filenames, or loggable metadata.

**RM-ARCHIVE-CRYPTO-0003:** Encryption, checksum, digest, signature, timestamp, transparency, and provenance are independent evidence. Decryption success does not establish publisher identity or content acceptance.

**RM-ARCHIVE-CRYPTO-0004:** Unauthenticated legacy encryption is disabled by default. If interoperability policy permits it, the result is explicitly unauthenticated and content remains untrusted until independent acceptance succeeds.

**RM-ARCHIVE-CRYPTO-0005:** Per-entry encryption does not imply authenticated container structure; encrypted names/data can coexist with mutable indexes or metadata. Coverage is exposed field by field.

**RM-ARCHIVE-CRYPTO-0006:** Wrong credentials, damaged ciphertext, tag failure, unsupported profile, missing key, and policy rejection avoid distinguishing oracles beyond authorized diagnostics.

**RM-ARCHIVE-TRUST-0001:** Signed-artifact acceptance binds exact container bytes or a declared canonical signed view. Extraction never implicitly verifies, trusts, clears quarantine, or authorizes execution.
