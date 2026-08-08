# Storage security, privacy, and accessibility

Observation, mount, unlock, write, format, raw access, unmount, eject, and device removal use distinct authorities. Native enforcement occurs again at each operation; identity evidence never grants access.

**RM-STORAGE-SECURITY-0001:** Untrusted filesystems, labels, icons, metadata, partition tables, and device firmware MUST be treated as hostile inputs at adapter boundaries.

**RM-STORAGE-SECURITY-0002:** Autorun, executable trust, quarantine/provenance, content indexing, thumbnail/preview generation, and application launching MUST NOT be implicit effects of the base storage services.

**RM-STORAGE-SECURITY-0003:** Encryption state observation MUST NOT expose keys, recovery material, account identifiers, or credential prompts. Unlock uses a separate secret/consent service with attenuated authority.

**RM-STORAGE-SECURITY-0004:** Mount paths, labels, filesystem/device identifiers, capacity/usage, network sources, busy-client details, and content-derived metadata MUST be privacy classified and redacted from ordinary telemetry.

**RM-STORAGE-ACCESS-0001:** User-facing mount/eject flows MUST expose device/volume distinction, current milestone, veto/failure, data-loss risk, and safe-to-remove state through keyboard and assistive technology, not sound/color alone.

**RM-STORAGE-ACCESS-0002:** Identical or empty labels MUST be disambiguated with localized, non-sensitive attributes; raw paths, UUIDs, and serials are not the default accessible name.

Operations initiated in a background or remote session follow explicit interaction policy and cannot silently display prompts in another user's session.
