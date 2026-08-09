# Restricted preview and thumbnail generation

**RM-CONTENT-PREVIEW-0001:** Preview requests bind immutable subject, detected and allowed candidate profiles, desired representation and dimensions/duration/pages, interaction policy, fonts/codecs/external-resource policy, color/accessibility policy, provider, and resource budget.

**RM-CONTENT-PREVIEW-0002:** Preview providers run with restricted filesystem, network, process, device, credential, clipboard, activation, plugin, and persistence authority appropriate to hostile parsers; in-process parsing requires an explicit accepted risk profile.

**RM-CONTENT-PREVIEW-0003:** Previews are inert derived representations by default: no scripts, macros, active forms, embedded applications, external navigation/fetch, autoplay, device access, file mutation, shell integration, or credential prompts.

**RM-CONTENT-PREVIEW-0004:** A preview result binds source and provider generations, pages/frames/time/ranges rendered, substitutions and omissions, truncation, active content suppressed, external resources blocked, color/font behavior, and semantic limitations.

**RM-CONTENT-PREVIEW-0005:** Thumbnail and failure caches are partitioned by principal/tenant and include source generation/digest, exact provider/profile/policy, requested geometry, security database generation where relevant, expiry, and failure class.

**RM-CONTENT-PREVIEW-0006:** Preview output remains untrusted encoded or pixel/text content with size, decode, color-profile, font, markup, accessibility, and display-safety validation before presentation.

**RM-CONTENT-PREVIEW-0007:** Cancellation, provider crash/hang, resource exhaustion, unsupported content, password needs, and partial render produce accessible bounded states and clean restricted-process/staging resources.
