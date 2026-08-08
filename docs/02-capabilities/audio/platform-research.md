# Audio platform research

| Platform | Native mechanisms | Architectural consequence |
|---|---|---|
| Windows | MMDevice enumeration, WASAPI shared/exclusive streams, event/timer buffering, `IAudioClock`, endpoint invalidation | Endpoint generation, sharing mode, effective buffering, event delivery, clock observation, and invalidation are independent evidence |
| Linux | PipeWire node/port graph and negotiated stream parameters; ALSA PCM devices with periods, buffers, timestamps, and XRUN recovery | Desktop routing and direct hardware PCM are different providers; graph quantum and hardware periods cannot be treated as universal |
| macOS | Core Audio HAL devices/clocks, Audio Unit render callbacks, and route/property change observation | Device time, host time, callback quantum, route changes, and aggregate/virtual devices require explicit correlation and generation handling |

## Sources

- Microsoft, [WASAPI overview](https://learn.microsoft.com/windows/win32/coreaudio/wasapi) and [`IAudioClock`](https://learn.microsoft.com/windows/win32/api/audioclient/nn-audioclient-iaudioclock)
- Microsoft, [Rendering a stream](https://learn.microsoft.com/windows/win32/coreaudio/rendering-a-stream) and [Recovering from an invalid-device error](https://learn.microsoft.com/windows/win32/coreaudio/recovering-from-an-invalid-device-error)
- PipeWire, [Streams](https://docs.pipewire.org/page_streams.html) and [Scheduling](https://docs.pipewire.org/page_scheduling.html)
- ALSA, [PCM interface](https://www.alsa-project.org/alsa-doc/alsa-lib/pcm.html)
- Apple, [Core Audio overview](https://developer.apple.com/library/archive/documentation/MusicAudio/Conceptual/CoreAudioOverview/Introduction/Introduction.html), [Audio Unit render callbacks](https://developer.apple.com/documentation/audiotoolbox/aurendercallback), and [audio clocks](https://developer.apple.com/documentation/coremedia/cmaudioclock-api)

## Synthesis

All three platforms expose native low-latency mechanisms, but none makes endpoint identity, default routing, requested latency, callback cadence, or wall-clock correlation immutable. Therefore the portable abstraction preserves negotiated state and uncertainty. PipeWire and system audio engines may add routing/conversion policy; direct ALSA or exclusive device access may remove some mediation while adding authority and coexistence constraints. These are selectable qualities, not a single portability tier.
