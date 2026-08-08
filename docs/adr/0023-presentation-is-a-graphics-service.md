# ADR-0023: Presentation is a graphics service over a window surface

**Status:** Accepted  
**Date:** 2026-08-08  
**Deciders:** Rusty Mill founders

## Context

Windowing creates a native presentation target, while DXGI, Vulkan WSI, and Metal own graphics images, synchronization, queue submission, pacing, and present results. Putting swap chains in windowing would make it depend on graphics. Putting window lifetime in graphics would reverse ownership and complicate software/nonvisual windows.

## Decision

Windowing owns the presentation-surface identity and generation. A graphics presentation platform service composes that surface with a selected device, queue, image pool, synchronization, frame policy, color mode, and evidence. Frame leases are bounded and generation/epoch scoped. Submission acceptance, presentation acceptance, and observed display are separate milestones. Reconfiguration creates a new session generation.

## Consequences

- Windows survive renderer/device recreation.
- Renderers retain semantic state and redraw after loss.
- Surface and device loss have one explicit recovery state machine.
- Headless rendering does not depend on windowing; windowing does not depend on a graphics API.
- End-to-end protected presentation requires evidence from every composed layer.

