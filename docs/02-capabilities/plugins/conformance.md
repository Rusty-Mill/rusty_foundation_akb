# Plugin conformance specification

| Area | Required evidence |
|---|---|
| Manifest | canonical parsing, unknown critical fields, bombs/limits, digest/signature/provenance distinctions |
| Discovery | no-code-execution proof, malicious paths/symlinks, duplicate conflict, observer loss/rescan |
| Resolution | interface/dependency graphs, cycles, feature ranges, platform/isolation/authority mismatch |
| ABI/protocol | ownership, allocation, panic/exception/trap, malformed data, async/cancellation, affinity/reentrancy |
| Isolation | denied ambient filesystem/network/process access, grant attenuation, broker validation, quotas/exhaustion |
| Lifecycle | startup deadline/failure, atomic readiness, quiesce, outstanding calls, crash/restart, terminal report |
| Update | staged immutable install, migration failure, atomic switch, rollback compatibility, revocation/emergency disable |
| Native loading | safe dependency search, signing/library validation, constructor failure, host restart requirement |
| Supply chain | SBOM/license/provenance/signature/key-rotation and vulnerability-policy fixtures |

Untrusted cases run only in disposable restricted processes or component runtimes. In-process adversarial native tests use sacrificial processes because undefined behavior cannot be safely contained. Reports bind OS/build, architecture, package digest, compiler/ABI/runtime/loader versions, isolation policy, grants, limits, signing/trust configuration, and every weakened platform protection.

