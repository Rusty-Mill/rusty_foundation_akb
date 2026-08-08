# Surface negotiation and presentation

Color negotiation composes with the graphics presentation service; it does not replace swap-chain/device/surface selection.

**RM-COLOR-SURFACE-0001:** A request MUST bind window/presentation-surface generation, content image description, rendering intent, required fidelity, acceptable formats/precision, alpha/composition, SDR/HDR policy, power/performance constraints, and degradation choices.

**RM-COLOR-SURFACE-0002:** The result MUST report selected buffer encoding/format, accepted content description, compositor interpretation, conversion ownership, rendering intent, target/preferred display evidence, headroom/reference-white assumptions, metadata path, and every substitution or unsupported dimension.

**RM-COLOR-SURFACE-0003:** Surface pixels and their image description commit atomically for one generation. A description MUST NOT be attached to pixels encoded under different semantics.

**RM-COLOR-SURFACE-0004:** Window migration, topology/mode/profile/headroom change, compositor restart, device loss, or surface recreation can invalidate the result. The renderer retains semantic content and creates a new generation; old buffers are not reinterpreted silently.

**RM-COLOR-SURFACE-0005:** SDR fallback, gamut reduction, precision reduction, metadata loss, compositor tone mapping, software conversion, and disabled HDR are named degradations. Protected content and direct scan-out are separate constraints and never inferred from color mode.

**RM-COLOR-SURFACE-0006:** Presentation acceptance is not proof that conversion occurred as requested or that the viewer saw a calibrated result. Evidence names the compositor/provider boundary.

See [ADR-0067](../../adr/0067-display-color-is-compositor-negotiation-not-appearance-proof.md).
