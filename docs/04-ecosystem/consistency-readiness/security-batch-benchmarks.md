# Security-foundation batch benchmark specification

**Status:** Planned composed scenarios; no baselines or budgets  
**Authority:** [Security batch integration review](security-batch-integration-review.md)

| Scenario | Composition | Required stage reporting |
|---|---|---|
| `rm.benchmark.security-batch.restricted-secret-workload@1` | authority → secret acquisition/mediated use → restricted workload | policy/attenuation, interaction, provider operation, manifest preparation, native controls, verification, release, readiness, shutdown, cleanup, redaction |
| `rm.benchmark.security-batch.issue-activate@1` | authority + random + crypto + validation + issuance | plan/proofing/POP, key operation, request, CA queue/commit/sign, delivery, parse/validate, key-bound install, activation/health, old-generation retirement, reconciliation |
| `rm.benchmark.security-batch.validate-channel@1` | crypto + validation + consumer authority | parsing, path/status/network/cache, crypto operations, identity/transcript/POP, consumer policy, authority enforcement, connection/effect, result invalidation |
| `rm.benchmark.security-batch.rotate-revoke@1` | secrets + crypto + validation + issuance + authority | successor create/distribute/use, caches/replicas/status, predecessor denial, aliases/partitions/in-flight work, durable effects, convergence, residuals |
| `rm.benchmark.security-batch.provider-loss-recovery@1` | all selected units sharing or separating providers | failure detection, cancellation/unknowns, issuance halt, workload containment, restore/rebind, generation invalidation, conformance recheck, reconciliation, evidence publication |
| `rm.benchmark.security-batch.policy-provider-update@1` | all selected units | discovery without side effects, new-plan resolution, compatibility, staged activation, cache/result invalidation, rollback/forward recovery, mixed-generation window, convergence |

## Comparison contract

Every run binds an exact compatible tuple of unit contracts, profiles, consumer policies, provider artifacts/configurations, OS/kernel/SDK, hardware/virtualization, authority/resource/identity contexts, key/secret/certificate/trust generations, algorithms/protocols, network/clock/cache, sandbox, interaction policy, workload/concurrency, fault schedule, build/toolchain, conformance result, and sanitized evidence provenance.

Report end-to-end and per-stage latency distributions, throughput, CPU, memory, allocations, native/provider calls, boundary transitions, copies/exposures, queue/network/interaction waits, retry/poll/backoff, locks/contention, durability operations, cancellation and indeterminate rates, reconciliation time, residual resources/effects, and diagnostic cost. Human interaction time is separate. Security material and derived fingerprints are never retained.

**RM-SECURITY-BATCH-BENCH-0001:** A baseline is comparable only when every selected authority, protection, algorithm, trust/status, issuance, isolation, lifecycle, failure, disclosure, and recovery guarantee is equivalent and its unit conformance prerequisites pass.

**RM-SECURITY-BATCH-BENCH-0002:** End-to-end totals MUST NOT hide policy, interaction, network, hardware/remote provider, CA queue, durability, installation/activation, revocation propagation, cleanup, or reconciliation stages.

**RM-SECURITY-BATCH-BENCH-0003:** Shared-provider and separated-provider variants MUST report boundary and assurance differences; fewer transitions or copies MUST NOT be interpreted as stronger security, compatibility, certification, or lifecycle evidence.

**RM-SECURITY-BATCH-BENCH-0004:** Failure, cancellation, timeout, provider loss, update, restore, and mixed-generation scenarios MUST measure truthful terminal/indeterminate states and reconciliation, never only the fast successful path.

**RM-SECURITY-BATCH-BENCH-0005:** Numeric budgets and native-performance or availability claims remain RFC-owned until representative Windows, Linux, and macOS runs pass applicable unit and batch conformance with reviewed methodology and raw evidence.

**RM-SECURITY-BATCH-BENCH-0006:** Planned scenarios, generated harness structure, or one platform/provider run MUST NOT be represented as a cross-platform benchmark result, optimization authorization, provider selection, or release gate pass.
