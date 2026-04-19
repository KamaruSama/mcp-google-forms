# `verify_answer_keys`

Diff the form's current answer keys against an expected list; report matches and mismatches.

## Signature

```python
verify_answer_keys(form_id: str, expected: list[dict]) -> dict
```

## Parameters

| Name | Type | Description |
|---|---|---|
| `form_id` | `str` | Target form |
| `expected` | `list[{"index": int, "correct": str}]` | Per-item expected correct answer value |

## Returns

```json
{
  "matches":    [{ "index": 0, "title": "...", "expected": "ถูก", "actual": ["ถูก"] }, ...],
  "mismatches": [{ "index": 5, "title": "...", "expected": "ผิด", "actual": ["ถูก"] }, ...]
}
```

## Example

```json
{
  "form_id": "1abc...",
  "expected": [
    { "index": 0, "correct": "ถูก" },
    { "index": 1, "correct": "ผิด" }
  ]
}
```

## Notes

- Match logic: `actual == [expected]` OR `expected in actual` (handles multi-answer questions).
- Great for regression-testing a quiz after edits, or for asserting PDF → form parity.

---

Part of [mcp-google-forms](../../../README.md) · © 2026 likezara™ · Kamaru
