
from pyrogram import __version__, filters
from pyrogram.types import (InlineKeyboardButton, CallbackQuery,
                            InlineKeyboardMarkup)
from pyrogram.types import Message, InlineKeyboardMarkup, CallbackQuery

@bot.on_callback_query(filters.regex("ekbquery"))
async def callback_query_ekb(bot, query: CallbackQuery):
    data = query.data
    
    if data == "ekbquery":
        await query.message.edit_text(
            f"**File Sharing ProBot**\n\n\n**Owner** : <a href='t.me/FileSharingProBot'>File Sharing Bot</a>\n\n**Language** : <a href='https://www.python.org'>Python 3</a>\n\n**Library** : <a href='https://pyrogram.org'>{__version__}</a>\n\n**Server** : <a href='https://heroku.com'>Heroku</a>\n\n**Channel** : <a href='https://t.me/orewa_void'>Tom Botz</a>\n\n**Developer** : <a href='tg://user?id=OWNER_ID'>Tom</a>",
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup(
                [
                    [InlineKeyboardButton("Close", callback_data="close")]
                ]
            )
        )
    
    elif data == "close":
        try:
            await query.message.delete()
            await query.message.reply_to_message.delete()
        except:
            pass

