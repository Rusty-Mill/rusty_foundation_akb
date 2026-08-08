# Object-storage conformance specification

**RM-OBJECT-CONFORMANCE-0001:** Reports bind provider/service/SDK/protocol builds, account/namespace/configuration generations, region/topology, security/encryption/versioning/retention/replication, workload, limits, clocks, fixtures, faults, billing mode, and canonical operation traces.

**RM-OBJECT-CONFORMANCE-0002:** Identity/key tests cover Unicode/encoding/case/delimiters/control/bidi/reserved names, URI/signing canonicalization, endpoint forms, live/exact/noncurrent/null/delete-marker/soft-delete states, validator/checksum/digest distinctions, and tenant/prefix authority.

**RM-OBJECT-CONFORMANCE-0003:** Read tests cover whole/range/multi-range, generation pinning, parallel/resume, overwrite/delete during ranges, cache/CDN staleness, archive restore, checksum/digest failures, truncation, slow consumers, cancellation, and every size/resource bound.

**RM-OBJECT-CONFORMANCE-0004:** Write/multipart tests fault every byte/part/complete/response boundary, replace parts, reorder/miss/duplicate manifests, race create/overwrite/delete/metadata, unknown completion, abort/expiry/GC, copy/compose transformations, checksums, encryption, retention, and bulk partial outcomes.

**RM-OBJECT-CONFORMANCE-0005:** Conditional/version tests cover all generation/metadata/validator preconditions, create-only and read-modify-write races, versioning mode changes, markers/permanent deletion/undelete, lifecycle/retention/hold conflicts, bulk frozen manifests, and exact restoration.

**RM-OBJECT-CONFORMANCE-0006:** CAS/delegation tests cover digest algorithms/length/media types, hostile/mismatched bytes, graph/tag/reference races, dedup isolation/GC pins, algorithm transition, signing canonicalization, expiry/clock/redirect/header broadening, CORS, leakage, and quarantined uploads.

**RM-OBJECT-CONFORMANCE-0007:** Listing/inventory/event/replication/recovery tests cover pagination mutation, token expiry, delayed/duplicate/gap/reordered events, inventory completeness, overwrite/delete replication races, region loss/failover/divergence, retained-version restore, provider migration, semantic loss, and erasure residuals.

**RM-OBJECT-CONFORMANCE-0008:** Cross-provider matrices compare canonical traces across selected AWS/Azure/GCP/local/content-addressed providers and Windows/Linux/macOS clients; unsupported consistency, conditions, retention, integrity, or recovery remain explicit gaps.

