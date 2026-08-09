# Native-provider trial matrix

The matrix compares capability semantics, not API-name symmetry. Exact providers remain an RFC/trial choice.

| Dimension | Windows | Linux | macOS | Required interpretation |
|---|---|---|---|---|
| OS/version frontier | declared | declared | declared | evidence expires outside frontier |
| Native provider/API generation | declared | declared | declared | mapping, not capability identity |
| Discovery and availability | measured | measured | measured | unsupported/degraded is typed |
| Authority and privilege | reviewed | reviewed | reviewed | native enforcement point named |
| Async and sync behavior | exercised | exercised | exercised | async-first and sync-complete claims separated |
| Cancellation/resource lifetime | exercised | exercised | exercised | terminal state and cleanup observable |
| Error/variance mapping | recorded | recorded | recorded | native evidence retained |
| Conformance assertions | results | results | results | no missing-as-pass |
| Benchmark scenarios | runs | runs | runs | comparable semantics required |
| Cross-cutting findings | findings | findings | findings | applicability and limitations explicit |

**RM-TRIAL-PROVIDER-0001:** Platform rows MUST identify exact tested versions and provider generations; family names alone are insufficient evidence.

**RM-TRIAL-PROVIDER-0002:** A provider MAY be excluded only with reviewed rationale and a consequence for the trial's portability claims.

**RM-TRIAL-PROVIDER-0003:** Provider-specific optimizations MUST preserve the named behavioral contract or be recorded as variance requiring contract review.

**RM-TRIAL-PROVIDER-0004:** The trial MUST preserve native error, timing, authority, and lifecycle evidence needed to diagnose abstraction loss.

