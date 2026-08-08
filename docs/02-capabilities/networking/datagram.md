# Datagrams

## Capability identity

`rm.network.datagram` sends and receives discrete transport messages with explicit local/peer and ancillary metadata.

**RM-NETWORK-DATAGRAM-0001:** Each successful receive represents one datagram and reports original/truncated length, source/destination observations where available, interface/path metadata, and provider flags.

**RM-NETWORK-DATAGRAM-0002:** Datagram delivery may be lost, duplicated, reordered, corrupted below verified checks, or rejected. Send acceptance is not peer receipt.

**RM-NETWORK-DATAGRAM-0003:** Oversize behavior is explicit: reject-before-send, fragmentation-permitted, provider segmentation, or accepted-with-risk. Receive truncation is never reported as a complete payload.

**RM-NETWORK-DATAGRAM-0004:** Connected datagram mode restricts default peer and may filter errors/traffic, but does not create reliable stream semantics or authenticate the peer.

**RM-NETWORK-DATAGRAM-0005:** Batch send/receive reports per-message outcomes and exact progress. Partial batch completion never implies partial datagram creation.

**RM-NETWORK-DATAGRAM-0006:** Multicast/broadcast, packet metadata, raw sockets, and privileged interface controls are separate optional capabilities with independent authority and platform evidence.

