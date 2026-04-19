# `verify_answer_keys`

เทียบเฉลยปัจจุบันกับเฉลยที่ต้องการ แล้วรายงานที่ตรงและไม่ตรง

## Signature

```python
verify_answer_keys(form_id: str, expected: list[dict]) -> dict
```

## พารามิเตอร์

| ชื่อ | ประเภท | คำอธิบาย |
|---|---|---|
| `form_id` | `str` | form ที่ต้องการ |
| `expected` | `list[{"index": int, "correct": str}]` | เฉลยที่คาดหวัง (ข้อละ 1 รายการ) |

## คืนค่า

```json
{
  "matches":    [{ "index": 0, "title": "...", "expected": "ถูก", "actual": ["ถูก"] }, ...],
  "mismatches": [{ "index": 5, "title": "...", "expected": "ผิด", "actual": ["ถูก"] }, ...]
}
```

## ตัวอย่าง

```json
{
  "form_id": "1abc...",
  "expected": [
    { "index": 0, "correct": "ถูก" },
    { "index": 1, "correct": "ผิด" }
  ]
}
```

## หมายเหตุ

- Logic การแมตช์: `actual == [expected]` หรือ `expected in actual` (รองรับข้อแบบ multi-answer)
- ใช้เช็คหลังแก้ quiz หรือเทียบกับ PDF master ได้

---

Part of [mcp-google-forms](../../../README.md) · © 2026 likezara™ · Kamaru
