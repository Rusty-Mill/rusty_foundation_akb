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

## Normative requirements

**RM-SECURITY-DELEGATION-0001:** Delegation MUST bind the exact parent authority generation, constraint summary, typed sender and audience, activation/expiry/use bounds, redelegation depth, channel binding, replay identity, provider/contract version, and nonsecret provenance.

**RM-SECURITY-DELEGATION-0002:** An envelope MUST NOT be treated as authority or a bearer credential unless an explicit transfer contract proves protected possession, authenticity, confidentiality where required, audience binding, freshness, replay resistance, and restoration semantics.

**RM-SECURITY-DELEGATION-0003:** Borrow, duplicate, move, and derive-and-send MUST retain distinct ownership, close, cancellation, failure, return, and recovery semantics.

**RM-SECURITY-DELEGATION-0004:** Derive-and-send MUST be the portable default; any broader mode MUST be explicitly selected and MUST NOT increase effective authority or redelegation depth.

**RM-SECURITY-DELEGATION-0005:** Cross-context transfer MUST use authenticated channel binding plus prepare, receiver validation, commit/acknowledgment, and cleanup or document an equally strong atomic native primitive.

**RM-SECURITY-DELEGATION-0006:** Audience mismatch, expiry, replay, unsupported constraint, parent invalidity, channel-binding failure, provider mismatch, or indeterminate validation MUST fail closed before receiver use.

**RM-SECURITY-DELEGATION-0007:** Timeout, cancellation, rejection, sender failure, receiver failure, and lost acknowledgment MUST yield an explicit ownership/authority inventory; the implementation MUST NOT guess whether a move committed.

**RM-SECURITY-DELEGATION-0008:** Redelegation MUST preserve provenance and monotonically reduce both authority and remaining delegation depth.

**RM-SECURITY-DELEGATION-0009:** Revocation claims MUST bind mechanism, target generations and aliases, propagation scope/latency, offline partitions, already-started operations, already-committed effects, observation method, and residual uncertainty.

**RM-SECURITY-DELEGATION-0010:** Delegation metadata, diagnostics, and audit MUST be audience-redacted and MUST NOT expose transferable native authority, bearer material, channel secrets, or sensitive resource details beyond the reviewer’s disclosure authority.
