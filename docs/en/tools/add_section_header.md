# `add_section_header`

Insert a section header / page-break between questions.

## Signature

```python
add_section_header(
    form_id: str,
    title: str,
    description: str | None = None,
    index: int | None = None,
) -> dict
```

## Parameters

| Name | Type | Default | Description |
|---|---|---|---|
| `form_id` | `str` | — | Target form |
| `title` | `str` | — | Section heading |
| `description` | `str \| None` | `None` | Optional longer text shown below the heading |
| `index` | `int \| None` | end | Insert position |

## Returns

Forms API `batchUpdate` response.

## Example

```json
{
  "form_id": "1abc...",
  "title": "Section 2 — Comprehension",
  "description": "Answer based on the passage above",
  "index": 10
}
```

## Notes

- Implemented via `pageBreakItem` — this also starts a new page for respondents.
- Not counted as a question; doesn't appear in grading.

---

Part of [mcp-google-forms](../../../README.md) · © 2026 likezara™ · Kamaru
