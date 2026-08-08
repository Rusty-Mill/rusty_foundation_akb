# ADR-0026: Semantic text is not glyph output

**Status:** Accepted  
**Date:** 2026-08-08  
**Deciders:** Rusty Mill founders

## Context

Shaping may combine, split, reorder, omit, or substitute glyphs. Bidi changes visual order without changing logical storage. Generated hyphens, ellipses, ligatures, marks, emoji sequences, and font fallback make character-to-glyph assumptions incorrect. Pixels and glyph IDs cannot support reliable editing, copy, search, accessibility, or security review.

## Decision

Semantic Unicode text and revisioned typed ranges remain authoritative. Shaping/layout produce immutable visual artifacts with explicit many-to-many cluster, caret, line, and geometry mappings back to semantic text. Glyph IDs are opaque to one exact font face instance. Accessibility, editing, copy, search, and diagnostics consume semantic content/policy—not pixels or reconstructed glyph order.

## Options considered

### Glyph-centric common representation

Convenient for rendering but destroys portable semantics and makes fallback/font changes observable as content changes.

### Character-per-glyph abstraction

Simple but false for most complex scripts, ligatures, marks, and emoji.

### Semantic text plus mapped visual artifacts

Preserves i18n/accessibility and permits native shaping/rasterization with explicit mappings.

## Consequences

- Every position/range API must name units and revisions.
- Layout retains logical/visual order and bidi affinity.
- Generated visual content cannot silently enter copied source text.
- Terminal cell semantics remain above glyph placement.

## Verification

Exercise many-to-many shaping, bidi, generated hyphens/ellipsis, fallback, hit testing, selection/copy, and accessibility on the pinned multilingual corpus.

