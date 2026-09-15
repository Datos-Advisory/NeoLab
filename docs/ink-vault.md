# Ink Vault v0.1

Ink Vault is NeoLab's first functional module. It accepts preserved handwriting sources and keeps their raw form intact.

## What it validates

`tools/neolab_validate_strokes.py` verifies a raw-ink session before it is rendered, transcribed, or indexed:

- complete Ncode page identity: section, owner, book, page;
- immutable SHA-256 reference to the source artifact;
- finite x/y coordinates and non-negative pressure;
- non-decreasing timestamps;
- valid pen-down, move, and pen-up ordering;
- complete strokes.

Run it with the synthetic example:

```powershell
python tools/neolab_validate_strokes.py neopen/samples/example-ink-session.json
```

The example is synthetic and contains no personal handwriting. When real data is available, store it under `private/`, keep it out of Git, and validate a copied session there.

## Processing order

```text
source archive / export
        ↓
hash + inventory
        ↓
raw-ink validation
        ↓
render or replay
        ↓
transcription and optional keywords
        ↓
search with provenance
```

NLP results are never allowed to alter raw events. They are a separate interpretation layer with a confidence score and review status.
