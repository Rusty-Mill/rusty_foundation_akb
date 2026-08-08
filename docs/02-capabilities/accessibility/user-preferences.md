# `rm.accessibility.user-preferences`

| Field | Value |
|---|---|
| Status | Draft |
| Contract version | 0.1.0 |

**RM-ACCESSIBILITY-PREF-0001:** A preference snapshot has revision/provenance and independently reports known/unknown high contrast, forced colors, reduced motion/transparency, increased contrast, text/cursor size, animation/blink, screen-reader/assistive-service activity where safely exposed, captions, audio description, mono audio, and input-assistance settings.

**RM-ACCESSIBILITY-PREF-0002:** Preferences are user intent inputs, not proof of disability, identity, diagnosis, or assistive-technology use. Applications apply relevant outcomes without profiling the user.

**RM-ACCESSIBILITY-PREF-0003:** Change subscription returns an initial snapshot plus increasing revisions or an explicit gap/resnapshot. Changes coordinate with theme/layout/rendering revisions without requiring application restart.

**RM-ACCESSIBILITY-PREF-0004:** Unknown/unavailable platform settings follow product-safe defaults. Providers do not invent equivalence between unrelated native settings.

**RM-ACCESSIBILITY-PREF-0005:** Reading preferences and assistive-service activity follows least-detail privacy policy and is excluded from default analytics/fingerprinting.

**RM-ACCESSIBILITY-PREF-0006:** A preference may affect presentation/pacing but does not mutate semantic domain truth. For example, reduced motion changes transitions, not logical state; forced colors preserve roles/actions, not application color identity.

