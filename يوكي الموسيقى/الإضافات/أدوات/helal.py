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
    filters.command(["سورس","السورس"],""))
async def sourc(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://graph.org/file/7f87be8bf898631bc70f5.jpg",
        caption=f"""𝖶𝖾𝗅𝖼𝗈𝗆𝖾 𝗍𝗈 𝗍𝗁𝖾 𝗆𝗈𝗈𝗇 𝗆𝗎𝗌𝗂𝖼 𝖻𝗈𝗍 .""",
        reply_markup=InlineKeyboardMarkup(
            [
            [
                InlineKeyboardButton("السورس", url=f"https://t.me/uzzdd")
                ]
            ]
        ),
    )     
@app.on_message(
    filters.command(["الاوامر"))
async def khalid(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://graph.org/file/1626ce37ecb8ba14ee377.jpg",
        caption=f"""𝑤𝑒𝑙𝑐𝑜𝑚𝑒 {message.from_user.mention}
        
« اليك قائـمة الاوامــر »
          

»**لتشغيل اغنيه اكتب : تشغيل او شغل**
»**لأنهاء الاغنيه اكتب : ايقاف او انهاء**
»**لايقاف الاغنيه مؤقت اكتب : قفي**
»**لتكملة الاغنيه من الايقاف المؤقت اكتب : كمل او استمر**
»**لتخطي الاغنيه اكتب : تخطي او التالي**
»**لكتم البوت في المحادثه اكتب : اسڪتي**
»**لألغاء كتم البوت في المحادثه اكتب : اتكلم او تكلمي**
»**لتحميـل الاغانـي اڪتب : بحث او تحميل**
»**لاعادة تشغيل البوت اكتب** : /restart.""",
      reply_markup=InlineKeyboardMarkup(
            [
            [
                InlineKeyboardButton("السورس", url=f"https://t.me/uzzdd")
                ]
            ]
        ),
