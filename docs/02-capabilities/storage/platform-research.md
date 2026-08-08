# Storage volume and removable-media platform research

| Platform | Native mechanisms | Architectural consequence |
|---|---|---|
| Windows | Volume GUID paths, drive letters/directory mount points, Mount Manager, volume information/free-space APIs, Configuration Manager safe-removal requests and vetoes | Volume, mount point, filesystem, and device-instance namespaces differ; one volume can have multiple mount paths; eject targets device generations and may require privilege |
| Linux | block/sysfs/udev entities, `/proc/<pid>/mountinfo`, mount namespaces, `mount`/`umount2`, filesystem sync/flush mechanisms, desktop UDisks2 policy | Mount visibility is per namespace; bind/overlay/network/user mounts break one-device/one-volume assumptions; privileged desktop operations commonly use a policy service |
| macOS | Disk Arbitration disks/descriptions/notifications/approval callbacks, mount/unmount/eject/claim operations, I/O Registry correlation | Whole disks, partitions, volumes, and mount points differ; unmount-all precedes eject; arbitration vetoes cannot prevent surprise removal |

## Primary sources

- Microsoft, [Naming a volume](https://learn.microsoft.com/windows/win32/fileio/naming-a-volume), [Volume management](https://learn.microsoft.com/windows/win32/fileio/volume-management), [Mount points](https://learn.microsoft.com/windows/win32/fileio/volume-mount-points), and [`CM_Request_Device_Eject`](https://learn.microsoft.com/windows/win32/api/cfgmgr32/nf-cfgmgr32-cm_request_device_ejectw)
- Linux, [`proc_pid_mountinfo(5)`](https://man7.org/linux/man-pages/man5/proc_pid_mountinfo.5.html), [`mount_namespaces(7)`](https://man7.org/linux/man-pages/man7/mount_namespaces.7.html), [`umount2(2)`](https://man7.org/linux/man-pages/man2/umount.2.html), and kernel [sysfs block-device ABI](https://docs.kernel.org/admin-guide/abi-stable.html)
- UDisks2, [D-Bus API](https://storaged.org/doc/udisks2-api/latest/)
- Apple, [Disk Arbitration overview](https://developer.apple.com/library/archive/documentation/DriversKernelHardware/Conceptual/DiskArbitrationProgGuide/Introduction/Introduction.html), [notifications and approvals](https://developer.apple.com/library/archive/documentation/DriversKernelHardware/Conceptual/DiskArbitrationProgGuide/ArbitrationBasics/ArbitrationBasics.html), and [disk manipulation](https://developer.apple.com/library/archive/documentation/DriversKernelHardware/Conceptual/DiskArbitrationProgGuide/ManipulatingDisks/ManipulatingDisks.html)

## Synthesis

The portable model must be graph-shaped and namespace-aware. Drive letters, `/dev` nodes, BSD disk names, mount paths, and volume identifiers are platform evidence—not interchangeable IDs. Safe user-session behavior often depends on platform arbitration/policy services, while low-level mount/eject mechanisms carry stronger privilege and race hazards.
