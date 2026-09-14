# NeoLab baseline knowledge

Reviewed 2026-09-14. Direct source findings, proposals, and uncertainties are separated below.

## Reviewed sources

- The 13-page `Caster Lite XML Format (nproj) Specification Document` (NeoLAB, 2017) describes a Caster Lite project for applying PDS3 Ncode to a PDF. It covers Ncode scope/page allocation, certificate and PDF paths, 72-DPI page geometry, symbols, and media resources. It is a production-authoring reference; it does not allocate Ncode IDs to NeoLab.
- The 27-page `Ncode Service Development Getting Started Guide v1.01` (NeoLAB, 2017) describes content PDF -> Ncode authoring/metadata -> print-quality validation -> Pen SDK -> back-end workflow. It requires carbon-black recognition and separate colour-production workflows. It warns that printer and PostScript support must be validated before production.
- The two 2015/2016 `Neo Notes Data File Format` PDFs describe historical `.neonotes` ZIP archives containing metadata, page data, audio, and voice-memo metadata. Strokes use normalized x/y/pressure plus time deltas. They are historical-format references, not proof of a current public import/export contract.
- [NeoLAB technology](https://neolab-home.vercel.app/en/technology) says NeoLAB develops the Ncode/dot-code/smartpen stack and says developers can build Neo smartpen applications. This is a company claim, not an interoperability guarantee.
- [NeoLAB partnership](https://neolab-home.vercel.app/en/partnership) lists education, publishing, stationery, medical, industrial, and finance and gives `global@neolab.net` for inquiries.
- [NeoLAB Form Solutions](https://shop.neosmartpen.com/pages/solutions) describes Ncode forms, pen capture, Bluetooth/USB transfer, and structured Excel/CSV/JPEG output. It supports the use case but does not document a NeoLab API.
- [DIY Ncode Printables](https://neolab.net/en/customer/ncode-pdf) supplies official ready-to-print Ncode PDFs. The page describes each as 50 pages and offers A4/A5 basic paper, planning templates, and storyboards. It recommends Adobe PDF Reader, a color laser printer, a PCL/PS driver, and a small recognition test before a full run. This is the approved public source for the listed ready-made forms; it does not grant NeoLab a right to modify, redistribute, allocate, or generate Ncode patterns.
- The [NeoSmartpen GitHub organization](https://github.com/NeoSmartpen) publishes current SDK repos as well as legacy projects. The [iOS SDK 2 README](https://github.com/NeoSmartpen/IOS-SDK2.0/blob/master/README.md) and [iOS SDK 3 README](https://github.com/NeoSmartpen/iOS-SDK3.0/blob/master/README.md) state GPLv3/non-commercial and separate commercial licensing; confirm current terms directly with NeoLAB.
- The user-provided [NISDK PDF](https://github.com/NeoSmartpen/IOS-SDK2.0/blob/master/NISDK.pdf) is a legacy iOS 2.3.5 SDK reference. It documents BLE, live/offline strokes, paper UI, nproj metadata, configuration, firmware, and older hardware. It is useful history, not the primary implementation target.

## Technical facts that affect implementation

The Ncode guide defines a 2.37 mm cell with 56 bits and gives the physical conversion: `inch = ncodeCoordinate * 56 / 600`. A page identity contains Section, Owner, Book, and Page; a page number alone is insufficient. Ncode input therefore needs page identity, coordinates, pressure, and timestamps.

Caster uses an `nproj` application format (version `2.31`, category `simple`) with zero-based pages and 72-DPI dimensions. A symbol can be a rectangle or polygon. It directs applications to skip undefined XML elements, so readers must be forward-compatible.

The historical Neo Notes specifications conflict in minor places: V1.0 has an optional version-3 stroke extra-data extension, while the 2016 document omits it; its rendering prose also conflicts with the schema's stroke/voice-memo type values. An importer must detect the actual version and bounds-check every record instead of relying on prose alone.

## NeoLab proposal

Start with ordinary, printable Daily Time Log and Daily Task List templates. A pen adapter will later convert a supported SDK's events into the same record model. NLP adds searchable suggestions after capture; it never overwrites raw strokes, transcribed text, or canonical fields.

Ncode is a release gate for a **new NeoLab-designed Ncode form**: it requires written vendor approval for Ncode allocation, authoring, colour-separated printing, quality validation, current device/SDK support, and commercial licensing. Never describe a normal PDF as Ncode-ready. NeoLAB's linked DIY PDFs are an exception because NeoLAB supplies them as ready-to-print Ncode PDFs.

## Questions for a partnership discussion

1. Which current smartpens, firmware, and SDKs support a new integration?
2. What commercial license and distribution model apply?
3. Can NeoLAB allocate page ranges and provide the current authoring/printing/certificate process?
4. Which printers, colour profiles, papers, and recognition-quality checks are approved?
5. What current structured-output, privacy, retention, and data-residency options exist?
6. May NeoLab use the NeoLAB, Ncode, or Neo Smartpen names/logos in public branding?
