# Filesystem Experimental promotion review

| Field | Value |
|---|---|
| Status | Proposed; no maturity change |
| Subject | Filesystem foundations 0.1.1; directory, resolution, file, metadata, atomic-replacement, and durability contracts 0.1.x |
| Architecture | Model 1.84.0 |
| Proposed decision | Eligible for explicit Experimental promotion review; remain Draft pending disposition |
| Implementation authority | None |

## Gate assessment

| Gate | State | Exact evidence | Qualification |
|---|---|---|---|
| Contract semantics | Pass | [directory](directory.md), [resolution](resolve.md), [file](file.md), [metadata](metadata.md), [replacement](atomic-replace.md), [durability](durability-model.md), ADR-0006/0007/0008 | append, exact metadata base, Windows share/delete policy, path serialization, and sandbox authority remain out of promoted scope or open |
| Dependencies/profile impact | Pass | [composition register](dependencies.md), [CLI profile](../profiles/foundation-cli.md), [desktop profile](../profiles/foundation-desktop.md), [server profile](../profiles/foundation-server.md), [source-linked graph](../../04-ecosystem/consistency-readiness/dependency-graph.md) | exact required/optional edges are registered; product filesystem and D-level selections remain open |
| Platform research | Pass | [platform research](platform-research.md), [source review](source-review.md) | exact OS/kernel/SDK, native mechanism, filesystem, mount/volume, sandbox, and storage generations are not selected |
| Cross-cutting planning | Pass | [quality review](cross-cutting.md) | no provider execution, power-failure proof, specialist product review, or native-performance result exists |
| Assertions/cases | Pass | [traceability](traceability.md), [conformance](conformance.md) | cases are specified but not executed; filesystem tiers cannot inherit results |
| Benchmark scenarios | Pass | [scenario mapping](traceability.md#benchmark-scenario-mapping), [benchmarks](benchmarks.md) | no baseline run, numeric budget, regression conclusion, or native-performance claim exists |
| Ownership/trial bounds | Qualified | [ownership](ownership.md), [trial governance](../../05-governance/implementation-trials/README.md) | role ownership exists; named people, independent signoffs, disposable environments, and fault apparatus are absent |

## Decision boundary

The generated scorecard may report planning eligibility. Filesystem remains Draft until an accepted record binds named accountable people, independent reviewers, exact contract/profile/provider/filesystem scope, R/D levels, excluded open questions, findings/waivers, decision date, and permitted trial constraints. A valid repository standards profile and separately accepted trial record remain required before code.

**RM-FILESYSTEM-PROMOTION-0001:** Eligibility MUST NOT change maturity, select native APIs/filesystems/async runtimes, resolve product policy, or authorize implementation without an explicit accepted decision.

**RM-FILESYSTEM-PROMOTION-0002:** Promotion MUST bind exact path, authority, resolution, resource, partial-I/O, cancellation, metadata, identity, atomicity, durability, error, platform, filesystem, and profile claims; omitted qualities remain unsupported or unknown.

**RM-FILESYSTEM-PROMOTION-0003:** Planned cases and scenarios MUST NOT be represented as passing portability, security, accessibility, native-performance, atomicity, durability, recovery, or resource-safety evidence.
