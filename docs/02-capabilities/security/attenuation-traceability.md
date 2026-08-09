# Authority-attenuation assertion and benchmark traceability

**Status:** Draft capability mapping  
**Authority:** [`rm.security.attenuate`](attenuation.md)

| Assertion | Covered normative source | Requirements | Verification intention |
|---|---|---|---|
| `rm.assertion.security.attenuate.subset@1` | `attenuation.md` | ATTENUATE-0001–0003/0009 | Property-test subset across every dimension; reject expansions/incomparable restrictions/ambient grants and preserve parent on failure. |
| `rm.assertion.security.attenuate.provenance@1` | `attenuation.md` | ATTENUATE-0004–0005/0010 | Verify nonsecret parent/request provenance, effective portable summaries, disclosure authority, and credential/policy-material redaction. |
| `rm.assertion.security.attenuate.lifecycle@1` | `attenuation.md` | ATTENUATE-0006–0009 | Verify independent close, declared parent-close effects, constrained duplication/transfer/depth, scoped revocation, aliases, in-flight behavior, and races. |
| `rm.assertion.security.attenuate.enforcement@1` | `attenuation.md` | A0–A3 claim model | Verify exact per-dimension enforcement vector, native mechanisms, bypass assumptions, and adversarial probes without scalar-score inference. |
| `rm.assertion.security.attenuate.dependencies@1` | `attenuation-dependencies.md` | DEPENDENCY-0001–0004 | Verify parent/resource authority inputs, service-consumer direction, restricted-execution boundary, and graph/profile distinctions. |
| `rm.assertion.security.attenuate.quality@1` | `attenuation-cross-cutting-review.md` | QUALITY-0001–0003 | Verify six quality dimensions, exact methods, claim limitations, and specialist boundaries. |
| `rm.assertion.security.attenuate.sources@1` | `attenuation-source-review.md` | SOURCE-0001–0004 | Verify authoritative sources, mechanism/version/deployment frontier, expiry/invalidation, and observed-versus-documented separation. |
| `rm.assertion.security.attenuate.ownership@1` | `attenuation-ownership.md` | OWNER-0001–0004 | Verify roles, provider/kind matrix, bounded trial, stop conditions, cleanup, and nonauthorization. |
| `rm.assertion.security.attenuate.readiness-boundary@1` | `attenuation-readiness-review.md`, `attenuation-traceability.md` | READINESS-0001–0003, TRACE-0001–0003 | Verify capability-dossier completeness without implying domain maturity, sandbox creation, universal revocation, or implementation authority. |

## Benchmark scenario mapping

| Scenario | Benchmark requirements | Legacy workload | Comparison contract |
|---|---|---|---|
| `rm.benchmark.security.attenuate.derive@1` | `RM-SECURITY-ATTENUATE-BENCH-0001`, `RM-SECURITY-ATTENUATE-BENCH-0004`, `RM-SECURITY-ATTENUATE-BENCH-0005` | SEC-BENCH-009 | Same parent, multidimensional restriction, native context, claim vector/bypasses, subset oracle, failure atomicity, and evidence boundary. |
| `rm.benchmark.security.attenuate.inspect@1` | `RM-SECURITY-ATTENUATE-BENCH-0002`, `RM-SECURITY-ATTENUATE-BENCH-0004`, `RM-SECURITY-ATTENUATE-BENCH-0005` | SEC-BENCH-010 | Same provenance depth/dimensions, summary, disclosure/redaction, native evidence, and absence of credential material. |
| `rm.benchmark.security.attenuate.concurrent-lifecycle@1` | `RM-SECURITY-ATTENUATE-BENCH-0003`, `RM-SECURITY-ATTENUATE-BENCH-0004`, `RM-SECURITY-ATTENUATE-BENCH-0005` | SEC-BENCH-011 | Same fanout/concurrency, parent-child alias topology, close/derive race, terminal semantics, and leak oracle. |
| `rm.benchmark.security.attenuate.transfer@1` | `RM-SECURITY-ATTENUATE-BENCH-0003`, `RM-SECURITY-ATTENUATE-BENCH-0004`, `RM-SECURITY-ATTENUATE-BENCH-0005` | SEC-BENCH-012 | Same child/depth, transport, receiver acceptance, cancel/reject/return policy, authority inventory, and cleanup. |
| `rm.benchmark.security.attenuate.revocation@1` | `RM-SECURITY-ATTENUATE-BENCH-0003`, `RM-SECURITY-ATTENUATE-BENCH-0004`, `RM-SECURITY-ATTENUATE-BENCH-0005` | SEC-BENCH-013 | Same scope/aliases, request time, in-flight phases, native mechanism, observation boundary, survivors/indeterminate outcomes, and reconciliation. |

**RM-SECURITY-ATTENUATE-TRACE-0001:** Every attenuation requirement and A-claim dimension MUST map to a stable assertion and executable case/review method before capability promotion.

**RM-SECURITY-ATTENUATE-TRACE-0002:** Windows, Linux, and macOS adapters MUST preserve assertion identity while reporting exact authority kind, native mechanisms, deployment context, claim vector, aliases, and bypass assumptions separately.

**RM-SECURITY-ATTENUATE-TRACE-0003:** Derivation success, portable subset, native enforcement, isolation, transfer, close, revocation request, revocation observation, in-flight effect, and sandbox verification MUST remain separate evidence boundaries.
