# ADR-0014: Direct process launch is the base contract

**Status:** Accepted  
**Date:** 2026-08-08  
**Deciders:** Rusty Mill founders

## Context

Process APIs often combine executable search, shell parsing, argument quoting, environment inheritance, resource inheritance, activation, and process creation. Windows passes a command-line string whose parsing depends on the target, while POSIX passes an argument vector. A single convenient “command” API would hide injection, search ambiguity, and non-round-trippable behavior.

## Decision

`rm.process.spawn` performs direct launch of an explicit executable with structured native arguments, explicit environment construction, and allowlisted inheritance. It never implicitly invokes a shell or searches for an executable. Search, shell execution, document/application activation, elevation, and durable service launch are distinct opt-in contracts.

Windows providers declare a target argument-parsing convention or accept an explicitly unsafe/nonportable verbatim command-line extension. They cannot claim universal argument round-trip fidelity.

## Options considered

### Universal command string

Familiar but conflates shell and native parsing, creates injection hazards, and is not portable.

### Always emulate POSIX argv on Windows

Convenient for compatible runtimes but false for arbitrary target parsers.

### Direct structured launch with declared adaptation

Requires explicit convention metadata but preserves intent and exposes incompatibility.

## Consequences

- Convenience search and shell layers remain possible without weakening the base.
- Argument conformance uses target probes and named conventions.
- Executable identity and authority are separate from display names.
- Existing tools with unusual Windows parsing may require a provider-specific adapter or verbatim extension.

## Verification

Cross-platform vectors cover empty arguments, quotes, whitespace, separators, native characters, length limits, executable ambiguity, search-path attacks, and unintended shell expansion.

