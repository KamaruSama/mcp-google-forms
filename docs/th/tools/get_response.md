# `get_response`

ดึงคำตอบ 1 ชุดตาม response ID

## Signature

```python
get_response(form_id: str, response_id: str) -> dict
```

## พารามิเตอร์

| ชื่อ | ประเภท | คำอธิบาย |
|---|---|---|
| `form_id` | `str` | form ที่ต้องการ |
| `response_id` | `str` | ID ของ response (ดูจาก `list_responses`) |

## คืนค่า

คำตอบ 1 ชุด:

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

## ตัวอย่าง

```json
{ "form_id": "1abc...", "response_id": "ACYDB..." }
```

## หมายเหตุ

- `answers` key คือ `questionId` (ไม่ใช่ `itemId`) — อ้างอิงจาก `get_form` → `items[].questionItem.question.questionId`
- ใช้เมื่อมี response ID อยู่แล้ว (จาก email notification หรือ webhook)

---

Part of [mcp-google-forms](../../../README.md) · © 2026 likezara™ · Kamaru
