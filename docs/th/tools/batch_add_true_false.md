# `batch_add_true_false`

เพิ่มข้อถูก/ผิดทีละหลายข้อใน API call เดียว

## Signature

```python
batch_add_true_false(
    form_id: str,
    questions: list[dict],
    start_index: int | None = None,
    clear_existing: bool = False,
) -> dict
```

## พารามิเตอร์

| ชื่อ | ประเภท | ค่าเริ่มต้น | คำอธิบาย |
|---|---|---|---|
| `form_id` | `str` | — | form ที่จะแก้ |
| `questions` | `list[{"title": str, "correct": bool, "points"?: int, "required"?: bool}]` | — | รายการข้อที่จะเพิ่ม (ตามลำดับ) |
| `start_index` | `int \| None` | ท้าย form | ตำแหน่งเริ่ม (0-based) |
| `clear_existing` | `bool` | `False` | ถ้า `True` — ลบของเก่าทั้งหมดก่อน |

## คืนค่า

Forms API `batchUpdate` response — 1 reply ต่อข้อที่สร้าง

## ตัวอย่าง

```json
{
  "form_id": "1abc...",
  "questions": [
    { "title": "ข้อ 1", "correct": true },
    { "title": "ข้อ 2", "correct": false, "points": 2 },
    { "title": "ข้อ 3", "correct": true }
  ]
}
```

## หมายเหตุ

- ลำดับไม่เปลี่ยน — ข้อแรกไป `start_index`, ข้อที่สองไป `start_index + 1` ฯลฯ
- `clear_existing=True` = ลบทุก item ที่มีอยู่ (รวมถึง section header ด้วย) ใช้ให้ระวัง

---

Part of [mcp-google-forms](../../../README.md) · © 2026 likezara™ · Kamaru
