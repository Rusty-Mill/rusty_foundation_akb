# Container entries and metadata

**RM-ARCHIVE-ENTRY-0001:** Entry descriptors expose raw name bytes/text evidence, normalized portable components, kind, logical/stored sizes, offsets where meaningful, codec/encryption identity, times, owner/group, permissions, platform attributes, links, sparse extents, extended attributes/streams/forks, comments, and integrity fields without fabricating absent values.

**RM-ARCHIVE-ENTRY-0002:** Entry kinds distinguish regular, directory, symbolic link, hard link, sparse file, device, FIFO, socket, whiteout, opaque/unknown, metadata-only, and format-extension records.

**RM-ARCHIVE-ENTRY-0003:** Duplicate names, overlapping extents, case/Unicode-equivalent names, parent/child type conflicts, multiple metadata records, and contradictory sizes/checksums are explicit conflicts resolved by selected policy, never incidental iteration order.

**RM-ARCHIVE-ENTRY-0004:** Metadata conversion reports exact, normalized, approximated, dropped, rejected, or preserved-opaque per field. Security descriptors, POSIX modes, ACLs, labels, capabilities, alternate streams, forks, quarantine, and executable intent are not assumed equivalent.

**RM-ARCHIVE-ENTRY-0005:** Enumeration is lazy and bounded but descriptors borrowed from a reader have explicit lifetime. Retention or parallel decode requires an owned immutable descriptor.

**RM-ARCHIVE-ENTRY-0006:** Listing treats names, comments, owners, links, and extension data as hostile display content with escaping, truncation, bidi/control handling, and accessible structured alternatives.
