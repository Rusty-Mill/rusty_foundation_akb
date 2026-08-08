# Profiles, calibration, and measurement

A profile characterizes a device or working space. Calibration changes a device toward a target. Measurement observes behavior. These operations and claims are independent.

**RM-COLOR-PROFILE-0001:** Profile discovery MUST expose scope, device/display generation binding, profile class/version/digest, source, install/selection time, active/inactive state, validation, engine compatibility, and authority—not just a file path or friendly name.

**RM-COLOR-PROFILE-0002:** Factory data, generic/vendor profile, OS override, user characterization, calibration curves/LUTs, application transform, and hardware state remain layered evidence. Double-application is a conformance failure.

**RM-COLOR-PROFILE-0003:** Installing/selecting profiles, changing calibration LUTs, brightness, white point, display mode, or HDR settings are privileged configuration services outside observation and ordinary presentation.

**RM-COLOR-MEASURE-0001:** A measurement record MUST bind instrument identity/calibration, geometry, patches, ambient/viewing conditions, display warmup/state, mode/settings, timestamps, uncertainty, procedure/version, and raw/derived result provenance.

**RM-COLOR-MEASURE-0002:** “Calibrated,” “accurate,” conformance-class, gamut coverage, contrast, white-point, and luminance claims require stated tolerance, sampling, uncertainty, and current configuration. Profile installation alone proves none of them.

**RM-COLOR-PROFILE-0004:** Profile/parser/transform artifacts are untrusted inputs with size/complexity bounds, recursion limits, digest provenance, quarantine, and reproducible failure reporting.
