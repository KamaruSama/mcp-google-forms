# `set_quiz_mode`

Toggle quiz grading on or off for a form.

## Signature

```python
set_quiz_mode(form_id: str, is_quiz: bool = True) -> dict
```

## Parameters

| Name | Type | Default | Description |
|---|---|---|---|
| `form_id` | `str` | — | Target form |
| `is_quiz` | `bool` | `True` | `True` for quiz (with grading + points); `False` for plain survey |

## Returns

Forms API `batchUpdate` response.

## Example

```json
{ "form_id": "1abc...", "is_quiz": false }
```

## Notes

- When you turn quiz mode **off**, existing questions remain but grading fields can no longer be edited — the API rejects new `grading` objects.
- When you turn it **on**, add questions with answer keys via `add_multiple_choice_question` / `add_true_false_question`.

---

Part of [mcp-google-forms](../../../README.md) · © 2026 likezara™ · Kamaru
