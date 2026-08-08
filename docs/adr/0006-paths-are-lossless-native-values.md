# ADR-0006: Paths are lossless native values

**Status:** Accepted  
**Date:** 2026-08-08  
**Deciders:** Rusty Mill founders

## Context

Windows filesystem names are represented through Unicode code units and multiple namespace grammars. POSIX filesystems generally expose names as byte sequences excluding separator and terminator bytes; those bytes need not be valid UTF-8. Filesystems also differ in case behavior, normalization, and stored spelling.

Requiring Unicode strings would either reject valid names or silently lose information. Applying a universal normalization or case-folding rule would change identity on some filesystems. Treating path comparison as object identity would create correctness and security defects.

## Decision

Represent paths losslessly in a platform-native value model with explicit grammar. Unicode display conversion is separate and may be lossy only when the caller selects that policy. Lexical equality does not prove filesystem-object identity. Case folding, Unicode normalization, and stored-spelling behavior belong to filesystem/provider discovery rather than the base path type.

Paths are semantic values, not capabilities. Serialization across platform families requires an explicit encoding and portability policy.

## Options considered

### UTF-8 strings

Simple and Rust-friendly, but cannot represent every valid POSIX name without rejection or loss.

### Normalized Unicode strings

Convenient comparison, but imposes semantics that filesystems do not share and can change actual names.

### Lossless native values

Preserves round trips and makes display and portability trade-offs explicit, at the cost of a more deliberate type model.

## Consequences

- User-facing display may require an explicit escaped or lossy representation.
- Portable configuration formats cannot assume arbitrary native paths are plain strings.
- Lexical and filesystem-resolved comparisons remain separate operations.
- APIs must prevent accidental use of display strings for filesystem access.

## Verification

Test round trips for invalid UTF-8 POSIX names, Windows nontrivial prefixes and code-unit sequences, separator/root parsing, display conversion, and absence of implicit normalization.
