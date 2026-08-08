# Capability profiles

Profiles are named, versioned declarations of the capabilities and quality levels needed by a workload. They avoid a one-size-fits-all platform dependency.

## Seed profiles

- **CLI:** process, terminal/stdio, filesystem, configuration, time, and diagnostics.
- **Desktop:** runtime, filesystem, networking, security, windowing, graphics, input, accessibility, i18n, audio, and observability.
- **Server:** runtime, async I/O, process, networking, security, configuration, time, and observability.
- **Embedded/headless:** minimal runtime and explicitly selected I/O capabilities under constrained resource budgets.

These names are placeholders until domain analysis establishes exact membership.

## Profile rules

- Required and optional members are explicit.
- Quality and security requirements may be stricter than base capability contracts.
- Profiles may extend another profile but cannot silently weaken it.
- Resolution produces a report of selected providers, unavailable requirements, emulation, and degradation.
- Profile versions follow compatibility rules and are included in conformance claims.
