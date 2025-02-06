from flask import Flask
from telegram import Bot

app = Flask(__name__)
API_TOKEN = '7551381595:AAHW7Chk4-8OLIwM6D4FQJUZMDLpH5SeFbQ'
bot = Bot(token=API_TOKEN)

@app.route('/')
def index():
    return "Hello, your bot is ready!"

if __name__ == '__main__':
    app.run(debug=True)