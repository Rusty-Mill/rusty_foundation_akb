# Domain-analysis method

**Status:** Accepted foundation method  
**Authority:** [RFC-0001](../rfc/0001-capability-specification-system.md)

Domain analysis discovers durable behavior before API or repository design. Its output is a reviewed map of user needs, capabilities, boundaries, dependencies, variance, and unknowns.

## Analysis sequence

### 1. Frame the domain

State the purpose, consumers, adjacent domains, non-goals, terminology, and known platform mechanisms. OS APIs are evidence about the problem space, not the taxonomy itself.

### 2. Collect scenarios

Describe concrete application outcomes across CLI, desktop, server, and constrained/headless workloads. Include success, failure, cancellation, concurrency, shutdown, recovery, accessibility, localization, and hostile-input scenarios.

### 3. Inventory native mechanisms

For Windows, Linux, and macOS, record mechanisms, semantic differences, lifecycle rules, privilege requirements, performance characteristics, and version constraints. Keep research descriptive and source-linked.

### 4. Identify candidate capabilities

Group behavior that has a cohesive contract and can be selected, secured, tested, and evolved independently. Split a candidate when its authority, lifecycle, availability, or compatibility can vary independently. Merge candidates when they cannot provide useful behavior alone.

### 5. Draw boundaries and dependencies

Classify graph edges as `requires`, `optionally-uses`, or `conflicts-with`. Move orchestration into a service when combining capabilities would otherwise create a cycle or inflate a base contract.

### 6. Specify behavior

Use the [capability template](capability-template.md). Assign stable requirement identifiers to normative statements. Define minimum guarantees before preferred quality levels.

### 7. Map variance

For every target platform, classify the expected realization as native, emulated, degraded, or unavailable. A proposed common contract is invalid if one target can satisfy it only by silently changing its meaning.

### 8. Design verification

Map requirements to conformance assertions and performance claims to benchmark scenarios. Identify hardware-, privilege-, timing-, and environment-sensitive evidence.

### 9. Evaluate profiles and ecosystem impact

Record which profiles include the capability and whether it creates new distribution, supply-chain, repository, or release constraints.

## Boundary tests

A candidate capability should have affirmative answers to most of these questions:

- Can its purpose be explained without naming an OS API?
- Does it expose one cohesive authority and resource lifecycle?
- Can a consumer require or omit it independently?
- Can a backend prove its behavior independently?
- Can it evolve without forcing unrelated capabilities to version?
- Does it avoid embedding application policy?

## Analysis deliverables

Each domain produces a domain overview, scenario catalog, platform research matrix, candidate capability list, dependency graph, open-question register, capability specifications, and planned conformance/benchmark evidence. Domain artifacts remain Draft until their governing RFC accepts them.

## Exit criteria

Domain analysis is ready for API design when terminology is stable, dependency cycles are resolved, platform variance is explicit, security and quality reviews are complete, and every normative requirement has a planned evidence path.
