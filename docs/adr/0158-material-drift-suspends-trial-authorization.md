# ADR-0158: Material drift suspends trial authorization

**Status:** Accepted  
**Date:** 2026-08-08  
**Deciders:** Rusty Mill architecture governance

## Context

Trial evidence and risk depend on exact architecture, contracts, standards, providers, tools, dependencies, platforms, and methods. Continuing after a material change can make the authorization and evidence misleading.

## Decision

A relevant change receives recorded materiality review. Material drift suspends affected trial work and claims until a revised generation passes its entry gates. Evidence reuse requires explicit validity reasoning.

## Options considered

Allow trials to track latest inputs automatically, invalidate on every change, or assess materiality. Automatic tracking hides semantic change; universal invalidation wastes unrelated evidence. Recorded materiality review preserves safety and proportionality.

## Consequences

Trials need input inventories and change logs. Some work pauses, but conclusions remain interpretable and stale authorization cannot silently persist.

## Verification

Audit trial generations against source, dependency, toolchain, platform/provider, standards, scope, and evidence-method changes.

## Follow-up

- Exercise invalidation and evidence-reuse rules in each authorized trial.

