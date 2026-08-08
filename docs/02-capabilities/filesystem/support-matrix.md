# Filesystem provider support matrix

| Field | Value |
|---|---|
| Status | Draft declaration schema |

Conformance claims are made against a platform, OS version, filesystem family, mount/volume options, storage topology, and provider version. “Works on Windows/Linux/macOS” is not a sufficient filesystem claim.

## Required declaration dimensions

| Dimension | Examples |
|---|---|
| Platform | Windows, Linux, macOS and exact build/kernel |
| Architecture | x86-64, Arm64 |
| Filesystem | NTFS, ReFS, FAT/exFAT, ext4, XFS, btrfs, APFS |
| Name behavior | case-sensitive/preserving, normalization, native encoding |
| Topology | local block, removable, network, virtual, container/sandbox |
| Resolution | supported R-levels by policy |
| I/O | sync/async/positioned/append behavior and limits |
| Metadata | field availability, precision, identity scope |
| Replacement | atomicity, same-filesystem rule, metadata/identity policy |
| Durability | supported D-levels and failure boundaries |
| Watching | not in initial slice; future quality declaration |

## Initial certification tiers

- **Core local:** primary native filesystem on each platform: NTFS, a selected mainstream Linux filesystem, and APFS.
- **Extended local:** additional local/removable filesystem families with documented degradation.
- **Network:** explicitly named protocol/server/filesystem combinations; no inheritance from local claims.
- **Sandboxed:** explicitly named application sandbox/container authority model.

Stable capability status requires Core-local evidence on all three target platforms. Extended, Network, and Sandboxed claims are independent evidence sets and may mature separately.

## Claim format

Each provider claim records capability contract versions, R and D levels, supported operations, known degradation, conformance report digest, benchmark report digest, and expiration/retest policy. Changes to OS, filesystem driver, mount policy, or storage topology may require recertification.
