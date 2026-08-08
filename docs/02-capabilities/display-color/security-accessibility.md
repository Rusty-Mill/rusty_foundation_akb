# Security, privacy, and accessibility

**RM-COLOR-SECURITY-0001:** Basic presentation negotiation, detailed display/profile observation, profile byte access, external measurement, calibration installation, mode/brightness control, and direct display ownership use separate authorities.

**RM-COLOR-SECURITY-0002:** Profiles, EDID/descriptors, display identities, gamut/luminance fingerprints, topology, ambient sensors, user settings, content metadata, and screenshots are minimized and excluded from default telemetry. Diagnostics prefer categorical capabilities and ephemeral correlations.

**RM-COLOR-SECURITY-0003:** Malformed profiles, metadata, shaders/LUTs, driver/compositor reports, and extreme component values MUST NOT cause code execution, unbounded allocation/work, non-finite propagation, cross-content leakage, or persistent display reconfiguration.

**RM-COLOR-ACCESS-0001:** Color management MUST preserve user contrast, color-filter, inversion, reduced-transparency, brightness, and flash/safety policy. An application fidelity request never overrides accessibility/system safety settings silently.

**RM-COLOR-ACCESS-0002:** Meaning and controls MUST NOT rely on hue, saturation, luminance, HDR, or subtle gamut differences alone. SDR/low-gamut/high-contrast/monochrome alternatives preserve semantic information.

**RM-COLOR-ACCESS-0003:** HDR transitions, highlights, adaptation, and test patterns obey bounded luminance/flash policy with warning and consent where exposure could be uncomfortable or unsafe. Reduced-motion does not automatically define luminance safety.

**RM-COLOR-ACCESS-0004:** Visual calibration UI has keyboard/screen-reader operation, textual numeric/state alternatives, localization, zoom, and procedures that acknowledge when color-vision or instrument assistance is required.
