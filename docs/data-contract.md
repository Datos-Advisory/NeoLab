# NeoLab data contract v0.1

The model is manual-first; any future pen adapter produces this same data.

| Invariant | Validation |
| --- | --- |
| Template is identifiable | Non-empty `template_id` and `template_version` |
| Day is unambiguous | ISO `YYYY-MM-DD` plus IANA `time_zone` |
| Time is non-negative | `end_time >= start_time`; cross-midnight names the next date |
| Task status is finite | `not_started`, `in_progress`, `blocked`, `done` |
| Human content survives | `raw_text` is immutable |
| NLP is auditable | `source`, `model_version`, `confidence` in [0,1], and `review_status` |

```json
{
  "template_id": "daily-time-log",
  "template_version": "0.1.0",
  "work_date": "2026-09-14",
  "time_zone": "America/New_York",
  "entries": [{"start_time": "09:00", "end_time": "10:30", "raw_text": "Project planning", "duration_minutes": 90}]
}
```

For same-day entries, `duration_minutes = 60 * (end_time - start_time)` in minutes. The value is recomputed during validation and is never trusted as input.

```json
{
  "template_id": "daily-task-list",
  "template_version": "0.1.0",
  "work_date": "2026-09-14",
  "tasks": [{"task_id": "local-001", "raw_text": "Prepare partnership outline", "status": "in_progress", "priority": 2}]
}
```

`priority` is an integer from 1 (highest) through 5 (lowest); `task_id` is unique within one list.

An enrichment record stores a keyword/transcription separately with `source`, `model_version`, `confidence`, and `review_status` (`pending`, `accepted`, `rejected`). Search can index raw text and accepted enrichments with their source labels.
