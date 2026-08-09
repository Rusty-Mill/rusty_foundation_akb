# Secure-random ownership and trial readiness

| Field | Value |
|---|---|
| Review status | Pass |
| Reviewed | 2026-08-08 |
| Accountable owner | Secure-random capability owner, initially exercised by Foundation maintainers |
| Architecture reviewer | Foundation architecture review |
| Security reviewer | Foundation cryptography/security review for source selection, provider/module boundary, readiness/failure, output secrecy, lifecycle, and claims |
| Evidence reviewer | Foundation secure-random conformance, platform-lifecycle, and performance review |
| Compatibility authority | Foundation architecture review until a dedicated compatibility council exists |

## Ownership duties

The owner maintains exact-fill/failure, source/fallback, readiness, sync/optional-async, output secrecy, fork/clone/snapshot/suspend/reinitialization, diagnostics, certification nonclaims, dependency/profile, source, quality, conformance, benchmark, and capability-readiness semantics. Provider owners maintain separate Windows, Linux, and macOS module/configuration/lifecycle frontiers. Consumer owners retain key/nonce/salt/token/password/identifier policy.

## Bounded trial plan

A later disposable trial may exercise zero/boundary/large/chunked fills, concurrent calls, first-use/readiness, cancellation where materially supported, controlled partial/failure injection, no-fallback/no-output disclosure, and supported fork, VM/container clone/snapshot, suspend/resume, sandbox, and reinitialization cases. Statistical tests are limited to integration-fault investigation and are neither pass criteria for unpredictability nor retained output artifacts.

The trial uses the [foundation trial template](../../05-governance/implementation-trials/trial-template.md), caller buffers immediately overwritten after exact assertions, no output persistence/fingerprinting, disposable isolated environments for lifecycle tests, bounded requests/concurrency, isolated native code, no production secrets, and no release publication. It does not select public Rust APIs, crates/workspaces, cryptographic library/provider, DRBG, key generation, password/token formats, certification claims, performance budgets, or production support.

Stop conditions include non-approved fallback, public partial output, predictable substitute output, source/provider ambiguity, output or derived-artifact leakage, hidden runtime, false readiness/cancellation, lifecycle duplication concern, provider/module/configuration drift, unverifiable certification language, unsafe host lifecycle testing, unbounded resource use, provenance loss, or material contract/environment drift.

**RM-SECURITY-RANDOM-OWNER-0001:** Promotion and trial records MUST name accountable people for capability and each claimed provider/module/configuration/platform/lifecycle context, exact generations, reviewer independence, and unresolved limitations.

**RM-SECURITY-RANDOM-OWNER-0002:** Trial hypotheses MUST distinguish provider construction, source readiness, native progress, public exact-fill success/failure, cancellation, caller use, lifecycle reinitialization, statistical investigation, and certification evidence.

**RM-SECURITY-RANDOM-OWNER-0003:** This bounded plan is evidence only and MUST NOT authorize implementation, native/unsafe code, cryptographic provider selection, secret/key generation, host snapshot/fork operations outside disposable scope, packaging, or release.

**RM-SECURITY-RANDOM-OWNER-0004:** Closeout MUST overwrite/release buffers and native state, remove only verified disposable fixtures, account for all logs/traces without output-derived data, retain negative nonsecret evidence, and exclude trial artifacts from release channels.
