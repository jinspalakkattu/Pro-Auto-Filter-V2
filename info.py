import re
from os import environ


auth_channel = environ.get('AUTH_CHANNEL')
AUTH_CHANNEL = int(auth_channel) if auth_channel and id_pattern.search(auth_channel) else auth_channel



default_start_msg = """
**ʜᴀɪ.. ɪ ᴀᴍ ᴍᴏᴠɪᴇꜱ ʟᴏᴋᴀᴍ ᴍᴀʟᴀʏᴀʟᴀᴍ ɢʀᴏᴜᴘ ꜰɪʟᴛᴇʀ ʙᴏᴛ 
"""
START_MSG = environ.get('START_MSG', default_start_msg)

FILE_CAPTION = environ.get("CUSTOM_FILE_CAPTION", "")
OMDB_API_KEY = environ.get("OMDB_API_KEY", "")
if FILE_CAPTION.strip() == "":
    CUSTOM_FILE_CAPTION=None
