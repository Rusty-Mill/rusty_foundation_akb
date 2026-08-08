# `rm.profile.foundation.server`

| Field | Value |
|---|---|
| Status | Draft |
| Version | 1.2.0 |
| Purpose | Long-running non-interactive service foundation with bounded shutdown and protected credentials |

## Workload assumptions

No interactive desktop session, unattended restart, concurrent I/O, explicit service identity, and observable graceful shutdown. Networking, configuration, process service, and observability capabilities remain explicit gaps.

## Required capabilities and services

**RM-PROFILE-FOUNDATION-SERVER-0001:** Requires the [CLI foundation](foundation-cli.md) capability set, `rm.security.secret-store` `>=0.1.0,<0.2.0`, and the orderly shutdown service `>=0.1.0,<0.2.0`.

**RM-PROFILE-FOUNDATION-SERVER-0002:** `rm.filesystem.atomic-replace` is conditionally required when the deployment persists mutable local state. The deployment predicate and required durability level are part of the request; an in-memory/stateless deployment does not select it.

## Security and interaction constraints

- **RM-PROFILE-FOUNDATION-SERVER-0003:** Secret store interaction is prohibited; it remains available before workload acceptance under the configured service identity.
- **RM-PROFILE-FOUNDATION-SERVER-0004:** Secret persistence, machine/service-account binding, exportability, replication, and recovery behavior are explicit.
- **RM-PROFILE-FOUNDATION-SERVER-0005:** No provider may depend on a desktop session or silently fall back to plaintext files.
- **RM-PROFILE-FOUNDATION-SERVER-0006:** Resolution and secret retrieval use explicit authority; environment variables do not become a secret store.
- **RM-PROFILE-FOUNDATION-SERVER-0007:** Restricted execution is optional for workers/helpers and must meet the manifest without interactive degradation.
- **RM-PROFILE-FOUNDATION-SERVER-0008:** Process supervision `>=0.1.0,<0.2.0` is conditionally required when the workload launches managed workers; minimum containment level and breakaway/orphan policy are request inputs.
- **RM-PROFILE-FOUNDATION-SERVER-0009:** Worker stdio capture conditionally requires `rm.ipc.byte-pipe` `>=0.1.0,<0.2.0` at Q2 or Q3 unless a bounded Q1 worker/saturation budget is accepted explicitly.
- **RM-PROFILE-FOUNDATION-SERVER-0010:** Native service registration and demand activation `>=0.1.0,<0.2.0` are conditional when the deployment is installed or activated by an OS service manager. Definitions bind immutable package generation, machine/user/container scope, service principal, structured launch, endpoint/interface identity, readiness, restart/backoff, budgets, update, and removal.
- **RM-PROFILE-FOUNDATION-SERVER-0011:** Durable scheduling `>=0.1.0,<0.2.0` is conditional when work survives process or host restart. Schedules preserve temporal domain, civil-zone/rule policy where applicable, eligibility window, missed/overlap/retry policy, authority, and generation; registration is not exact execution or application-result evidence.
- **RM-PROFILE-FOUNDATION-SERVER-0012:** Background triggers are untrusted at-least-once invalidation hints. Attempts revalidate authoritative state, principal/policy/resources, acquire idempotent or transactional work claims, checkpoint explicitly, and report cancellation/crash/timeout/effect ambiguity without claiming exactly once.
- **RM-PROFILE-FOUNDATION-SERVER-0013:** Evidence covers system/user/container managers, demand/persistent/timed/event workloads, noninteractive credential access, namespace collision, partial registration, duplicate/lost triggers, clock/sleep/reboot/downtime, quotas/dependency loss, overlap/retry/crash loops, update/coexist/drain/rollback/removal, service-manager restart, and activation/schedule/recovery benchmarks.
- **RM-PROFILE-FOUNDATION-SERVER-0014:** Cryptographic operations/key management `>=0.1.0,<0.2.0` are conditional when protecting data, authenticating messages, deriving keys, signing/verifying, or establishing shared keys. Resolution binds versioned workload policy, exact suite/parameters/encoding, provider/module/protection/certification evidence, opaque key generation/usage/export/lifetime, service principal, and noninteractive authority.
- **RM-PROFILE-FOUNDATION-SERVER-0015:** Private/symmetric keys are non-exportable operation capabilities by default. Noninteractive access, remote/HSM outage, rate limits, provider loss, rotation/overlap/rollback, backup/migration, revocation/destruction, and algorithm transition are explicit; software fallback cannot weaken hardware/export/certification policy.
- **RM-PROFILE-FOUNDATION-SERVER-0016:** Evidence includes official/adversarial vectors, nonce allocation across processes/restarts/snapshots, malformed encodings and oracle behavior, concurrency/cancellation, key usage/exhaustion/rotation, provider/hardware/remote failure, policy transition, certification/attestation scope, secret exposure/zeroization mapping, timing review, and sustained throughput/latency/fairness benchmarks.

## Operational constraints

Deadline timers and cancellation support bounded multi-phase shutdown. Sync paths cannot create a runtime, while async I/O waits use native readiness/completion where available. Conformance includes high concurrency, credential rotation conflict, locked/unavailable provider, clock suspend behavior, cancellation races, and supervisor termination.

## History

- **1.2.0:** Adds conditional versioned cryptographic policy, opaque operation-scoped keys, exact primitive/composition/transfer contracts, noninteractive provider/hardware evidence, lifecycle, conformance, and benchmarks.
- **1.1.0:** Adds conditional OS-managed service registration/demand activation and durable scheduling with exact scope/principal, trigger reconciliation, attempt/checkpoint/retry, budget, update, conformance, and benchmark requirements.
- **1.0.0:** Adds direct process launch/control through CLI 1.0.0 and conditional supervision/pipe requirements for managed workers.
- **0.1.0:** Initial non-interactive runtime, filesystem, secret-store, and shutdown trial.
