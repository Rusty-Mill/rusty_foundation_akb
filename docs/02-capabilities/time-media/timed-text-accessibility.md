# Timed text, chapters, and accessibility

**RM-MEDIA-TEXT-0001:** A timed-text cue MUST carry track/source generation, cue identity/revision, start/end and exact time domain, language/script/direction, role/kind, payload format, region/style constraints, ordering, and provenance/validation.

**RM-MEDIA-TEXT-0002:** Subtitle, caption, SDH, forced narrative, audio-description cue/track, chapter, transcript, karaoke, metadata, and interactive overlay are distinct roles. User preference and product policy select them explicitly.

**RM-MEDIA-TEXT-0003:** Text payloads are untrusted and bounded by bytes, cues, nesting, styles, regions, glyphs, images/fonts, updates, and active duration. Scripts, network loads, arbitrary markup, and unsafe font/image references are prohibited unless a separate sandboxed contract exists.

**RM-MEDIA-TEXT-0004:** Cue rendering uses the text/i18n/color/accessibility foundations for Unicode, bidi, language, line breaking, safe areas, contrast, user font/size/color/background preferences, and semantic output. Native styling cannot override accessibility requirements silently.

**RM-MEDIA-ACCESS-0001:** Playback controls are keyboard/switch/screen-reader operable with labeled state, position/duration/live edge, buffering/seek/errors, track/language selection, rate/volume/mute, captions/audio description, and full-screen/PiP state where selected.

**RM-MEDIA-ACCESS-0002:** Reduced-motion, flash/luminance safety, color alternatives, caption/audio-description preference, mono/downmix, hearing-device routing, and cognitive controls are explicit policy inputs. Content essential to understanding has an accessible alternative.

**RM-MEDIA-ACCESS-0003:** Transcript/search/navigation maps semantic text positions and chapters to exact media ranges without treating approximate cue timing as sample-accurate identity.
