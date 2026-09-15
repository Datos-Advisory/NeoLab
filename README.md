# NeoLab

NeoLab is a vendor-neutral project for structured daily paper templates and a future Neo Smartpen/Ncode integration.

| Area | Purpose |
| --- | --- |
| `daily-templates` | Daily Time Log and Daily Task List template definitions and validation rules. |
| `neopen` | A future integration boundary for licensed Neo Smartpen/Ncode capture. |

Read [the evidence-based baseline](docs/baseline.md) and [the data contract](docs/data-contract.md) first.

For old Neo Studio recovery, follow [the private recovery workflow](docs/recovery.md). The included inventory tool reads files without editing them and produces a local manifest; private source data is ignored by Git.

For the vendor-supported desktop-sync route and the limits of the documentation MCP connection, see [NeoLAB Cloud bridge](docs/neolab-cloud.md).

Official NeoLAB-ready Ncode downloads are catalogued in [Ncode papers](docs/ncode-papers.md). They are external vendor files; NeoLab links to them and does not redistribute them.

NeoLab's current direction is documented in [product scope](docs/product-scope.md) and the [official NeoLAB GitHub review](docs/neo-github-review.md). The first deliverable is a local, user-owned Ink Vault that preserves raw handwriting before transcription or NLP.

The repository-level use boundary is recorded in the [NeoSmartpen license audit](docs/neo-license-audit.md).

The first executable component is [Ink Vault](docs/ink-vault.md): it validates a raw-ink session locally before it is replayed, rendered, transcribed, or searched.

## Status

Planning scaffold only. NeoLab has no NeoLAB endorsement, Ncode allocation, print approval, device-support guarantee, or commercial SDK license.

## Principles

1. Preserve raw input and original structured fields.
2. Validate deterministic fields before enrichment.
3. Store NLP suggestions with provenance, confidence, and review status.
4. Use versioned templates and explicit time zones.
5. Do not commit vendor SDKs, Ncode assets, certificates, page ranges, or customer captures.

## License

No license is selected yet. Choose one after deciding whether this will be an open-source template project, a commercial project, or both with separately licensed components.
