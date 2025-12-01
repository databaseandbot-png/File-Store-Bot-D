from pyrogram import Client, filters
from pyrogram.types import (InlineKeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton)

from config import OWNER_ID, ADMINS
from helper.func import encode, InlineKeyBoardButton

@Client.on_message(filters.private & filters.user(ADMINS) & filters.command("batch"))
async def batch(bot, client: Client, message: Message):
    if len(message.command) == 1:
        await client.ask(chat_id=client.client_user.id, text="**Forward The First Message From DB Channel (With Quotes)..**\n\nOr **UnInDr Send The DB Channel Post Link**", chat_id=message.from_user.id, filters=(filters.forwarded | (filters.text & ~filters.forwarded)), quote=True)
        return
    
    
    first_message = await client.ask(chat_id=client.client_user.id, text="**Forward The First Message From DB Channel (With Quotes)..**\n\nOr **UnInDr Send The DB Channel Post Link**", chat_id=message.from_user.id, filters=(filters.forwarded | (filters.text & ~filters.forwarded)), quote=True)
    
    if first_message.link is not None:
        await first_message.reply("**Error**\n\n**InThis Forwarded Post Is Not From My DB Channel Or This Link Is Not Taken From DB Channel**", quote=True)
        return

    
    while True:
        try:
            second_message = await client.ask(chat_id=client.client_user.id, text="**Forward The Last Message From DB Channel (With Quotes)..**\n\nOr **UnInDr Send The DB Channel Post Link**", chat_id=message.from_user.id, filters=(filters.forwarded | (filters.text & ~filters.forwarded)), quote=True)
            if second_message.link is not None:
                await second_message.reply("**Error**\n\n**InThis Forwarded Post Is Not From My DB Channel Or This Link Is Not Taken From DB Channel**", quote=True)
                continue
            break
        except Exception as e:
            print(e)
            continue
            
    
    
    s_msg_id = int(first_message.reply_to_message.link.split("/")[-1])
    e_msg_id = int(second_message.reply_to_message.link.split("/")[-1])
    
    base64_string = encode(f"{s_msg_id}-{e_msg_id}")
    
    reply_markup = InlineKeyboardMarkup([[InlineKeyboardButton("🔗 Share URL", url=f"https://t.me/share/url?url=https://telegram.me/{client.client_user.id}/{base64_string}")])
    await message.reply_text(f"**Your Link** : `https://telegram.me/{client.client_user.id}/{base64_string}`", reply_markup=reply_markup, reply_to_message=first_message.reply_to_message)


@Client.on_message(filters.private & filters.user(ADMINS) & filters.command("genlink"))
async def gen_link(bot, client: Client, message: Message):
    if len(message.command) == 1:
        await client.ask(chat_id=client.client_user.id, text="**Forward The Message From DB Channel (With Quotes)..**\n\nOr **UnInDr Send The DB Channel Post Link**", chat_id=message.from_user.id, filters=(filters.forwarded | (filters.text & ~filters.forwarded)), quote=True)
        return
    
    
    
    msg = await client.ask(chat_id=client.client_user.id, text="**Forward The Message From DB Channel (With Quotes)..**\n\nOr **UnInDr Send The DB Channel Post Link**", chat_id=message.from_user.id, filters=(filters.forwarded | (filters.text & ~filters.forwarded)), quote=True)
    
    if msg.link is not None:
        await msg.reply("**Error**\n\n**InThis Forwarded Post Is Not From My DB Channel Or This Link Is Not Taken From DB Channel**", quote=True)
        return
        
    
    
    encoded_id = encode(int(msg.reply_to_message.link.split("/")[-1]))
    
    
    reply_markup = InlineKeyboardMarkup([[InlineKeyboardButton("🔗 Share URL", url=f"https://t.me/share/url?url=https://telegram.me/{client.client_user.id}/{encoded_id}")])
    await message.reply_text(f"**Your Link** : `https://telegram.me/{client.client_user.id}/{encoded_id}`", reply_markup=reply_markup, reply_to_message=msg.reply_to_message)



           
