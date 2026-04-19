# `delete_question`

Permanently remove the item at the given index.

## Signature

```python
delete_question(form_id: str, index: int) -> dict
```

## Parameters

| Name | Type | Description |
|---|---|---|
| `form_id` | `str` | Target form |
| `index` | `int` | 0-based item position to delete |

## Returns

Forms API `batchUpdate` response.

## Example

```json
{ "form_id": "1abc...", "index": 5 }
```

## Notes

- After deletion, all items after `index` shift up by 1. If deleting multiple items in a loop, iterate from highest to lowest index to avoid index drift.
- Deletion is immediate — no soft-delete, no confirmation.

---

Part of [mcp-google-forms](../../../README.md) · © 2026 likezara™ · Kamaru
