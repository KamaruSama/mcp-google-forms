# `list_responses`

ดึงคำตอบทั้งหมดที่ส่งเข้ามาของ form

## Signature

```python
list_responses(form_id: str) -> dict
```

## พารามิเตอร์

| ชื่อ | ประเภท | คำอธิบาย |
|---|---|---|
| `form_id` | `str` | form ที่ต้องการ |

## คืนค่า

ผลลัพธ์ดิบจาก [Forms API `responses.list`](https://developers.google.com/forms/api/reference/rest/v1/forms.responses/list):

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

## ตัวอย่าง

```json
{ "form_id": "1abc..." }
```

## หมายเหตุ

- ใช้ scope `forms.responses.readonly` (server ขอมาให้แล้ว)
- ถ้า form ใหญ่ ใช้ `nextPageToken` ผ่าน [`raw_batch_update`](raw_batch_update.md) เพื่อ paginate

---

Part of [mcp-google-forms](../../../README.md) · © 2026 likezara™ · Kamaru
