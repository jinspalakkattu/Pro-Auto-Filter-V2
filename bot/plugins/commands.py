#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) @AlbertEinsteinTG & @Mrk_YT

from pyrogram import filters, Client
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, CallbackQuery
from pyrogram.errors import UserNotParticipant
from bot import Translation # pylint: disable=import-error
from bot.database import Database # pylint: disable=import-error

db = Database()

@Client.on_message(filters.command(["start"]) & filters.private, group=1)
async def start(bot, update):
    update_channel = "@bigmoviesworld"
    try:
        file_uid = update.command[1]
    except IndexError:
        file_uid = False
    
    if file_uid:
        file_id, file_name, file_caption, file_type = await db.get_file(file_uid)
        
        if (file_id or file_type) == None:
            return
      
    if update_channel:
        try:
            user = await bot.get_chat_member(update_channel, update.chat.id)
            if user.status == "kicked out":
               await update.reply_text("🤭 Sorry Dude, You are B A N N E D 🤣🤣🤣")
               return
        except UserNotParticipant:
#             await update.reply_text(f"Join @{update_channel} To Use Me")
            file_link = f"https://t.me/{bot.username}?start={file_uid}"
            await update.reply_text(
                text="❣ READ THIS INSTRUCTION ❣ \n\n🗣️ചോദിക്കുന്ന സിനിമകൾ നിങ്ങൾക്ക് ലഭിക്കണം എന്നുണ്ടെങ്കിൽ നിങ്ങൾ താഴെ കൊടുത്തിട്ടുള്ള ചാനലിൽ ജോയിൻ ചെയ്യണം. ജോയിൻ ചെയ്ത ശേഷം വീണ്ടും ഗ്രൂപ്പിൽ പോയി ആ ബട്ടനിൽ അമർത്തിയാൽ നിങ്ങൾക്ക് ഞാൻ ആ സിനിമ പ്രൈവറ്റ് ആയി അയച്ചു തരുന്നതാണ്..😍 \n\n🗣 In Order To Get The Movie Requested By You in Our Groups, You Will Have To Join Our Official Channel First. After That, Try Accessing That Movie Again From Our Group. I'll Send You That Movie Privately...😍 \n\nJoin Our Main Channel 🙏</b>",
                reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton("📽ɢᴏʀᴜᴘ📽", url="https://t.me/bigmoviesworld"),
                        InlineKeyboardButton("try Again",url=file_link)
                    ]
            ]
        )
    )
                      
            return
        except Exception:
            await update.reply_text("Something Wrong. Contact my Support Group")
            return
    
        
        caption = file_caption if file_caption != ("" or None) else ("<code>" + file_name + "</code>")
        
        if file_type == "document":
        
            await bot.send_document(
                chat_id=update.chat.id,
                document = file_id,
                caption =f"<b>FILM NAME📽️</b>: <code><b> {file_name}</b> </code>\n<b>❤️Join [★Ⓜ️🌀𝚅𝙸𝙴𝚂_𝙲𝙻𝚄𝙱_𝟸⭕️𝟷𝟿™★] For New Movies.</b>\n❤️<u> 𝚃𝚑𝚊𝚗𝚔𝚢𝚘𝚞 𝙵𝚘𝚛 𝚄𝚜𝚒𝚗𝚐 𝙾𝚞𝚛 𝚂𝚎𝚛𝚟𝚒𝚌𝚎 𝙿𝚕𝚎𝚊𝚜𝚎 𝚂𝚞𝚙𝚙𝚘𝚛𝚝 𝚄𝚜 𝙱𝚢 𝚂𝚑𝚊𝚛𝚒𝚗𝚐 𝙾𝚞𝚛 𝙲𝚑𝚊𝚗𝚗𝚎𝚕/𝙶𝚛𝚘𝚞𝚙 𝙻𝚒𝚗𝚔 𝚃𝚘 𝚈𝚘𝚞𝚛 𝙵𝚛𝚒𝚎𝚗𝚍𝚜</u> \n\n❁𝕁𝕠𝕚𝕟 𝕆𝕦𝕣 ℂ𝕙𝕒𝕟𝕟𝕖𝕝𝕤❁  \n⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱  \n📌𝕮𝖍𝖆𝖓𝖓𝖊𝖑: @mcnewmovies➻ \n📌𝕮𝖍𝖆𝖓𝖓𝖊𝖑 : @MCmoviesall➻ \n👥𝕲𝖗𝖔𝖚𝖕 : @Movies_Club_2019 ➻ \n👥𝕲𝖗𝖔𝖚𝖕 : @Movies_Club_2019",
                parse_mode="html",
                reply_to_message_id=update.message_id,
                reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton('𝙎𝙃𝘼𝙍𝙀', url="https://t.me/share/url?url=https%3A//t.me/share/url%3Furl%3Dhttps%253A//t.me/bigmoviesworld")
                ],
                [
                    InlineKeyboardButton('𝙂𝙍𝙊𝙐𝙋', url="https://t.me/bigmoviesworld"),
                    InlineKeyboardButton('𝙊𝙏𝙏 𝙍𝙀𝙇𝙀𝘼𝙎𝙀', url="https://t.me/bigmoviesworld")
                ],
                [
                    InlineKeyboardButton('𝙎𝙐𝙋𝙋𝙊𝙍𝙏', url="https://t.me/bigmoviesworld"),
                    InlineKeyboardButton('𝘾𝙃𝘼𝙉𝙉𝙀𝙇', url="https://t.me/bigmoviesworld")
                ]
            ]
        )
    )

        elif file_type == "video":
        
            await bot.send_video(
                chat_id=update.chat.id,
                video = file_id,
                caption = caption,
                parse_mode="html",
                reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton('𝙎𝙃𝘼𝙍𝙀', url="https://t.me/share/url?url=https%3A//t.me/share/url%3Furl%3Dhttps%253A//t.me/bigmoviesworld")
                ],
                [
                    InlineKeyboardButton('𝙂𝙍𝙊𝙐𝙋', url="https://t.me/bigmoviesworld"),
                    InlineKeyboardButton('𝙊𝙏𝙏 𝙍𝙀𝙇𝙀𝘼𝙎𝙀', url="https://t.me/bigmoviesworld")
                ],
                [
                    InlineKeyboardButton('𝙎𝙐𝙋𝙋𝙊𝙍𝙏', url="https://t.me/bigmoviesworld"),
                    InlineKeyboardButton('𝘾𝙃𝘼𝙉𝙉𝙀𝙇', url="https://t.me/bigmoviesworld")
                ]
            ]
        )
    )
            
        elif file_type == "audio":
        
            await bot.send_audio(
                chat_id=update.chat.id,
                audio = file_id,
                caption = caption,
                parse_mode="html",
                reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton('𝙎𝙃𝘼𝙍𝙀', url="https://t.me/share/url?url=https%3A//t.me/share/url%3Furl%3Dhttps%253A//t.me/bigmoviesworld")
                ],
                [
                    InlineKeyboardButton('𝙂𝙍𝙊𝙐𝙋', url="https://t.me/bigmoviesworld"),
                    InlineKeyboardButton('𝙊𝙏𝙏 𝙍𝙀𝙇𝙀𝘼𝙎𝙀', url="https://t.me/bigmoviesworld")
                ],
                [
                    InlineKeyboardButton('𝙎𝙐𝙋𝙋𝙊𝙍𝙏', url="https://t.me/bigmoviesworld"),
                    InlineKeyboardButton('𝘾𝙃𝘼𝙉𝙉𝙀𝙇', url="https://t.me/bigmoviesworld")
                ]
            ]
        )
    )

        else:
            print(file_type)
        
        return

    buttons = [[
            InlineKeyboardButton('★[ɢʀᴏᴜᴘ]★', url='https://t.me/bigmoviesworld'),
            InlineKeyboardButton('★[ɢʀᴏᴜᴘ]★', url='https://t.me/Mazhatthullikal')
        ],[
            InlineKeyboardButton('★[ᴄʜᴀɴɴᴇʟ]★', url='https://t.me/NAZRIYAUPDATES'),
            InlineKeyboardButton('★[ɢʀᴏᴜᴘ]★', url='https://t.me/Movieslokammalayalam')
        ],[
            InlineKeyboardButton('☬ད D̾E̾V̾ ཌ☬', url='https://t.me/kinzanoufal')
        ]]
    
    reply_markup = InlineKeyboardMarkup(buttons)
                                 
    await bot.send_video(
                chat_id = update.chat.id,
                video= "https://telegra.ph/file/ec5404d035924f1113d8d.mp4",
                caption=f"<b>📍Hello:- {update.from_user.mention}</b> സുഖമാണ?</b>"
                        f"<b><a href='https://t.me/kinzanoufal'>👇Admin</a></b>. \n\n"
                        f"<b>നിങ്ങൾ സിനിമ ചോദിക്കുന്നതിനു മുമ്പ് ടൈപ്പ് ചെയ്തത് ശരിയാണോന്ന് പരിശോധിക്കുക.👍അല്ലെങ്കിൽ മുകളിലുള്ള വീഡിയോ കണ്ടു അത് പോലെ അയക്കുക</b>(25 Sec)",
                parse_mode="html",
    reply_markup=reply_markup,        reply_to_message_id=update.message_id
            )
                    
@Client.on_message(filters.command(["help"]) & filters.private, group=1)
async def help(bot, update):
    buttons = [[
        InlineKeyboardButton('Close', callback_data='close')
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
            InlineKeyboardButton('★[ᴄʜᴀɴɴᴇʟ]★', url='https://t.me/bigmoviesworld'),
            InlineKeyboardButton('★[ɢʀᴏᴜᴘ]★', url='https://t.me/movieslokammalayalam')
        ],[
            InlineKeyboardButton('☬ད D̾E̾V̾ ཌ☬', url='https://t.me/kinzanoufal')
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
