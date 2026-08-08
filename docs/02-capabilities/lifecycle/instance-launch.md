# Instance and launch model

## Capability identity

`rm.lifecycle.instance` describes one running application instance and its launch evidence.

**RM-LIFECYCLE-INSTANCE-0001:** An instance has a unique process-local epoch, product/build identity, native process identity, launch reason set, initial activation set, session observations, and capability-resolution report identity.

**RM-LIFECYCLE-INSTANCE-0002:** `created`, `initializing`, `ready`, `quiescing`, and `terminated-observation` are portable service states. Native callbacks may skip observations; the model never synthesizes an earlier guarantee from a later event.

**RM-LIFECYCLE-INSTANCE-0003:** Readiness is application-defined and revisioned. Process start, event-loop entry, first window creation, first frame presentation, and user-interactive readiness are separate milestones.

**RM-LIFECYCLE-INSTANCE-0004:** Launch arguments, environment capture, working-directory observation, activation payloads, and restoration candidates remain distinct inputs with provenance and trust classification.

**RM-LIFECYCLE-INSTANCE-0005:** Multi-instance policy is an explicit platform service decision. Single-instance coordination cannot infer identity from process names or use activation forwarding as an authority bypass.

**RM-LIFECYCLE-INSTANCE-0006:** Lifecycle delivery is ordered per application instance, bounded, non-reentrant, and affinity-aware. Required native replies use predeclared policy when application code cannot safely run synchronously.

