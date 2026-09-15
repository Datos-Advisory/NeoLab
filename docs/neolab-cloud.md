# NeoLAB Cloud bridge

NeoLAB Cloud is NeoLAB Convergence's desktop application for uploading and managing handwriting from Neo smart pens. It connects an authenticated user, a paired pen, and NeoLAB services such as NeoStudio Web. It is the supported operational bridge between a physical pen and NeoLab's preservation workflow.

## What it supports today

The public guide describes this sequence:

1. Install NeoLAB Cloud for Windows or macOS.
2. Sign in with a NeoLAB, Google, or Apple account.
3. Agree to the service terms.
4. Pair a Neo smart pen over Bluetooth or connect a supported device such as RECO over USB.
5. Upload handwriting through NeoLAB Cloud and view it in NeoStudio Web.

The Windows guide lists Windows 10 or later, Bluetooth 4.0 or later, Chrome, 2 GB memory, and 100 MB of storage. Treat these as vendor-published minimums, and confirm compatibility with the installed release before relying on them.

## NeoStudio Web connection

NeoStudio Web is the browser-facing part of this supported path. The vendor guide says NeoLAB Cloud must be running before signing in to NeoStudio Web; after login, the Cloud-connected device list is synchronized to the web application.

If no device is listed in NeoStudio Web, use **Connected Devices** → **+ Device Connection**, then choose the pen from the devices detected by the NeoLAB Cloud desktop application. If it is already connected in NeoLAB Cloud, its device list links automatically at NeoStudio Web login.

Writing with an Ncode page using a pen connected through NeoLAB Cloud opens the matching page and displays handwriting in real time. The web app also documents page editing, bookmarks, and notebook locking/renaming.

There is an important capture constraint: one connected pen is assigned to one NeoLAB service/window at a time. When NeoStudio and Grida Board are both open, NeoStudio takes priority until the user explicitly transfers the device. With multiple NeoStudio windows, the most recently opened window receives the connected-device list. For a reliable archive run, keep one NeoStudio Web window open and avoid switching the pen between services.

## MCP status

`neolab-cloud-support` is configured as a Codex MCP server at GitBook's published MCP endpoint. It gives Codex access to the public NeoLAB Cloud support documentation.

It does **not** provide NeoLab access to a user's NeoLAB Cloud account, pen, notebooks, uploads, or raw handwriting. The guide describes an end-user desktop application and sign-in flow; it does not publish a user-data API, OAuth client registration flow, or API key scheme for third-party applications.

## NeoLab integration boundary

Use NeoLAB Cloud as the vendor-supported collection and synchronization bridge:

```text
Neo smart pen → NeoLAB Cloud → NeoStudio Web / supported export → private NeoLab archive
```

NeoLab may ingest files that the user exports or explicitly supplies. It must preserve source files and hashes, then derive searchable text, keywords, and structured records separately. Do not scrape private cloud traffic, reuse browser credentials, or infer undocumented endpoints.

## Next partnership question

To create a direct NeoLab-to-NeoLAB connection, ask NeoLAB Convergence whether it offers a documented partner API or export mechanism that can provide:

- user-authorized notebook/page exports;
- raw stroke events with page identity and timestamps, when available;
- recordings linked to pages;
- OAuth or another revocable authorization method; and
- a license that permits this use.

Until NeoLAB confirms that path, the safe first integration is export/import rather than direct cloud access.

## Sources

- [Introduction to NeoLAB Cloud](https://neolabdev.gitbook.io/neolab-cloud_en/neolab-cloud-guide/introduction-to-neolab-cloud)
- [Download and system requirements](https://neolabdev.gitbook.io/neolab-cloud_en/neolab-cloud-guide/introduction-to-neolab-cloud/download-neolab-cloud)
- [NeoLAB Cloud user guide](https://neolabdev.gitbook.io/neolab-cloud_en/neolab-cloud-guide/how-to-use-neolab-cloud)
- [NeoStudio Web connection guide](https://neolabdev.gitbook.io/neolab-cloud_en/connection-with-neostudio-web-1)
- [NeoStudio Web real-time handwriting](https://neolabdev.gitbook.io/neolab-cloud_en/connection-with-neostudio-web-1/real-time-handwriting)
- [Connected-service switching](https://neolabdev.gitbook.io/neolab-cloud_en/connection-with-neostudio-web-1/conncet-device-change-connected-services)
- [NeoLAB Convergence](https://neolab.net/en)
