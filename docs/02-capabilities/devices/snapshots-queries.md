# Device snapshots and queries

A snapshot binds observer generation, query, start/end monotonic observations, revision, completeness, namespace/provider versions, devices, typed edges, projected properties, redactions, and diagnostic quality.

**RM-DEVICE-SNAPSHOT-0001:** Enumeration MUST return an immutable revisioned snapshot with explicit completeness and observation bounds.

**RM-DEVICE-SNAPSHOT-0002:** The provider MUST distinguish present, started/usable, disabled, disconnected, suspended, faulted, and unknown states only where the native source supports them; it MUST NOT collapse unknown into absent or usable.

**RM-DEVICE-SNAPSHOT-0003:** Filtering MUST use typed class, relationship, state, and property predicates. Platform-native predicates MAY be available only through a disclosed extension and MUST NOT redefine portable matches.

**RM-DEVICE-SNAPSHOT-0004:** Enumeration limits, truncation, per-property errors, permission redaction, malformed native data, and partial topology MUST be represented in the result.

**RM-DEVICE-SNAPSHOT-0005:** Cancellation returns no snapshot unless the contract explicitly returns a labeled partial diagnostic result; a partial result MUST NOT enter ordinary selection.

Sync enumeration is permitted only when its blocking and affinity behavior is declared. The async path performs potentially blocking property retrieval outside native notification callbacks and supports cancellation/deadlines without creating a hidden runtime.
