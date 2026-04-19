# `list_responses`

List all submitted responses for a form.

## Signature

```python
list_responses(form_id: str) -> dict
```

## Parameters

| Name | Type | Description |
|---|---|---|
| `form_id` | `str` | Target form |

## Returns

Raw [Google Forms API `responses.list`](https://developers.google.com/forms/api/reference/rest/v1/forms.responses/list) response:

```json
{
  "responses": [
    {
      "responseId": "ACYDB...",
      "createTime": "2026-04-20T10:00:00Z",
      "lastSubmittedTime": "2026-04-20T10:05:00Z",
      "answers": { "<questionId>": { ... } },
      "totalScore": 8.0
    },
    ...
  ],
  "nextPageToken": "..."
}
```

## Example

```json
{ "form_id": "1abc..." }
```

## Notes

- Requires the `forms.responses.readonly` scope (already requested by this server).
- For large forms, paginate using `nextPageToken` via [`raw_batch_update`](raw_batch_update.md) or future pagination support.

---

Part of [mcp-google-forms](../../../README.md) · © 2026 likezara™ · Kamaru
