# `list_questions`

ลิสต์ข้อใน form แบบย่อ — index, itemId, ชื่อ, เฉลย, คะแนน

## Signature

```python
list_questions(form_id: str) -> list[dict]
```

## พารามิเตอร์

| ชื่อ | ประเภท | คำอธิบาย |
|---|---|---|
| `form_id` | `str` | form ที่ต้องการ |

## คืนค่า

```json
[
  {
    "index": 0,
    "itemId": "420ba593",
    "title": "1) 2+2 = ?",
    "correctAnswer": ["4"],
    "points": 1
  },
  ...
]
```

Item ที่ไม่ใช่คำถาม (section header, info) — `correctAnswer: null`, `points: null`

## ตัวอย่าง

```json
{ "form_id": "1abc..." }
```

## หมายเหตุ

- `index` เป็นเลขตำแหน่ง 0-based ใช้กับ `deleteItem` / `updateItem` / `moveItem`

---

Part of [mcp-google-forms](../../../README.md) · © 2026 likezara™ · Kamaru
