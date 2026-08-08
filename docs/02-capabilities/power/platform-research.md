# Power and energy-management platform research

| Platform | Native mechanisms | Architectural consequence |
|---|---|---|
| Windows | system power/battery status and power-setting notifications; energy-saver state; Power Requests/execution-state APIs; suspend/resume lifecycle | Settings are independent observations; display/system requests have different scopes and can be overridden; modern standby changes background assumptions |
| Linux | UPower power-device/aggregate state; systemd-logind sleep/shutdown/idle inhibitor locks and preparation signals; power-profiles services; kernel thermal/power sysfs | Desktop services, logind policy, and raw kernel data are distinct providers; delay/block inhibitors have privilege and maximum-time semantics; namespaces/sessions matter |
| macOS | IOKit power-source notifications; IOPM assertions/activity; ProcessInfo low-power and thermal state; NSWorkspace/IOKit sleep-wake notifications | Assertions and activities are scoped hints with named reasons; thermal/low-power state is qualitative; App Nap and platform lifecycle affect effective execution |

## Primary sources

- Microsoft, [Power management](https://learn.microsoft.com/windows/win32/power/power-management-portal), [power-setting GUIDs](https://learn.microsoft.com/windows/win32/power/power-setting-guids), [Power Requests](https://learn.microsoft.com/windows-hardware/design/device-experiences/powercfg-command-line-options#option-requests), and [energy-saver notification sample](https://learn.microsoft.com/samples/microsoft/windows-classic-samples/powersettingregisternotification/)
- UPower, [service API](https://upower.freedesktop.org/docs/UPower/) and [device properties](https://upower.freedesktop.org/docs/Device.html)
- systemd, [Inhibitor locks](https://systemd.io/INHIBITOR_LOCKS/) and [`org.freedesktop.login1`](https://www.freedesktop.org/software/systemd/man/latest/org.freedesktop.login1.html)
- Apple, [Power Management](https://developer.apple.com/library/archive/documentation/Performance/Conceptual/power_efficiency_guidelines_osx/), [`IOPMAssertionCreateWithName`](https://developer.apple.com/documentation/iokit/1557134-iopmassertioncreatewithname), and [`ProcessInfo` thermal state](https://developer.apple.com/documentation/foundation/processinfo/thermalstate)

## Synthesis

No target provides a universal joule budget or guaranteed performance mode for ordinary applications. Portable behavior therefore observes qualified state, expresses workload intent, adapts explicitly, and uses narrow bounded assertion leases only for concrete user-visible needs. Correctness assumes requests can be denied or defeated.
