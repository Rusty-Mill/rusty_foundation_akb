# `rm.windowing.display-topology`

| Field | Value |
|---|---|
| Status | Draft |
| Contract version | 0.1.0 |

**RM-WINDOWING-DISPLAY-0001:** A topology snapshot has a monotonic revision and stable-within-session opaque display identities; identities are not hardware serial numbers and must not be used for authorization.

**RM-WINDOWING-DISPLAY-0002:** Each display record distinguishes available logical bounds, work area, pixel mode, transform/orientation, effective scale, refresh information, color metadata, primary status, and whether each field is known, estimated, or unavailable.

**RM-WINDOWING-DISPLAY-0003:** Enumeration and change delivery are race-safe: a subscriber receives an initial snapshot plus later increasing revisions or a gap indication requiring resnapshot.

**RM-WINDOWING-DISPLAY-0004:** Mirroring, virtual displays, remote sessions, headless outputs, hot unplug, mode changes, and mixed-scale layouts are modeled without assuming a rectangular global desktop.

**RM-WINDOWING-DISPLAY-0005:** Display removal does not invalidate an already emitted snapshot value, but references cannot be used for new placement after the provider reports removal.

**RM-WINDOWING-DISPLAY-0006:** EDID, physical dimensions, device names, and topology details are privacy-sensitive optional evidence and require declared authority where the platform protects them.

