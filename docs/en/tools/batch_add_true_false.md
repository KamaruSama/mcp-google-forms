# `batch_add_true_false`

Bulk-add multiple True/False questions in a single API call.

## Signature

```python
batch_add_true_false(
    form_id: str,
    questions: list[dict],
    start_index: int | None = None,
    clear_existing: bool = False,
) -> dict
```

## Parameters

| Name | Type | Default | Description |
|---|---|---|---|
| `form_id` | `str` | — | Target form |
| `questions` | `list[{"title": str, "correct": bool, "points"?: int, "required"?: bool}]` | — | Questions to add in order |
| `start_index` | `int \| None` | end of form | 0-based insertion start |
| `clear_existing` | `bool` | `False` | If `True`, deletes all existing items first |

## Returns

Forms API `batchUpdate` response — one reply per created item.

## Example

```json
{
  "form_id": "1abc...",
  "questions": [
    { "title": "Q1", "correct": true },
    { "title": "Q2", "correct": false, "points": 2 },
    { "title": "Q3", "correct": true }
  ]
}
```

## Notes

- Order is preserved: the first item ends up at `start_index`, the second at `start_index + 1`, etc.
- `clear_existing=True` is destructive — deletes **all** existing items (including non-question ones).

---

Part of [mcp-google-forms](../../../README.md) · © 2026 likezara™ · Kamaru
