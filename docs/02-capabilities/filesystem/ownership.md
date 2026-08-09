# Filesystem ownership and trial readiness

| Field | Value |
|---|---|
| Review status | Pass |
| Reviewed | 2026-08-08 |
| Accountable owner | Filesystem capability owner, initially exercised by Foundation maintainers |
| Architecture reviewer | Foundation architecture review |
| Security reviewer | Foundation security/privacy review for namespace authority, traversal, disclosure, ACL/share policy, native handles, and sandbox boundaries |
| Evidence reviewer | Foundation filesystem conformance, reliability, and performance review |
| Compatibility authority | Foundation architecture review until a dedicated compatibility council exists |

## Ownership duties

The domain owner maintains path, authority, R-level, resource/I/O, metadata, replacement, D-level, error, dependency/profile, source, conformance, benchmark, and promotion semantics. Provider owners maintain distinct Windows, Linux, and macOS mappings plus filesystem-family support frontiers. Actual promotion and trial records name accountable people, exact environments, and reviewer-independence limitations.

## Bounded trial plan

A later disposable trial may exercise lossless native paths, opened directory authority, R-level resolution under adversarial namespace mutation, positioned sync/async partial I/O, cancel/complete races, metadata availability and identity, same-filesystem atomic replacement, and D0–D3 claims where support and safe fault apparatus exist. The minimum matrix includes NTFS, ext4, and APFS plus declared case/normalization variants, one removable or constrained configuration, and one network boundary; additional filesystems cannot inherit results.

The trial uses the [foundation trial template](../../05-governance/implementation-trials/trial-template.md), synthetic nonsensitive trees and payloads, disposable volumes/containers where needed, bounded storage/fault injection, isolated native code, no production data, no privileged destructive host operations, and no release publication. It does not select public Rust APIs, crates/workspaces, async runtime, serialization, repository topology, product path policy, sandbox authority model, supported filesystem list, performance budgets, or production durability claims.

Stop conditions include containment escape, authority escalation, unsafe path loss, uninitialized/aliased resource exposure, buffer reuse before terminal completion, false confirmed cancellation, hidden copy-delete, atomicity or durability claim inflation, destructive target ambiguity, host-volume risk, sensitive path/native-error leakage, unbounded resource retention, provenance loss, or material source/contract/environment drift.

**RM-FILESYSTEM-OWNER-0001:** Promotion and trial records MUST name accountable people for the domain and each claimed provider/filesystem, exact generations/options, reviewer independence, and unresolved limitations.

**RM-FILESYSTEM-OWNER-0002:** Trial hypotheses MUST distinguish path parsing, lookup containment, opened-object identity, transfer completion, namespace visibility, each D-level, and remote acknowledgement.

**RM-FILESYSTEM-OWNER-0003:** This bounded plan is evidence only and MUST NOT authorize implementation, unsafe/native interfaces, privileged access, destructive fault injection, packaging, or release.

**RM-FILESYSTEM-OWNER-0004:** Closeout MUST release handles/buffers/completion state, remove only verified disposable fixtures, revoke temporary authority, account for traces and fault apparatus, retain negative evidence, and prevent trial artifacts from entering release channels.
