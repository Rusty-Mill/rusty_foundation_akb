# Filesystem Experimental promotion review

| Field | Value |
|---|---|
| Status | Proposed; no maturity change |
| Subject | Filesystem foundations 0.1.1; directory, resolution, file, metadata, atomic-replacement, and durability contracts 0.1.x |
| Architecture | Model 1.99.0 |
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
| Ownership/trial bounds | Qualified | [ownership](ownership.md), [trial governance](../../05-governance/implementation-trials/README.md) | role owner named (see Named ownership, below); independent second reviewers, disposable environments, and fault apparatus remain absent |
| Candidate R/D-level evidence (external, non-authoritative) | Qualified | [TRIAL-0002](../../05-governance/implementation-trials/rustils-trial-proposal.md), rustils PR [#122](https://github.com/baileyrd/rustils/pull/122), `rustils` `docs/behavior/fs.md` and `docs/divergences.md` #013/#014 at commit `cc1c699130c1ed92428e2a9003f81dc0732e0305` | see Candidate R/D-level evidence section below; this is cited input evidence from an external repository per RFC-0002's rollout rule, not evidence collected under this AKB's own conformance suite, and does not itself satisfy the Assertions/cases or Benchmark scenarios gates above |

## Candidate R/D-level evidence (external, non-authoritative)

TRIAL-0002 cited `baileyrd/rustils` as candidate input evidence for this domain (among others). Since that citation, rustils closed part of the gap its own comparison record (`RT-002`) flagged, in [rustils#122](https://github.com/baileyrd/rustils/pull/122):

| Backend | R-level (`open_dir`/`create_dir`) | R-level (`open`/`access`/`metadata`/etc.) | D-level (`write_atomic`) |
|---|---|---|---|
| Linux | **R2** (`openat2` `RESOLVE_NO_SYMLINKS\|RESOLVE_NO_XDEV`, 5.6+ kernel; falls back to R1 on `ENOSYS`) | R1 (unchanged — plain `openat`/`*at`; a terminal-symlink-following promise these ops already make is preserved) | **D2** (`fsync` on the directory's own fd after the publishing rename; strace-verified) |
| Windows | **R2, link-confinement half only** (`OBJ_DONT_REPARSE`; no NT flag equivalent to `RESOLVE_NO_XDEV` exists, so mount-confinement is not claimed) | R1 (unchanged, same reasoning as Linux) | D1 (no directory-durability claim — no documented, verifiable NTFS guarantee for flushing a directory handle was found) |

Neither backend claims R3: no `RESOLVE_IN_ROOT`/root-constraint request exists on either side, and rustils' own `Dir` contract does not promise beneath-confinement (a relative path containing `..`, or a symlink whose target is absolute, is not prevented from resolving outside the opened directory's own subtree).

This evidence is **qualified, not adopted**: it comes from an externally, independently governed repository's own parity suite (strace-verified for the Linux D2 claim; a committed, real-Windows-CI-executed parity test for the Windows R2-link-confinement claim), not from this AKB's own conformance harness, and per `RM-RUSTILS-TRIAL-0003` it must not be represented as Rusty-Mill conformance or promotion by its own existence. It narrows what a future accepted decision would need to independently verify — it does not substitute for that verification.

## Decision boundary

The generated scorecard may report planning eligibility. Filesystem remains Draft until an accepted record binds named accountable people, independent reviewers, exact contract/profile/provider/filesystem scope, R/D levels, excluded open questions, findings/waivers, decision date, and permitted trial constraints. A valid repository standards profile and separately accepted trial record remain required before code.

## Named ownership (bootstrap staffing)

Per `governance.md`'s explicit allowance ("one person may hold several roles initially"): **baileyrd** is named as Filesystem capability owner and as the architecture, security, standards, and evidence reviewer roles this gate assessment references, until independent reviewers are added. This closes the "named people" half of the Ownership/trial bounds gate; independent signoffs, disposable environments, and fault apparatus remain open, and this naming alone does not change Status above — per `RM-FILESYSTEM-PROMOTION-0001`, only an explicit accepted decision does that.

**RM-FILESYSTEM-PROMOTION-0001:** Eligibility MUST NOT change maturity, select native APIs/filesystems/async runtimes, resolve product policy, or authorize implementation without an explicit accepted decision.

**RM-FILESYSTEM-PROMOTION-0002:** Promotion MUST bind exact path, authority, resolution, resource, partial-I/O, cancellation, metadata, identity, atomicity, durability, error, platform, filesystem, and profile claims; omitted qualities remain unsupported or unknown.

**RM-FILESYSTEM-PROMOTION-0003:** Planned cases and scenarios MUST NOT be represented as passing portability, security, accessibility, native-performance, atomicity, durability, recovery, or resource-safety evidence.
