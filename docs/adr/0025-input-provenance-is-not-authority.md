# ADR-0025: Input provenance is not authority

**Status:** Accepted  
**Date:** 2026-08-08  
**Deciders:** Rusty Mill founders

## Context

Input may originate from hardware, the OS, accessibility technology, remote sessions, replay, testing, or application injection. Platforms expose different and incomplete origin indicators. Treating “real” input as authorized excludes assistive technology and still does not make the action safe; treating every event identically loses anti-spoofing and audit evidence.

## Decision

Every portable input event carries the strongest provider-evidenced provenance class and assurance, with `unknown` as a valid value. Provenance informs policy but never grants authority. Focused observation, background capture, pointer lock/confinement, and injection are separate capabilities/authorities. Accessibility-originated input follows ordinary focus/security policy without being downgraded to untrusted by default.

## Consequences

- Security-sensitive actions still perform their own authorization/confirmation.
- Synthetic, remote, and accessibility workflows remain testable and usable.
- Providers cannot fabricate hardware origin or silently erase transformations.
- Stable device identity and global observation require explicit privacy authority.

