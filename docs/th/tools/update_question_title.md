# `update_question_title`

เปลี่ยนชื่อ/ข้อความของข้อตาม index

## Signature

```python
update_question_title(form_id: str, index: int, new_title: str) -> dict
```

## พารามิเตอร์

| ชื่อ | ประเภท | คำอธิบาย |
|---|---|---|
| `form_id` | `str` | form ที่จะแก้ |
| `index` | `int` | ตำแหน่ง 0-based |
| `new_title` | `str` | ชื่อใหม่ |

## คืนค่า

Forms API `batchUpdate` response

## ตัวอย่าง

```json
{
  "form_id": "1abc...",
  "index": 3,
  "new_title": "ข้อความใหม่"
}
```

## หมายเหตุ

- ใช้ `updateMask: "title"` — ตัวเลือก เฉลย และ flag required ไม่ถูกแตะ
- ใช้ `list_questions` ก่อน เพื่อดู `index` ที่ถูกต้อง

---

Part of [mcp-google-forms](../../../README.md) · © 2026 likezara™ · Kamaru
