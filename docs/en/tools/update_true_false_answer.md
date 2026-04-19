# `update_true_false_answer`

Update the answer key (correct True/False) of an existing T/F question. Preserves the title and required flag.

## Signature

```python
update_true_false_answer(
    form_id: str,
    index: int,
    correct_answer: bool,
    points: int = 1,
) -> dict
```

## Parameters

| Name | Type | Default | Description |
|---|---|---|---|
| `form_id` | `str` | — | Target form |
| `index` | `int` | — | 0-based item position |
| `correct_answer` | `bool` | — | `True` → "ถูก"; `False` → "ผิด" |
| `points` | `int` | `1` | Updated point value |

## Returns

Forms API `batchUpdate` response.

## Example

```json
{ "form_id": "1abc...", "index": 7, "correct_answer": false }
```

## Notes

- Assumes the item is a T/F question built by [`add_true_false_question`](add_true_false_question.md) (2 options: "ถูก"/"ผิด"). Using it on other question types will replace options and break the item.
- Raises `IndexError` if `index` is out of range.

---

Part of [mcp-google-forms](../../../README.md) · © 2026 likezara™ · Kamaru
