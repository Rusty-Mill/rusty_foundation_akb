# ADR-0068: Image format detection is evidence, not trust

**Status:** Accepted  
**Date:** 2026-08-08

## Context

Extensions, MIME types, signatures, container brands, installed codec patterns, and decoder acceptance can conflict or be attacker-controlled. Platform codec frameworks may discover third-party handlers automatically. Treating recognition as validation would route hostile bytes into overprivileged code and hide ambiguous/polyglot inputs.

## Decision

Image probing is a bounded side-effect-free operation that reports independent evidence, ambiguity, bytes inspected, provider provenance, and required next work. Detection selects only candidate capabilities under policy; all subsequent container, metadata, and pixel parsing remains untrusted, budgeted, and isolated according to risk.

## Consequences

- MIME/extension and magic mismatches are observable policy inputs.
- Installed/native codec presence does not automatically authorize use.
- Probing cannot fetch external resources, materialize full images, or establish content authenticity.
