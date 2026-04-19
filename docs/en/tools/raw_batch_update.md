# `raw_batch_update`

Escape hatch: send raw Google Forms API `batchUpdate` requests. For operations not covered by the dedicated tools (e.g. `updateSettings`, `updateFormInfo`, image attachments via `questionItem.image`, `moveItem` between sections).

## Signature

```python
raw_batch_update(form_id: str, requests: list[dict]) -> dict
```

## Parameters

| Name | Type | Description |
|---|---|---|
| `form_id` | `str` | Target form |
| `requests` | `list[dict]` | Array of `Request` objects per [Forms API docs](https://developers.google.com/forms/api/reference/rest/v1/forms/batchUpdate#Request) |

## Returns

Raw `batchUpdate` response: `{"replies": [...], "writeControl": {...}}`.

## Examples

**Attach an image to a question**
```json
{
  "form_id": "1abc...",
  "requests": [{
    "updateItem": {
      "item": {
        "title": "ข้อ 20 ความลงตัว ESC+CPAR",
        "questionItem": {
          "question": {
            "required": true,
            "grading": { "pointValue": 1, "correctAnswers": { "answers": [{ "value": "ถูก" }] } },
            "choiceQuestion": {
              "type": "RADIO",
              "options": [{ "value": "ถูก" }, { "value": "ผิด" }]
            }
          },
          "image": {
            "sourceUri": "https://drive.google.com/uc?export=view&id=FILE_ID",
            "altText": "PCAR/ESC diagram"
          }
        }
      },
      "location": { "index": 19 },
      "updateMask": "title,questionItem"
    }
  }]
}
```

**Rebuild a question atomically**
```json
{
  "form_id": "1abc...",
  "requests": [
    { "deleteItem": { "location": { "index": 5 } } },
    { "createItem": { "item": { ... }, "location": { "index": 5 } } }
  ]
}
```

## Notes

- All requests run **in a single transaction** — if any fails, none are applied.
- Indexes shift between requests in the same batch (a `deleteItem` at index 3 moves index 4 → 3 for subsequent requests).
- Use this when a dedicated tool doesn't exist; prefer named tools for clarity.

---

Part of [mcp-google-forms](../../../README.md) · © 2026 likezara™ · Kamaru
