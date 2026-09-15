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
- [NeoLAB Convergence](https://neolab.net/en)
