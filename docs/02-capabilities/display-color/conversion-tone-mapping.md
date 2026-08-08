# Conversion, gamut mapping, and tone mapping

`rm.color.transform` converts bounded image/color values between immutable descriptions under an explicit plan.

**RM-COLOR-TRANSFORM-0001:** A plan MUST bind source/destination descriptions, rendering intent, chromatic adaptation, black-point handling, gamut-map/tone-map policy, reference-white mapping, alpha/order policy, precision, dithering, metadata policy, engine/version, and hardware/software provenance.

**RM-COLOR-TRANSFORM-0002:** Decode transfer, matrix/range conversion, chromatic adaptation, gamut mapping, tone mapping, alpha composition, output encoding, and quantization are ordered stages. A provider MUST disclose fused or omitted stages without changing semantics.

**RM-COLOR-TRANSFORM-0003:** Relative and absolute luminance systems remain distinguishable. SDR white, diffuse/reference white, paper white, mastering peak, content peak, display peak, and current headroom are not interchangeable.

**RM-COLOR-TRANSFORM-0004:** Static metadata, dynamic metadata, scene analysis, user brightness, ambient adaptation, power/thermal policy, and accessibility settings are separate inputs. Missing metadata follows a declared conservative policy, never a fabricated mastering environment.

**RM-COLOR-TRANSFORM-0005:** Conversion reports clipping, out-of-gamut mapping, over/under-range handling, precision loss, metadata preservation/drop, and output bounds. Deterministic claims bind the exact engine and algorithm version.

**RM-COLOR-TRANSFORM-0006:** CPU/GPU transforms are cancellation-aware and bounded by pixels, profile/metadata size, allocation, compilation, time, and in-flight work. Untrusted profiles/metadata are validated outside restricted realtime/UI paths.
