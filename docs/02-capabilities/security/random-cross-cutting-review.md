# Secure-random cross-cutting review

| Field | Value |
|---|---|
| Review status | Pass |
| Reviewed | 2026-08-08 |
| Review frontier | `rm.security.random` 0.1.0; architecture model 1.89.0 |
| Accountable owner | Secure-random capability owner |
| Open blocking findings | None for capability planning eligibility; provider, cryptographic, platform-lifecycle, and implementation evidence remain required |

| Dimension | Exact requirements | Planned evidence | Findings, limits, or non-applicability |
|---|---|---|---|
| Security/privacy | RANDOM-0001–0003/0006/0009–0012 | exact-source/provenance inspection, fail/partial-fault injection, no-fallback oracle, output/intermediate canary scans, certification-scope review | statistical appearance cannot prove unpredictability; output is secret-quality material; provider/module/configuration boundary matters |
| Performance | RANDOM-BENCH-0001–0005, RANDOM-0004–0008 | equivalent warm/cold/concurrent/failure scenarios with exact-fill, readiness, no-output-artifact, and fail-closed gates | no latency/throughput budget or native-performance claim exists; security semantics cannot be disabled for comparison |
| Accessibility | readiness/failure/cancellation consumer surfaces | keyboard and assistive-technology review of selecting-product startup/error/recovery prompts, stable nonsecret statuses, bounded cancellable readiness feedback | base fill normally has no UI; product interaction must not expose output or misleadingly offer insecure fallback |
| Internationalization | binary output and sanitized diagnostics | locale-independent error/status mapping, bidi/control-safe provider labels, localized product errors without source/output mutation | bytes have no text/locale semantics; encoding/random-string/password generation are separate consumers |
| Observability | RANDOM-0009/0011–0012 | bounded provider/readiness/failure counters, sanitized causal traces, redaction/cardinality/recursion review, evidence link validation | no bytes, hashes, checksums, prefixes, uniqueness samples, compressibility, or output-derived fingerprint may enter telemetry |
| Operations | RANDOM-0006/0008/0010–0012 | startup/source outage, fork, VM/container clone/snapshot, suspend/resume, reinitialization, provider update, restricted/sandbox context, recovery drill | exact lifecycle support, readiness policy, module validation mode, health monitoring, incident response, and operator runbook remain deployment inputs |

**RM-SECURITY-RANDOM-QUALITY-0001:** Every trial MUST bind each quality dimension to exact provider/module/configuration/platform methods, owners, findings, and affected claims.

**RM-SECURITY-RANDOM-QUALITY-0002:** Source readiness, native fill, public success, caller use, statistical diagnostics, module validation, and product security claims MUST remain separate evidence boundaries.

**RM-SECURITY-RANDOM-QUALITY-0003:** Performance, accessibility, internationalization, and observability mechanisms MUST NOT inspect, retain, transform, or derive fingerprints from random output.
