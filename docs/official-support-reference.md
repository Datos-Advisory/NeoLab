# Official Neo Smartpen support reference

**Source reviewed:** [Neo Smartpen FAQ](https://shop.neosmartpen.com/pages/faqs), 2026-09-14. This page is a support reference, not a software or Ncode license.

## Facts that affect NeoLab

| Topic | Vendor guidance | NeoLab consequence |
| --- | --- | --- |
| Paper | The pen works only on paper printed with an Ncode pattern; ordinary paper and non-Ncode notebooks cannot create smartpen input. | Daily Templates remain ordinary PDFs and structured records until NeoLAB authorizes an Ncode allocation and print workflow. |
| Multiple notebooks | Each Ncode notebook has a unique pattern, allowing one pen to keep notebooks separate. | Preserve `section`, `owner`, `book`, and `page` source identity; never infer identity from a displayed notebook title alone. |
| Missing handwriting | Update pen firmware and app, then use the app's Sync function to import saved handwriting. | The recovery workflow should collect/sync pen-resident data before reset, unpairing, or migration. |
| Exports | Neo Studio is described as exporting PDF, PNG, and TXT, and sharing with services such as Google Drive, OneNote, and Evernote. | Archive each available export, but label it as a rendered/text derivative. It is not proof that raw stroke timing or pressure is preserved. |
| Current application | Real-time automatic sync is described as Neo Studio 2-only. | Neo Studio 2 is the working bridge; Neo Studio 2022 remains preservation/migration source material. |
| Older hardware | N2 and M1 are stated to still work with Neo Studio, while update and repair options may be limited. | Record pen model and firmware in an archive manifest; avoid firmware/reset actions before collection. |
| Discontinued apps | Neo Notes, Neo Studio 2022, and Pen Manager are described as discontinued; most old notes can be transferred to Neo Studio 2. | Do not uninstall the old app until source data, migration result, and exports have been checked. |

## How this fits the GitHub review

The FAQ explains supported user behavior. It does not change the repository license findings in [NeoSmartpen license audit](neo-license-audit.md): public GPL SDK code remains GPL-3.0, and Ncode generation remains a separate commercial boundary. A support claim that a notebook or export works does not grant rights to copy SDK code, make Ncode patterns, or distribute vendor files.

## Recovery order

1. Keep the old app and pen unchanged.
2. Sync pen-resident handwriting through the official app.
3. Create the device backup and obtain every available PDF, PNG, TXT, recording, or migration result.
4. Compare notebook/page counts and spot-check handwriting after migration.
5. Use NeoLab to hash and organize user-supplied exports, without claiming that rendered exports include raw stroke data.

See [iOS recovery](ios-recovery.md), [NeoLAB Cloud bridge](neolab-cloud.md), and [Ink Vault](ink-vault.md) for the corresponding implementation boundaries.
