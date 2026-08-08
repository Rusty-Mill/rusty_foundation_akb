# Remote presentation and controlled input benchmark specification

| Benchmark | Measures |
|---|---|
| View startup | local grant/peer-channel ready to first encoded, received, decoded, and remotely presented frame |
| Glass-to-glass | local source observation to remote presentation, including encode/network/decode stages and uncertainty |
| Input response | remote event creation/receipt/admission/native acceptance to next causally correlated captured and remote-presented change |
| Input stability | event delay/jitter/loss/reorder/rejection, queue age/occupancy, state divergence and recovery under sustained load |
| Mapping change | resize/crop/scale/rotation/topology/keymap revision convergence and stale-event rejection latency |
| Congestion | quality/latency adaptation, frame/event fairness, bounded memory, input starvation prevention and recovery |
| Revocation | local stop to admission closure, last injection, active-state release/cancel, last transmitted frame, buffer release, indicator clear |
| Recovery | reconnect, participant/transport replacement, provider loss, lock/switch/sleep/resume and neutral device-state restoration |
| Resource | CPU/GPU/encode/network, memory/bandwidth, allocations, wakeups, energy and thermal behavior by source/rate/input load |

Results report p50/p95/p99/max and distributions for every named boundary, clock-correlation error, achieved frame/event rate, drops/rejections by cause, queue age/occupancy, pressed/contact ambiguity, CPU/GPU, copies/allocations, memory/bandwidth/network, power, and thermal state. Runs disclose machines, OS/build, GPU/driver/compositor/portal, network path/emulation, transport/codec, source/color/cursor/audio configuration, participant/device classes, authority/indicator state, mappings/keymap, downstream workload, and raw measurement method. Human consent time is UX evidence, not engine latency.
