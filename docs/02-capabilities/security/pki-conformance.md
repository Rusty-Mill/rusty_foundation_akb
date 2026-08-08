# Certificate, trust-store, and PKI-validation conformance specification

| Area | Required evidence |
|---|---|
| Parsing | RFC/standards and adversarial DER/PEM vectors, length/nesting/count limits, duplicate/unknown critical extensions, time/string/name forms, original-byte signature binding |
| Trust stores | anchors versus intermediates/distrust/trusted leaves, system/enterprise/user/application precedence, purpose constraints, enumeration privacy, update generations |
| Construction | unordered/duplicate/adversarial bags, cross-signing/alternate issuers/anchors, loops/same-subject keys, bounded search, provenance and deterministic preference |
| Validation | signatures, time, basic/path/name/policy constraints, KU/EKU/purpose, critical extensions, algorithm/strength, anchor rules, historical/current policy |
| Identity/pins | DNS/IP/URI/email/application profiles, SAN/CN policy, IDNs/wildcards/NUL/case/trailing dot, name constraints, proof-of-possession nonclaim, rotation/recovery pins |
| Status/network | CRL/delta/OCSP/stapled/blocklist, good/revoked/unknown/stale/unavailable, responder authority, replay, offline/proxy/redirect/SSRF, cache and hard/soft fail |
| Results/lifecycle | evidence-rich categories, overrides/exceptions, result expiry/dependencies, store/policy/clock/provider updates, cancellation/resource limits, redacted diagnostics |

Corpora include RFC 5280/6960-derived vectors, public path-validation suites with compatible licensing, independently generated roots/intermediates/leaves/status objects, malformed DER, ambiguous names, critical extensions, policy/name constraints, cross-signs, algorithm transitions, revoked/unknown/stale evidence, hostile AIA/CRL/OCSP locators, cache rollback, and clock/store changes. Reports bind OS/build/library/provider, parser/profile/policy versions, trust snapshot sources/generation, verification clock/time, reference identity, network/revocation/cache mode, candidate/path/anchor digests, status evidence, overrides/pins, and every identity/authorization/freshness nonclaim.
