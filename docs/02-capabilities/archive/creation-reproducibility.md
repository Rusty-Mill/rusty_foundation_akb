# Creation and reproducibility

**RM-ARCHIVE-CREATE-0001:** A creation plan binds source snapshot/authority, selected entries, portable names, metadata mapping, traversal/link policy, format/profile, codec parameters/dictionaries, encryption/signing, ordering, limits, and destination publication semantics.

**RM-ARCHIVE-CREATE-0002:** Source traversal does not follow links by default and detects graph cycles, source replacement, mount/reparse transitions, unreadable entries, volatile files, sparse regions, and metadata/data races.

**RM-ARCHIVE-CREATE-0003:** Snapshot consistency is qualified as atomic filesystem snapshot, provider snapshot, handle-stable read set, revalidated best effort, or inconsistent. Completion cannot overstate the selected boundary.

**RM-ARCHIVE-REPRO-0001:** A reproducibility profile pins entry byte ordering; path encoding/normalization; timestamp value, zone, precision, and clamping; ownership; permissions; attributes; extension-field order; comments; padding; codec parameters; dictionaries; and provider/tool generations.

**RM-ARCHIVE-REPRO-0002:** Deterministic creation means identical eligible logical input under one profile yields identical bytes. Reproducible provenance additionally identifies how eligibility and logical input were established.

**RM-ARCHIVE-REPRO-0003:** Parallel compression may reorder completion but never canonical output order. Providers disclose if threading, hardware, or library upgrades affect bytes.

**RM-ARCHIVE-CREATE-0004:** Creation writes to isolated staging, finalizes all indexes/authentication, verifies requested digests, flushes at the selected durability level, and conditionally publishes by atomic replace or returns a weaker named milestone.
