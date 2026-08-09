# IPC byte-pipe cross-cutting review

| Field | Value |
|---|---|
| Review status | Pass |
| Reviewed | 2026-08-08 |
| Review frontier | IPC foundations 0.1.1; architecture model 1.86.0 |
| Accountable owner | IPC capability owner |
| Open blocking findings | None for planning eligibility; provider, runtime, process-integration, accessibility, and performance evidence remain required |

| Dimension | Exact requirements | Planned evidence | Findings, limits, or non-applicability |
|---|---|---|---|
| Security/privacy | PIPE-0001–0002/0005/0009/0014–0015 | endpoint direction/authority inventories, concurrent process-inheritance canaries, broken-peer signal containment, transfer-denial and diagnostic content scans | anonymous/local is not authenticated or confidential; stream contents and native identifiers are sensitive; transferred endpoints delegate authority |
| Performance | BENCH-0001–0009, PIPE-0003/0006–0013 | equivalent create/transfer/concurrency/async/redirection/terminal scenarios with byte-correctness, leak, bounded-memory, and Q-level gates | no fixed capacity, fairness, atomicity, numeric budget, or native-performance claim exists before representative runs |
| Accessibility | consumer progress/cancel/error/status obligations | assistive-technology and keyboard review of selecting-product stream/capture surfaces, stable EOF/broken-peer/cancel vocabulary, bounded progress feedback | byte-pipe owns no UI or text semantics; products still owe accessible status, control, and recovery surfaces |
| Internationalization | byte transparency and diagnostic non-capture | arbitrary byte corpus, locale-independent status/error mapping, bidi/control-safe labels for endpoint diagnostics, explicit text-adapter tests outside this domain | bytes have no encoding, normalization, newline, or locale semantics; text conversion is an explicit adapter responsibility |
| Observability | PIPE-0003–0008/0012–0015 | structured byte-count/state/terminal records, endpoint correlations, queue/saturation/loss metrics, content-redaction and cardinality review, native trace correlation | telemetry cannot prove payload meaning, confidentiality, fairness, atomicity beyond scope, peer identity, or final process consumption |
| Operations | endpoint lifecycle, EOF reference accounting, backpressure, Q1 saturation, process/pipeline cleanup | failure/cancel/close injection, duplicate/inheritance inventories, resource exhaustion, long churn, worker saturation, pipeline reconciliation, shutdown drills | exact capacity tuning, worker budgets, spill/capture policy, quotas, runtime integration, and operator runbooks remain product/trial inputs |

**RM-IPC-QUALITY-0001:** Every trial MUST bind all quality dimensions to exact provider mechanisms, owners, methods, findings, and affected claims.

**RM-IPC-QUALITY-0002:** Write acceptance, buffer residency, reader consumption, EOF, broken peer, cancellation, endpoint close, and process/pipeline reconciliation MUST remain distinct evidence boundaries.

**RM-IPC-QUALITY-0003:** Provider-specific capacity, atomicity, readiness/completion, signal, and inheritance behavior MUST be tested without promoting availability to a portable guarantee.
