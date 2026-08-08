# Cursor and audio

## Cursor

Cursor policy is `hidden`, `embedded`, or `separate_metadata`. Separate metadata includes shape revision, hotspot, source coordinate space, position, visibility, scale, timestamp, and applicability interval.

**RM-SCREEN-CAPTURE-AUX-0001:** Cursor mode MUST be negotiated and reported; a provider MUST NOT silently burn a cursor into frames that were accepted as cursor-free.

**RM-SCREEN-CAPTURE-AUX-0002:** Separate cursor metadata MUST be generation- and time-correlated with frames and MUST make missing, stale, outside-source, hidden, and unsupported states distinct.

**RM-SCREEN-CAPTURE-AUX-0003:** Cursor shape and position are sensitive interaction data and MUST follow frame-equivalent disclosure, telemetry, retention, and delegation policy.

## Audio

Desktop/system or application audio is a separately selected stream with exact PCM format, channel layout, source scope, sample clock, timestamps, discontinuities, and correlation to captured frames.

**RM-SCREEN-CAPTURE-AUX-0004:** Screen pixels MUST NOT imply authority for system, application, microphone, communications, or protected audio. Each selected audio class requires explicit native and Rusty Mill authority.

**RM-SCREEN-CAPTURE-AUX-0005:** Application-audio scope, current-process inclusion/exclusion, mixing, volume effects, protected-content behavior, and unsupported isolation MUST be explicit.

**RM-SCREEN-CAPTURE-AUX-0006:** Audio/video correlation MUST declare clock mapping, skew uncertainty, discontinuity, buffering, and drift-correction ownership; a shared delivery callback is not proof of a shared clock.

**RM-SCREEN-CAPTURE-AUX-0007:** Feedback and echo risk from local preview, conferencing, or remote playback MUST be surfaced to the composing service; the capture capability MUST NOT silently suppress or process audio.

Camera overlay, microphone capture, encoding, muxing, recording, and conferencing remain separately negotiated compositions.
