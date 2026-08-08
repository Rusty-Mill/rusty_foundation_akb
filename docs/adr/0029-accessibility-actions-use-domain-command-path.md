# ADR-0029: Accessibility actions use the ordinary domain command path

**Status:** Accepted  
**Date:** 2026-08-08  
**Deciders:** Rusty Mill founders

## Context

Native accessibility APIs allow assistive technologies to invoke controls, set values/selections, scroll, expand, and edit text. Directly mutating backend/UI objects would bypass domain validation, authorization, confirmation, state machines, observability, and equivalent keyboard/pointer behavior. Refusing programmatic actions would make custom UI unusable.

## Decision

Platform adapters translate native invocations into versioned semantic action requests and dispatch them through the same domain command handlers used by other interaction paths. Provenance is retained but grants no authority. Acceptance, command completion, state commitment, and native notification remain separate milestones; stale and disabled requests fail explicitly.

## Consequences

- Assistive actions and other input produce equivalent application outcomes.
- Security/destructive-operation policy cannot be bypassed through accessibility APIs.
- Actions remain operable without fabricating key/pointer events.
- Conformance can compare semantic transitions across invocation methods.

