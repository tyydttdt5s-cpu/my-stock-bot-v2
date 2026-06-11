import requests

CHANNEL_ACCESS_TOKEN = "rNenPUfA3sVKidCeSqGdlw2LZCslHAIVJQoE7RItdtO1PY0+QngLrrFYjc12smDRySGcjIMUFlV1QSfSIBpKtRV8NCxCU5MmTZoXDn5pdHhbPgBmJBtsQh+6j0TPQ//blM+UV113E3u11uBWNotAQQdB04t89/1O/w1cDnyilFU="

USER_ID = "Uf9b775044fde7a9ff98dae88fd62e920"

url = "https://api.line.me/v2/bot/message/push"

headers = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {CHANNEL_ACCESS_TOKEN}"
}

data = {
    "to": USER_ID,
    "messages": [
        {
            "type": "text",
            "text": "🚀 股票助手推播測試成功！"
        }
    ]
}

response = requests.post(url, headers=headers, json=data)

print(response.status_code)
print(response.text)