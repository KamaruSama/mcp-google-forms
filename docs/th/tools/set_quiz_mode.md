# `set_quiz_mode`

เปิด/ปิดโหมด Quiz (ให้คะแนน) ของ form

## Signature

```python
set_quiz_mode(form_id: str, is_quiz: bool = True) -> dict
```

## พารามิเตอร์

| ชื่อ | ประเภท | ค่าเริ่มต้น | คำอธิบาย |
|---|---|---|---|
| `form_id` | `str` | — | form ที่จะแก้ |
| `is_quiz` | `bool` | `True` | `True` = เปิด quiz (มีคะแนน); `False` = survey ธรรมดา |

## คืนค่า

Forms API `batchUpdate` response

## ตัวอย่าง

```json
{ "form_id": "1abc...", "is_quiz": false }
```

## หมายเหตุ

- **ปิด** quiz mode — ข้อที่มีอยู่ยังอยู่ แต่แก้ field grading ไม่ได้อีก (API จะปฏิเสธ)
- **เปิด** quiz mode — สามารถใส่เฉลยกับข้อใหม่ผ่าน `add_multiple_choice_question` / `add_true_false_question`

---

Part of [mcp-google-forms](../../../README.md) · © 2026 likezara™ · Kamaru
