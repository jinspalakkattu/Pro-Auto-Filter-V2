#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) @AlbertEinsteinTG & @Mrk_YT

from pyrogram import filters, Client
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, CallbackQuery
from bot import Translation # pylint: disable=import-error
from bot.database import Database # pylint: disable=import-error

db = Database()

@Client.on_message(filters.command(["start"]) & filters.private, group=1)
async def start(bot, update):
    
    try:
        file_uid = update.command[1]
    except IndexError:
        file_uid = False
    
    if file_uid:
        file_id, file_name, file_caption, file_type = await db.get_file(file_uid)
        
        if (file_id or file_type) == None:
            return
        
        caption = file_caption if file_caption != ("" or None) else ("<code>" + file_name + "</code>")
        
        if file_type == "document":
        
            await bot.send_document(
                chat_id=update.chat.id,
                document = file_id,
                caption = caption,
                parse_mode="html",
                reply_to_message_id=update.message_id,
                reply_markup=InlineKeyboardMarkup(
                    [
                        [
                            InlineKeyboardButton
                                (
                                    '🔰 Official Channel 🔰', url="https://t.me/joinchat/NGvoejZMNlQ5Mjg1"
                                )
                        ]
                    ]
                )
            )

        elif file_type == "video":
        
            await update.bot.send_video(
                chat_id=update.chat.id,
                video = file_id,
                caption = caption,
                parse_mode="html",
                reply_markup=InlineKeyboardMarkup(
                    [
                        [
                            InlineKeyboardButton
                                (
                                    '🔰 Official Channel 🔰', url="https://t.me/joinchat/NGvoejZMNlQ5Mjg1"
                                )
                        ]
                    ]
                )
            )
            
        elif file_type == "audio":
        
            await update.bot.send_audio(
                chat_id=update.chat.id,
                audio = file_id,
                caption = caption,
                parse_mode="html",
                reply_markup=InlineKeyboardMarkup(
                    [
                        [
                            InlineKeyboardButton
                                (
                                    '🔰 Official Channel 🔰', url="https://t.me/joinchat/NGvoejZMNlQ5Mjg1"
                                )
                        ]
                    ]
                )
            )

        else:
            print(file_type)
        
        return

    buttons = [[
        InlineKeyboardButton('♻️ɢʀօʊք♻️', url='https://t.me/Movies_Club_2019'),
        InlineKeyboardButton('🛠️ɦɛʟք🛠️', callback_data="help")
    ],[
        InlineKeyboardButton('🎞️օȶȶ ʊքɖǟȶɛֆ🎞️', url='https://t.me/mcnewmovies')
   ]]
    
    reply_markup = InlineKeyboardMarkup(buttons)
    
    await bot.send_photo(
                chat_id = update.chat.id,
                photo= "https://telegra.ph/file/fe98b3ef0ecd39f908a2f.jpg",
                caption=f"<b>😎ഞാൻ ധാ 👉 @Movies_Club_2019 👈ഇവിടുത്തെ കില്ലാടി ആണ്</b>\n <b><u>😎എന്റെ പവർ കാണാണോ ഗ്രൂപ്പിൽ കേറി വാ</u></b>",
    reply_markup=reply_markup,        reply_to_message_id=update.message_id
            )



@Client.on_message(filters.command(["help"]) & filters.private, group=1)
async def help(bot, update):
    buttons = [[
        InlineKeyboardButton('🏠 𝙷𝚘𝚖𝚎', callback_data='start'),
        InlineKeyboardButton('𝙰𝚋𝚘𝚞𝚝 🚩', callback_data='about')
    ],[
        InlineKeyboardButton('🔐 𝙲𝚕𝚘𝚜𝚎 🔐', callback_data='close')
    ]]
    
    reply_markup = InlineKeyboardMarkup(buttons)
    
    await bot.send_message(
        chat_id=update.chat.id,
        text=Translation.HELP_TEXT,
        reply_markup=reply_markup,
        parse_mode="html",
        reply_to_message_id=update.message_id
    )


@Client.on_message(filters.command(["about"]) & filters.private, group=1)
async def about(bot, update):
    
    buttons = [[
        InlineKeyboardButton('👤 @𝙼𝚛𝚔_𝚈𝚃 👤', url='https://t.me/MRK_YT')
    ],[
        InlineKeyboardButton('👤 @𝙰𝚕𝚋𝚎𝚛𝚝𝙴𝚒𝚗𝚜𝚝𝚎𝚒𝚗𝚃𝙶 👤', url='https://t.me/AlbertEinsteinTG')
    ],[
        InlineKeyboardButton('🏠 𝙷𝚘𝚖𝚎', callback_data='start'),
        InlineKeyboardButton('𝙲𝚕𝚘𝚜𝚎 🔐', callback_data='close')
    ]]
    reply_markup = InlineKeyboardMarkup(buttons)
    
    await bot.send_message(
        chat_id=update.chat.id,
        text=Translation.ABOUT_TEXT,
        reply_markup=reply_markup,
        disable_web_page_preview=True,
        parse_mode="html",
        reply_to_message_id=update.message_id
    )
