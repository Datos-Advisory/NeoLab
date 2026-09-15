# NeoLab product scope v0.1

NeoLab is a user-owned handwriting archive and daily-template system built around NeoLAB-compatible digital ink.

## First product: Ink Vault

**Goal:** keep a user's handwritten work portable and searchable without losing the original trace.

| Input | What NeoLab preserves | What NeoLab may derive |
| --- | --- | --- |
| Neo smartpen event stream | page identity, ordered dots, pressure, time, pen state, source reference | replay, rendering, transcription, keywords, search index |
| Neo Studio export | original file, PDF/SVG/audio, source hash, notebook/page metadata | searchable text and reviewable tags |
| Scan/image | original image/PDF and capture method | OCR text, keywords, page classification |

Raw ink always remains separate from interpretation. A transcription can be corrected, and a keyword can be rejected, without changing the original dots or original export.

## First daily templates

1. **Daily Time Log**: work date, time zone, start/end time, activity, notes, total minutes.
2. **Daily Task List**: date, task, status, priority, notes, review state.

These launch as ordinary templates plus structured exports. Official NeoLAB DIY Ncode PDFs can be used for early pen workflow testing. New NeoLab Ncode forms are a later partnership-controlled release.

## Non-goals for v0.1

- No reverse engineering of Neo Studio private data.
- No copying NeoLAB SDK code or Ncode patterns.
- No automatic rewriting of handwritten text by NLP.
- No claim of NeoLAB, Moleskine, or LAMY endorsement.

## Success check

A user can import one preserved source, render/replay it, export it without loss, and search raw or accepted derived text while seeing where each search result came from.
