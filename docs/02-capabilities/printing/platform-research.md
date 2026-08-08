# Platform research

This mapping identifies native realization candidates, not semantic equivalence.

| Concern | Windows | Linux | macOS |
|---|---|---|---|
| Discovery/capabilities | Print Spooler queues; PrintCapabilities/Print Schema; modern print support varies | CUPS/IPP printer objects and attributes; desktop portal where sandboxed | AppKit/Core Printing destination and `NSPrintInfo`; CUPS/IPP below platform UI |
| Document path | XPS/OpenXPS package/PrintTicket paths, GDI for legacy workloads, newer Print Support workflows | CUPS filters/backend or driverless IPP with PDF/PWG Raster/Apple Raster as negotiated | `NSPrintOperation`/view pagination commonly generates PDF and hands to system printing |
| Job lifecycle | Spooler job identifiers/status/control; rendering and port/device completion differ | IPP/CUPS job states/reasons, receipts and retained history vary | Print operation plus CUPS/IPP job observation; UI and sandbox constraints apply |
| Artifact output | Application PDF/XPS/file pipeline or virtual queue; semantics differ | Direct PDF/artifact pipeline or virtual queue | AppKit PDF print/copy operations or direct artifact pipeline |

## Portability findings

1. Windows PrintTicket preferences must be validated against PrintCapabilities; legacy GDI and XPS-style paths expose materially different representation and lifecycle boundaries.
2. IPP explicitly models Printer, Job, and Document objects and makes capabilities dependent on the submitted document format. `completed` and page/impression/sheet counters are provider reports.
3. macOS printing centers `NSPrintOperation`, `NSPrintInfo`, and paginated view output and can generate PDF rather than send to a printer; system UI and CUPS handoff boundaries remain visible.
4. Driverless IPP is an important provider path, not the universal architecture. Sandboxes, portals, enterprise accounting, secure release, offline queues, legacy drivers, and virtual destinations require truthful discovery.

## Primary references

- [Microsoft: Print Ticket API](https://learn.microsoft.com/en-us/windows/win32/printdocs/print-ticket-api)
- [Printer Working Group: IPP guide](https://www.pwg.org/ipp/ippguide.html)
- [OpenPrinting: CUPS implementation of IPP](https://openprinting.github.io/cups/doc/spec-ipp.html)
- [Apple: AppKit Printing API](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/Printing/osxp_printingapi/osxp_printingapi.html)
- [Apple: Printing From Your App](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/Printing/osxp_printapps/osxp_printapps.html)
