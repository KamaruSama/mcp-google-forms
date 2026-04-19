# `add_true_false_question`

เพิ่มข้อถูก/ผิดทีละข้อ พร้อมเฉลยและคะแนน

## Signature

```python
add_true_false_question(
    form_id: str,
    title: str,
    correct_answer: bool,
    points: int = 1,
    index: int | None = None,
    required: bool = True,
) -> dict
```

## พารามิเตอร์

| ชื่อ | ประเภท | ค่าเริ่มต้น | คำอธิบาย |
|---|---|---|---|
| `form_id` | `str` | — | form ที่จะแก้ |
| `title` | `str` | — | ข้อความคำถาม |
| `correct_answer` | `bool` | — | `True` → "ถูก" คือเฉลย; `False` → "ผิด" คือเฉลย |
| `points` | `int` | `1` | คะแนนที่ได้เมื่อตอบถูก |
| `index` | `int \| None` | ท้าย form | ตำแหน่งที่จะแทรก (0-based) |
| `required` | `bool` | `True` | บังคับตอบ |

## คืนค่า

Forms API `batchUpdate` response พร้อม `itemId` ใหม่

## ตัวอย่าง

```json
{
  "form_id": "1abc...",
  "title": "พระอาทิตย์ขึ้นทางทิศตะวันออก",
  "correct_answer": true,
  "points": 1
}
```

## หมายเหตุ

- แสดงเป็น RADIO 2 ตัวเลือก: "ถูก" / "ผิด"
- Forms API ไม่มีชนิด T/F ตรงๆ — ตัวนี้ห่อ `choiceQuestion` + `grading.correctAnswers` ให้

---

Part of [mcp-google-forms](../../../README.md) · © 2026 likezara™ · Kamaru
