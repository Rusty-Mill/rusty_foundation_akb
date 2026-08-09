# PKI-validation ownership and trial readiness

| Field | Value |
|---|---|
| Review status | Pass |
| Reviewed | 2026-08-08 |
| Accountable owner | PKI validation owner, initially exercised by Foundation maintainers |
| Architecture reviewer | Foundation architecture review |
| PKI/cryptography reviewer | Independent qualified review for parsing, paths, constraints, algorithms, identity profiles, status, pins, and trust nonclaims |
| Platform/privacy reviewer | Foundation platform trust-provider, network/SSRF, privacy, and accessibility review |
| Evidence reviewer | Foundation PKI conformance, interoperability, lifecycle, and performance review |
| Compatibility authority | Foundation architecture review until a dedicated compatibility council exists |

## Ownership duties

The owner maintains typed parsing/original bytes, trust snapshots/provenance/precedence, candidate/path construction, validation/purpose/time/algorithms, identity profiles/pins, revocation/status/freshness, network/cache/privacy, results/overrides/invalidation, dependencies/profiles, source/quality review, conformance, benchmarks, and dossier boundaries. Provider owners maintain separate Windows, Linux, and macOS library/store/policy/network frontiers. Consumer owners retain exact identity/purpose/trust program, proof-of-possession/transcript, freshness, account mapping, authorization, and action policy.

## Bounded trial plan

A later disposable trial may run pinned licensed RFC/public and independently generated roots, intermediates, leaves, CRLs, OCSP responses, identities, and trust snapshots through one exact provider/library path per platform. It may exercise malformed/ambiguous bounded parsing; unordered/duplicate/cross-signed/loop/same-subject/alternate-anchor graphs; constraints/purpose/algorithm/time; typed IDN/wildcard/IP/URI identities; revoked/good/unknown/stale/unavailable status; hostile AIA/CRL/OCSP locators; offline/proxy/redirect/SSRF/cache rollback; overrides/pins; trust/clock/provider updates; cancellation/resource bounds; and staged/sustained benchmarks.

The trial uses the [foundation trial template](../../05-governance/implementation-trials/trial-template.md), generated/disposable private PKI and status services, isolated network namespaces/VMs, no public or enterprise trust-store mutation, no production names/anchors/credentials, bounded objects/graphs/network/concurrency/time, pinned corpora/toolchains/providers, and isolated native/unsafe parsers. It does not select permanent Rust APIs/crates, production trust programs/stores, public Internet retrieval, identity profiles, default soft/hard fail, pins/overrides, performance budgets, or release support.

Stop conditions include input escape/unbounded parse/search/network, presented terminal treated as anchor, provider-policy substitution, unsupported identity guessing, unknown status reported good, SSRF/private-network or credential leakage, hidden blocking network, unauthorized trust mutation/exception, stale result reuse, sensitive evidence leakage, fabricated cancellation/indeterminate result, unsafe host-store changes, provenance/corpus/license loss, or material drift.

**RM-PKI-OWNER-0001:** Promotion and trial records MUST name accountable people for the unit and every claimed standards/profile/provider/platform/trust/network context, exact generations/revisions, reviewer independence/qualifications, and unresolved limitations.

**RM-PKI-OWNER-0002:** Trial hypotheses MUST distinguish parsing, inspection, candidate acquisition, path construction/preference, validation, identity matching, status retrieval/validation, network/cache, result publication/expiry/invalidation, proof-of-possession, and authorization.

**RM-PKI-OWNER-0003:** This bounded plan is evidence only and MUST NOT authorize implementation, native/unsafe code, public/enterprise trust-store changes, external network scanning, live revocation load, production certificates/keys, provider/library dependencies, exceptions/pins, packaging, or release.

**RM-PKI-OWNER-0004:** Closeout MUST account for every generated certificate/key/status object, trust source/snapshot, provider cache/store, network service/route/proxy fixture, pin/override, log/trace/report, dependency/cache, and host change; remove only verified disposable assets and retain sanitized reproducible evidence/nonclaims.
