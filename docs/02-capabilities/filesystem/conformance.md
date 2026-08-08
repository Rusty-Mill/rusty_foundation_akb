# Filesystem foundations conformance specification

| Field | Value |
|---|---|
| Status | Draft |
| Suite version | 0.1.0 |
| Scope | Path model, resolution, regular-file I/O, metadata, atomic replacement, and error semantics |

## Evidence classes

- **D:** deterministic functional assertion.
- **C:** concurrent, adversarial, or model-based assertion.
- **E:** environment/filesystem-sensitive assertion.
- **R:** architecture/API/artifact review.
- **P:** performance observation supplied by the benchmark suite.

Results identify suite/provider/contract versions, OS and filesystem, mount/volume options, architecture, storage type, virtualization, security context, and artifact provenance.

## Path-model assertions

| Assertion | Decision/rule | Class | Pass condition |
|---|---|---|---|
| CT-FS-PATH-001 | ADR-0006 | D | Native values round-trip without loss, including non-Unicode POSIX names and valid Windows-native sequences. |
| CT-FS-PATH-002 | ADR-0006 | D | Display conversion reports exact, escaped, or lossy mode and never mutates the path value. |
| CT-FS-PATH-003 | Path principles 4–5 | D | Grammar parsing and lexical operations perform no filesystem access. |
| CT-FS-PATH-004 | Path prohibited assumptions | D/R | No implicit case fold, Unicode normalization, separator rewrite, or object-identity claim exists. |
| CT-FS-PATH-005 | ADR-0007 | D/R | Parent removal/canonicalization alone is never exposed as a containment proof. |

## Resolution assertions

| Assertion | Requirements | Class | Pass condition |
|---|---|---|---|
| CT-FS-RESOLVE-001 | 0001, 0011 | D | Resolution requires a directory authority and rejects absolute/device forms in the base operation. |
| CT-FS-RESOLVE-002 | 0002 | D | Lexical rejection and lookup failure have distinct typed outcomes. |
| CT-FS-RESOLVE-003 | 0003, 0008 | E/R | Link/reparse/mount policy is discoverable and weakened fallbacks are explicit. |
| CT-FS-RESOLVE-004 | 0004 | C | Link and ancestor rename/swap races cannot escape the declared containment level. |
| CT-FS-RESOLVE-005 | 0005 | C | Object-kind substitution between lookup steps cannot cause a mismatched resource to be returned. |
| CT-FS-RESOLVE-006 | 0006 | D/C | All creation dispositions satisfy exclusive/truncate/existing behavior under races. |
| CT-FS-RESOLVE-007 | 0007 | D/R | Granted access never exceeds the request; platform sharing/deletion effects match declared policy. |
| CT-FS-RESOLVE-008 | 0009, 0010 | C | Every error/cancel path leaks no usable partial resource and successful resources close safely. |
| CT-FS-RESOLVE-009 | 0012 | D/R | Diagnostics redact components beyond granted diagnostic authority. |
| CT-FS-RESOLVE-010 | ADR-0007 | E | Provider claim is tested across supported local, removable, and network filesystem classes. |

Resolution results additionally record and verify the provider's [R0–R3 resolution quality](resolution-quality.md). R1+ assertions use adversarial concurrent mutation; a static no-link fixture is insufficient evidence.

## Directory-resource assertions

| Assertion | Requirements | Class | Pass condition |
|---|---|---|---|
| CT-FS-DIRECTORY-001 | 0001, 0009 | D/R | Lookup, enumeration, mutation, metadata, and sync authority are distinct; relative authority does not grant absolute namespace access. |
| CT-FS-DIRECTORY-002 | 0002 | C | Rename/move of the external binding does not retarget operations on the opened directory resource. |
| CT-FS-DIRECTORY-003 | 0003 | C | Explicit close/drop is safe under concurrent use and double close is unrepresentable. |
| CT-FS-DIRECTORY-004 | 0004, 0010 | E/D | Enumeration round-trips native names, applies disclosure policy, and claims no ordering unless selected. |
| CT-FS-DIRECTORY-005 | 0005 | C/E | Concurrent create/remove/rename behavior matches the declared non-snapshot or snapshot quality. |
| CT-FS-DIRECTORY-006 | 0006 | D/C | Namespace mutations require authority and satisfy exclusive/idempotent semantics under races. |
| CT-FS-DIRECTORY-007 | 0007 | E | Directory synchronization reports achieved D-level or explicit unsupported status. |
| CT-FS-DIRECTORY-008 | 0008 | E | Identity scope and reuse match the metadata contract. |

## File-resource assertions

| Assertion | Requirements | Class | Pass condition |
|---|---|---|---|
| CT-FS-FILE-001 | 0001, 0002 | D/C | Granted access is inspectable; explicit close/drop is safe and double close cannot occur. |
| CT-FS-FILE-002 | 0003, 0007 | C | Concurrent positioned I/O does not alter shared cursor state and matches declared overlap semantics. |
| CT-FS-FILE-003 | 0004, 0005 | D/E | Short transfer and EOF are represented as progress, not generic failure. |
| CT-FS-FILE-004 | 0006 | D | Offset/length/size overflow fails before unsafe native conversion. |
| CT-FS-FILE-005 | 0008 | C/R | Buffers and operation state cannot be reused before terminal async completion. |
| CT-FS-FILE-006 | 0009 | C | Completion/cancellation races preserve actual terminal outcome and partial effects. |
| CT-FS-FILE-007 | 0010 | D/R | Sync path functions without creating or nesting an executor. |
| CT-FS-FILE-008 | 0011 | E | Extend/truncate results match declared zero-fill, sparse, and allocation behavior. |
| CT-FS-FILE-009 | 0012, 0013 | E | Content, metadata, and directory durability scopes are separately exercised and reported. |
| CT-FS-FILE-010 | 0014 | D | Portable category and provider evidence survive representative failures. |

## Metadata assertions

| Assertion | Requirements | Class | Pass condition |
|---|---|---|---|
| CT-FS-META-001 | 0001, 0009 | C | Handle, path-following, and no-follow subjects are explicit and path races are documented/tested. |
| CT-FS-META-002 | 0002, 0003 | D/E | Unsupported/unavailable/unknown fields are not fabricated as zero or epoch values. |
| CT-FS-META-003 | 0004 | E | Regular, directory, link/reparse, and uncommon kinds are distinguished or preserved as unknown extensions. |
| CT-FS-META-004 | 0005 | E | Logical and allocated size are distinct where supported. |
| CT-FS-META-005 | 0006 | E | Timestamp kind and precision are accurate; birth time is never inferred from change time. |
| CT-FS-META-006 | 0007 | E/R | Identity equality and reuse behavior match declared scope across rename, replacement, deletion, and remount. |
| CT-FS-META-007 | 0008 | C | Snapshot remains immutable and makes no live-state guarantee during mutation. |
| CT-FS-META-008 | 0010, 0011 | E/R | Security and unknown native attributes are not misleadingly flattened or dropped silently. |

## Atomic-replacement assertions

| Assertion | Requirements | Class | Pass condition |
|---|---|---|---|
| CT-FS-REPLACE-001 | 0001, 0002 | D/E | Explicit authorities and same-filesystem eligibility are enforced before the claimed operation. |
| CT-FS-REPLACE-002 | 0003, 0008 | C | Concurrent observers see old or replacement binding; no copy-delete fallback claims atomicity. |
| CT-FS-REPLACE-003 | 0004, 0011 | E/R | Visibility and durability are separate; required sync sequence and scope are reported. |
| CT-FS-REPLACE-004 | 0005, 0006 | E | Metadata and identity results match each selected policy on each filesystem. |
| CT-FS-REPLACE-005 | 0007 | E | Injected native failures produce accurate replaced/not-replaced/partial/indeterminate outcomes. |
| CT-FS-REPLACE-006 | 0009 | E/C | Backup overwrite, atomicity, metadata, and cleanup match policy under races. |
| CT-FS-REPLACE-007 | 0010 | C | Cancellation around commit never reports canceled after replacement became visible. |
| CT-FS-REPLACE-008 | 0012 | D/R | Required namespace and metadata authority is checked without silent escalation. |

## Durability assertions

| Assertion | Requirements | Class | Pass condition |
|---|---|---|---|
| CT-FS-DURABILITY-001 | 0001, 0002 | D/R | Every sync outcome declares D-level/failure model; buffered completion alone never claims D1. |
| CT-FS-DURABILITY-002 | 0003 | E | D1 survives the declared crash/restart experiment with content and retrieval-critical metadata intact. |
| CT-FS-DURABILITY-003 | 0004, 0009 | E | D2 survives namespace crash experiments; unsupported directory sync cannot pass. |
| CT-FS-DURABILITY-004 | 0005 | E/R | D3 maps to documented cache flush/ordering and passes supported fault-injection or power-cut evidence. |
| CT-FS-DURABILITY-005 | 0006, 0007 | C/E | Sync failures and cancellation races report visible state and known/indeterminate durability truthfully. |
| CT-FS-DURABILITY-006 | 0008 | E/R | Remote claims identify client, server, protocol, and stable acknowledgement boundary. |
| CT-FS-DURABILITY-007 | 0010 | R | Benchmarks and comparisons use equivalent D-levels. |

## Error-model assertions

Use generated and injected failures to cover every base category. Verify context-dependent retry metadata, redaction, preservation of provider code/domain, partial progress, causal chaining, unknown-code fallback, and prohibition on message parsing. Mapping coverage is reported per operation/provider rather than as one global table.

## Filesystem test matrix

The initial matrix should include at least:

- Windows: NTFS plus one ReFS/FAT/removable configuration when supported.
- Linux: ext4 plus one copy-on-write filesystem and one network/filesystem boundary case.
- macOS: APFS in default and case-sensitive configurations where available.
- Cross-platform: one network share protocol and one constrained/sandboxed environment.

Stable claims enumerate exact tested families and options; untested filesystems are not implied conforming merely because the OS is supported.

Each published report conforms to the [provider support matrix](support-matrix.md) and links R-level, D-level, filesystem tier, assertion results, and benchmark digest.
