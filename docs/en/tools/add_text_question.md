# `add_text_question`

Add a short-answer or paragraph text question, with an optional answer key (for quiz mode).

## Signature

```python
add_text_question(
    form_id: str,
    title: str,
    correct_answers: list[str] | None = None,
    points: int = 0,
    paragraph: bool = False,
    index: int | None = None,
    required: bool = True,
) -> dict
```

## Parameters

| Name | Type | Default | Description |
|---|---|---|---|
| `form_id` | `str` | — | Target form |
| `title` | `str` | — | Question text |
| `correct_answers` | `list[str] \| None` | `None` | Accepted correct strings (case-sensitive exact match) |
| `points` | `int` | `0` | Score; has no effect unless `correct_answers` is set |
| `paragraph` | `bool` | `False` | `False` = short single-line; `True` = multi-line textarea |
| `index` | `int \| None` | end | Insert position |
| `required` | `bool` | `True` | Mandatory answer |

## Returns

Forms API `batchUpdate` response.

## Examples

**Short answer with key**
```json
{
  "form_id": "1abc...",
  "title": "What is 2 + 2?",
  "correct_answers": ["4", "four"],
  "points": 1
}
```

**Paragraph, no grading (survey)**
```json
{
  "form_id": "1abc...",
  "title": "Any feedback?",
  "paragraph": true,
  "required": false
}
```

## Notes

- Omit `correct_answers` to add a non-graded text question (works even when quiz mode is off).
- Text grading is exact-match; use multiple synonyms in `correct_answers` to accept variations.

---

Part of [mcp-google-forms](../../../README.md) · © 2026 likezara™ · Kamaru
