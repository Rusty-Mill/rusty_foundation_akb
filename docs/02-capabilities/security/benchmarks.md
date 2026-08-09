# Security foundation benchmark specification

**Status:** Draft

## Principle

Performance evidence must never weaken source choice, fail-closed behavior, memory initialization, or diagnostic secrecy. Native baseline and Rusty Mill measurements use the same source semantics and build mode.

## Measurements

### Secure-random comparison requirements

- **RM-SECURITY-RANDOM-BENCH-0001:** Fill comparisons **MUST** bind the same approved OS source, provider initialization/readiness state, request sizes/chunking, exact-fill/failure semantics, memory policy, concurrency, and build mode.
- **RM-SECURITY-RANDOM-BENCH-0002:** First-use comparisons **MUST** separate provider construction, source readiness wait, first fill, cancellation, and failure boundaries and **MUST NOT** silently prewarm one candidate.
- **RM-SECURITY-RANDOM-BENCH-0003:** Failure comparisons **MUST** use controlled provider fault injection, confirm no usable partial output or fallback, and retain only sanitized non-output diagnostics.
- **RM-SECURITY-RANDOM-BENCH-0004:** Every run **MUST** record provider/module artifact and configuration, OS/kernel/SDK, hardware/virtualization/clone context, security mode, toolchain/build, request/concurrency matrix, warmup, samples/statistics, and conformance result without random-derived artifacts.
- **RM-SECURITY-RANDOM-BENCH-0005:** Numeric budgets and native-performance claims **MUST** derive from reviewed representative runs; statistical properties, uniqueness, checksums, compressibility, or provider names **MUST NOT** establish security or correctness.

| ID | Measurement | Required reporting |
|---|---|---|
| SEC-BENCH-001 | Warm fill latency at 0, 16, 32, 256, 4 KiB, 64 KiB, and 1 MiB | p50/p95/p99, throughput, CPU time, allocations |
| SEC-BENCH-002 | First-use/provider-initialization latency | Distribution, initialization path, source readiness state |
| SEC-BENCH-003 | Concurrent fill scaling | Threads/tasks, aggregate throughput, tail latency, contention indicators |
| SEC-BENCH-004 | Abstraction overhead against native source | Absolute delta and ratio by size; identical failure checks |
| SEC-BENCH-005 | Failure-path latency | Fault mechanism, diagnostic cost, confirmation of no output disclosure |
| SEC-BENCH-006 | Secret create/retrieve/replace/delete | Provider, item size/class, interaction state, warm/cold latency distributions |
| SEC-BENCH-007 | Secret-store contention and scale | Item count, concurrency, lookup mode, throughput, p95/p99, provider serialization |
| SEC-BENCH-008 | Scoped reveal and opaque-use overhead | Native baseline, exposure mode, copies, allocations, boundary transitions |
| SEC-BENCH-009 | Authority derivation | constraint dimensions, parent/child representation, A-claim vector, p50/p95/p99, allocations, native calls |
| SEC-BENCH-010 | Constraint inspection/provenance | chain depth, dimensions, redaction mode, serialization-free report size, latency, allocations |
| SEC-BENCH-011 | Concurrent derivation/close | parent fanout, concurrency, close race, successes/failures, contention, tail latency |
| SEC-BENCH-012 | Transfer and delegation-depth enforcement | hop count, transport boundary, receiver policy, rejection/return path, cleanup latency |
| SEC-BENCH-013 | Revocation observation | scope, alias set, operation phase, request-to-observation latency, survivors/indeterminate outcomes |
| SEC-BENCH-014 | Restricted manifest validation and preparation | manifest shape, authority dimensions, provider discovery, validation/preparation latency, allocations/native calls, rejection cause |
| SEC-BENCH-015 | Restricted creation, enforcement, verification, and release | native stages, restriction set, release boundary, p50/p95/p99, allocations/native calls, verified outcome |
| SEC-BENCH-016 | Restricted readiness and supervised lifecycle | release-to-ready, ready-to-stop, descendant policy, shutdown/reap latency, terminal accounting |
| SEC-BENCH-017 | Restricted failure, cancellation, and reconciliation | injection stage, cancellation phase, child execution oracle, authority/resource reconciliation latency and outcome |
| SEC-BENCH-018 | Restricted abstraction overhead against equivalent native composition | exact mechanisms/constraints, stage deltas and ratios, conformance equivalence, residual assumptions |
| SEC-BENCH-019 | Secret conditional replace and delete lifecycle | generations/conflicts, acceptance/visibility, replica/backup/GC/erasure observations, reconciliation latency |
| SEC-BENCH-020 | Secret opaque/scoped/owned operation boundary | named operation, provider boundary, copies/exposures, transitions, latency/throughput, allocations/native calls |
| SEC-BENCH-021 | Secret interaction and cancellation | provider/product prompt stages, human time separated, cancellation phase, terminal/indeterminate outcome, recovery |
| SEC-BENCH-022 | Secret provider failure and recovery | fault boundary, partial state, public result, generation/visibility reconciliation, diagnostic overhead |

### Authority-attenuation comparison requirements

- **RM-SECURITY-ATTENUATE-BENCH-0001:** Derivation comparisons **MUST** bind identical parent authority, requested operation/resource/lifetime/audience/delegation restrictions, native context, A-claim vector, and subset/failure oracle.
- **RM-SECURITY-ATTENUATE-BENCH-0002:** Inspection/provenance comparisons **MUST** bind identical chain depth, constraint dimensions, disclosure/redaction authority, native evidence policy, and nonsecret output semantics.
- **RM-SECURITY-ATTENUATE-BENCH-0003:** Concurrency/transfer/revocation comparisons **MUST** bind identical alias topology, delegation depth, transport and receiver policy, close/revoke schedule, in-flight operations, terminal outcomes, and cleanup boundary.
- **RM-SECURITY-ATTENUATE-BENCH-0004:** Every run **MUST** record provider artifact, OS/kernel/SDK, authority kind, native enforcement/identity/sandbox context, complete claim vector and bypass assumptions, concurrency/topology, samples/statistics, and conformance result without authority material.
- **RM-SECURITY-ATTENUATE-BENCH-0005:** A faster baseline that drops an incomparable constraint, uses broader ambient credentials, weakens enforcement/alias/revocation semantics, or omits subset/bypass probes **MUST NOT** be treated as equivalent; numeric budgets require reviewed representative runs.

### Authority-unit comparison requirements

- **RM-SECURITY-AUTHORITY-BENCH-0001:** Policy-decision comparisons **MUST** bind identical policy/evaluator versions, subject/resource/environment evidence and generations, authority, requested operation, freshness, obligations, disclosure policy, and decision oracle.
- **RM-SECURITY-AUTHORITY-BENCH-0002:** Enforcement comparisons **MUST** separate advisory evaluation, native enforcement, operation progress/effect, audit publication, and reconciliation and bind an identical race/fault schedule.
- **RM-SECURITY-AUTHORITY-BENCH-0003:** Delegation comparisons **MUST** bind identical parent/child constraints, transfer mode, authenticated channel/audience, replay/use/depth bounds, prepare/accept/commit schedule, failure injection, and final authority inventory.
- **RM-SECURITY-AUTHORITY-BENCH-0004:** Expiry/revocation comparisons **MUST** bind identical authority generations, alias/partition topology, clocks, in-flight phases, committed effects, propagation mechanism, observation oracle, residuals, and cleanup boundary.
- **RM-SECURITY-AUTHORITY-BENCH-0005:** Every run **MUST** record exact provider artifact, OS/kernel/SDK, authority/resource kinds, native identity/enforcement/sandbox context, policy and evidence generations, ambient inputs, channel topology, claim vector, workload, samples/statistics, conformance result, and sanitized provenance; numeric budgets require reviewed representative runs.

### Restricted-execution comparison requirements

- **RM-SECURITY-RESTRICTED-BENCH-0001:** Preparation comparisons **MUST** bind the same immutable manifest, authority inputs, provider discovery, validation, attenuation, and rejection semantics without releasing application-controlled code.
- **RM-SECURITY-RESTRICTED-BENCH-0002:** Launch comparisons **MUST** report creation, restriction application, verification, release, readiness, supervision, termination, reaping, and cleanup as separate stages; creation alone **MUST NOT** count as success.
- **RM-SECURITY-RESTRICTED-BENCH-0003:** Failure and cancellation comparisons **MUST** inject at every supported pre-release and post-release boundary and prove whether child code executed, which authority transferred, and how every child and prepared resource was reconciled.
- **RM-SECURITY-RESTRICTED-BENCH-0004:** Every run **MUST** record exact OS/kernel/SDK, native mechanisms and configuration, manifest digest without sensitive values, enforced/degraded/unsupported constraints, supervision level, hardware/virtualization, toolchain/build, samples/statistics, and conformance outcome.
- **RM-SECURITY-RESTRICTED-BENCH-0005:** A native baseline is equivalent only when it enforces and verifies the same constraints with the same release, inheritance, readiness, descendant, failure, cancellation, audit, and cleanup semantics; numeric budgets and native-performance claims require reviewed representative runs.

### Secret-protection comparison requirements

- **RM-SECURITY-SECRET-BENCH-0001:** Lifecycle comparisons **MUST** bind the same provider/store/item class, protection vector, item size, account/session/sandbox/interaction state, generation/collision policy, operation milestones, replication/backup context, and cleanup contract.
- **RM-SECURITY-SECRET-BENCH-0002:** Scale comparisons **MUST** bind the same item population, lookup and enumeration authority, metadata sensitivity policy, concurrency, provider quotas/serialization, consistency, and terminal outcomes.
- **RM-SECURITY-SECRET-BENCH-0003:** Exposure comparisons **MUST** bind the same named consumer operation, opaque/scoped/owned mode, provider boundary, interaction policy, copy/allocation rules, secret-canary checks, and output semantics; a baseline that reveals reusable material is not equivalent to non-reveal.
- **RM-SECURITY-SECRET-BENCH-0004:** Every run **MUST** record exact provider/service/store/item artifact and configuration, OS/kernel/SDK, account/session/sandbox, claim vector, interaction/exposure, replication/backup, toolchain/build, workload/concurrency, stages, samples/statistics, conformance result, and sanitized provenance without secret-derived artifacts.
- **RM-SECURITY-SECRET-BENCH-0005:** Provider acceptance, logical visibility, replica/backup state, garbage collection, cryptographic erasure, and physical erasure **MUST** remain separate; numeric budgets and native-performance, security, hardware, non-export, or deletion claims require reviewed representative evidence.

## Controls

Record hardware, virtualization, power policy, OS/kernel, security configuration, compiler/toolchain, artifact digest, warmup, sample count, and confidence interval. Never persist output buffers. A checksum or compressibility score of generated material is also prohibited because it unnecessarily derives data from secret-quality output.

Regression budgets remain unset until representative Windows, Linux, and macOS baselines exist. No single cross-platform latency budget is presumed.

Interactive prompt time is reported separately from provider processing and never included in an abstraction-overhead ratio. Benchmarks use generated ephemeral test values, destroy them under the provider's declared semantics, and never record values or secret-derived fingerprints.
