# `auth_status`

Report whether the OAuth credentials and token are present on disk.

## Signature

```python
auth_status() -> dict
```

## Parameters

None.

## Returns

```json
{
  "config_dir": "/home/user/.config/google-forms-mcp",
  "credentials_present": true,
  "token_present": false,
  "credentials_path": "/home/user/.config/google-forms-mcp/credentials.json"
}
```

- `credentials_present` → whether `credentials.json` (from Google Cloud Console) exists.
- `token_present` → whether the user has completed OAuth consent and a refresh token is cached.

## Example

```json
{}
```

## Notes

- If `credentials_present` is `false`, place the OAuth desktop JSON at the listed path.
- If `token_present` is `false`, the first tool call will trigger a browser consent flow.

---

Part of [mcp-google-forms](../../../README.md) · © 2026 likezara™ · Kamaru
