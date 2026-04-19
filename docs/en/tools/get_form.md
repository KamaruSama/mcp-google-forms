# `get_form`

Fetch the full form definition — metadata, settings, items, and questions.

## Signature

```python
get_form(form_id: str) -> dict
```

## Parameters

| Name | Type | Description |
|---|---|---|
| `form_id` | `str` | Target form |

## Returns

The raw [Google Forms API `forms.get`](https://developers.google.com/forms/api/reference/rest/v1/forms/get) response:

```json
{
  "formId": "1abc...",
  "info": { "title": "...", "documentTitle": "..." },
  "settings": { "quizSettings": { "isQuiz": true } },
  "items": [ ... ],
  "revisionId": "00000005",
  "responderUri": "..."
}
```

## Example

```json
{ "form_id": "1abc..." }
```

## Notes

- Verbose — prefer [`list_questions`](list_questions.md) for a concise item overview.
- `revisionId` is useful for optimistic concurrency (`writeControl`) if doing multi-step edits.

---

Part of [mcp-google-forms](../../../README.md) · © 2026 likezara™ · Kamaru
