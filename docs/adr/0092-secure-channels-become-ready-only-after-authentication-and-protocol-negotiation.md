# ADR-0092: Secure channels become ready only after authentication and protocol negotiation

**Status:** Accepted  
**Date:** 2026-08-08

## Context

TCP connection, QUIC Initial keys, cryptographic handshake progress, certificate signature/path validity, hostname matching, client authentication, and ALPN selection occur at different times. Calling a channel “connected” after any one milestone invites application data onto an unauthenticated peer or wrong protocol.

## Decision

A secure channel becomes application-ready only after the cryptographic handshake is complete or QUIC-confirmed as required, all configured peer and client authentication succeeds against the original service identity and current policy, and a compatible application protocol plus authenticated transport parameters are selected. Earlier states remain observable for orchestration but cannot expose ordinary established-data APIs.

## Consequences

- Connection metrics report transport, crypto, authentication, protocol, and readiness separately.
- QUIC Initial protection cannot be mistaken for peer authentication.
- Optional client authentication and legacy profiles need explicit readiness rules.
- Application protocols receive a generation-bound evidence object before bytes.

