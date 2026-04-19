# `move_question`

ย้ายข้อจาก index หนึ่งไปอีก index — ข้อระหว่างกลางจะเลื่อนให้

## Signature

```python
move_question(form_id: str, from_index: int, to_index: int) -> dict
```

## พารามิเตอร์

| ชื่อ | ประเภท | คำอธิบาย |
|---|---|---|
| `form_id` | `str` | form ที่จะแก้ |
| `from_index` | `int` | ตำแหน่งปัจจุบัน |
| `to_index` | `int` | ตำแหน่งปลายทาง |

## คืนค่า

Forms API `batchUpdate` response

## ตัวอย่าง

```json
{ "form_id": "1abc...", "from_index": 8, "to_index": 2 }
```

## หมายเหตุ

- ข้อถูก **ลบออก** จาก `from_index` แล้ว **แทรก** ที่ `to_index` — ข้ออื่นเลื่อนตาม
- การย้ายภายใน form ไม่กระทบเนื้อหาข้อ ตัวเลือก เฉลย และ response ที่ส่งมาแล้ว

---

Part of [mcp-google-forms](../../../README.md) · © 2026 likezara™ · Kamaru
