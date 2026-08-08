# ADR-0056: Capture authority is session-scoped and revocable

**Status:** Accepted  
**Date:** 2026-08-08

## Context

Camera enumeration and permission status do not mean a process may currently capture. Users, administrators, hardware privacy controls, competing clients, sandbox brokers, and system policy can deny or revoke access while an application is running.

## Decision

Capture uses explicit authority bound to principal, purpose, media/device scope, outputs/metadata, delegation, and lifetime. Permission prompting is a separate user-interaction operation. Native authority and device generation are revalidated at session start and during capture; revocation or privacy-control inconsistency suspends or invalidates the session.

## Consequences

- Discovery remains side-effect free and cannot trigger prompts.
- Products define accessible permission/revocation recovery UX.
- Frames and derived outputs cannot outlive or exceed delegated policy implicitly.
