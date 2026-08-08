# Process foundation conformance specification

**Status:** Draft

## Evidence scope

Reports bind contract/provider/artifact versions to OS/kernel, architecture, runtime/parser convention, sandbox/service context, filesystem context, and suite version. Sensitive arguments and environment values are replaced with typed canary identifiers, never recorded.

## Assertions

| ID | Requirements | Method |
|---|---|---|
| PROC-SPAWN-001 | 0001, 0002 | Launch an argument-vector probe across empty, whitespace, quote, slash, Unicode/native, and limit cases; prove named convention or reject |
| PROC-SPAWN-002 | 0003, 0015 | Exercise empty/snapshot/overlay environment, case and duplicate rules, size limits, and canary redaction |
| PROC-SPAWN-003 | 0004, 0013 | Race concurrent launches while cycling inheritable resources; child inventories must equal exact allowlists |
| PROC-SPAWN-004 | 0005 | Verify child working directory without parent mutation and race directory replacement where applicable |
| PROC-SPAWN-005 | 0006, 0009 | Inject preparation, creation, pre-image, immediate-exit, crash/signal/exception, and readiness failures |
| PROC-SPAWN-006 | 0007, 0008 | Stress identifier reuse, concurrent waiters, repeated queries, reaping, and close races |
| PROC-SPAWN-007 | 0010, 0011 | Drop/cancel at every launch milestone; verify child ownership and reconcile indeterminate creation |
| PROC-SPAWN-008 | 0012 | Verify direct sync paths and native async notification without hidden runtime creation |
| PROC-SPAWN-009 | 0014, 0015 | Validate error mapping and scan logs/traces/metrics/crash/report sinks for canaries |
| PROC-SPAWN-010 | 0016 | Verify base spawn does not claim sandbox, descendant, service, or restricted-identity guarantees |

## Control and supervision assertions

| ID | Assertion |
|---|---|
| PROC-CONTROL-001 | PID reuse and stale numeric identifiers cannot redirect an action from the owned child object |
| PROC-CONTROL-002 | Accepted control dispatch is never reported as terminal completion without wait/status evidence |
| PROC-CONTROL-003 | Cooperative and interrupt actions never silently become forced termination |
| PROC-SUPERVISE-001 | Descendant creation/exit races match the declared dynamic membership semantics |
| PROC-SUPERVISE-002 | Breakaway, nesting, supervisor failure, and child-created groups/jobs match the claimed P0–P3 level |
| PROC-SUPERVISE-003 | Root exit, known-set exit, and contained-set empty are distinguished |
| PROC-SUPERVISE-004 | Phased shutdown reports each dispatch, timeout, escalation, and terminal reconciliation outcome |

## Executable-resolution assertions

| ID | Assertion |
|---|---|
| PROC-RESOLVE-001 | Changing ambient current directory, `PATH`, or platform search settings cannot affect a fixed explicit request |
| PROC-RESOLVE-002 | Root order, suffix order, case policy, and rejection reasons deterministically select the expected candidate |
| PROC-RESOLVE-003 | Traversal, separator, absolute, device, link/reparse, inaccessible, and insufficient-quality cases fail as specified |
| PROC-RESOLVE-004 | Concurrent candidate replacement is prevented by the claimed mechanism or disclosed and detected by identity policy |

## Pipeline assertions

| ID | Assertion |
|---|---|
| PROC-PIPELINE-001 | Fault every construction step; no case leaves an unknown running child or leaked endpoint |
| PROC-PIPELINE-002 | Endpoint inventories prove unused copies close before release and EOF arrives after the final intended writer closes |
| PROC-PIPELINE-003 | Simultaneously saturate stdout and stderr captures; bounded concurrent drainage follows policy without deadlock |
| PROC-PIPELINE-004 | Capture overflow exercises fail, truncate, spill, and backpressure policies with exact disclosure and authority checks |
| PROC-PIPELINE-005 | Each node failure position exercises upstream/downstream continuation, stop, termination, EOF, and broken-peer policy |
| PROC-PIPELINE-006 | Cancellation at every lifecycle milestone reconciles all children, endpoints, captures, and terminal statuses |
| PROC-PIPELINE-007 | Aggregate policies preserve the complete node result map and never misreport partial success as all-success |
| PROC-PIPELINE-008 | Sensitive topology canaries are absent from unauthorized diagnostic and evidence fields |

## Cross-platform vectors

The same logical child probe prints length-delimited argument/environment observations to an explicitly inherited channel. Expected vectors are generated without shell syntax. Platform-specific tests cover Windows command-line conventions and handle lists, Linux pidfds/fd closing and post-spawn failure, and macOS spawn attributes, sandbox context, and lifecycle guidance.
