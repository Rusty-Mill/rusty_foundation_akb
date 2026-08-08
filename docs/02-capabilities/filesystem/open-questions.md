# Filesystem foundations open questions

**Status:** Active register

| ID | Question | Why it matters | Evidence or decision needed |
|---|---|---|---|
| FS-Q001 | What minimum containment strength is required for Stable `rm.filesystem.resolve`? | macOS and older Linux/Windows paths may lack equivalent atomic constraints. | Adversarial prototypes and support policy |
| FS-Q002 | Is a directory resource part of `resolve` or a separate capability? | Directory authority is foundational to secure composition. | Two consumer/domain designs |
| FS-Q003 | Should append be a file capability quality or a separate operation contract? | Atomic append and positioned-write semantics vary. | Platform/filesystem matrix |
| FS-Q004 | What durability levels are portable? | Flush APIs, caches, filesystems, devices, and power-loss behavior differ. | Crash/power-failure research and ADR |
| FS-Q005 | Which metadata fields belong in the base snapshot? | Too many fields create false portability; too few force platform branching. | CLI/server/desktop scenarios |
| FS-Q006 | How is Windows share/delete policy represented without infecting portable callers? | It materially affects open, rename, and replacement. | Policy model RFC |
| FS-Q007 | Is atomic replacement a capability or a platform service over resolution, file sync, and namespace mutation? | It coordinates several resources but maps to a native atomic mechanism. | Layering review after conformance design |
| FS-Q008 | What is the portable error taxonomy? | Raw errno/Win32 codes are unstable; excessive normalization loses recovery detail. | Cross-platform failure inventory |
| FS-Q009 | How should path values serialize across platform families? | Lossless native representation may not be meaningful elsewhere. | Packaging/configuration scenarios |
| FS-Q010 | Which filesystem families are required for conformance? | NTFS/ReFS/FAT, ext4/XFS/btrfs, APFS, and network filesystems expose different guarantees. | Support matrix RFC |
| FS-Q011 | Is filesystem watching a journal, invalidation stream, or multiple quality levels? | Native services differ in granularity, persistence, and loss behavior. | Dedicated watch domain analysis |
| FS-Q012 | How are sandbox/bookmark/capability authorities represented on macOS and other platforms? | Path access may not equal durable authority. | Security model research |
