# Storage volume benchmark specification

| Benchmark | Measures |
|---|---|
| Observation | enumeration and reconciliation latency versus entities, properties, mounts, namespaces, and cold/warm state |
| Change convergence | attach/media-change/mount/unmount/remove hint to coherent snapshot publication under bursts and loss |
| Property/capacity | retrieval latency, native calls, optional-media wake/spin-up effects, malformed/error behavior |
| Mount/unmount | request-to-effective-state distribution with policy/authentication excluded or separately measured |
| Removal | quiesce, flush stages, unmount, eject, and observation convergence individually; veto and surprise-removal paths |
| Scale | CPU/memory/handles with many mounts, virtual devices, namespaces, subscribers, and flapping media |
| Idle/power | observer wakeups/CPU/memory and removable-media power/spin effects |

Results report p50/p95/p99/max, completion/veto/failure counts, time per milestone, rescans, lost/coalesced hints, CPU, allocations, handles, and power effects. Runs disclose device/media/bridge, filesystem, effective mount/cache options, dirty bytes/files, flush stage, OS/build, policy/privilege, namespace/session, provider, power mode, and injected load. Mount speed is never presented as durability or safe-removal quality without the corresponding staged evidence.
