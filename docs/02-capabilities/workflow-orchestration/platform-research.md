# Platform and standards research

## Primary references

- [BPMN 2.0.2](https://www.omg.org/spec/BPMN/2.0.2/) defines processes, tasks, events, gateways, subprocesses, transactions, compensation, human performers, and executable interchange notation.
- [Serverless Workflow specification](https://serverlessworkflow.io/) defines a portable workflow model for events, functions, data, states, timeouts, errors, retries, authentication, and execution metadata.
- [Amazon States Language](https://states-language.net/spec.html) defines task, choice, wait, parallel, map, success/failure, retry, and catch semantics in a JSON state-machine language.
- [Temporal durable execution](https://docs.temporal.io/workflow-execution) documents event histories, deterministic replay, activities, timers, signals, child workflows, retries, cancellation, and versioning constraints.

## Platform families

Windows, Linux, and macOS provide timers, service scheduling, IPC, process execution, persistence, notification, authentication, and UI primitives but no common durable application-workflow engine. Portable semantics therefore live above operating-system adaptation and compose selected persistence, messaging, scheduling, coordination, and interaction providers.

## Conclusion

BPMN and vendor languages are mappings, not the Rusty Mill model. Products select exact notation/engine while preserving history, effect, task, migration, and conformance contracts.
