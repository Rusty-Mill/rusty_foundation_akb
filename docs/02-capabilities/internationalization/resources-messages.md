# Resource and typed-message service

| Field | Value |
|---|---|
| Status | Draft platform service 0.1.0 |

**RM-I18N-MESSAGE-0001:** A resource bundle declares immutable bundle/domain/version/digest, available locale manifests, schema/compiler version, fallback policy, translator metadata, and signature/provenance where resources cross a trust boundary.

**RM-I18N-MESSAGE-0002:** Messages use stable semantic identifiers and typed argument schemas. Argument names, types, select/plural categories, formatting skeletons, sensitivity, and rich-semantic spans are validated at build/package time where possible and at runtime at trust boundaries.

**RM-I18N-MESSAGE-0003:** A complete user-facing sentence/phrase is one translatable message. Code does not concatenate grammatical fragments, infer word order, or pluralize by appending suffixes.

**RM-I18N-MESSAGE-0004:** Resolution binds exact locale context and bundle generation and reports requested key, resolved locale/fallback step, message version, arguments, and typed missing/invalid/format failure without exposing sensitive values.

**RM-I18N-MESSAGE-0005:** Plural/select behavior uses the exact cardinal/ordinal rules and visible numeric value under the context data version. `one` is a grammatical category, not universally numeric one.

**RM-I18N-MESSAGE-0006:** Rich messages produce semantic spans with allowlisted roles (emphasis, link target identity, code, user data) rather than executable markup. Translators cannot inject commands, URLs, privileged accessibility roles, format specifiers, or bidi overrides outside schema policy.

**RM-I18N-MESSAGE-0007:** Missing/invalid translations follow explicit release and runtime policy: fail build, designated fallback with telemetry-safe diagnostic, or developer marker. Empty translation is distinct from missing.

**RM-I18N-MESSAGE-0008:** Pseudolocales exercise expansion, contraction, diacritics, bidi mirroring/isolation, long words, non-Latin digits, and untranslatable-token preservation without being shipped as normal user locales accidentally.

**RM-I18N-MESSAGE-0009:** Hot resource updates are authenticated/versioned, publish atomically, create a new bundle generation/context, and cannot reinterpret in-flight message identifiers or schemas silently.

