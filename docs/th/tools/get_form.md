# `get_form`

ดึงข้อมูล form แบบเต็ม — metadata, settings, items, และคำถามทั้งหมด

## Signature

```python
get_form(form_id: str) -> dict
```

## พารามิเตอร์

| ชื่อ | ประเภท | คำอธิบาย |
|---|---|---|
| `form_id` | `str` | form ที่ต้องการ |

## คืนค่า

ผลลัพธ์ดิบจาก [Forms API `forms.get`](https://developers.google.com/forms/api/reference/rest/v1/forms/get):

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

## ตัวอย่าง

```json
{ "form_id": "1abc..." }
```

## หมายเหตุ

- ข้อมูลเยอะ — ถ้าอยากดูแค่ลิสต์ข้อ ใช้ [`list_questions`](list_questions.md) แทน
- `revisionId` ใช้คู่กับ `writeControl` ได้ ถ้าทำ multi-step edit

---

Part of [mcp-google-forms](../../../README.md) · © 2026 likezara™ · Kamaru
