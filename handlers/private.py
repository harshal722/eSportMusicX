from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

from config import BOT_NAME as bn
from helpers.filters import other_filters2


@Client.on_message(other_filters2)
async def start(_, message: Message):
    await message.reply_photo("https://telegra.ph/file/112048220d9c6db5b752d.jpg")
    await message.reply_text(
        f"""**Hey, I'm {bn} 🎵

I can play music in your group's voice call. And Developed By - [𝗛𝗔𝗥𝗦𝗛](https://t.me/Harsh_722).

Add me to your group and play music freely!**
        """,
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🔱 𝗢𝗪𝗡𝗘𝗥 🔱", url="https://t.me/Harsh_722")
                  ],[
                    InlineKeyboardButton(
                        "🎧 𝗔𝗦𝗦𝗜𝗦𝗧𝗔𝗡𝗧 ", url="https://t.me/IronHeart_Assistant_722"
                    ),
                    InlineKeyboardButton(
                        "🛡 𝗦𝗨𝗣𝗣𝗢𝗥𝗧 🛡", url="https://t.me/ironheartsupport722"
                    )
                ],[ 
                    InlineKeyboardButton(
                        "𝗔𝗗𝗗 𝗧𝗢 𝗚𝗥𝗢𝗨𝗣  🛒", url="https://t.me/Harsh7_Musicbot?startgroup=true"
                    )]
            ]
        ),
     disable_web_page_preview=True
    )

@Client.on_message(filters.command("start") & ~filters.private & ~filters.channel)
async def gstart(_, message: Message):
      await message.reply_text("""**⚡️ 𝗜𝗿𝗼𝗻𝗛𝗲𝗮𝗿𝘁 𝗠𝘂𝘀𝗶𝗰 ⚡️**""",
      reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "⚜ 𝗦𝗨𝗣𝗣𝗢𝗥𝗧 ⚜", url="https://t.me/ironheartsupport722")
                ]
            ]
        )
   )


