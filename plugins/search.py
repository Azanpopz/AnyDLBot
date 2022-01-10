from pyrogram import Client ,filters
import os
from py_youtube import Data, Search 
from pyrogram.types import *
from config import Config
import os
import ytthumb
import requests
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, InlineQueryResultPhoto
from youtubesearchpython import VideosSearch
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton



import os
import ytthumb
import requests
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, InlineQueryResultPhoto
from youtubesearchpython import VideosSearch





import logging

from pyrogram import Client as app
from pyrogram.types import Message
from youtube_search import YoutubeSearch

logging.basicConfig(
    level=logging.DEBUG, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger(__name__)

import pyrogram

logging.getLogger("pyrogram").setLevel(logging.WARNING)


@Client.on_message(pyrogram.filters.command(["search"]))
async def ytsearch(_, message: Message):
    try:
        if len(message.command) < 2:
            await message.reply_text("/search needs an argument!")
            return
        query = message.text.split(None, 1)[1]
        m = await message.reply_text("Searching....")
        results = YoutubeSearch(query, max_results=4).to_dict()
        i = 0
        text = ""
        while i < 4:
            text += f"Title - {results[i]['title']}\n"
            text += f"Duration - {results[i]['duration']}\n"
            text += f"Views - {results[i]['views']}\n"
            text += f"Channel - {results[i]['channel']}\n"
            text += f"https://youtube.com{results[i]['url_suffix']}\n\n"
            reply_markup = InlineKeyboardMarkup(
            [[InlineKeyboardButton(text="Watch Video 📹", url=f"https://youtube.com"])]]
        )
            i += 1
        await m.edit(text, disable_web_page_preview=True)
    except Exception as e:
        await message.reply_text(str(e))

