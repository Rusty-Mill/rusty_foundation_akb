# Signatures, verification, and agreement

**RM-CRYPTO-PUBLIC-0001:** Signature plans MUST bind algorithm/parameter set, key generation, message-versus-prehash mode, digest and domain/context, signature encoding, randomness/determinism policy, malleability/canonicality policy, and size limits.

**RM-CRYPTO-PUBLIC-0002:** Verification returns cryptographic validity for exact bytes, public key, algorithm, parameters, context, encoding, and policy generation. It does not establish signer identity, trust, authorization, freshness, intent, certificate status, or semantic document validity.

**RM-CRYPTO-PUBLIC-0003:** Verification MUST reject malformed, noncanonical where policy requires, wrong-context, wrong-parameter, trailing-data, and algorithm-confusion inputs before reporting valid.

**RM-CRYPTO-PUBLIC-0004:** Key agreement MUST bind local private-key authority, validated peer public-key type/parameters, protocol transcript/context, contributory/small-subgroup validation where applicable, and a specified KDF; raw shared secrets MUST NOT become general exportable bytes by default.

**RM-CRYPTO-PUBLIC-0005:** Hybrid or multi-algorithm agreement/signature MUST specify component ordering/encoding, composition combiner, required-versus-optional components, downgrade rules, failure behavior, and combined security claim. Concatenation alone is not a generic proof.

**RM-CRYPTO-PUBLIC-0006:** Public-key encryption and key encapsulation, if selected, MUST define padding/encoding, label/context, ciphertext validation, implicit rejection/oracle resistance, decapsulation failure, and derived-key use; raw asymmetric primitives are not public application contracts.

**RM-CRYPTO-PUBLIC-0007:** Certificate parsing/path validation, revocation, transparency, timestamping, identity proofing, code/document signing policy, and protocol authentication are separate services composed over signature/verification operations.
