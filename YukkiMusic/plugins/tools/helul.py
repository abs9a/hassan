import sys
import asyncio
import requests
import re
import string
from pyrogram.types import Message
from aiohttp import ClientSession
from pyrogram import filters, Client
from strings import get_command
from pyrogram.types import (InlineKeyboardButton,CallbackQuery,InlineKeyboardMarkup, Message)
from YukkiMusic import (Apple, Resso, SoundCloud, Spotify, Telegram, YouTube, app)

#########
#الاوامر    
@app.on_message(
    filters.command(["المطور","السورس"],""))
async def khalid(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://graph.org/file/7f87be8bf898631bc70f5.jpg",
        caption=f"""𝖶𝖾𝗅𝖼𝗈𝗆𝖾 𝗍𝗈 𝗍𝗁𝖾 𝗆𝗈𝗈𝗇 𝗆𝗎𝗌𝗂𝖼 𝖻𝗈𝗍 .""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                InlineKeyboardButton("𝖺𝖡𝗌 𝖠𝗁𝗆𝖾𝖽", url=f"https://t.me/r6r8r"),
                ],[
                InlineKeyboardButton(
                        "𝖬𝗒 𝖲𝖳𝗎𝖿𝖿", url=f"https://t.me/uzzdd"),
                ]
            ]
        ),
    )
