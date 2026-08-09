# Cancellation, termination, and compensation

**RM-WORKFLOW-CANCEL-0001:** Cancellation is a cooperative workflow request with issuer/authority, reason, scope, frontier, propagation policy, deadline, and outcome; it does not prove in-flight activities or external effects stopped.

**RM-WORKFLOW-CANCEL-0002:** Termination is an administrative state transition that prevents further ordinary orchestration under defined policy and records outstanding activities/tasks/children/timers/effects; it does not undo or necessarily cancel them.

**RM-WORKFLOW-CANCEL-0003:** Compensation plans bind the exact observed original effect, compensating action/version, subject/actor/authority, target generation, preconditions, ordering/dependencies, retry/idempotency, deadline, and expected residual.

**RM-WORKFLOW-CANCEL-0004:** Compensation success proves only its stated new effect. Refund, delete, restore, release, notify, or inverse command cannot claim the original observation, disclosure, external transfer, or irreversible effect vanished.

**RM-WORKFLOW-CANCEL-0005:** Compensation order is derived from declared dependency/effect history rather than blindly reversing definition order; parallel effects may require independent or coordinated compensation.

**RM-WORKFLOW-CANCEL-0006:** Failed, partial, refused, expired, impossible, or policy-denied compensation leaves the workflow in an explicit residual state with escalation and repair rather than relabeling it rolled back.
