import requests

CHANNEL_ACCESS_TOKEN = "rNenPUfA3sVKidCeSqGdlw2LZCslHAIVJQoE7RItdtO1PY0+QngLrrFYjc12smDRySGcjIMUFlV1QSfSIBpKtRV8NCxCU5MmTZoXDn5pdHhbPgBmJBtsQh+6j0TPQ//blM+UV113E3u11uBWNotAQQdB04t89/1O/w1cDnyilFU="

headers = {
    "Authorization": f"Bearer {CHANNEL_ACCESS_TOKEN}"
}

r = requests.get(
    "https://api.line.me/v2/bot/info",
    headers=headers
)

print(r.status_code)
print(r.text)