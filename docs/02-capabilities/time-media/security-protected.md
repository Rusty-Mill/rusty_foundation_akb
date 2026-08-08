# Security, privacy, and protected content

**RM-MEDIA-SECURITY-0001:** Source/network/file authority, external references, track metadata, clear decode, hardware codec use, protected decode/presentation, capture, recording, export, license acquisition, and persistent cache use separate grants and enforcement.

**RM-MEDIA-SECURITY-0002:** Containers, codecs, subtitles, fonts/images, metadata, indexes, manifests, side data, profiles, and device/provider responses are untrusted and bounded. Remote/plugin media defaults to isolated parsing/codec providers where available.

**RM-MEDIA-SECURITY-0003:** Provider selection records framework/codec/plugin origin, version/build/signature/update source, process/sandbox boundary, hardware/driver, supported subset, crash history, and supply-chain evidence. Installed codec presence is not selection authority.

**RM-MEDIA-PRIVACY-0001:** Titles, paths/URLs, viewing history/position, track/language/accessibility choices, content identifiers/hashes, metadata, license/account/device IDs, subtitles/transcripts, frames/samples, and thumbnails are sensitive and excluded from default telemetry.

**RM-MEDIA-PROTECTED-0001:** Encryption signaling, key acquisition, license policy, secure decode, protected memory, protected presentation, output restrictions, screenshot/capture policy, and attestation are separate capabilities. Base demux/decode MUST NOT expose keys or claim a secure path.

**RM-MEDIA-PROTECTED-0002:** Protected-path selection binds exact source/license/device/display/session generations and reports every fallback/nonclaim. Clear software fallback is prohibited unless content policy explicitly permits it.

**RM-MEDIA-SECURITY-0004:** Cancellation, seek, track switch, provider crash, device loss, suspend, logout, and shutdown release sensitive resources by owner lifetime; callbacks are not relied upon to erase secrets or revoke remote licenses.
