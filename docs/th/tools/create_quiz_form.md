# `create_quiz_form`

สร้าง Google Form ใหม่ พร้อมเปิดโหมด Quiz

## Signature

```python
create_quiz_form(title: str, document_title: str | None = None) -> dict
```

## พารามิเตอร์

| ชื่อ | ประเภท | ค่าเริ่มต้น | คำอธิบาย |
|---|---|---|---|
| `title` | `str` | — | ชื่อ form ที่ผู้ตอบเห็น |
| `document_title` | `str \| None` | `= title` | ชื่อไฟล์ใน Drive |

## คืนค่า

```json
{
  "formId": "1abc...",
  "responderUri": "https://docs.google.com/forms/d/e/.../viewform",
  "editUrl": "https://docs.google.com/forms/d/.../edit"
}
```

## ตัวอย่าง

```json
{ "title": "แบบทดสอบ: การนิเทศการศึกษา", "document_title": "Supervision Quiz" }
```

## หมายเหตุ

- โหมด Quiz ถูกเปิดอัตโนมัติผ่าน `updateSettings` หลังสร้าง
- เก็บ `formId` ไว้ — ต้องใช้กับ tool อื่นทุกครั้ง

---

Part of [mcp-google-forms](../../../README.md) · © 2026 likezara™ · Kamaru
