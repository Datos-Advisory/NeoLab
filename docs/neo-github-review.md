# Official NeoLAB GitHub review

Reviewed 2026-09-14 from the official [NeoSmartpen organization](https://github.com/NeoSmartpen). This review distinguishes a usable technical contract from code that NeoLab may redistribute.

| Repository | What it establishes | NeoLab decision |
| --- | --- | --- |
| [WEB-SDK2.0](https://github.com/NeoSmartpen/WEB-SDK2.0) | Browser Bluetooth connection, live dots, page identity, pressure, timestamps, tilt, offline-data requests, Ncode-to-screen mapping, and `.nproj` support. | Use as the primary prototype reference. Do not copy or bundle it in NeoLab without a license decision. |
| [WEB-SDK-Sample](https://github.com/NeoSmartpen/WEB-SDK-Sample) | A reference UI for the Web SDK. | Use for manual compatibility testing only. |
| [iOS-SDK3.0](https://github.com/NeoSmartpen/iOS-SDK3.0) | iOS pen connection, supported-model history, live/offline data, and commercial-license contact path. | Use only if an iOS native adapter becomes necessary. |
| [Android-SDK2.0](https://github.com/NeoSmartpen/Android-SDK2.0) | Android integration path. | Evaluate after the browser proof of concept. |
| [Windows-SDK2.0](https://github.com/NeoSmartpen/Windows-SDK2.0) | Windows integration path. | Useful for a desktop collector later. |
| [Ncode-SDK2.0](https://github.com/NeoSmartpen/Ncode-SDK2.0) | Ncode-generation tooling and a separate production-print workflow. | Treat as vendor-controlled and private until NeoLAB grants the correct rights and allocation. |
| [Documentations](https://github.com/NeoSmartpen/Documentations) | Historical Caster, Ncode, Neo Notes, and protocol documentation. | Source reference only; its README says the public protocol document is v1.0 and directs v2.0 requests to NeoLAB. |

## Verified Web SDK event contract

The SDK's `PenDotEvent` provides the values NeoLab needs to preserve real writing:

- page identity: `section`, `owner`, `book`, `page`;
- physical input: `x`, `y`, pressure (`f`), pen-down/move/up type, pen tip type, color, tilt/twist;
- timing: absolute `timeStamp` and `timeDiff`;
- context: device identifier passed to the callback and optional SmartPlate indicator.

This means NeoLab can preserve a replayable raw-ink record before any transcription, NLP, or search enrichment.

## License boundary

The current Web, iOS, Android, Windows, and sample repositories declare GPL-3.0. NeoLab will not copy their source code, package their SDKs, or claim their APIs are open for commercial redistribution. A production integration requires either a GPL-compatible NeoLab distribution or a commercial agreement with NeoLAB. The iOS SDK README directs commercial-license requests to `global@neolab.net`.

## Resulting implementation order

1. Publish vendor-neutral schemas, validation, and local import tools.
2. Build a no-SDK demo using synthetic events and ordinary template data.
3. Validate a browser connector with a supported Neo pen and NeoLAB's Web SDK in a separate licensed/private module.
4. Add approved Ncode template generation only after NeoLAB confirms allocation, printing, and license terms.
