# ADR-0090: Certificate requests prove key possession, not issuance authority

**Status:** Accepted  
**Date:** 2026-08-08

## Context

A valid PKCS #10 or protocol request signature is often described as proof that a certificate should be issued with its requested subject, names, usages, and extensions. An attacker controlling a key can make a valid request for unauthorized identifiers or CA capabilities; enrollment agents and attestation add other evidence but do not change that distinction.

## Decision

A certificate request is immutable evidence of requested claims and, when its context-bound proof validates, control or authorized use of the corresponding private key. Identity proofing, identifier control, requester/account/device authentication, profile/template selection, approval, issuance authorization, and certificate construction are independent policy checks. The CA constructs issued fields and records requested-versus-issued differences rather than blindly copying the request.

## Consequences

- Request builders cannot self-grant subject names, usages, constraints, or validity.
- POP methods preserve challenge, channel, replay, algorithm, and verifier evidence.
- On-behalf-of enrollment requires explicit subject/requester/agent delegation.
- Attestation is scoped key/device evidence rather than general identity or authority.

