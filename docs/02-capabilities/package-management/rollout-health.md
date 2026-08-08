# Rollout and health

**RM-PACKAGE-ROLLOUT-0001:** Rollout policy binds population/scope, channel/ring/cohort assignment, eligibility predicates, start/deadline, concurrency/rate/bandwidth budgets, pause/abort thresholds, approval, telemetry source, privacy, and policy generation.

**RM-PACKAGE-ROLLOUT-0002:** Cohort assignment is stable and auditable. Targeting cannot be inferred from mutable device labels alone or manipulated by an untrusted mirror/client clock.

**RM-PACKAGE-ROLLOUT-0003:** Download, stage, install, activate, restart/reboot, health observation, promote, hold, pause, abort, and rollback are separate campaign milestones with denominators and unknown/offline devices.

**RM-PACKAGE-ROLLOUT-0004:** Health predicates are product-defined, versioned, privacy-reviewed, and resistant to survivorship bias. Native install success, process start, readiness, crash rate, domain correctness, performance, and user outcome are different signals.

**RM-PACKAGE-ROLLOUT-0005:** Automatic promotion/abort binds minimum sample/coverage, observation window, baseline, statistical/risk thresholds, missing-data treatment, late events, and human override. A lack of telemetry is not success.

**RM-PACKAGE-ROLLOUT-0006:** Mandatory/security updates declare urgency, deadline, deferral count/window, active-work protection, accessibility, restart/reboot, offline behavior, and emergency exception authority without claiming perfect enforcement.

**RM-PACKAGE-ROLLOUT-0007:** Peer/content-delivery optimization cannot alter accepted metadata/artifact identity or reveal cohort, installed inventory, account, or device identity beyond policy.

**RM-PACKAGE-ROLLOUT-0008:** Campaign evidence is aggregatable but each device result remains bound to plan, package, policy, installed pre/post generations, milestones, and health evidence.

