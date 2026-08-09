# Windowing cross-cutting review

| Field | Value |
|---|---|
| Review status | Pass |
| Reviewed | 2026-08-08 |
| Review frontier | Windowing 0.1.1; architecture model 1.83.0 |
| Accountable owner | Windowing capability owner |
| Open blocking findings | None for planning eligibility; native/provider and product evidence remain required |

| Dimension | Exact requirements | Planned evidence | Findings, limits, or non-applicability |
|---|---|---|---|
| Security/privacy | WINDOW-0011–0012, DISPLAY-0001/0006, SURFACE-0006–0007 | sensitive-title and topology canaries, provenance/policy cases, capture-protection truthfulness, unsafe native-handle review | capture exclusion is best-effort/provider-specific; display identity is not authority; native escape remains separately unsafe |
| Performance | BENCH-0001–0007, EVENT-0002–0004 | semantic scenarios for creation, resize, scale traversal, topology storms, churn, and surface regeneration | no native-performance or fixed budget claim exists before provider runs |
| Accessibility | WINDOW-0006/0011, committed focus/visibility/state observations | native title/role/root exposure, keyboard chrome, focus transitions, close/fullscreen announcements, high-contrast/reduced-motion integration | application accessibility-tree content remains outside windowing but consumer obligations persist |
| Internationalization | WINDOW-0011 and logical coordinate model | Unicode title conversion/loss/truncation, bidi title corpus, locale-independent identities/geometry, localized native error review | windowing carries semantic text but does not own translation, shaping, or widget layout |
| Observability | committed revisions, event gaps/coalescing, topology/surface generations, provider evidence | structured snapshot/event/result schemas, native trace correlation, redaction/cardinality/loss review | logs are evidence and cannot prove visible presentation, focus, accessibility, or security |
| Operations | lifecycle, hot-plug/remote/headless, provider loss, shutdown/resource release | failure injection at creation/destruction/callback/surface phases, topology reconciliation, long churn, session transition recovery | exact compositor/session support frontier and operator diagnostics remain trial-bound |

**RM-WINDOWING-QUALITY-0001:** Every trial MUST bind each quality dimension to exact platform/provider methods, owners, findings, and affected claims.

**RM-WINDOWING-QUALITY-0002:** Windowing evidence MUST keep native-window state, compositor observation, graphics presentation, input focus, accessibility exposure, and capture protection distinct.

**RM-WINDOWING-QUALITY-0003:** Provider-specific native chrome, title, topology, placement, activation, transparency, and capture behavior MUST be tested without promoting availability to a portable guarantee.

