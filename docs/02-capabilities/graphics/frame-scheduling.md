# Frame scheduling and timing model

**RM-GRAPHICS-FRAME-0001:** Simulation/update, render preparation, graphics submission, presentation acceptance, and observed display are separate clocks/milestones. The scheduler cannot infer one from another.

**RM-GRAPHICS-FRAME-0002:** Each frame carries a monotonically increasing session-local frame ID, semantic content revision, window/surface generation, device epoch, target timing, and causal input revision where applicable.

**RM-GRAPHICS-FRAME-0003:** Pacing policy declares maximum frames in flight, late-frame behavior, coalescing/drop policy, refresh adaptation, idle/occluded behavior, and whether simulation is decoupled from render cadence.

**RM-GRAPHICS-FRAME-0004:** Latency measurement distinguishes input observation, application update, submission, present acceptance, and displayed feedback. Unsupported milestones remain unknown rather than estimated without provenance.

**RM-GRAPHICS-FRAME-0005:** Variable refresh, tearing, mailbox/immediate modes, and timed presentation are negotiated semantics. A provider cannot map them to a generic “vsync off” flag without reporting variance.

**RM-GRAPHICS-FRAME-0006:** Occlusion, inactivity, reduced motion, battery/power policy, thermal pressure, and remote-session conditions may reduce cadence under disclosed policy without starving lifecycle/event processing.

**RM-GRAPHICS-FRAME-0007:** Frame callbacks and completion handlers are non-reentrant portable events. Native callback threads do not execute arbitrary renderer/application code.

