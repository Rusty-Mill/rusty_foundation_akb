# File and object-reference authority

**RM-ACTIVATION-FILE-0001:** A file target MUST distinguish lossless native path/display locator, opened object/capability, storage-provider token/bookmark/document-portal reference, claimed/detected content type, object identity/generation, access mode, scope, lifetime, and provenance.

**RM-ACTIVATION-FILE-0002:** Read, edit/write, print, reveal parent, execute, move/delete, metadata, and persistent-future access are separate operations. An open/view activation grants only the native authority explicitly supplied and validated.

**RM-ACTIVATION-FILE-0003:** A path string never proves containment, continued identity, content type, safety, or authority. Providers prefer handle/object-based activation and disclose replacement/race behavior where only a locator can cross the broker.

**RM-ACTIVATION-FILE-0004:** Writable handoff requires explicit user/product intent and attenuated capability. Read-only fallback MUST NOT be silently upgraded, and inability to enforce requested access causes failure or named degradation.

**RM-ACTIVATION-FILE-0005:** Remote, cloud-placeholder, virtual, removable, quarantined, downloaded, executable/script, archive, symlink/reparse, and directory targets remain explicit evidence. Observation/activation does not hydrate, mount, execute, clear quarantine, or trust content automatically.

**RM-ACTIVATION-FILE-0006:** Persistent bookmarks/tokens are opaque provider-scoped secret-like references with generation, scope, expiry/revocation, storage protection, and stale-target handling. They are not portable serialized authority.

**RM-ACTIVATION-FILE-0007:** Handler receives content as hostile input and applies its own parser/import limits. Broker/type selection does not validate the file or authorize embedded effects.
