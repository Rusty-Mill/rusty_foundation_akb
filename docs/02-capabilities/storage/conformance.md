# Storage volume conformance specification

| Area | Required evidence |
|---|---|
| Entities | device/media/region/filesystem/mount distinctions, generation replacement, duplicate labels/UUIDs, stale and ambiguous matching |
| Observation | namespace-bound coherent snapshots, completeness, event loss/reconciliation, suspend/resume, service restart, surprise removal |
| Topology | multi-partition, logical/virtual/aggregate, disk image, network, bind/overlay, multiple mounts and namespaces |
| Properties | capacity boundaries/overflow, read-only/features, unknown/redacted/error, encoding/malformed labels, provenance |
| Mount | target conflict, effective options, unlock/interaction separation, policy denial, read-only fallback prohibition, reconciliation |
| Unmount/eject | busy/veto, whole-media scope, force/lazy distinctions, privilege, staged progress, duplicate requests, surprise unplug |
| Durability | dirty data/metadata, supported flush stages, device/bridge cache nonclaims, power loss, ambiguous completion |
| Security | hostile filesystem metadata, no autorun, least authority, stale-generation destructive-op rejection, telemetry redaction |
| Accessibility | identical labels, keyboard/AT operation, nonvisual progress/veto/safe-removal state, localized risk messaging |

Fixtures include fixed/removable USB media, card readers with media replacement, optical where available, virtual disks/images, encrypted/locked media, multiple partitions, read-only media, network filesystems, bind/overlay mounts, namespace/container isolation, remote sessions, and fault injection. Destructive tests use disposable media only.

Reports bind OS/kernel/build, session/namespace/container, privileges/policy service, device/transport/bridge, filesystem, mount options, cache/flush support, power mode, provider versions, and every identity/durability/eject nonclaim.
