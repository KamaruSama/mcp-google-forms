# `rename_form`

แก้ชื่อ form คำอธิบาย หรือชื่อไฟล์ใน Drive

## Signature

```python
rename_form(
    form_id: str,
    title: str | None = None,
    description: str | None = None,
    document_title: str | None = None,
) -> dict
```

## พารามิเตอร์

| ชื่อ | ประเภท | คำอธิบาย |
|---|---|---|
| `form_id` | `str` | form ที่จะแก้ |
| `title` | `str \| None` | ชื่อใหม่ (ที่ผู้ตอบเห็น) |
| `description` | `str \| None` | คำอธิบายใหม่ (ใต้ชื่อ) |
| `document_title` | `str \| None` | ชื่อไฟล์ใน Drive |

ต้องใส่อย่างน้อย 1 ใน 3 ตัวหลัง

## คืนค่า

Forms API `batchUpdate` response

## ตัวอย่าง

```json
{
  "form_id": "1abc...",
  "title": "ชื่อใหม่",
  "description": "คำชี้แจงสำหรับผู้ตอบ"
}
```

## หมายเหตุ

- `updateMask` สร้างจาก field ที่ใส่ — field ที่ไม่ใส่จะไม่ถูกแตะ

---

Part of [mcp-google-forms](../../../README.md) · © 2026 likezara™ · Kamaru
