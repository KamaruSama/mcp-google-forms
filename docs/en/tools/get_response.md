# `get_response`

Fetch a single response by its response ID.

## Signature

```python
get_response(form_id: str, response_id: str) -> dict
```

## Parameters

| Name | Type | Description |
|---|---|---|
| `form_id` | `str` | Target form |
| `response_id` | `str` | Response identifier (from `list_responses`) |

## Returns

A single response object:

```json
{
  "responseId": "ACYDB...",
  "createTime": "2026-04-20T10:00:00Z",
  "answers": {
    "75a0c3fa": { "textAnswers": { "answers": [{ "value": "นาย" }] } },
    ...
  },
  "totalScore": 8.0
}
```

## Example

```json
{ "form_id": "1abc...", "response_id": "ACYDB..." }
```

## Notes

- Keys in `answers` are `questionId` (not `itemId`). Cross-reference via `get_form` → `items[].questionItem.question.questionId`.
- Useful when you already have the response ID from an email notification or webhook.

---

Part of [mcp-google-forms](../../../README.md) · © 2026 likezara™ · Kamaru
