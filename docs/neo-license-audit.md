# NeoSmartpen public GitHub license audit

**Reviewed:** 2026-09-14  
**Scope:** every public repository in [`NeoSmartpen`](https://github.com/NeoSmartpen), including license, notice, copying, and open-source-named files in every tracked folder of each default branch. This is a technical licensing inventory, not legal advice.

## Result

| Repository | State | License evidence | NeoLab handling |
| --- | --- | --- | --- |
| [IOS-SDK](https://github.com/NeoSmartpen/IOS-SDK) | Archived | Root `LICENSE`: GNU GPL v3.0 | Do not copy into a proprietary NeoLab component. |
| [IOS-Sample](https://github.com/NeoSmartpen/IOS-Sample) | Archived | Root `LICENSE`: GNU GPL v3.0 | Treat sample source as GPL-3.0. |
| [Documentations](https://github.com/NeoSmartpen/Documentations) | Active | No license or notice file found | Read/reference only; no reuse or redistribution grant is stated. |
| [UWP-SDK](https://github.com/NeoSmartpen/UWP-SDK) | Active | Root `LICENSE`: GNU GPL v3.0 | Treat source and bundled SDK material as GPL-3.0. |
| [Ncode-SDK](https://github.com/NeoSmartpen/Ncode-SDK) | Archived | No `LICENSE`; README says commercial license is required, with a limited test key for prototypes | Do not copy, deploy, or generate Ncode pages without an explicit NeoLAB license. |
| [Windows-SDK2.0](https://github.com/NeoSmartpen/Windows-SDK2.0) | Active | Root `LICENSE`: GNU GPL v3.0 | Treat source and bundled SDK material as GPL-3.0. |
| [IOS-SDK2.0](https://github.com/NeoSmartpen/IOS-SDK2.0) | Active | Root `LICENSE`: GNU GPL v3.0 | Treat source and bundled SDK material as GPL-3.0. |
| [Android-SDK2.0](https://github.com/NeoSmartpen/Android-SDK2.0) | Active | Root `LICENSE`: GNU GPL v3.0 | Treat source and bundled SDK material as GPL-3.0. |
| [Ncode-SDK2.0](https://github.com/NeoSmartpen/Ncode-SDK2.0) | Active | No `LICENSE`; README says commercial license is required, mentions a limited test key, commercial SDK and unique-page licenses | No copying or production Ncode generation without written permission/license. |
| [iOS-SDK3.0](https://github.com/NeoSmartpen/iOS-SDK3.0) | Active | Root `LICENSE`: GNU GPL v3.0 | Treat source and bundled SDK material as GPL-3.0. |
| [neolab-data-platform](https://github.com/NeoSmartpen/neolab-data-platform) | Archived | No license or notice file found | Reference API documentation only; no code/data reuse permission is stated. |
| [WEB-SDK2.0](https://github.com/NeoSmartpen/WEB-SDK2.0) | Active | Root `LICENSE.txt`: GNU GPL v3.0 | Use only if NeoLab is prepared to meet GPL-3.0 distribution terms or NeoLAB supplies a separate commercial license. |
| [WEB-SDK-Sample](https://github.com/NeoSmartpen/WEB-SDK-Sample) | Active | Root `LICENSE.txt`: GNU GPL v3.0 | Treat sample source as GPL-3.0. |

## What the GPL repositories contain

Each of the nine license files begins **“GNU General Public License, Version 3, 29 June 2007.”** I found no extra permission, linking exception, or separate commercial exception in those license files.

GPL-3.0 permits use, study, and modification. When distributing a covered program or a derivative work, it requires the recipient receive GPL-3.0 rights and the corresponding source under its terms. A NeoLab feature can therefore *interoperate* with a Neo pen without copying GPL SDK code. Copying, modifying, or shipping NeoSmartpen GPL code needs a deliberate GPL-3.0 compliance decision or a separate license from NeoLAB.

## Ncode is a separate commercial boundary

`Ncode-SDK` and `Ncode-SDK2.0` describe themselves as Ncode generation SDKs. Their READMEs use the phrase “open-source library,” but neither repository supplies an open-source license grant. Both say that an Ncode SDK commercial license is required; the newer README also lists unique Ncode page licensing. The specific commercial terms must come directly from NeoLAB and should not be inferred from the historical README prices.

The Ncode paper patterns, page identities, allocation, production keys, and printing workflow must remain outside this public repository unless NeoLAB expressly authorizes their use and distribution.

## Non-code documentation and historical platform repository

Neither `Documentations` nor `neolab-data-platform` includes a repository license. Public availability alone is not a reusable-code or redistribution license. NeoLab may link to the documents, summarize facts with source attribution, and build independently. It should not publish copied PDFs, documentation text, API examples, or data-platform material without permission.

## NeoLab decision

NeoLab stays clean-room and vendor-neutral:

1. Keep our original schema, validator, daily templates, archive manifest, and NLP code independent.
2. Link to official SDKs and Ncode downloads; do not vendor their source, binaries, PDFs, Ncode patterns, or sample projects.
3. Use the NeoLAB Cloud desktop/export flow for user-owned data.
4. Ask NeoLAB for a written commercial SDK/Ncode/partner API license before direct device integration or generated Ncode templates.

## Primary evidence

- [IOS-SDK2.0 GPL-3.0 license](https://github.com/NeoSmartpen/IOS-SDK2.0/blob/c595710361c4627881a8fc0d6435a67a148c52a6/LICENSE)
- [WEB-SDK2.0 license](https://github.com/NeoSmartpen/WEB-SDK2.0/blob/master/LICENSE.txt)
- [Ncode-SDK2.0 licensing section](https://github.com/NeoSmartpen/Ncode-SDK2.0#license)
- [NeoSmartpen organization repositories](https://github.com/NeoSmartpen)
- [GNU GPL-3.0 text](https://www.gnu.org/licenses/gpl-3.0.html)
