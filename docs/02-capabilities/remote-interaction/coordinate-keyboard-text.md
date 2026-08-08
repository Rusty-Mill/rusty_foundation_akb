# Coordinate, keyboard, and text semantics

**RM-REMOTE-INTERACTION-MAPPING-0001:** Absolute pointing MUST bind the event to a capture stream/source generation, logical coordinate extent, crop/scale/rotation revision, and clipping policy; desktop-global pixels are not the portable model.

**RM-REMOTE-INTERACTION-MAPPING-0002:** Relative motion MUST preserve units, acceleration ownership, precision, coalescing, device generation, and ordering with buttons and scrolling.

**RM-REMOTE-INTERACTION-MAPPING-0003:** Touch and pen MUST model contact/tool identity, lifecycle, coordinates, pressure/tilt where supported, frame grouping, cancellation, maximum contacts, and topology-change termination.

**RM-REMOTE-INTERACTION-MAPPING-0004:** Keyboard injection MUST distinguish physical usage/scan intent, logical key intent, modifier/lock state, repeat, keymap/layout generation, and text intent. No universal key-code round trip is claimed.

**RM-REMOTE-INTERACTION-MAPPING-0005:** Text insertion and IME/composition control are separate from keyboard emulation. A provider MUST NOT synthesize keystrokes for text when that changes shortcuts, layout, dead-key, security, or accessibility semantics without explicit degradation acceptance.

**RM-REMOTE-INTERACTION-MAPPING-0006:** Gesture recognition belongs to the receiving system unless a separately selected semantic gesture contract identifies recognition ownership and fallback.

**RM-REMOTE-INTERACTION-MAPPING-0007:** Capture resize, crop, display migration, keymap/layout, focus, scale, or session changes MUST retire incompatible queued events and active contacts before a new mapping revision becomes usable.

Remote display geometry may lag local topology. The service reports this uncertainty and rejects coordinates against obsolete observation revisions rather than guessing.
