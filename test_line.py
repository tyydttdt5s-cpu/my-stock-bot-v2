import requests

LINE_TOKEN = "你的Channel Access Token"

message = "🚀 股票系統測試成功！LINE推播正常運作"

url = "https://notify-api.line.me/api/notify"

headers = {
    "Authorization": f"Bearer {LINE_TOKEN}"
}

data = {
    "message": message
}

response = requests.post(url, headers=headers, data=data)

print(response.status_code)
print(response.text)