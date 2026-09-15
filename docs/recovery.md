# Recover Neo Studio data safely

This workflow creates an inventory before migration, conversion, OCR, or NLP. It protects the original data and provides an audit trail for every later derivative.

## 1. Preserve before changing anything

1. Keep Neo Studio 2022 installed and do not clear its storage, sign out, uninstall it, or reset the pen.
2. Create a device backup. Use an encrypted Finder/iTunes backup for iPhone/iPad; on Android, make a device backup and copy user-visible Neo Studio files through Files or USB.
3. In Neo Studio 2022, use the pen-data-transfer function to collect remaining offline strokes before resetting or re-pairing the pen.
4. Export notebooks/pages as PDF and SVG when offered. Export recordings separately. Do not treat an export as a replacement for the app data.
5. Copy recovered files into `private/source/`. This directory is ignored by Git and must never be pushed to GitHub.

## 2. Build a read-only inventory

From the NeoLab folder, run:

```powershell
python tools/neolab_archive.py private/source --output private/archive-manifest.json
```

The tool calculates SHA-256 hashes, size, timestamp, extension, and safe ZIP entry names. It does not alter, extract, move, upload, or transmit source files.

Review `private/archive-manifest.json` after every acquisition step. A later conversion must reference the SHA-256 of its source file.

## 3. Keep three layers of data

| Layer | Examples | Rule |
| --- | --- | --- |
| Original | device backup, original app data, `.neonotes`, raw audio | Immutable; never edited. |
| Preservation export | PDF, SVG, PNG, audio copy | Generated copies; record source hash and export time. |
| Interpretation | text transcription, tags, NLP keywords | Editable and reviewable; never replaces raw writing. |

PDF/PNG preserve what the page looked like. SVG preserves vector shapes. Historical `.neonotes` archives can preserve ordered pen dots, pressure, timing, and audio references. The recovery process must retain every available layer.

## 4. Migrate only after inventory

After source preservation is complete, use Neo Studio 2's vendor-supported migration path. NeoLAB states that most notes from older apps can be transferred. Compare notebook/page counts and spot-check writing and recordings before treating migration as complete.

## What we need from you

Tell us whether the old app is on Android or iPhone/iPad, whether it opens, and whether the pen still connects. That determines the precise collection path.

For an iPhone/iPad, use the dedicated [iOS recovery procedure](ios-recovery.md).
