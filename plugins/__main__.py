import requests
from pyrogram import Client as Bot

from plugins.config import API_HASH
from plugins.config import API_ID
from plugins.config import BG_IMAGE
from plugins.config import BOT_TOKEN
from plugins.services.callsmusic import run

response = requests.get(BG_IMAGE)
file = open("./etc/foreground.png", "wb")
file.write(response.content)
file.close()

bot = Bot(
    ":memory:",
    API_ID,
    API_HASH,
    bot_token=BOT_TOKEN,
    plugins=dict(root="VCsMusicBot.modules"),
)

bot.start()
run()
