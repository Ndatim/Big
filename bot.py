from flask import Flask, request
import telegram

TOKEN = "7551381595:AAHW7Chk4-8OLIwM6D4FQJUZMDLpH5SeFbQ"
bot = telegram.Bot(token=TOKEN)

app = Flask(__name__)

@app.route("/", methods=["GET"])
def home():
    return "Bot is running!"

@app.route(f"/{TOKEN}", methods=["POST"])
def respond():
    update = telegram.Update.de_json(request.get_json(force=True), bot)
    chat_id = update.message.chat.id
    bot.send_message(chat_id=chat_id, text="Hello!")
    return "OK"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
