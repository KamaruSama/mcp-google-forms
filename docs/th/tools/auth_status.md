# `auth_status`

ตรวจว่าไฟล์ OAuth credential และ token อยู่ในตำแหน่งที่ถูกต้องหรือไม่

## Signature

```python
auth_status() -> dict
```

## พารามิเตอร์

ไม่มี

## คืนค่า

```json
{
  "config_dir": "/home/user/.config/google-forms-mcp",
  "credentials_present": true,
  "token_present": false,
  "credentials_path": "/home/user/.config/google-forms-mcp/credentials.json"
}
```

- `credentials_present` → มีไฟล์ `credentials.json` จาก Google Cloud Console มั้ย
- `token_present` → ผ่าน OAuth consent และ cache refresh token มั้ย

## ตัวอย่าง

```json
{}
```

## หมายเหตุ

- ถ้า `credentials_present: false` — วางไฟล์ JSON ที่ path ที่แสดง
- ถ้า `token_present: false` — ตอนเรียก tool แรกจะเปิด browser ให้ยืนยันสิทธิ์

---

Part of [mcp-google-forms](../../../README.md) · © 2026 likezara™ · Kamaru
