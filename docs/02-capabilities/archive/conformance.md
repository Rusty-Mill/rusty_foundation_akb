# Conformance

**RM-ARCHIVE-CONFORMANCE-0001:** Codec suites use official vectors and generated boundary corpora for empty/small/large data, every chunk split, concatenation, dictionaries, checksums, truncation, trailing/skippable content, invalid distances/lengths, parameter extremes, and differential decode.

**RM-ARCHIVE-CONFORMANCE-0002:** Container corpora cover every record/extension/kind, unknown fields, ZIP64/large offsets, streaming descriptors, pax headers, sparse files, duplicate/overlapping entries, inconsistent local/index records, split volumes, truncation, padding, and polyglots.

**RM-ARCHIVE-CONFORMANCE-0003:** Path suites cross-product absolute/relative roots, dot components, separators, drives/UNC/devices, reserved names, trailing dot/space, case folding, Unicode normalization, invalid encodings, length limits, duplicate aliases, links, reparse/mount races, and special objects on each platform/filesystem.

**RM-ARCHIVE-CONFORMANCE-0004:** Extraction fault injection interrupts every read, decode, verify, write, metadata, flush, rename, overwrite, cleanup, and recovery boundary and verifies declared atomicity, residual evidence, containment, least privilege, and idempotent recovery.

**RM-ARCHIVE-CONFORMANCE-0005:** Resource suites exercise nested and high-ratio bombs, huge sparse logical sizes, excessive entries/metadata/frames/volumes, slow sources/sinks, backpressure, cancellation, concurrency, tenant fairness, diagnostic bounds, and integer/allocation edges.

**RM-ARCHIVE-CONFORMANCE-0006:** Reproducibility suites vary traversal order, locale, time zone, host metadata, thread count, chunking, provider, architecture, OS, filesystem, and clean build root; expected byte identity is checked only within the declared profile.

**RM-ARCHIVE-CONFORMANCE-0007:** Encryption suites test KDF/profile parameters, nonce uniqueness, wrong/missing/rotated keys, header/entry authentication, tampering at every covered field, unauthenticated legacy rejection, oracle resistance, cancellation, and unverified-output policy.

**RM-ARCHIVE-CONFORMANCE-0008:** Reports bind corpus version/digests, OS/build/filesystem, provider/library, format/profile, codec parameters/dictionaries, budgets, security policy, source/sink capabilities, and every skipped/degraded assertion.
