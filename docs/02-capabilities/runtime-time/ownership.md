# Runtime and time ownership and trial readiness

| Field | Value |
|---|---|
| Review status | Pass |
| Reviewed | 2026-08-08 |
| Accountable owner | Runtime/time capability owner, initially exercised by Foundation maintainers |
| Architecture reviewer | Foundation architecture review |
| Security reviewer | Foundation security review for precision, wake authority, unsafe/FFI, and cancellation |
| Evidence reviewer | Foundation conformance and performance review |
| Compatibility authority | Foundation architecture review until a dedicated compatibility council exists |

## Ownership duties

The accountable owner maintains contract generations, dependency declarations, platform/source frontier, open questions, assertion/case/scenario mappings, findings, and promotion evidence. Named people must be assigned in an actual promotion or trial record; role ownership here does not authorize work.

## Bounded trial plan

If the exact subject is promoted to Experimental, a later trial proposal may compare native mappings for active/continuous clock reads, deadline delivery, cooperative cancellation, and orderly shutdown on declared Windows, Linux, and macOS versions. It must use the [foundation trial template](../../05-governance/implementation-trials/trial-template.md), isolate unstable surfaces, prohibit release/public API claims, and define disposal. This plan does not select providers, crate boundaries, metadata format, runtime, or executor.

Stop conditions include semantic mismatch, undeclared privilege or wake behavior, unbounded resource growth, unsafe invariant failure, non-isolated privileged CI, evidence/provenance loss, or material input drift.

**RM-RUNTIME-OWNER-0001:** A promotion or trial record MUST replace role-only placeholders with accountable people and disclose review-independence limitations.

**RM-RUNTIME-OWNER-0002:** Ownership MUST include closure or explicit acceptance of every open question affecting the exact promoted subject; unrelated questions MAY remain open only with documented non-impact.

**RM-RUNTIME-OWNER-0003:** The bounded plan is promotion evidence only and MUST NOT be interpreted as trial authorization.

**RM-RUNTIME-OWNER-0004:** Trial disposal MUST revoke authority, retain positive and negative evidence, and prevent experimental artifacts from entering release channels.

