# Portable path value model

| Field | Value |
|---|---|
| Status | Draft semantic model |
| Kind | Common value model, not a capability |
| Decision | [ADR-0006](../../adr/0006-paths-are-lossless-native-values.md) |

## Purpose

Represent filesystem names losslessly across Windows, Linux, and macOS while separating lexical manipulation from authority-bearing filesystem resolution.

## Principles

1. A path value is not required to be valid Unicode.
2. Native encoding is preserved losslessly for round-trip use on its originating platform family.
3. Display conversion is explicit and may be lossy; it never changes the underlying value.
4. Component parsing follows the selected platform grammar, not host-locale rules.
5. Lexical operations do not access the filesystem and do not resolve links, aliases, mount points, junctions, or case behavior.
6. Equality of path values means equality under an explicitly selected lexical comparison, not proof that two paths name the same object.

## Structural vocabulary

- **Component:** one name between separators.
- **Root designator:** platform grammar element selecting an absolute namespace root.
- **Prefix:** Windows drive, UNC, device, or verbatim namespace prefix where applicable.
- **Relative path:** component sequence interpreted under an explicit directory authority.
- **Parent component:** lexical `..`, whose security meaning is determined only during resolution.
- **Stored spelling:** exact name representation returned by enumeration or metadata where available.

## Required operations

- Construct from native representation without loss.
- Inspect absolute/relative form and components under a declared grammar.
- Join components lexically.
- Obtain parent and file-name components lexically.
- Convert to a display string with an explicit loss policy.
- Reject embedded native terminators or invalid structural forms at the platform boundary.

## Prohibited assumptions

- UTF-8 validity on POSIX filesystems.
- Case sensitivity or insensitivity from OS identity.
- Unicode normalization equivalence.
- A universal separator rewrite that preserves native namespace meaning.
- `canonicalize`-then-open as a secure containment strategy.
- Persistence or global uniqueness of path spelling.

## Comparison modes

- **Exact native:** byte/code-unit exact within the same grammar.
- **Lexical portable:** limited structural comparison for configuration and tests; not object identity.
- **Filesystem-resolved:** provider operation that determines whether resolved handles identify the same live object within a declared scope.

Case folding and Unicode normalization are filesystem/provider behavior and may require volume-specific discovery. They do not belong in the base value type.
