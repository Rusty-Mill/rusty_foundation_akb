# Storage capacity and properties

Capacity observations state boundary and units: total addressable, filesystem total, free, available-to-caller, reserved, quota-limited, reclaimable estimate, allocation unit, physical/logical sector, and uncertainty. Values are revision-bound and can change immediately.

**RM-STORAGE-PROPERTY-0001:** Capacity MUST distinguish filesystem free space from space available to the current authority and MUST report unknown/overflow/stale separately.

**RM-STORAGE-PROPERTY-0002:** Byte, block, sector, and allocation-unit values MUST carry exact units and reject overflow during conversion.

**RM-STORAGE-PROPERTY-0003:** Filesystem type/version, case behavior, normalization, maximum component/path, timestamp quality, feature flags, read-only state, and remote/removable/virtual hints MUST be evidence with provenance, not assumptions derived from OS or path syntax.

**RM-STORAGE-PROPERTY-0004:** Labels and mount display names are untrusted, potentially sensitive user-facing text with explicit encoding and truncation/error state.

**RM-STORAGE-PROPERTY-0005:** Rotational, solid-state, removable, hot-pluggable, encrypted, network, and health characteristics MUST report source and uncertainty; they MUST NOT silently drive destructive, security, or durability policy.

Health telemetry, SMART, wear, bad blocks, temperature, and predictive failure are a separate device-health capability due to privilege, privacy, vendor variance, and operational consequences.
