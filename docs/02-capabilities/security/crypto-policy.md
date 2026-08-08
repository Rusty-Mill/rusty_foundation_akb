# Algorithm suites and policy

A `CryptoWorkload` states purpose/protocol role, allowed operation families, minimum security strength, confidentiality/authenticity horizon, interoperability constraints, key origin/protection/export requirements, interaction, latency/throughput/size limits, deprecation deadlines, compliance claims, and degradation policy. Resolution produces an immutable `CryptoPlan` naming exact algorithms, parameter sets, encodings, provider/module generation, and unsupported/nonclaim evidence.

**RM-CRYPTO-POLICY-0001:** Algorithms MUST be selected by stable semantic identity plus exact parameters and operation purpose; provider names, string aliases, key size alone, and operating-system identity are insufficient.

**RM-CRYPTO-POLICY-0002:** Policy MUST be versioned and bind protection horizon, minimum strength, allowed/required/prohibited algorithms and parameters, legacy verify/decrypt exceptions, transition dates, provider constraints, and evidence source.

**RM-CRYPTO-POLICY-0003:** Generation, encryption, signing, verification, decryption, derivation, agreement, wrapping, import, and export MAY have different policy states. Legacy verification/decryption MUST NOT silently authorize new signing/encryption.

**RM-CRYPTO-POLICY-0004:** Provider defaults and automatic algorithm substitution are prohibited. Resolution reports every unsupported constraint, approximation, provider conversion, and fallback before key or operation creation.

**RM-CRYPTO-POLICY-0005:** Algorithm agility MUST preserve protocol/on-disk identifiers, downgrade resistance, negotiation transcript binding, multi-key transition, rollback policy, and retained legacy-read horizon; it is not a generic algorithm string parameter.

**RM-CRYPTO-POLICY-0006:** Compliance and certification policy MUST name standard/profile revision, provider/module/version, platform/configuration, operating mode, boundary, algorithm/operation, and evidence status. No application-wide `compliant=true` claim is permitted.

**RM-CRYPTO-POLICY-0007:** Policy updates publish a new generation. Existing keys/data retain creation/use policy evidence and are re-evaluated explicitly for continued use, migration, verification, decryption, or retirement.
