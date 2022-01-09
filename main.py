import os
import asyncio
from urllib.parse import urlparse
from pyrogram.errors import UserNotParticipant, UserBannedInChannel
from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from youtube_dl import YoutubeDL
from opencc import OpenCC
from config import Config
import wget

import os
import logging
import pyrogram
from config import Config  

if __name__ == "__main__" :
    plugins = dict(
        root="plugins"
    )
    Jebot= pyrogram.Client(
        "CaptionBot",
        bot_token=Config.BOT_TOKEN,
        api_id=Config.API_ID,
        api_hash=Config.API_HASH,
        plugins=plugins,
        workers=300
    )
    



print(
    """
Bot Started!
Join @Infinity_BOTs
"""
)

Jebot.run()
