# Clipboard and drag-and-drop platform research

**Status:** Research evidence; normative conclusions live in contracts and ADRs.

## Windows: OLE data transfer

OLE uses `IDataObject` for both clipboard and drag-and-drop. A source enumerates formats/media and renders requested data lazily; clipboard retains the object until requested, while drag targets inspect formats during enter/update and receive the object at drop. Microsoft guidance warns against expensive rendering during hover. Shell formats also distinguish preferred and actually performed drop effects, showing that move/copy intent and final result are separate facts.

Primary sources: [Data Transfer interfaces](https://learn.microsoft.com/en-us/windows/win32/com/data-transfer-interfaces), [Shell Data Object](https://learn.microsoft.com/en-us/windows/win32/shell/dataobject), [`IDataObject`](https://learn.microsoft.com/en-us/windows/win32/api/objidl/nn-objidl-idataobject), [OLE clipboard](https://learn.microsoft.com/en-us/windows/win32/dataxchg/ole-clipboard), [Shell clipboard formats](https://learn.microsoft.com/en-us/windows/win32/shell/clipboard).

## Linux: Wayland and X11

Wayland data-device protocols expose sources/offers, MIME types, selection ownership, drag actions, enter/motion/leave/drop, accepted types/actions, and pipe-based data transfer. Primary selection is a separate protocol and is not universally available. X11 selections are owner-mediated conversions; ICCCM `TARGETS`, `MULTIPLE`, and `INCR` show lazy format negotiation and incremental transfer, while ownership can vanish with the source.

Primary sources: [Wayland `wl_data_device`](https://wayland.app/protocols/wayland#wl_data_device), [primary selection](https://wayland.app/protocols/primary-selection-unstable-v1), [data-control extension](https://wayland.app/protocols/wlr-data-control-unstable-v1), [X11 ICCCM selections](https://www.x.org/releases/current/doc/xorg-docs/icccm/icccm.html#Peer_to_Peer_Communication_by_Means_of_Selections).

The privileged data-control extension is compositor-specific and cannot be the portable clipboard baseline.

## macOS: pasteboards and dragging

`NSPasteboard` is a system/shared transfer service containing multiple items and types, including declared/lazy owner-provided data. Dragging uses a drag pasteboard plus source operations, target/location/session state, and final operation. File promises defer generating files until a target supplies a destination and accepts the drop.

Primary sources: [`NSPasteboard`](https://developer.apple.com/documentation/appkit/nspasteboard), [Drag and Drop](https://developer.apple.com/documentation/appkit/drag-and-drop), [`NSDraggingInfo`](https://developer.apple.com/documentation/appkit/nsdragginginfo), [`NSFilePromiseProvider`](https://developer.apple.com/documentation/appkit/nsfilepromiseprovider), [`NSFilePromiseReceiver`](https://developer.apple.com/documentation/appkit/nsfilepromisereceiver).

## Derived portability conclusions

| Concern | Portable rule |
|---|---|
| Formats | Enumerated typed offers before requested materialization |
| Large payloads | Bounded async/incremental stream |
| Ownership | Generation/lease; source may disappear |
| Drag hover | Negotiate metadata, avoid expensive content rendering |
| Move | Target commit then source mutation/deletion |
| File promises | Destination authority plus transactional fulfillment |

