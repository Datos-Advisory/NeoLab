# Neo Studio 2022 recovery on iPhone or iPad

Use this procedure in order. The aim is to retain an independent device backup, app-visible exports, and any pen-resident handwriting before migration.

## Before opening or changing the app

1. Do not uninstall Neo Studio 2022, offload it, clear its data, sign out, or reset the smartpen.
2. Connect the iPhone/iPad to a trusted computer with a cable.
3. Create an **encrypted local backup**:
   - On Windows, use Apple Devices or iTunes, select the device, select **Back up all data on your iPhone to this computer**, select **Encrypt local backup**, set a password you will retain, then choose **Back Up Now**.
   - On macOS, use Finder, select the device, select **Back up all of the data on your iPhone to this Mac**, select **Encrypt local backup**, then choose **Back Up Now**.
4. Confirm the backup finished and record its date/time. Do not depend only on iCloud for this recovery copy.

## Collect data from Neo Studio 2022

1. Open Neo Studio 2022 while the pen is charged and nearby.
2. Connect the pen. If the pen indicator shows saved/offline handwriting, use the app's **Transfer pen data** or sync function. Keep the app open until it completes.
3. Make a notebook inventory: notebook title, approximate page count, date range, and whether it has audio. Screenshots are sufficient for this inventory.
4. For each important notebook/page, use the app's Share/Export controls to create:
   - PDF for a readable preservation copy;
   - SVG if offered, for a vector handwriting copy;
   - recordings/audio separately, if the app offers them.
5. Save exports to Files, iCloud Drive, or another location that can be copied to the computer. Use a date-named folder such as `NeoLab-Recovery-2026-09-14`.
6. Create a second encrypted device backup after pen transfer and exports finish.

## Migrate only after preservation

1. Install Neo Studio 2 alongside the old app; do not remove Neo Studio 2022.
2. Use Neo Studio 2's supported migration/import path and the same account where applicable.
3. Compare notebook names, page counts, and a sample of handwriting/recordings against the inventory.
4. Keep the original app and both encrypted backups until every important notebook has been checked.

## Bring a local copy to NeoLab

Copy exported files from the computer into `private/source/`, then run:

```powershell
python tools/neolab_archive.py private/source --output private/archive-manifest.json
```

Do not upload the `private/` folder to GitHub. The manifest hashes each source file so later converted PDFs, transcripts, and keywords can be traced back to the exact original export.

## Limits

iOS keeps app internals in a sandbox. A Finder/iTunes backup is the preservation copy; normal Files access may expose only what Neo Studio 2022 explicitly exports. Do not use unofficial tools to alter the app container. If an important notebook is visible in the app but has no usable export/migration path, keep the backup and contact NeoLAB support before changing the app.
