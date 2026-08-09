# Trial evidence plan

Evidence is planned before code so the trial cannot redefine success after observing results.

| Evidence class | Minimum binding |
|---|---|
| Semantics | Capability requirements to stable assertions and executable cases |
| Variance | OS/version/provider/feature matrix, discovery, degradation, and typed failure |
| Performance | Stable benchmark scenario, workload, environment, baselines, samples, uncertainty, and raw results |
| Safety | Threat model, authority boundaries, unsafe/FFI invariants, negative/adversarial tests |
| Inclusive quality | Accessibility and i18n applicability, test method, findings, limitations |
| Operations | Logs/metrics/traces, loss/redaction, failure injection, cleanup and recovery |
| Provenance | Source revision, lock state, toolchain, runner, configuration, artifacts, attestations |

**RM-TRIAL-EVIDENCE-0001:** Every claimed result MUST link to the exact assertion, case or benchmark scenario, attempt/run identity, environment, inputs, and artifacts that support it.

**RM-TRIAL-EVIDENCE-0002:** Failed, cancelled, timed-out, excluded, and invalid attempts MUST remain visible and MUST NOT be removed from aggregates without recorded rationale.

**RM-TRIAL-EVIDENCE-0003:** Performance evidence MUST accompany semantic correctness evidence and MUST NOT generalize beyond comparable semantics and environments.

**RM-TRIAL-EVIDENCE-0004:** A missing platform/provider result is `unknown`, not portable success; a supported variance must be recorded as contract input rather than normalized away.

