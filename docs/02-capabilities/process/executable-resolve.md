# `rm.process.executable-resolve` — Executable resolution

| Field | Value |
|---|---|
| Status | Draft |
| Contract version | 0.1.0 |
| Domain | Process |
| Owner | Unassigned |
| Candidate profiles | CLI, Desktop, Server; optional Embedded/headless |

## Purpose

Resolve a native program name against an explicit ordered set of directory authorities and suffix/format policy, producing an executable candidate and an auditable resolution report suitable for direct launch.

This capability does not reproduce an ambient shell, desktop association, Windows App Paths, application activation, script interpreter selection, or package-manager command alias system.

## Requirements

- **RM-PROCESS-RESOLVE-0001:** Search roots **MUST** be explicit ordered directory authorities; process current directory and ambient `PATH` **MUST NOT** be consulted by the base contract.
- **RM-PROCESS-RESOLVE-0002:** Program names **MUST** be a single relative native component; separators, absolute forms, parent traversal, and device prefixes **MUST** be rejected.
- **RM-PROCESS-RESOLVE-0003:** Suffix candidates and ordering **MUST** be explicit policy; platform defaults such as `PATHEXT` are optional captured inputs, never hidden ambient state.
- **RM-PROCESS-RESOLVE-0004:** Resolution **MUST** use `rm.filesystem.resolve` traversal policy and report its resolution quality.
- **RM-PROCESS-RESOLVE-0005:** Candidate eligibility **MUST** define regular-file/executable-format/access checks without claiming those prechecks guarantee later launch.
- **RM-PROCESS-RESOLVE-0006:** The result **MUST** preserve selected root index, native name, candidate identity evidence, rejected-candidate reasons under disclosure policy, and remaining replacement race.
- **RM-PROCESS-RESOLVE-0007:** An empty search list, no eligible candidate, ambiguous match under policy, or insufficient resolution quality **MUST** return a structured unsatisfied result.
- **RM-PROCESS-RESOLVE-0008:** A resolved candidate **MUST NOT** confer broader filesystem or process authority than its input roots and launch authority.
- **RM-PROCESS-RESOLVE-0009:** Caching **MUST** bind to root/candidate identity and policy inputs and **MUST** declare invalidation and staleness.
- **RM-PROCESS-RESOLVE-0010:** Search diagnostics **MUST** avoid disclosing inaccessible directory contents or sensitive paths beyond caller authority.

## Race model

Resolution is advisory until direct launch. Where a platform cannot launch the inspected executable object, replacement can occur between inspection and native image open. Providers disclose the race and may require code identity/hash/signature policy at image confirmation. A path string is never promoted to durable executable identity.

## Dependencies

Requires `rm.filesystem.directory`, `rm.filesystem.resolve`, and `rm.filesystem.metadata`. It produces input for `rm.process.spawn`; it does not require spawn and does not launch by itself.

