# Filesystem error model

| Field | Value |
|---|---|
| Status | Draft cross-capability model |
| Scope | Portable semantic categories with preserved provider diagnostics |

## Goals

- Support reliable recovery decisions without requiring OS-code matching.
- Preserve native diagnostic evidence for logging, support, and platform extensions.
- Distinguish permanent semantic failure, policy denial, transient conditions, partial effects, cancellation, and indeterminate state.
- Avoid pretending that every native error maps uniquely to one portable category.

## Error record

Every filesystem failure contains:

- Stable semantic category.
- Operation and capability identifier.
- Resource/path role, redacted according to diagnostic authority.
- Whether retry can be considered and under what changed condition.
- Progress or observable state when partial effects are possible.
- Provider code/domain and bounded diagnostic message.
- Causal chain when a higher-level service wraps a lower-level failure.

Provider details supplement the category; they do not replace it.

## Base categories

| Category | Meaning | Typical recovery question |
|---|---|---|
| NotFound | Required namespace binding or resource no longer exists | Re-resolve or create? |
| AlreadyExists | Exclusive creation or destination constraint failed | Choose another name or replacement policy? |
| AccessDenied | Identity, ACL, mode, sandbox, sharing, or policy denied access | Request different authority or report? |
| InvalidPath | Value is invalid for the selected grammar/provider | Correct input? |
| EscapesAuthority | Resolution would violate containment/traversal policy | Reject as security event? |
| WrongObjectKind | Resolved object is not the required kind | Select another operation? |
| ReadOnly | Filesystem/resource does not permit mutation | Use another destination? |
| BusyOrShared | Open/share/lock/mount state prevents the operation | Retry after state change? |
| StorageExhausted | Physical or logical storage allocation failed | Free space or choose another volume? |
| QuotaExceeded | Caller/account/project quota blocked allocation | Adjust quota? |
| NameTooLong | Component or total path exceeds provider limit | Shorten or change layout? |
| TooManyLinks | Resolution exceeded link/reparse traversal limit | Treat as malformed/cyclic namespace? |
| ResourceLimit | Descriptor/handle, memory-lock, or kernel queue limit reached | Back off or raise configured limit? |
| Unsupported | Provider/filesystem cannot provide requested semantics | Negotiate another quality/capability? |
| InvalidRange | Offset, length, or size is invalid or unrepresentable | Correct request? |
| Interrupted | Operation stopped before terminal progress by an external interruption | Retry according to idempotency? |
| Canceled | Operation reached a confirmed canceled terminal outcome | Propagate cancellation? |
| StaleOrDisconnected | Resource/provider lost stable connection or generation | Reconnect and re-resolve? |
| DataCorruption | Integrity validation or filesystem reported corruption | Stop and preserve evidence? |
| DeviceFailure | Device/media/provider I/O failed | Fail over or escalate? |
| PartialEffect | Operation failed with known partial progress/state | Reconcile using reported state? |
| Indeterminate | Provider cannot determine observable effect | Inspect/reconcile before retry? |
| OtherProviderFailure | No stable portable category applies | Use provider evidence and conservative handling |

## Classification rules

1. Categories describe observed semantics, not guessed root cause.
2. Retryability is contextual metadata, never a universal property of a category.
3. Access denial does not reveal whether a hidden path exists.
4. Cancellation is reported only after the operation confirms its canceled terminal outcome.
5. Partial write/read progress accompanies the result defined by the operation contract; progress is not discarded.
6. Atomic replacement uses `PartialEffect` or `Indeterminate` when a provider documents or cannot resolve intermediate namespace states.
7. Unknown native codes map to `OtherProviderFailure` with preserved code/domain, not to a misleading nearest category.
8. Error messages are not parsed for program logic.

## Information disclosure

Diagnostic policy may redact full paths, ancestor names, object identities, security descriptors, user identities, mount details, and provider messages. Portable categories remain available after redaction. Access checks should avoid turning error distinctions into a namespace-existence oracle.

## Open mapping work

A future evidence table will map representative Win32/NTSTATUS, errno, and macOS provider errors to categories per operation. Mappings belong to provider conformance data because the same native code can mean different semantics in different operations.
