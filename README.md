# mcp-google-forms

**MCP server for managing Google Forms — quizzes, grading, images, responses.**

Exposes 19 tools for creating, editing, inspecting, and managing Google Forms through the Model Context Protocol. Built for use with Claude Code, Claude Desktop, or any MCP-compatible client.

📖 **[อ่านภาษาไทย →](README.th.md)**

---

## Tools at a glance

| Section | Tool | Purpose |
|---|---|---|
| Auth | [`auth_status`](docs/en/tools/auth_status.md) | Check OAuth credential state |
| Create / metadata | [`create_quiz_form`](docs/en/tools/create_quiz_form.md) | New form in quiz mode |
| | [`rename_form`](docs/en/tools/rename_form.md) | Change title/description |
| | [`set_quiz_mode`](docs/en/tools/set_quiz_mode.md) | Toggle quiz on/off |
| Read | [`get_form`](docs/en/tools/get_form.md) | Full form JSON |
| | [`list_questions`](docs/en/tools/list_questions.md) | Concise item list |
| | [`verify_answer_keys`](docs/en/tools/verify_answer_keys.md) | Diff current vs expected answer keys |
| Add | [`add_true_false_question`](docs/en/tools/add_true_false_question.md) | Single T/F question |
| | [`batch_add_true_false`](docs/en/tools/batch_add_true_false.md) | Bulk T/F |
| | [`add_multiple_choice_question`](docs/en/tools/add_multiple_choice_question.md) | Radio / checkbox / dropdown |
| | [`add_text_question`](docs/en/tools/add_text_question.md) | Short or paragraph text |
| | [`add_section_header`](docs/en/tools/add_section_header.md) | Page break / section |
| Edit | [`update_question_title`](docs/en/tools/update_question_title.md) | Rename question |
| | [`update_true_false_answer`](docs/en/tools/update_true_false_answer.md) | Re-key a T/F answer |
| | [`delete_question`](docs/en/tools/delete_question.md) | Remove item |
| | [`move_question`](docs/en/tools/move_question.md) | Reorder |
| Responses | [`list_responses`](docs/en/tools/list_responses.md) | All submitted responses |
| | [`get_response`](docs/en/tools/get_response.md) | One response by ID |
| Escape hatch | [`raw_batch_update`](docs/en/tools/raw_batch_update.md) | Raw Forms API calls |

---

## Install

### 1. Enable API + get credentials

1. Go to https://console.cloud.google.com → create/select a project
2. **APIs & Services → Library** → enable **Google Forms API**
3. **OAuth consent screen** → External → add yourself as test user
4. **Credentials → Create Credentials → OAuth client ID → Desktop app**
5. Download JSON → save as:
   ```
   ~/.config/google-forms-mcp/credentials.json
   ```

### 2. Register with Claude Code

```bash
claude mcp add google-forms -s user -- \
  uv run --directory /path/to/mcp-google-forms python server.py
```

### 3. First use

On the first tool call, the server opens a browser for OAuth consent. Token is cached at `~/.config/google-forms-mcp/token.json`.

---

## Scopes

- `forms.body` — create/edit form structure
- `forms.responses.readonly` — read responses
- `drive.file` — attach images via Drive

---

## Support the project ❤

If this tool helps your workflow, consider supporting development:

- **Ko-fi:** https://ko-fi.com/kamaru

---

## Contact

- **Portfolio / general:** k.kamarux@gmail.com
- **Commercial / licensing:** contact@likezara.com

---

Copyright © 2026 **likezara™**. All rights reserved.
Developed by **Kamaru** (pen name).
