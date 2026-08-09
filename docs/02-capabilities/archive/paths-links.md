# Paths, links, and special objects

**RM-ARCHIVE-PATH-0001:** Archive names are parsed into a portable component sequence before host mapping. Absolute roots, drive/device/UNC prefixes, empty/dot/dot-dot components, separators, NUL/control bytes, reserved names, trailing dot/space, and invalid encodings are recognized before filesystem access.

**RM-ARCHIVE-PATH-0002:** Destination mapping binds case and Unicode behavior, normalization, separator rules, component/path length, reserved names, stream/fork syntax, collision policy, and reversible rename mapping where selected.

**RM-ARCHIVE-PATH-0003:** Lexical containment is necessary but insufficient. Extraction resolves each creation relative to a held destination capability and rejects symlink, reparse, mount, junction, hard-link, and rename races that could escape it.

**RM-ARCHIVE-LINK-0001:** Link targets are parsed and authorized independently from entry names. Default untrusted extraction rejects symbolic and hard links; a stronger profile may create only targets proven contained in the staged graph.

**RM-ARCHIVE-LINK-0002:** Hard-link identity and ordering are graph properties. Forward references, cycles, missing targets, links to pre-existing destination objects, and link-to-link chains have explicit policies.

**RM-ARCHIVE-SPECIAL-0001:** Devices, FIFOs, sockets, mount-like objects, whiteouts, privileged metadata, setuid/setgid/sticky bits, capabilities, and security labels are rejected by default and require separate platform-specific authority.

**RM-ARCHIVE-PATH-0004:** Portability analysis can validate without extraction and returns every unmappable, lossy, conflicting, security-sensitive, or provider-unsupported entry.
