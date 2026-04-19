# `update_true_false_answer`

แก้เฉลยของข้อถูก/ผิดที่มีอยู่แล้ว (ชื่อและ required flag คงเดิม)

## Signature

```python
update_true_false_answer(
    form_id: str,
    index: int,
    correct_answer: bool,
    points: int = 1,
) -> dict
```

## พารามิเตอร์

| ชื่อ | ประเภท | ค่าเริ่มต้น | คำอธิบาย |
|---|---|---|---|
| `form_id` | `str` | — | form ที่จะแก้ |
| `index` | `int` | — | ตำแหน่ง 0-based |
| `correct_answer` | `bool` | — | `True` → "ถูก"; `False` → "ผิด" |
| `points` | `int` | `1` | คะแนนใหม่ |

## คืนค่า

Forms API `batchUpdate` response

## ตัวอย่าง

```json
{ "form_id": "1abc...", "index": 7, "correct_answer": false }
```

## หมายเหตุ

- สมมุติว่าข้อนั้นสร้างจาก [`add_true_false_question`](add_true_false_question.md) (2 ตัวเลือก "ถูก"/"ผิด") — ถ้าใช้กับข้อประเภทอื่น ตัวเลือกจะถูกทับ
- `index` นอก range → raise `IndexError`

---

Part of [mcp-google-forms](../../../README.md) · © 2026 likezara™ · Kamaru
