# Process environment model

**Status:** Draft semantic model

## Construction modes

| Mode | Meaning |
|---|---|
| Empty | Begin with no variables except provider-mandated entries disclosed in the result |
| Snapshot | Begin from an explicit captured environment snapshot |
| Overlay | Apply ordered set/remove operations to an explicit base snapshot |

Implicit “inherit current environment at the eventual launch instant” is a convenience extension because concurrent process-global mutation can race with construction.

## Rules

- Keys and values are lossless native string values with platform validation; embedded native terminators are rejected.
- Comparison and duplicate-key behavior follow a declared provider rule. Windows case-insensitive environment-name behavior is not imposed on POSIX providers.
- Construction yields one deterministic effective map or fails before launch.
- Invalid entries, encoding conversion loss, size overflow, and provider-mandated collisions are errors, not silently dropped values.
- Ordering is not a portable semantic property except where a provider requires deterministic native serialization.
- Environment variables are ambient data delivered to all child code and commonly observable through debugging or same-account facilities; they are not a secret store.
- Secret-derived values require explicit disclosure policy, minimize lifetime, and remain subject to platform leakage limitations.
- Provider-added or rewritten entries are included in the launch disclosure with sensitive values redacted.

## Concurrency

Snapshots are immutable. Builders are independently owned or explicitly synchronized. Launch consumes/finalizes an immutable environment so later parent mutation cannot change it.

