# Security foundation conformance specification

**Status:** Draft

## Evidence scope

Every report identifies capability/contract version, provider and artifact digest, OS/kernel version, architecture, sandbox/container state, relevant security configuration, test-suite version, and deviations. Reports contain no generated random bytes or credentials.

## Authority-model assertions

| ID | Assertion |
|---|---|
| SEC-AUTH-001 | Derivation rejects every attempted operation, resource, lifetime, audience, or delegation expansion |
| SEC-AUTH-002 | Closed authority cannot begin a new operation |
| SEC-AUTH-003 | Identical display identifiers from different namespaces/issuers do not compare equal |
| SEC-AUTH-004 | Missing evidence and indeterminate policy fail closed at enforcement boundaries |
| SEC-AUTH-005 | Advisory permit never suppresses a later native denial |
| SEC-AUTH-006 | Audit output excludes configured secret and credential canaries |
| SEC-AUTH-007 | Transfer cancellation and receiver rejection preserve unambiguous ownership |
| SEC-AUTH-008 | Each claimed attenuation enforcement level survives its documented bypass probes |

## `rm.security.random` assertions

| ID | Requirements | Method |
|---|---|---|
| SEC-RNG-001 | 0001, 0004 | Exercise zero, boundary, typical, and provider-limit-crossing lengths; verify exact initialization |
| SEC-RNG-002 | 0002, 0011 | Fault-inject partial native progress/failure; verify no success or accessible partial material |
| SEC-RNG-003 | 0003, 0006 | Disable/fail source in a controlled provider; verify fail-closed behavior and no fallback |
| SEC-RNG-004 | 0007, 0008 | Verify direct sync path and readiness/cancellation behavior without hidden runtime creation |
| SEC-RNG-005 | 0009 | Seed buffers with canaries and inspect all diagnostic and telemetry sinks |
| SEC-RNG-006 | 0010 | Exercise supported fork/clone/snapshot lifecycle scenarios and document unsupported ones |
| SEC-RNG-007 | 0012 | Verify certification fields are absent unless linked to scoped evidence |

## Statistical testing boundary

Statistical batteries may detect gross provider or integration failures but cannot prove unpredictability or cryptographic security. Conformance trusts the documented OS cryptographic source, verifies correct use and failure handling, and treats suspicious statistical results as investigation triggers rather than a certification.

## `rm.security.secret-store` assertions

| ID | Assertion |
|---|---|
| SEC-SECRET-001 | Selection rejects each individually mismatched or unknown protection dimension before plaintext submission |
| SEC-SECRET-002 | Create collision never overwrites; explicit replace observes generation/conflict semantics |
| SEC-SECRET-003 | Non-exportable and scoped-reveal items cannot be obtained through an owned-export path |
| SEC-SECRET-004 | Prompt-required, prompt-forbidden, locked, logged-out, and headless cases produce declared outcomes without unsafe blocking |
| SEC-SECRET-005 | Cancellation races return confirmed canceled, completed, or indeterminate with no fabricated state |
| SEC-SECRET-006 | Secret and sensitive-metadata canaries are absent from every configured diagnostic, telemetry, crash, and report sink |
| SEC-SECRET-007 | Delete reports only evidenced visibility, replica, backup, garbage-collection, and erasure effects |
| SEC-SECRET-008 | Logout, lock, password/account change, sandbox, migration, restore, and synchronization probes match scoped provider claims |
| SEC-SECRET-009 | Item identifiers and lookup attributes do not authorize access and are isolated by provider namespace |
| SEC-SECRET-010 | Fault injection at every native boundary preserves ownership and never exposes partially initialized plaintext |

## Adversarial platform matrix

Run supported tests in ordinary and sandboxed contexts, under resource pressure, during high concurrency, and across process lifecycle events. Platform-specific probes must confirm the actual native source rather than inferring it from the OS name.

## Restricted execution assertions

| ID | Assertion |
|---|---|
| SEC-RESTRICT-001 | Child-controlled code cannot execute before required restrictions are verified |
| SEC-RESTRICT-002 | Only allowlisted handles/descriptors, environment, working directory, and IPC are present |
| SEC-RESTRICT-003 | Filesystem, network, process-control, and descendant attempts match the manifest and disclosed enforcement levels |
| SEC-RESTRICT-004 | Setup cancellation and every injected launch failure leave no running unrestricted child or leaked prepared authority |
| SEC-RESTRICT-005 | Required unsupported controls fail construction; permitted degradation is disclosed before release |
| SEC-RESTRICT-006 | Supervisor failure and termination obey declared descendant and cleanup policy |
