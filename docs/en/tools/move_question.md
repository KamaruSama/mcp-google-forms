# `move_question`

Move an item from one index to another, shifting other items to make room.

## Signature

```python
move_question(form_id: str, from_index: int, to_index: int) -> dict
```

## Parameters

| Name | Type | Description |
|---|---|---|
| `form_id` | `str` | Target form |
| `from_index` | `int` | Current 0-based position |
| `to_index` | `int` | Destination 0-based position |

## Returns

Forms API `batchUpdate` response.

## Example

```json
{ "form_id": "1abc...", "from_index": 8, "to_index": 2 }
```

## Notes

- The item is **removed** from `from_index` then **inserted** at `to_index` — other items shift accordingly.
- Moving within a form preserves the item's content, options, grading, and responses already submitted.

---

Part of [mcp-google-forms](../../../README.md) · © 2026 likezara™ · Kamaru
