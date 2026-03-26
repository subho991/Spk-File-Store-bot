# Don't Remove Credit @CodeFlix_Bots, @rohit_1888
# Ask Doubt on telegram @CodeflixSupport
#
# Copyright (C) 2025 by Codeflix-Bots@Github, < https://github.com/Codeflix-Bots >.
#
# This file is part of < https://github.com/Codeflix-Bots/FileStore > project,
# and is released under the MIT License.
# Please see < https://github.com/Codeflix-Bots/FileStore/blob/master/LICENSE >
#
# All rights reserved.
#

import os
from os import environ,getenv
import logging
from logging.handlers import RotatingFileHandler

#rohit_1888 on Tg
#--------------------------------------------
#Bot token @Botfather
TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "")
APP_ID = int(os.environ.get("APP_ID", "")) #Your API ID from my.telegram.org
API_HASH = os.environ.get("API_HASH", "") #Your API Hash from my.telegram.org
#--------------------------------------------

CHANNEL_ID = int(os.environ.get("CHANNEL_ID", "")) #Your db channel Id
OWNER = os.environ.get("OWNER", "") # Owner username without @
OWNER_ID = int(os.environ.get("OWNER_ID", "")) # Owner id
#--------------------------------------------
PORT = os.environ.get("PORT", "8001")
#--------------------------------------------
DB_URI = os.environ.get("DATABASE_URL", "")
DB_NAME = os.environ.get("DATABASE_NAME", "Cluooo")
#--------------------------------------------
FSUB_LINK_EXPIRY = int(os.getenv("FSUB_LINK_EXPIRY", "10"))  # 0 means no expiry
BAN_SUPPORT = os.environ.get("BAN_SUPPORT", "http://t.me/CallOwner_Bot")
TG_BOT_WORKERS = int(os.environ.get("TG_BOT_WORKERS", "200"))
#--------------------------------------------
START_PIC = os.environ.get("START_PIC", "https://telegra.ph/file/ec17880d61180d3312d6a.jpg")
FORCE_PIC = os.environ.get("FORCE_PIC", "https://telegra.ph/file/e292b12890b8b4b9dcbd1.jpg")

#--------------------------------------------
# Enable or Disable Verify Mode
VERIFY_MODE = os.environ.get("VERIFY_MODE", "False").lower() == "true"
SHORTLINK_URL = os.environ.get("SHORTLINK_URL", "")
SHORTLINK_API = os.environ.get("SHORTLINK_API", "")
VERIFY_EXPIRE = int(os.environ.get('VERIFY_EXPIRE', 21600)) # Add time in seconds
TUT_VID = os.environ.get("TUT_VID","")

#--------------------------------------------

#--------------------------------------------
HELP_TXT = "<b><blockquote>ᴛʜɪs ɪs ᴀɴ ғɪʟᴇ sᴛᴏʀᴇ ʙᴏᴛ ᴡᴏʀᴋ ғᴏʀ @spklinks\n\n❏ ʙᴏᴛ ᴄᴏᴍᴍᴀɴᴅs\n├/start : sᴛᴀʀᴛ ᴛʜᴇ ʙᴏᴛ\n├/myplan : ᴄʜᴇᴄᴋ ʏᴏᴜʀ ᴘʀᴇᴍɪᴜᴍ sᴛᴀᴛᴜs\n└@CallOwner_Bot : ᴄᴏɴᴛᴀᴄᴛ ʜᴇʀᴇ ᴛᴏ ɢᴇᴛ Membership\n\n sɪᴍᴘʟʏ ᴄʟɪᴄᴋ ᴏɴ ʟɪɴᴋ ᴀɴᴅ sᴛᴀʀᴛ ᴛʜᴇ ʙᴏᴛ ᴊᴏɪɴ ʙᴏᴛʜ ᴄʜᴀɴɴᴇʟs ᴀɴᴅ ᴛʀʏ ᴀɢᴀɪɴ ᴛʜᴀᴛs ɪᴛ.....!\n\n ᴅᴇᴠᴇʟᴏᴘᴇᴅ ʙʏ <a href=https://t.me/spk_links>suvo</a></blockquote></b>"
ABOUT_TXT = "<b><blockquote>◈ ᴄʀᴇᴀᴛᴏʀ: <a href=https://t.me/spk_links>Suvo</a>\n◈ ꜰᴏᴜɴᴅᴇʀ ᴏꜰ : <a href=https://t.me/spk_links> 𝚂𝙿𝙺 𝙻𝙸𝙽𝙺𝚂 </a>\n◈ ᴀɴɪᴍᴇ ᴄʜᴀɴɴᴇʟ : <a href=https://t.me/+SInyGLpoVWw1Nzhl>ᴀɴɪᴍᴇ ᴄʀᴜɪsᴇ</a>\n◈ ᴀᴅᴜʟᴛ ᴄʜᴀɴɴᴇʟ : <a href=https://t.me/spk_links>𝚂𝙿𝙺 𝙻𝙸𝙽𝙺𝚂</a>\n◈ ᴀᴅᴜʟᴛ ᴍᴀɴɢᴀ : <a href=https://t.me/spk_links>ʜᴇɴᴛᴀɪ ᴍᴀɴɢᴀ</a>\n◈ ᴅᴇᴠᴇʟᴏᴘᴇʀ : <a href=https://t.me/spk_links>Suvo</a></blockquote></b>"
#--------------------------------------------
#--------------------------------------------
START_MSG = os.environ.get("START_MESSAGE", "<b>ʜᴇʟʟᴏ {mention}\n\n<blockquote> ɪ ᴀᴍ ғɪʟᴇ sᴛᴏʀᴇ ʙᴏᴛ, ɪ ᴄᴀɴ sᴛᴏʀᴇ ᴘʀɪᴠᴀᴛᴇ ғɪʟᴇs ɪɴ sᴘᴇᴄɪғɪᴇᴅ ᴄʜᴀɴɴᴇʟ ᴀɴᴅ ᴏᴛʜᴇʀ ᴜsᴇʀs ᴄᴀɴ ᴀᴄᴄᴇss ɪᴛ ғʀᴏᴍ sᴘᴇᴄɪᴀʟ ʟɪɴᴋ.</blockquote></b>")
FORCE_MSG = os.environ.get("FORCE_SUB_MESSAGE", "ʜᴇʟʟᴏ {mention}\n\n<b><blockquote>ᴊᴏɪɴ ᴏᴜʀ ᴄʜᴀɴɴᴇʟs ᴀɴᴅ ᴛʜᴇɴ ᴄʟɪᴄᴋ ᴏɴ ʀᴇʟᴏᴀᴅ button ᴛᴏ ɢᴇᴛ ʏᴏᴜʀ ʀᴇǫᴜᴇꜱᴛᴇᴅ ꜰɪʟᴇ.</b></blockquote>")

CMD_TXT = """<blockquote><b>›› ᴀᴅᴍɪɴ ᴄᴏᴍᴍᴀɴᴅꜱ:</b></blockquote>

<blockquote><b>🚀 ɢᴇɴᴇʀᴀʟ</b></blockquote>

<b>›› /start :</b> ꜱᴛᴀʀᴛ ᴛʜᴇ ʙᴏᴛ ᴏʀ ɢᴇᴛ ᴘᴏꜱᴛꜱ  
<b>›› /myplan :</b> ᴄʜᴇᴄᴋ ʏᴏᴜʀ ᴘʀᴇᴍɪᴜᴍ ꜱᴛᴀᴛᴜꜱ  
<b>›› /commands :</b> ᴠɪᴇᴡ ᴀʟʟ ᴀᴠᴀɪʟᴀʙʟᴇ ᴄᴏᴍᴍᴀɴᴅꜱ  

<blockquote><b>🔗 ʟɪɴᴋ ɢᴇɴᴇʀᴀᴛɪᴏɴ</b></blockquote>

<b>›› /batch :</b> ᴄʀᴇᴀᴛᴇ ʟɪɴᴋ ꜰᴏʀ ᴍᴏʀᴇ ᴛʜᴀɴ ᴏɴᴇ ᴘᴏꜱᴛꜱ  
<b>›› /custom_batch :</b> ᴄʀᴇᴀᴛᴇ ᴄᴜꜱᴛᴏᴍ ʙᴀᴛᴄʜ ꜰʀᴏᴍ ᴄʜᴀɴɴᴇʟ/ɢʀᴏᴜᴘ  
<b>›› /genlink :</b> ᴄʀᴇᴀᴛᴇ ʟɪɴᴋ ꜰᴏʀ ᴏɴᴇ ᴘᴏꜱᴛ  

<blockquote><b>📊 ʙᴏᴛ ꜱᴛᴀᴛɪꜱᴛɪᴄꜱ</b></blockquote>

<b>›› /users :</b> ᴠɪᴇᴡ ʙᴏᴛ ꜱᴛᴀᴛɪꜱᴛɪᴄꜱ 
<b>›› /stats :</b> ᴄʜᴇᴄᴋ ʏᴏᴜʀ ʙᴏᴛ ᴜᴘᴛɪᴍᴇ 
<b>›› /count :</b> ᴄᴏᴜɴᴛ ꜱʜᴏʀᴛɴᴇʀ ᴄʟɪᴄᴋꜱ  

<blockquote><b>📢 ʙʀᴏᴀᴅᴄᴀꜱᴛ ᴄᴏᴍᴍᴀɴᴅꜱ</b></blockquote>

<b>›› /broadcast :</b> ʙʀᴏᴀᴅᴄᴀꜱᴛ ᴀɴʏ ᴍᴇꜱꜱᴀɢᴇꜱ ᴛᴏ ʙᴏᴛ ᴜꜱᴇʀꜱ  
<b>›› /dbroadcast :</b> ʙʀᴏᴀᴅᴄᴀꜱᴛ ᴀɴʏ ᴍᴇꜱꜱᴀɢᴇꜱ ᴡɪᴛʜ ᴀᴜᴛᴏ ᴅᴇʟᴇᴛᴇ   
<b>›› /pbroadcast :</b> ᴘɪɴ ᴀ ʙʀᴏᴀᴅᴄᴀꜱᴛ ᴛᴏ ᴀʟʟ ᴜꜱᴇʀ'ꜱ ᴄʜᴀᴛ  

<blockquote><b>⏳ ᴀᴜᴛᴏ ᴅᴇʟᴇᴛᴇ</b></blockquote>

<b>›› /dlt_time :</b> ꜱᴇᴛ ᴀᴜᴛᴏ ᴅᴇʟᴇᴛᴇ ᴛɪᴍᴇ ꜰᴏʀ ꜰɪʟᴇꜱ 
<b>›› /check_dlt_time :</b> ᴄʜᴇᴄᴋ ᴄᴜʀʀᴇɴᴛ ᴅᴇʟᴇᴛᴇ ᴛɪᴍᴇ ꜱᴇᴛᴛɪɴɢ  

<blockquote><b>🚫 ᴜꜱᴇʀ ᴍᴀɴᴀɢᴇᴍᴇɴᴛ</b></blockquote>

<b>›› /ban :</b> ʙᴀɴ ᴀ ᴜꜱᴇʀ ꜰʀᴏᴍ ᴜꜱɪɴɢ ᴛʜᴇ ʙᴏᴛ  
<b>›› /unban :</b> ᴜɴʙᴀɴ ᴀ ᴘʀᴇᴠɪᴏᴜꜱʟʏ ʙᴀɴɴᴇᴅ ᴜꜱᴇʀ   
<b>›› /banlist :</b> ɢᴇᴛ ʟɪꜱᴛ ᴏꜰ ʙᴀɴɴᴇᴅ ᴜꜱᴇʀꜱ  
<b>›› /delreq :</b> ʀᴇᴍᴏᴠᴇ ᴜꜱᴇʀꜱ ᴛʜᴀᴛ ʟᴇꜰᴛ ᴄʜᴀɴɴᴇʟ ᴀɴᴅ ɴᴏᴛ ɢᴇᴛᴛɪɴɢ ʀᴇQᴜᴇꜱᴛ ꜰꜱᴜʙ  

<blockquote><b>📺 ꜰᴏʀᴄᴇ ꜱᴜʙꜱᴄʀɪʙᴇ</b></blockquote>

<b>›› /addchnl :</b> ᴀᴅᴅ ᴀ ᴄʜᴀɴɴᴇʟ ꜰᴏʀ ꜰᴏʀᴄᴇ ꜱᴜʙꜱᴄʀɪᴘᴛɪᴏɴ  
<b>›› /delchnl :</b> ʀᴇᴍᴏᴠᴇ ᴀ ꜰᴏʀᴄᴇ ꜱᴜʙꜱᴄʀɪʙᴇ ᴄʜᴀɴɴᴇʟ  
<b>›› /listchnl :</b> ᴠɪᴇᴡ ᴀʟʟ ᴀᴅᴅᴇᴅ ꜰᴏʀᴄᴇ ꜱᴜʙꜱᴄʀɪʙᴇ ᴄʜᴀɴɴᴇʟꜱ 
<b>›› /fsub_mode :</b> ᴛᴏɢɢʟᴇ ꜰᴏʀᴄᴇ ꜱᴜʙꜱᴄʀɪʙᴇ ᴏɴ ᴏʀ ᴏꜰꜰ 

<blockquote><b>👮 ᴀᴅᴍɪɴ ᴍᴀɴᴀɢᴇᴍᴇɴᴛ</b></blockquote>

<b>›› /add_admin :</b> ᴀᴅᴅ ᴀ ɴᴇᴡ ᴀᴅᴍɪɴ  
<b>›› /deladmin :</b> ʀᴇᴍᴏᴠᴇ ᴀɴ ᴀᴅᴍɪɴ 
<b>›› /admins :</b> ʟɪꜱᴛ ᴀʟʟ ᴄᴜʀʀᴇɴᴛ ᴀᴅᴍɪɴꜱ   

<blockquote><b>⭐ ᴘʀᴇᴍɪᴜᴍ ᴍᴀɴᴀɢᴇᴍᴇɴᴛ</b></blockquote>

<b>›› /addpremium :</b> ɢʀᴀɴᴛ ᴘʀᴇᴍɪᴜᴍ ᴀᴄᴄᴇꜱꜱ ᴛᴏ ᴀ ᴜꜱᴇʀ   
<b>›› /premium_users :</b> ʟɪꜱᴛ ᴀʟʟ ᴘʀᴇᴍɪᴜᴍ ᴜꜱᴇʀꜱ   
<b>›› /remove_premium :</b> ʀᴇᴍᴏᴠᴇ ᴘʀᴇᴍɪᴜᴍ ꜰʀᴏᴍ ᴀ ᴜꜱᴇʀ   
"""
#--------------------------------------------
CUSTOM_CAPTION = os.environ.get("CUSTOM_CAPTION", "<b>• ʙʏ @spklink</b>") #set your Custom Caption here, Keep None for Disable Custom Caption
PROTECT_CONTENT = True if os.environ.get('PROTECT_CONTENT', "True") == "True" else False #set True if you want to prevent users from forwarding files from bot
#--------------------------------------------
#Set true if you want Disable your Channel Posts Share button
DISABLE_CHANNEL_BUTTON = os.environ.get("DISABLE_CHANNEL_BUTTON", "True") == 'True'
#--------------------------------------------
BOT_STATS_TEXT = "<b>BOT UPTIME</b>\n{uptime}"
USER_REPLY_TEXT = "ʙᴀᴋᴋᴀ ! ʏᴏᴜ ᴀʀᴇ ɴᴏᴛ ᴍʏ ꜱᴇɴᴘᴀɪ!!"

#==========================(BUY PREMIUM)====================#

OWNER_TAG = os.environ.get("OWNER_TAG", "@CallOwner_Bot")
UPI_ID = os.environ.get("UPI_ID", "17273797@jio")
QR_PIC = os.environ.get("QR_PIC", "https://telegra.ph/file/3e83c69804826b3cba066-16cffa90cd682570da.jpg")
SCREENSHOT_URL = os.environ.get("SCREENSHOT_URL", "http://t.me/CallOwner_Bot")
#--------------------------------------------
#Time and its price
#3 Days
PRICE1 = os.environ.get("PRICE1", "15 rs")
#7 Days
PRICE2 = os.environ.get("PRICE2", "30 rs")
#1 Month
PRICE3 = os.environ.get("PRICE3", "60 rs")
#2 Month
PRICE4 = os.environ.get("PRICE4", "90 rs")
#3 Month
PRICE5 = os.environ.get("PRICE5", "120 rs")

#===================(END)========================#

LOG_FILE_NAME = "filesharingbot.txt"

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s - %(levelname)s] - %(name)s - %(message)s",
    datefmt='%d-%b-%y %H:%M:%S',
    handlers=[
        RotatingFileHandler(
            LOG_FILE_NAME,
            maxBytes=50000000,
            backupCount=10
        ),
        logging.StreamHandler()
    ]
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)


def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
   
