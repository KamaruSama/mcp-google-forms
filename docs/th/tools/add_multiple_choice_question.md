# `add_multiple_choice_question`

เพิ่มคำถามแบบตัวเลือก (radio / checkbox / dropdown) พร้อมเฉลย

## Signature

```python
add_multiple_choice_question(
    form_id: str,
    title: str,
    options: list[str],
    correct_answers: list[str],
    points: int = 1,
    kind: Literal["RADIO", "CHECKBOX", "DROP_DOWN"] = "RADIO",
    index: int | None = None,
    required: bool = True,
) -> dict
```

## พารามิเตอร์

| ชื่อ | ประเภท | ค่าเริ่มต้น | คำอธิบาย |
|---|---|---|---|
| `form_id` | `str` | — | form ที่จะแก้ |
| `title` | `str` | — | ข้อความคำถาม |
| `options` | `list[str]` | — | ตัวเลือกที่ผู้ตอบเห็น (≥ 2 ตัว) |
| `correct_answers` | `list[str]` | — | ตัวเลือกที่เป็นเฉลย (ต้องตรงกับใน `options`) |
| `points` | `int` | `1` | คะแนน |
| `kind` | `"RADIO" \| "CHECKBOX" \| "DROP_DOWN"` | `"RADIO"` | ประเภท widget |
| `index` | `int \| None` | ท้าย | ตำแหน่งที่แทรก |
| `required` | `bool` | `True` | บังคับตอบ |

## คืนค่า

Forms API `batchUpdate` response พร้อม `itemId` ใหม่

## ตัวอย่าง

**เลือก 1 (radio)**
```json
{
  "form_id": "1abc...",
  "title": "เมืองหลวงของฝรั่งเศส?",
  "options": ["Paris", "London", "Berlin", "Rome"],
  "correct_answers": ["Paris"]
}
```

**เลือกหลาย (checkbox)**
```json
{
  "form_id": "1abc...",
  "title": "จำนวนเฉพาะ:",
  "options": ["2", "3", "4", "5"],
  "correct_answers": ["2", "3", "5"],
  "kind": "CHECKBOX"
}
```

## หมายเหตุ

- `RADIO` / `DROP_DOWN` — ใส่ `correct_answers` ตัวเดียว
- `CHECKBOX` — ผู้ตอบต้องติ๊ก **ครบ** ตามรายการถึงจะได้คะแนน ติ๊กขาด/เกิน = 0
- ตัวเลือกที่เป็น `""` จะทำให้ API error

---

Part of [mcp-google-forms](../../../README.md) · © 2026 likezara™ · Kamaru
