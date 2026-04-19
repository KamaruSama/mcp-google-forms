# `raw_batch_update`

ทางออกฉุกเฉิน: ส่งคำสั่ง Forms API `batchUpdate` ดิบๆ สำหรับงานที่ dedicated tool ยังไม่มี (เช่น `updateSettings`, `updateFormInfo`, แนบภาพผ่าน `questionItem.image`, `moveItem` ข้าม section)

## Signature

```python
raw_batch_update(form_id: str, requests: list[dict]) -> dict
```

## พารามิเตอร์

| ชื่อ | ประเภท | คำอธิบาย |
|---|---|---|
| `form_id` | `str` | form ที่จะแก้ |
| `requests` | `list[dict]` | Array of `Request` objects ตาม [Forms API docs](https://developers.google.com/forms/api/reference/rest/v1/forms/batchUpdate#Request) |

## คืนค่า

ดิบ `batchUpdate` response: `{"replies": [...], "writeControl": {...}}`

## ตัวอย่าง

**แนบภาพเข้ากับข้อ**
```json
{
  "form_id": "1abc...",
  "requests": [{
    "updateItem": {
      "item": {
        "title": "ข้อ 20 ความลงตัว ESC+CPAR",
        "questionItem": {
          "question": {
            "required": true,
            "grading": { "pointValue": 1, "correctAnswers": { "answers": [{ "value": "ถูก" }] } },
            "choiceQuestion": {
              "type": "RADIO",
              "options": [{ "value": "ถูก" }, { "value": "ผิด" }]
            }
          },
          "image": {
            "sourceUri": "https://drive.google.com/uc?export=view&id=FILE_ID",
            "altText": "PCAR/ESC diagram"
          }
        }
      },
      "location": { "index": 19 },
      "updateMask": "title,questionItem"
    }
  }]
}
```

**ลบแล้วสร้างใหม่ใน transaction เดียว**
```json
{
  "form_id": "1abc...",
  "requests": [
    { "deleteItem": { "location": { "index": 5 } } },
    { "createItem": { "item": { ... }, "location": { "index": 5 } } }
  ]
}
```

## หมายเหตุ

- ทุก request ใน array รันใน **transaction เดียว** — ถ้ามีอะไร fail ไม่มีผล side-effect
- Index จะเลื่อนระหว่าง request ใน batch เดียวกัน (`deleteItem` ที่ index 3 จะทำให้ index 4 → 3 สำหรับ request ถัดไป)
- ใช้ตัวนี้เมื่อไม่มี dedicated tool ถ้ามีใช้ tool ที่มีชื่อเฉพาะจะอ่านง่ายกว่า

---

Part of [mcp-google-forms](../../../README.md) · © 2026 likezara™ · Kamaru
