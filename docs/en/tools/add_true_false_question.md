# `add_true_false_question`

Append (or insert) a single True/False question with answer key and point value.

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

## Parameters

| Name | Type | Default | Description |
|---|---|---|---|
| `form_id` | `str` | — | Target form |
| `title` | `str` | — | Question text |
| `correct_answer` | `bool` | — | `True` → "ถูก" is correct; `False` → "ผิด" is correct |
| `points` | `int` | `1` | Points awarded for correct answer |
| `index` | `int \| None` | end of form | 0-based position to insert |
| `required` | `bool` | `True` | Whether answering is mandatory |

## Returns

Forms API `batchUpdate` response including the new `itemId`.

## Example

```json
{
  "form_id": "1abc...",
  "title": "The sun rises in the east.",
  "correct_answer": true,
  "points": 1
}
```

## Notes

- The question is rendered as a RADIO with exactly 2 options: "ถูก" and "ผิด" (Thai for True/False).
- Google Forms API has no native T/F type; this tool wraps `choiceQuestion` + `grading.correctAnswers`.

---

Part of [mcp-google-forms](../../../README.md) · © 2026 likezara™ · Kamaru
