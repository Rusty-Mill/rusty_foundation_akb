# Capture privacy, security, and accessibility

Camera pixels and metadata are sensitive user/environment observations. Privacy applies from native capture through buffers, previews, analysis, encoding, diagnostics, transport, persistence, and deletion.

**RM-CAPTURE-PRIVACY-0001:** Capture MUST be secure-by-default: no background activation, hidden preview, remote delegation, recording, upload, or persistence without separately declared purpose and authority.

**RM-CAPTURE-PRIVACY-0002:** Platform privacy indicators and hardware shutters MUST NOT be suppressed, spoofed, or treated as optional product chrome. Indicator/shutter inconsistency invalidates or suspends capture.

**RM-CAPTURE-PRIVACY-0003:** Frames and sensitive metadata MUST be excluded from ordinary logs, crash dumps, metrics labels, and diagnostic bundles; bounded pseudonymous session IDs are used instead.

**RM-CAPTURE-PRIVACY-0004:** Delegation MUST attenuate device, duration, format, metadata, transformation, destination, and retention authority. A frame handle crossing process/device boundaries uses explicit transfer and revocation semantics.

**RM-CAPTURE-PRIVACY-0005:** Virtual cameras, screen-derived cameras, remote cameras, and synthetic sources MUST disclose provenance; they MUST NOT impersonate trusted physical capture sources.

**RM-CAPTURE-ACCESS-0001:** Permission, device selection, preview state, start/stop, errors, interruptions, and recording/streaming state MUST have keyboard and assistive-technology paths and nonvisual indicators.

**RM-CAPTURE-ACCESS-0002:** Products MUST provide equivalent alternatives when camera use is not essential, and must not require visual framing feedback without an accessible guidance path.
