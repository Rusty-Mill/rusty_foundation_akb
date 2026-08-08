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

## Cross-platform vectors

The same logical child probe prints length-delimited argument/environment observations to an explicitly inherited channel. Expected vectors are generated without shell syntax. Platform-specific tests cover Windows command-line conventions and handle lists, Linux pidfds/fd closing and post-spawn failure, and macOS spawn attributes, sandbox context, and lifecycle guidance.

