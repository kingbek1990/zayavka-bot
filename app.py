import requests
import time

BOT_TOKEN = "8717622332:AAE5qo9XMC7a4TY6ckNpKRgCysLhf9wNTWQ"
TRELLO_KEY = "6ca88f5a985a209852bcf9eae6f6c6c5"
TRELLO_TOKEN = "ATTAb8ec71a6c12dbc366f8ba6e4f21ef0ce0b48c890d80fd272c8ca1de7d065247143CCD020"
LIST_ID = "LIST_ID = "620b1a3185051d76e3fc3a27""

def get_updates(offset=None):
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/getUpdates"
    params = {"offset": offset}
    return requests.get(url, params=params).json()

def send_message(chat_id, text):
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    params = {
        "chat_id": chat_id,
        "text": text
    }
    requests.get(url, params=params)

def create_card(text):
    url = "https://api.trello.com/1/cards"
    params = {
        "key": TRELLO_KEY,
        "token": TRELLO_TOKEN,
        "idList": LIST_ID,
        "name": text
    }
    requests.post(url, params=params)

last_update_id = None

while True:
    updates = get_updates(last_update_id)

    for update in updates.get("result", []):
        last_update_id = update["update_id"] + 1
        message = update.get("message", {})
        chat_id = message.get("chat", {}).get("id")
        text = message.get("text", "")

        if text.startswith("/zayavka"):
            create_card(text)
            send_message(chat_id, "✅ Trelloga qo‘shildi!")

    time.sleep(2)
