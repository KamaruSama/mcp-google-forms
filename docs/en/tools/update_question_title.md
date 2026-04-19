# `update_question_title`

Change the text/title of the question at a given index.

## Signature

```python
update_question_title(form_id: str, index: int, new_title: str) -> dict
```

## Parameters

| Name | Type | Description |
|---|---|---|
| `form_id` | `str` | Target form |
| `index` | `int` | 0-based item position |
| `new_title` | `str` | Replacement title |

## Returns

Forms API `batchUpdate` response.

## Example

```json
{
  "form_id": "1abc...",
  "index": 3,
  "new_title": "Updated question text"
}
```

## Notes

- Uses `updateMask: "title"` — options, grading, and required flag are preserved.
- Use `list_questions` first to find the right `index`.

---

Part of [mcp-google-forms](../../../README.md) · © 2026 likezara™ · Kamaru
