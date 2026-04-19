# mcp-google-forms

**MCP server สำหรับจัดการ Google Forms — ทำข้อสอบ ใส่เฉลย แนบภาพ ดูคำตอบ**

ให้ 19 เครื่องมือสำหรับสร้าง แก้ไข ตรวจสอบ และจัดการ Google Forms ผ่าน Model Context Protocol ใช้ร่วมกับ Claude Code, Claude Desktop หรือ MCP client อื่นๆ ได้

📖 **[Read in English →](README.md)**

---

## สรุปเครื่องมือ

| หมวด | เครื่องมือ | หน้าที่ |
|---|---|---|
| Auth | [`auth_status`](docs/th/tools/auth_status.md) | เช็คสถานะ OAuth credential |
| สร้าง / metadata | [`create_quiz_form`](docs/th/tools/create_quiz_form.md) | สร้าง form ใหม่ในโหมด Quiz |
| | [`rename_form`](docs/th/tools/rename_form.md) | เปลี่ยนชื่อ/คำอธิบาย |
| | [`set_quiz_mode`](docs/th/tools/set_quiz_mode.md) | เปิด/ปิดโหมด Quiz |
| อ่าน | [`get_form`](docs/th/tools/get_form.md) | ดูข้อมูล form แบบเต็ม (JSON) |
| | [`list_questions`](docs/th/tools/list_questions.md) | ลิสต์ข้อทั้งหมดแบบย่อ |
| | [`verify_answer_keys`](docs/th/tools/verify_answer_keys.md) | เทียบเฉลยปัจจุบันกับเฉลยที่คาดหวัง |
| เพิ่มข้อ | [`add_true_false_question`](docs/th/tools/add_true_false_question.md) | เพิ่มข้อถูก/ผิดทีละข้อ |
| | [`batch_add_true_false`](docs/th/tools/batch_add_true_false.md) | เพิ่มข้อถูก/ผิดทีละชุด |
| | [`add_multiple_choice_question`](docs/th/tools/add_multiple_choice_question.md) | เพิ่มข้อแบบตัวเลือก (radio/checkbox/dropdown) |
| | [`add_text_question`](docs/th/tools/add_text_question.md) | เพิ่มข้อตอบแบบข้อความ |
| | [`add_section_header`](docs/th/tools/add_section_header.md) | เพิ่มหัวข้อแบ่งตอน / page break |
| แก้ไข | [`update_question_title`](docs/th/tools/update_question_title.md) | เปลี่ยนชื่อข้อ |
| | [`update_true_false_answer`](docs/th/tools/update_true_false_answer.md) | แก้เฉลยข้อถูก/ผิด |
| | [`delete_question`](docs/th/tools/delete_question.md) | ลบข้อ |
| | [`move_question`](docs/th/tools/move_question.md) | สลับตำแหน่งข้อ |
| คำตอบ | [`list_responses`](docs/th/tools/list_responses.md) | ดูคำตอบทั้งหมด |
| | [`get_response`](docs/th/tools/get_response.md) | ดูคำตอบทีละชุดตาม ID |
| escape hatch | [`raw_batch_update`](docs/th/tools/raw_batch_update.md) | ส่งคำสั่ง Forms API ดิบๆ |

---

## ติดตั้ง

### 1. เปิด API + สร้าง credential

1. เข้า https://console.cloud.google.com → สร้าง/เลือก Project
2. **APIs & Services → Library** → เปิดใช้ **Google Forms API**
3. **OAuth consent screen** → External → เพิ่มตัวเองเป็น test user
4. **Credentials → Create Credentials → OAuth client ID → Desktop app**
5. ดาวน์โหลด JSON → เก็บไว้ที่:
   ```
   ~/.config/google-forms-mcp/credentials.json
   ```

### 2. ลงทะเบียนกับ Claude Code

```bash
claude mcp add google-forms -s user -- \
  uv run --directory /path/to/mcp-google-forms python server.py
```

### 3. ใช้งานครั้งแรก

ครั้งแรกที่เรียก tool ใดๆ server จะเปิด browser ให้อนุมัติ OAuth — token จะถูกเก็บไว้ที่ `~/.config/google-forms-mcp/token.json`

---

## Scopes ที่ใช้

- `forms.body` — สร้าง/แก้ไขโครงสร้าง form
- `forms.responses.readonly` — อ่านคำตอบ
- `drive.file` — แนบภาพผ่าน Drive

---

## สนับสนุนผู้พัฒนา ❤

ถ้าเครื่องมือนี้มีประโยชน์กับคุณ ช่วยสนับสนุนได้ที่:

- **Ko-fi:** https://ko-fi.com/kamaru

---

## ติดต่อ

- **Portfolio / ทั่วไป:** k.kamarux@gmail.com
- **เชิงพาณิชย์ / ลิขสิทธิ์:** contact@likezara.com

---

Copyright © 2026 **likezara™**. สงวนลิขสิทธิ์
พัฒนาโดย **Kamaru** (นามปากกา)
