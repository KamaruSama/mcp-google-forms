# `rename_form`

Update the form's displayed title, description, and/or Drive document title.

## Signature

```python
rename_form(
    form_id: str,
    title: str | None = None,
    description: str | None = None,
    document_title: str | None = None,
) -> dict
```

## Parameters

| Name | Type | Description |
|---|---|---|
| `form_id` | `str` | Target form |
| `title` | `str \| None` | New respondent-facing title |
| `description` | `str \| None` | New description (appears under title) |
| `document_title` | `str \| None` | New Drive file name |

At least one of the three last args is required.

## Returns

Forms API `batchUpdate` response.

## Example

```json
{
  "form_id": "1abc...",
  "title": "Updated title",
  "description": "Instructions for respondents"
}
```

## Notes

- `updateMask` is built from which fields you supplied — untouched fields are preserved.

---

Part of [mcp-google-forms](../../../README.md) · © 2026 likezara™ · Kamaru
