# Display color observation

`rm.color.display-observer` extends windowing topology with a revisioned color-state projection. It does not expose authority to configure the display.

**RM-COLOR-DISPLAY-0001:** A snapshot MUST bind windowing display identity/generation, provider and observation revision, active mode, composition mode, preferred/current image description, supported encodings/precisions, SDR reference-white behavior, potential/current dynamic-range headroom, and field provenance.

**RM-COLOR-DISPLAY-0002:** Reported/estimated/measured minimum, sustained/full-frame/peak luminance, gamut/color volume, bit depth, local dimming, ambient adaptation, and HDR/WCG/automatic-management state MUST remain distinct with units, validity, age, and uncertainty.

**RM-COLOR-DISPLAY-0003:** Hardware descriptor, OS override, installed profile, user calibration, compositor mode, application query, and external measurement are separate evidence sources with precedence and conflict reporting.

**RM-COLOR-DISPLAY-0004:** Potential support, enabled state, current availability, surface eligibility, chosen presentation path, and observed output MUST NOT be collapsed into `supports_hdr` or `is_color_managed`.

**RM-COLOR-DISPLAY-0005:** A window spanning displays has an explicit provider-selected target/strategy and confidence. The model MUST NOT invent one color volume that claims simultaneous exact appearance across heterogeneous displays.

**RM-COLOR-DISPLAY-0006:** EDID/vendor/product/serial, installed-profile identity, topology, luminance/gamut fingerprint, ambient sensors, and user settings are privacy-sensitive and minimized by authority and telemetry policy.
