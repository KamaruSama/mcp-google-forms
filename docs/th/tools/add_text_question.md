# `add_text_question`

เพิ่มคำถามแบบพิมพ์ตอบ (สั้น หรือ paragraph) ใส่เฉลยก็ได้ (ถ้าโหมด quiz)

## Signature

```python
add_text_question(
    form_id: str,
    title: str,
    correct_answers: list[str] | None = None,
    points: int = 0,
    paragraph: bool = False,
    index: int | None = None,
    required: bool = True,
) -> dict
```

## พารามิเตอร์

| ชื่อ | ประเภท | ค่าเริ่มต้น | คำอธิบาย |
|---|---|---|---|
| `form_id` | `str` | — | form ที่จะแก้ |
| `title` | `str` | — | ข้อความคำถาม |
| `correct_answers` | `list[str] \| None` | `None` | คำตอบที่ยอมรับ (case-sensitive เท่ากันเป๊ะ) |
| `points` | `int` | `0` | คะแนน (ไม่มีผลถ้าไม่ใส่ `correct_answers`) |
| `paragraph` | `bool` | `False` | `False` = ช่องเดียว; `True` = textarea หลายบรรทัด |
| `index` | `int \| None` | ท้าย | ตำแหน่งที่แทรก |
| `required` | `bool` | `True` | บังคับตอบ |

## คืนค่า

Forms API `batchUpdate` response

## ตัวอย่าง

**ตอบสั้นพร้อมเฉลย**
```json
{
  "form_id": "1abc...",
  "title": "2 + 2 = ?",
  "correct_answers": ["4", "four", "สี่"],
  "points": 1
}
```

**Paragraph (survey ไม่ให้คะแนน)**
```json
{
  "form_id": "1abc...",
  "title": "ข้อเสนอแนะเพิ่มเติม?",
  "paragraph": true,
  "required": false
}
```

## หมายเหตุ

- ไม่ใส่ `correct_answers` = ข้อแบบไม่ให้คะแนน (ใช้ได้แม้ quiz mode ปิด)
- การเทียบคำตอบเป็น exact match — ใส่ synonym หลายตัวช่วยได้

---

Part of [mcp-google-forms](../../../README.md) · © 2026 likezara™ · Kamaru
