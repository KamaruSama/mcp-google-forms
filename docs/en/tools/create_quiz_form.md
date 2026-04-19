# `create_quiz_form`

Create a new Google Form with quiz grading enabled.

## Signature

```python
create_quiz_form(title: str, document_title: str | None = None) -> dict
```

## Parameters

| Name | Type | Default | Description |
|---|---|---|---|
| `title` | `str` | — | Displayed form title (shown to respondents) |
| `document_title` | `str \| None` | `= title` | File name in Drive |

## Returns

```json
{
  "formId": "1abc...",
  "responderUri": "https://docs.google.com/forms/d/e/.../viewform",
  "editUrl": "https://docs.google.com/forms/d/.../edit"
}
```

## Example

```json
{ "title": "Quiz: การนิเทศการศึกษา", "document_title": "Supervision Quiz" }
```

## Notes

- Quiz mode is enabled automatically via a follow-up `updateSettings` request.
- Keep `formId` — it's required for every subsequent tool call.

---

Part of [mcp-google-forms](../../../README.md) · © 2026 likezara™ · Kamaru
