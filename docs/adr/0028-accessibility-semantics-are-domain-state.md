# ADR-0028: Accessibility semantics are domain state, not adapter output

**Status:** Accepted  
**Date:** 2026-08-08  
**Deciders:** Rusty Mill founders

## Context

UI Automation, AT-SPI, macOS Accessibility, and ARIA expose related but nonidentical role, state, pattern/interface, text, action, event, and virtualization models. Building semantics from pixels or renderer nodes loses names, relationships, reading order, hidden/virtual content, text ranges, and intent. Making a native API's vocabulary portable would privilege one platform and encourage backend-owned application semantics.

## Decision

Applications/domain frameworks publish an immutable versioned semantic model independent of rendering and native APIs. Platform adapter services map that model to native accessibility contracts and report mapping variance. Semantic text/ranges refer to authoritative application text; geometry binds semantic, layout, and window revisions. Native adapters cannot redefine roles, focus, actions, or application state.

## Options considered

### Derive from renderer/display list

Low authoring effort but cannot recover intent, logical order, relationships, or virtualized content reliably.

### Adopt one native accessibility API as common model

Detailed but nonportable and forces other platforms into false mappings.

### Domain semantics with native adapters

Requires intentional semantics but preserves platform fidelity, testability, and nonvisual operation.

## Consequences

- Custom UI frameworks must produce semantics alongside visual state.
- Headless semantic conformance is possible but does not replace native AT tests.
- Native mapping gaps remain visible provider evidence.
- Pixels and glyphs never become accessibility truth.

## Verification

Compare one canonical semantic scenario corpus with UIA, AT-SPI, and macOS adapter snapshots/events/actions plus representative assistive-technology outcomes.

