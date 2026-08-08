# Storage durability and failure

Storage removal composes existing [filesystem durability](../filesystem/durability-model.md); it does not redefine it. Evidence distinguishes application-buffer transfer, OS page-cache writeback, filesystem metadata commit, device-cache flush, bridge/controller cache, and stable media where knowable.

**RM-STORAGE-DURABILITY-0001:** A removal plan MUST state the requested durability stage for each dirty resource and preserve unsupported/unknown stages.

**RM-STORAGE-DURABILITY-0002:** Flush success MUST NOT be represented as stronger than the underlying filesystem, device, transport, power-loss, and provider guarantees.

**RM-STORAGE-DURABILITY-0003:** The service MUST distinguish flush failure, busy/veto, permission/policy denial, unsupported eject, surprise removal, media error, device reset, and observation uncertainty.

**RM-STORAGE-DURABILITY-0004:** After surprise removal or ambiguous failure, open resources and mounts become suspect or invalidated; recovery requires generation-aware reconciliation and domain-specific integrity checks.

**RM-STORAGE-DURABILITY-0005:** Retrying mount, unmount, or eject MUST declare idempotency against the current generation and MUST NOT apply a stale request to newly inserted media.

Filesystem checking/repair, journal replay control, partition recovery, undelete, secure erase, and data salvage remain explicit specialized services. A provider cannot advertise them as ordinary recovery from an unmount/eject failure.
