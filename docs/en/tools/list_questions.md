# `list_questions`

Return a concise list of the form's items with index, title, answer key, and points.

## Signature

```python
list_questions(form_id: str) -> list[dict]
```

## Parameters

| Name | Type | Description |
|---|---|---|
| `form_id` | `str` | Target form |

## Returns

```json
[
  {
    "index": 0,
    "itemId": "420ba593",
    "title": "1) What is 2+2?",
    "correctAnswer": ["4"],
    "points": 1
  },
  ...
]
```

Non-question items (section headers, info fields) have `correctAnswer: null` and `points: null`.

## Example

```json
{ "form_id": "1abc..." }
```

## Notes

- The `index` is the 0-based location used by `deleteItem` / `updateItem` / `moveItem` operations.

---

Part of [mcp-google-forms](../../../README.md) · © 2026 likezara™ · Kamaru
