from flask import Flask, request
import requests

app = Flask(__name__)

CHANNEL_ACCESS_TOKEN = "rNenPUfA3sVKidCeSqGdlw2LZCslHAIVJQoE7RItdtO1PY0+QngLrrFYjc12smDRySGcjIMUFlV1QSfSIBpKtRV8NCxCU5MmTZoXDn5pdHhbPgBmJBtsQh+6j0TPQ//blM+UV113E3u11uBWNotAQQdB04t89/1O/w1cDnyilFU="

@app.route("/callback", methods=["POST"])
def callback():
    body = request.json

    print("\n=== 收到 LINE Event ===")
    print(body)

    for event in body["events"]:

        if event["type"] == "message":

            reply_token = event["replyToken"]
            user_text = event["message"]["text"]

            url = "https://api.line.me/v2/bot/message/reply"

            headers = {
                "Authorization": f"Bearer {CHANNEL_ACCESS_TOKEN}",
                "Content-Type": "application/json"
            }

            data = {
                "replyToken": reply_token,
                "messages": [
                    {
                        "type": "text",
                        "text": f"你剛剛說：{user_text}"
                    }
                ]
            }

            requests.post(url, headers=headers, json=data)

    return "OK"

if __name__ == "__main__":
    app.run(port=5000)