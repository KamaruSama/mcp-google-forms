# `add_multiple_choice_question`

Add a choice question (radio, checkbox, or dropdown) with options and an answer key.

## Signature

```python
add_multiple_choice_question(
    form_id: str,
    title: str,
    options: list[str],
    correct_answers: list[str],
    points: int = 1,
    kind: Literal["RADIO", "CHECKBOX", "DROP_DOWN"] = "RADIO",
    index: int | None = None,
    required: bool = True,
) -> dict
```

## Parameters

| Name | Type | Default | Description |
|---|---|---|---|
| `form_id` | `str` | — | Target form |
| `title` | `str` | — | Question text |
| `options` | `list[str]` | — | Visible options (≥ 2) |
| `correct_answers` | `list[str]` | — | Values considered correct — must match entries in `options` |
| `points` | `int` | `1` | Score awarded |
| `kind` | `"RADIO" \| "CHECKBOX" \| "DROP_DOWN"` | `"RADIO"` | Widget type |
| `index` | `int \| None` | end | Insert position |
| `required` | `bool` | `True` | Mandatory answer |

## Returns

Forms API `batchUpdate` response with the new `itemId`.

## Examples

**Single-select (radio)**
```json
{
  "form_id": "1abc...",
  "title": "Capital of France?",
  "options": ["Paris", "London", "Berlin", "Rome"],
  "correct_answers": ["Paris"]
}
```

**Multi-select (checkbox)**
```json
{
  "form_id": "1abc...",
  "title": "Prime numbers:",
  "options": ["2", "3", "4", "5"],
  "correct_answers": ["2", "3", "5"],
  "kind": "CHECKBOX"
}
```

## Notes

- For `RADIO` / `DROP_DOWN`, supply exactly one entry in `correct_answers`.
- For `CHECKBOX`, the user must tick **exactly** the listed set to score — partial matches = 0.
- `kind` is empty-checked — options with `""` value produce API errors.

---

Part of [mcp-google-forms](../../../README.md) · © 2026 likezara™ · Kamaru
