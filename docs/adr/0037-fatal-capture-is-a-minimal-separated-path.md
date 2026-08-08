# ADR-0037: Fatal capture is a minimal separated path

**Status:** Accepted  
**Date:** 2026-08-08

## Context

A fatal exception or signal may occur while allocators, locks, runtimes, threads, or process memory are inconsistent. Ordinary logging, formatting, symbolication, compression, consent UI, and upload are unsafe or unreliable in that context.

## Decision

The in-process fatal path performs only a bounded platform-proven minimal handoff/capture using preallocated state. Post-processing, symbolication, redaction, packaging, retention decisions, and upload occur out of process or on a later healthy launch. Raw artifacts are treated as restricted sensitive data.

## Options considered

- Full in-process crash reporter: feature rich but unsafe under corrupted state.
- Depend only on platform defaults: safest integration but insufficient for portable product/build evidence and policy composition.
- Minimal cooperative capture plus separated analysis: bounded risk with explicit platform variance.

## Consequences

- Crash capture remains best effort and platform-specific safety evidence is required.
- Products must provision exact debug-artifact identity and a separate analysis path.
- Rich crash metadata must be preclassified/preallocated or collected later; it cannot be improvised during failure.

