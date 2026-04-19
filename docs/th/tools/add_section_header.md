# `add_section_header`

แทรก section header / page break ระหว่างข้อ

## Signature

```python
add_section_header(
    form_id: str,
    title: str,
    description: str | None = None,
    index: int | None = None,
) -> dict
```

## พารามิเตอร์

| ชื่อ | ประเภท | ค่าเริ่มต้น | คำอธิบาย |
|---|---|---|---|
| `form_id` | `str` | — | form ที่จะแก้ |
| `title` | `str` | — | ชื่อ section |
| `description` | `str \| None` | `None` | คำอธิบายใต้ชื่อ section |
| `index` | `int \| None` | ท้าย | ตำแหน่งที่แทรก |

## คืนค่า

Forms API `batchUpdate` response

## ตัวอย่าง

```json
{
  "form_id": "1abc...",
  "title": "ตอนที่ 2 — ความเข้าใจ",
  "description": "ตอบตามบทอ่านด้านบน",
  "index": 10
}
```

## หมายเหตุ

- ใช้ `pageBreakItem` — ผู้ตอบจะเจอหน้าใหม่ด้วย
- ไม่นับเป็นข้อ — ไม่มีคะแนน

---

Part of [mcp-google-forms](../../../README.md) · © 2026 likezara™ · Kamaru
