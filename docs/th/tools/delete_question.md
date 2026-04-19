# `delete_question`

ลบข้อตาม index ถาวร

## Signature

```python
delete_question(form_id: str, index: int) -> dict
```

## พารามิเตอร์

| ชื่อ | ประเภท | คำอธิบาย |
|---|---|---|
| `form_id` | `str` | form ที่จะแก้ |
| `index` | `int` | ตำแหน่ง 0-based ของข้อที่จะลบ |

## คืนค่า

Forms API `batchUpdate` response

## ตัวอย่าง

```json
{ "form_id": "1abc...", "index": 5 }
```

## หมายเหตุ

- หลังลบ ข้อหลังจากนั้นจะเลื่อนขึ้น 1 ตำแหน่ง — ถ้าลบหลายข้อ loop จาก index สูง → ต่ำ เพื่อไม่ให้เลขเลื่อน
- ลบทันที ไม่มี soft-delete / ไม่มีถาม confirm

---

Part of [mcp-google-forms](../../../README.md) · © 2026 likezara™ · Kamaru
