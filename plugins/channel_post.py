
import asyncio
from pyrogram import filters, Client
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram.errors import FloodWait

from config import ADMINS, CHANNEL_ID, DISABLE_CHANNEL_BUTTON
from helper.func import encode

@Client.on_message(filters.private & filters.user(ADMINS) & filters.command(["start", "users", "broadcast", "batch", "genlink"]) | filters.channel & filters.text & filters.incoming & filters.chat(CHANNEL_ID) & ~filters.edited, group=-1)
async def get_bot_channel_post(client, message: Message):
    if message.text and message.text.startswith(("/start", "/users", "/broadcast", "/batch", "/genlink")):
        await asyncio.sleep(2)
        return

    try:
        if not DISABLE_CHANNEL_BUTTON:
            reply_markup = InlineKeyboardMarkup([[InlineKeyboardButton("🔗 SHARE URL", url=f"https://t.me/share/url?url={message.link}")]])
        else:
            reply_markup = None
        await message.copy(chat_id=client._db.db_channel_id, disable_notification=True, reply_markup=reply_markup)
    except FloodWait as e:
        await asyncio.sleep(e.value)
        await get_bot_channel_post(client, message)
    except Exception as e:
        print(f"**something Went Wrong** {e}")
        
    converted_id = message.id
    if message.chat.username:
        string = f"t.me/{message.chat.username}/{converted_id}"
    else:
        string = f"https://t.me/c/{str(message.chat.id)[4:]}/{converted_id}"
        
    link = f"http://t.me/share/url?url={string}"
    
    if not DISABLE_CHANNEL_BUTTON:
        reply_markup = InlineKeyboardMarkup([[InlineKeyboardButton("Here Is Your Inline Link!", url=link)]])
    else:
        reply_markup = None
    await message.reply_text(f"**Here Is Your Inline Link!**", reply_markup=reply_markup, disable_web_page_preview=True)

    await message.reply_text(f"**EDIT THIS**", reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("EDIT BUTTON", callback_data="reply_markup")]]) )

@Client.on_post_message(filters.channel & filters.incoming & ~filters.edited & filters.chat(CHANNEL_ID) & ~filters.media_group, group=-1)
async def edit_post_message(client, message: Message):
    if not DISABLE_CHANNEL_BUTTON:
        reply_markup = InlineKeyboardMarkup([[InlineKeyboardButton("🔗 SHARE URL", url=f"https://t.me/share/url?url={message.link}")]])
    else:
        reply_markup = None
    await message.edit_reply_markup(reply_markup=reply_markup)


@Client.on_post_message(filters.channel & filters.incoming & filters.chat(CHANNEL_ID) & ~filters.edited & filters.media_group, group=-1)
async def get_bot_channel_reply_markup(client, message: Message):
    await asyncio.sleep(2)
    
    converted_id = message.id
    if message.chat.username:
        string = f"t.me/{message.chat.username}/{converted_id}"
    else:
        string = f"https://t.me/c/{str(message.chat.id)[4:]}/{converted_id}"
        
    link = f"http://t.me/share/url?url={string}"
    
    if not DISABLE_CHANNEL_BUTTON:
        reply_markup = InlineKeyboardMarkup([[InlineKeyboardButton("Here Is Your Inline Link!", url=link)]])
    else:
        reply_markup = None
    try:
        await client.edit_message_reply_markup(chat_id=message.chat.id, message_id=message.id, reply_markup=reply_markup)
    except Exception as e:
        print(f"**something Went Wrong** {e}")


