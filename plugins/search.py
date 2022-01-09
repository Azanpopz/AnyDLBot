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





@Client.on_message(filters.command("srt"))
async def text(bot, update):
    
    text = "Search youtube videos using below buttons.\n\nMade by @FayasNoushad"
    reply_markup = InlineKeyboardMarkup(
        [
            [InlineKeyboardButton(text="Search here", switch_inline_query_current_chat="")],
            [InlineKeyboardButton(text="Search in another chat", switch_inline_query="")]
        ]
    )
    
    

@Client.on_message(filters.command("search"))

async def search(bot, update):
    await message.reply_results
    results = VideosSearch(update.text, limit=5).result()
    answers = []
    
    for result in results:
        thumbnail = ytthumb.thumbnail(result["id"])
        reply_markup = InlineKeyboardMarkup(
            [[InlineKeyboardButton(text="Watch Video 📹", url=result["link"])]]
        )
        
    
    
    await update.reply_text(
        text=risults,
        reply_markup=reply_markup,
        disable_web_page_preview=True,
        quote=True
    )

