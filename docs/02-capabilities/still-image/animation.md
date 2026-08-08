# Animation and multi-image containers

Frame decode yields frame pixels and control metadata. `rm.image.animation-compositor` is a separate stateful service that produces canvas revisions.

**RM-IMAGE-ANIMATION-0001:** An animation descriptor MUST state canvas, frame count or bounded unknown, loop semantics, default/background policy, timing unit/rules, frame rectangles, blend/source operation, disposal, dependencies, and metadata provenance.

**RM-IMAGE-ANIMATION-0002:** Encoded duration, normalized effective duration, presentation deadline, decode readiness, and actual display time remain distinct. Zero, negative/invalid, extreme, and sub-resolution durations follow declared format/provider policy.

**RM-IMAGE-ANIMATION-0003:** Compositing uses checked clipped geometry and exact blend/disposal order. Previous-canvas restoration has a bounded snapshot/copy strategy; frames outside the canvas or with invalid dependencies fail safely.

**RM-IMAGE-ANIMATION-0004:** Random access declares required keyframe/dependency replay and cost. Seeking MUST NOT pretend independent-frame access where prior disposal/blend state is required.

**RM-IMAGE-ANIMATION-0005:** Playback has explicit frame-drop/repeat/catch-up, pause/background, reduced-motion, power, cancellation, and memory policy. Decode threads never own UI timing.

**RM-IMAGE-ANIMATION-0006:** Multi-page TIFF, icon variants, burst/sequence items, stereoscopic/depth/auxiliary images, and animation are separate container relationships; one is not inferred from multiple frames.
