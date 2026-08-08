# Device discovery platform research

| Platform | Native mechanisms | Architectural consequence |
|---|---|---|
| Windows | Configuration Manager/SetupAPI device instances and interfaces; `CM_Register_Notification`; device property model | Device instance, interface, container, and class are distinct namespaces; registration-before-enumeration reduces but does not eliminate reconciliation needs |
| Linux | Kernel device model, sysfs hierarchy/attributes, uevents, and udev database/monitor | Sysfs paths and `/dev` nodes have different roles; uevents may race with state reads and udev policy; namespace/container views affect visibility |
| macOS | I/O Registry services/properties/planes, matching dictionaries, matching/termination/interest notifications | Registry services are driver/service objects in multiple relationship planes; notification iterators must be drained/rearmed and services can be republished |

## Primary sources

- Microsoft, [`CM_Register_Notification`](https://learn.microsoft.com/windows/win32/api/cfgmgr32/nf-cfgmgr32-cm_register_notification), [Retrieving device interfaces](https://learn.microsoft.com/windows-hardware/drivers/install/device-interface-classes), and [device property model](https://learn.microsoft.com/windows-hardware/drivers/install/unified-device-property-model--windows-vista-and-later-)
- Linux kernel, [The Linux device model](https://docs.kernel.org/driver-api/driver-model/overview.html), [sysfs rules](https://docs.kernel.org/admin-guide/sysfs-rules.html), and [kobject uevent API](https://docs.kernel.org/core-api/kobject.html)
- systemd, [`udev`](https://www.freedesktop.org/software/systemd/man/latest/udev.html) and [`sd_device_monitor`](https://www.freedesktop.org/software/systemd/man/latest/sd_device_monitor_new.html)
- Apple, [`IOServiceAddMatchingNotification`](https://developer.apple.com/documentation/iokit/1514362-ioserviceaddmatchingnotification), [`IOService`](https://developer.apple.com/documentation/kernel/ioservice), and [I/O Kit device matching](https://developer.apple.com/library/archive/documentation/DeviceDrivers/Conceptual/IOKitFundamentals/Matching/Matching.html)

## Synthesis

Every target exposes enumeration plus notifications, but object identity, hierarchy, readiness, properties, and delivery guarantees differ. None justifies a permanent cross-platform `DeviceId` or a portable lossless hotplug log. Portable value comes from typed snapshots, provenance, generation replacement, explicit query scope, and reconciliation. Class-specific APIs remain the authority and behavior boundary for using hardware.
