# Path validation and policy

A `ValidationPolicy` binds purpose/profile, verification time and clock quality, trust snapshot, algorithm/strength policy, initial policy set, name constraints, basic constraints/path length, key usage and extended usage, reference identity, critical-extension processors, revocation/status/transparency policy, network mode, override/pin policy, and provider requirements.

**RM-PKI-VALIDATE-0001:** Validation MUST process exact selected path and anchor under a named policy/profile/version; generic `valid_certificate` is not a portable result.

**RM-PKI-VALIDATE-0002:** Every non-anchor certificate MUST satisfy signature, validity time, issuer relationship, basic/name/policy constraints, path length, key usage/extended usage, critical extensions, algorithm/strength, and applicable status policy at its role.

**RM-PKI-VALIDATE-0003:** Purpose MUST be explicit. Server, client, code, document, email, timestamp, device, enterprise, and attestation uses MUST NOT inherit interchangeable extended-key-usage or identity semantics.

**RM-PKI-VALIDATE-0004:** Validation time MUST identify clock source, uncertainty/quality, selected instant, and historical/current policy. Current trust/revocation data MUST NOT be silently used as proof of historical validity.

**RM-PKI-VALIDATE-0005:** Algorithm policy MUST separately govern certificate signatures, subject keys, anchor constraints, status signatures, and legacy path segments. Provider acceptance cannot override prohibited algorithms or parameters.

**RM-PKI-VALIDATE-0006:** Validation success MUST report the exact path, anchor/trust source, policy and trust generations, identity match, time, status quality, provider/version, network/cache use, overrides, pins, warnings, and nonclaims.

**RM-PKI-VALIDATE-0007:** Path validation establishes policy-qualified certificate evidence only. It does not prove private-key possession, peer/channel binding, account identity, authorization, certificate issuance correctness, compromise absence, or semantic content validity.
