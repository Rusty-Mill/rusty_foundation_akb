# Device discovery scope and scenarios

## Goals

`rm.device.observer` supports bounded enumeration, typed filtering, topology inspection, change observation, and resolution of a still-current device reference. Consumers include device pickers, diagnostics, class-specific capability resolvers, and recovery coordinators.

## Non-goals

The base contract does not open a device, speak USB/HID/storage/camera/audio protocols, install or select drivers, mount volumes, eject media, modify power state, claim exclusive access, infer a human owner, or provide remote inventory management.

## Scenarios

- Enumerate currently usable display adapters matching a class constraint without opening them.
- Populate an accessible device picker while redacting identifiers the user need not see.
- Observe docking, hotplug, virtual-device publication, driver restart, and removal.
- Reconcile after notification overflow or suspend/resume.
- Correlate a class-specific endpoint with the underlying platform device only when the provider proves the relationship.
- Detect that a saved reference is stale and require explicit policy before choosing a replacement.
- Shut down an observer while a change callback and re-enumeration are in flight.

**RM-DEVICE-SCOPE-0001:** Discovery MUST remain usable without selecting any class-specific I/O capability.

**RM-DEVICE-SCOPE-0002:** A query MUST state its observation scope, included device/service classes, presence/availability policy, property projection, and authority.

**RM-DEVICE-SCOPE-0003:** Providers MUST expose unsupported filters, properties, topology edges, and change qualities instead of silently broadening or narrowing a query.
