from flask import Flask, request, jsonify
import requests
import config

app = Flask(__name__)

SLACK_BOT_TOKEN = config.SLACK_BOT_TOKEN
USER_ID = config.USER_ID  # 본인 Slack 사용자 ID

@app.route("/slack/events", methods=["POST"])
def slack_events():
    data = request.json

    # URL 검증 처리
    if "challenge" in data:
        return jsonify({"challenge": data["challenge"]})

    # reaction_added 이벤트 처리
    if data.get("event", {}).get("type") == "reaction_added":
        event = data["event"]
        item_user = event.get("item_user")  # 반응이 추가된 메시지 작성자
        if item_user == USER_ID:  # 본인의 메시지인지 확인
            reaction = event["reaction"]
            send_message(f"스레드에 '{reaction}' 반응이 추가되었습니다!")

    return jsonify({"status": "ok"})

def send_message(text):
    url = "https://slack.com/api/chat.postMessage"
    headers = {"Authorization": f"Bearer {SLACK_BOT_TOKEN}"}
    payload = {"channel": USER_ID, "text": text}
    requests.post(url, headers=headers, json=payload)

if __name__ == "__main__":
    app.run(port=3000)