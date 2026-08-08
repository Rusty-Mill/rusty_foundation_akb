# Audio device topology

## Endpoint model

`rm.audio.device-observer` enumerates render and capture endpoints and publishes revisioned snapshots. An endpoint descriptor contains a provider-scoped identity, generation, direction set, availability, transport class when safely knowable, nominal formats, channel capabilities, latency ranges, and privacy-relevant properties. It does not convey permission to open the endpoint.

**RM-AUDIO-DEVICE-0001:** Device snapshots MUST distinguish stable-within-provider identity, current generation, direction, availability, and observation revision.

**RM-AUDIO-DEVICE-0002:** A provider MUST invalidate or advance the generation when an endpoint disappears, is replaced, or changes in a way that invalidates an open stream contract.

**RM-AUDIO-DEVICE-0003:** The system default is a revisioned routing-policy selection, not a stable device identity. Consumers MUST NOT persist “default” as if it named a physical endpoint.

**RM-AUDIO-DEVICE-0004:** Enumeration MUST NOT open capture hardware, prompt for capture permission, or activate an endpoint merely to discover ordinary metadata.

**RM-AUDIO-DEVICE-0005:** Device names, transport hints, and topology metadata are untrusted, potentially sensitive display data and MUST NOT be used as authority or canonical identity.

## Change model

Events identify the old and new snapshot revisions and classify addition, removal, default-route change, metadata change, availability change, and invalidation. Overflow or lost change delivery forces full reconciliation. A stream retains its selected generation until explicitly migrated or invalidated.

Aggregate, virtual, Bluetooth, network, and software endpoints may have clocks or latency behavior unlike built-in hardware. Providers disclose these characteristics instead of inventing a physical-device equivalence.
