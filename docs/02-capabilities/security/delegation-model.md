# Authority delegation model

**Status:** Draft

## Delegation envelope

Delegation transfers an authority reference or creates a derived authority for another execution context. A delegation envelope binds:

- authority kind and constraint summary;
- sender and intended audience identities in typed namespaces;
- allowed operations and resource scope;
- issuance, activation, expiry, and maximum-use conditions;
- permitted redelegation depth;
- channel binding and replay identifier;
- provider and contract version;
- audit correlation without secret material.

The envelope is metadata, not necessarily the native authority itself. It cannot be treated as a bearer credential unless a future transfer contract explicitly defines cryptographic protection and replay semantics.

## Transfer modes

| Mode | Semantics |
|---|---|
| Borrow | Receiver may use authority only while a bounded session remains valid; sender retains ownership |
| Duplicate | Receiver gets an independently closable reference with no broader effective rights |
| Move | Sender relinquishes its Rusty Mill reference after confirmed receiver acceptance |
| Derive-and-send | Sender attenuates first, then transfers the narrower child |

Derive-and-send is the portable default. The send protocol uses prepare, receiver validation, commit/acknowledgment, and cleanup so cancellation cannot silently produce ambiguous ownership. Native duplication may occur internally but does not define portable semantics.

## Failure rules

- An untrusted or unauthenticated channel cannot carry authority.
- Audience mismatch, expiry, replay, unsupported constraints, or provider mismatch fails closed.
- Timeout before acknowledgment leaves ownership according to the chosen transfer protocol; it never guesses.
- Receiver rejection preserves sender ownership unless native transfer semantics make that impossible and the contract discloses the exception.
- Audit records distinguish requested, prepared, accepted, rejected, expired, revoked, and indeterminate transfer states.

## Revocation

Revocation is not assumed. Where offered, it has a named mechanism, scope, propagation latency, offline behavior, effect on duplicates, and effect on in-flight operations. Expiry limits future authorization but cannot claw back data already observed or effects already committed.

