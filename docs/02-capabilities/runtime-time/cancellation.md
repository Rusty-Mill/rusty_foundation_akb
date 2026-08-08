# `rm.runtime.cancellation` — Cooperative cancellation

**Status:** Draft  
**Contract version:** 0.1.0  
**Domain:** Runtime  
**Owner:** Unassigned  
**Profiles:** CLI, Desktop, Server, Embedded/headless (candidate required member)

## Purpose

Propagate an idempotent request that work should stop, allowing operations to cooperate without unsafe thread termination or false claims about native abort behavior.

## Non-goals

- Killing threads, unwinding arbitrary foreign code, or guaranteeing immediate termination.
- Treating cancellation as failure or erasing a successful result that won a race.
- Defining how every I/O capability maps cancellation to its native mechanism.

## Semantic model

A cancellation source controls state observed through one or more tokens. State changes once from active to requested and never returns to active. Tokens may be arranged in parent/child scopes; cancellation flows from parent to child, never upward.

## Requirements

- **RM-RUNTIME-CANCEL-0001:** Requesting cancellation **MUST** be idempotent and safe from any thread.
- **RM-RUNTIME-CANCEL-0002:** Once requested, every existing and future observer of the same token **MUST** eventually observe cancellation.
- **RM-RUNTIME-CANCEL-0003:** An observer registered after cancellation **MUST** observe the requested state without waiting for another transition.
- **RM-RUNTIME-CANCEL-0004:** Cancellation observation **MUST** support async waiting without dedicating a worker thread and synchronous polling without an async runtime.
- **RM-RUNTIME-CANCEL-0005:** Dropping a source **MUST NOT** implicitly request cancellation unless the creating contract explicitly selected that policy.
- **RM-RUNTIME-CANCEL-0006:** A child token **MUST** observe parent cancellation; child cancellation **MUST NOT** cancel its parent or siblings.
- **RM-RUNTIME-CANCEL-0007:** Cancellation callbacks, if supported, **MUST NOT** execute while an internal cancellation-state lock is held.
- **RM-RUNTIME-CANCEL-0008:** An operation racing cancellation against completion **MUST** report the outcome that actually becomes terminal; a cancellation request alone **MUST NOT** be reported as confirmed cancellation.
- **RM-RUNTIME-CANCEL-0009:** Operation contracts **MUST** define their cancellation points, resource cleanup, partial effects, and retry safety.
- **RM-RUNTIME-CANCEL-0010:** Cancellation propagation **MUST** remain bounded in stack use for deeply nested scopes.

## Outcome vocabulary

- **Requested:** the signal changed state.
- **Observed:** the operation reached a cancellation point.
- **Confirmed canceled:** the operation terminated with its documented canceled outcome.
- **Completed:** the operation completed normally, possibly after a cancellation request lost the race.
- **Failed:** the operation terminated for a reason other than cancellation.

## Platform realization

The base capability can be implemented in portable userspace using atomic state and wait/notification primitives. Backends for individual operations may additionally request native cancellation. Windows `CancelIoEx`, for example, marks I/O for cancellation but requires observing final completion to distinguish normal completion, cancellation, and failure. Apple Dispatch cancellation does not interrupt work already executing. These are representative reasons not to promise forced abort.

## Security and reliability

Cancellation authority should be scoped: possessing an observer token does not imply permission to cancel. Callback panics/failures must not prevent other observers from being notified. Cancellation does not excuse skipping mandatory cleanup or audit events.

## Conformance plan

Test request idempotence, late registration, concurrent observers, parent/child direction, callback reentrancy, completion races, source drop policy, deep hierarchies, and cleanup. Model-based concurrency tests should verify the one-way state machine.

## Open questions

- Are callbacks part of the base capability or an upper-layer convenience?
- Should linked cancellation combine parents with any-of semantics only, or also support all-of composition?
- What fairness guarantee, if any, applies to a large observer set?
