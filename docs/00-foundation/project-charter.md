# Project charter

**Status:** Accepted foundation intent  
**Last updated:** 2026-08-08

## Mission

Create a Rust-first, high-performance, capability-based OS abstraction and application platform that lets applications express required behavior once and receive faithful, native implementations on Windows, Linux, and macOS.

Rusty Mill is not a lowest-common-denominator wrapper. It provides stable capability semantics, makes platform differences explicit, and preserves access to native performance and advanced features.

## Vision

Applications depend on capabilities and behavioral contracts rather than Win32, POSIX, Cocoa, or backend-specific mechanisms. Backends translate those contracts into the best supported native mechanism and report unsupported or degraded behavior explicitly.

## Objectives

- Define a shared architectural language for capabilities, services, interfaces, contracts, backends, resources, events, and policies.
- Specify complete, testable behavioral contracts before designing public Rust APIs.
- Support async-first composition while remaining sync-complete.
- Deliver native performance with measurable overhead budgets and zero-cost abstractions where feasible.
- Make secure behavior the default and unsafe or privileged behavior explicit.
- Treat accessibility, internationalization, observability, security, and performance as architectural concerns.
- Establish conformance and benchmark suites as peer products of the implementation.
- Build an ecosystem that can evolve without forcing a monolithic dependency graph or release train.

## Initial target platforms

- Windows
- Linux
- macOS

Additional backends are possible only when the capability contracts remain coherent; they are not an initial milestone.

## Non-goals

- Replacing operating-system kernels or system DLLs.
- Hiding every meaningful platform difference.
- Reproducing every native API one-for-one.
- Promising identical performance where operating systems expose different primitives.
- Creating implementation crates before capability boundaries and contracts are reviewed.
- Defaulting to microservices, dynamic plugins, or process boundaries without a concrete isolation or scaling need.

## Deliverables

The long-term program has three equally important outputs:

1. The architecture knowledge base and specifications.
2. Rust implementation crates and platform backends.
3. Conformance, compatibility, and benchmark suites.

## Success criteria

- Application code selects capabilities and profiles without branching on OS identity for normal operation.
- Every stable capability has a behavioral contract and machine-testable conformance requirements.
- Platform-specific variance is discoverable before use and observable at runtime.
- Overhead and native-path performance are measured continuously on all supported platforms.
- Releases are reproducible, attestable, upgradeable, and governed by documented compatibility policy.
