#
# Copyright (C) 2025 by Codeflix-Bots@Github, < https://github.com/Codeflix-Bots >.
#
# This file is part of < https://github.com/Codeflix-Bots/FileStore > project,
# and is released under the MIT License.
# Please see < https://github.com/Codeflix-Bots/FileStore/blob/master/LICENSE >
#
# All rights reserved.

from pyrogram import Client 
from bot import Bot
from config import *
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery
from database.database import *

@Bot.on_callback_query()
async def cb_handler(client: Bot, query: CallbackQuery):

    data = query.data

    if data == "help":
        await query.message.edit_text(
            text=HELP_TXT.format(first=query.from_user.first_name),
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup([
                [InlineKeyboardButton("ʜᴏᴍᴇ", callback_data='start'),
                 InlineKeyboardButton("ᴄʟᴏꜱᴇ", callback_data='close')]
            ])
        )

    elif data == "about":
        await query.message.edit_text(
            text=ABOUT_TXT.format(first=query.from_user.first_name),
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup([
                [InlineKeyboardButton('ʜᴏᴍᴇ', callback_data='start'),
                 InlineKeyboardButton('ᴄʟᴏꜱᴇ', callback_data='close')]
            ])
        )

    elif data == "start":
        await query.message.edit_text(
            text=START_MSG.format(first=query.from_user.first_name),
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup([
                [InlineKeyboardButton("ʜᴇʟᴘ", callback_data='help'),
                 InlineKeyboardButton("ᴀʙᴏᴜᴛ", callback_data='about')]
            ])
        )

    elif data == "premium":
        name = query.from_user.username or query.from_user.first_name
        
        # Try to delete the original message
        try:
            await query.message.delete()
        except:
            pass
        
        # Send premium details with photo
        try:
            # Check if QR_PIC is a valid file_id or URL
            if QR_PIC:
                await client.send_photo(
                    chat_id=query.message.chat.id,
                    photo=QR_PIC,
                    caption=(
                        f"👋 Hello {name}\n\n"
                        f"🎖️ Available Plans :\n\n"
                        f"● {PRICE1}  For 3 Days Prime Membership\n\n"
                        f"● {PRICE2}  For 7 Days Prime Membership\n\n"
                        f"● {PRICE3}  For 1 Month Prime Membership\n\n"
                        f"● {PRICE4}  For 2 Months Prime Membership\n\n"
                        f"● {PRICE5}  For 3 Months Prime Membership\n\n\n"
                        f"💵 Pay via UPI: <code>{UPI_ID}</code>\n\n"
                        f"♻️ After Payment You Will Get Instant Membership\n\n"
                        f"‼️ Must Send Screenshot after payment & If anyone want custom time membrship then ask admin"
                ),
                reply_markup=InlineKeyboardMarkup(
                    [
                        [InlineKeyboardButton("👤 ADMIN 24/7", url=SCREENSHOT_URL)],
                        [InlineKeyboardButton("🔒 Close", callback_data="close")]
                        ]
                    )
                )
            else:
                # If QR_PIC is not set, send just text
                await client.send_message(
                    chat_id=query.message.chat.id,
                    text=(
                        f"👋 **Hello {name}**\n\n"
                        f"🎖️ **Available Plans :**\n\n"
                        f"● `{PRICE1}`  For 3 Days Prime Membership\n\n"
                        f"● `{PRICE2}`  For 7 Days Prime Membership\n\n"
                        f"● `{PRICE3}`  For 1 Month Prime Membership\n\n"
                        f"● `{PRICE4}`  For 2 Months Prime Membership\n\n"
                        f"● `{PRICE5}`  For 3 Months Prime Membership\n\n\n"
                        f"💵 **Pay via UPI:** `<code>{UPI_ID}</code>`\n\n"
                        f"♻️ After payment, send screenshot to admin\n\n"
                        f"‼️ Contact admin for custom plans"
                    ),
                    reply_markup=InlineKeyboardMarkup(
                        [
                            [InlineKeyboardButton("👤 Contact Admin", url=SCREENSHOT_URL)],
                            [InlineKeyboardButton("🔒 Close", callback_data="close")]
                        ]
                    ),
                    disable_web_page_preview=True
                )
        except Exception as e:
            print(f"Error in premium callback: {e}")
            # Fallback: send message without photo if there's an error
            await client.send_message(
                chat_id=query.message.chat.id,
                text=(
                    f"👋 Hello {name}\n\n"
                    f"🎖️ Available Plans :\n\n"
                    f"● {PRICE1}  For 3 Days Prime Membership\n\n"
                    f"● {PRICE2}  For 7 Days Prime Membership\n\n"
                    f"● {PRICE3}  For 1 Month Prime Membership\n\n"
                    f"● {PRICE4}  For 2 Months Prime Membership\n\n"
                    f"● {PRICE5}  For 3 Months Prime Membership\n\n\n"
                    f"💵 Pay via UPI: <code>{UPI_ID}</code>\n\n"
                    f"♻️ After Payment You Will Get Instant Membership\n\n"
                    f"‼️ Must Send Screenshot after payment & If anyone want custom time membrship then ask admin"
                ),
                reply_markup=InlineKeyboardMarkup(
                    [
                        [InlineKeyboardButton("👤 ADMIN 24/7", url=SCREENSHOT_URL)],
                        [InlineKeyboardButton("🔒 Close", callback_data="close")]
                    ]
                ),
                disable_web_page_preview=True
            )

    elif data == "close":
        try:
            await query.message.delete()
        except:
            pass

    elif data.startswith("rfs_ch_"):
        cid = int(data.split("_")[2])
        try:
            chat = await client.get_chat(cid)
            mode = await db.get_channel_mode(cid)
            status = "🟢 ᴏɴ" if mode == "on" else "🔴 ᴏғғ"
            new_mode = "ᴏғғ" if mode == "on" else "on"
            buttons = [
                [InlineKeyboardButton(f"ʀᴇǫ ᴍᴏᴅᴇ {'OFF' if mode == 'on' else 'ON'}", callback_data=f"rfs_toggle_{cid}_{new_mode}")],
                [InlineKeyboardButton("‹ ʙᴀᴄᴋ", callback_data="fsub_back")]
            ]
            await query.message.edit_text(
                f"Channel: {chat.title}\nCurrent Force-Sub Mode: {status}",
                reply_markup=InlineKeyboardMarkup(buttons)
            )
        except Exception:
            await query.answer("Failed to fetch channel info", show_alert=True)

    elif data.startswith("rfs_toggle_"):
        parts = data.split("_")
        if len(parts) >= 3:
            cid = int(parts[2])
            action = parts[3] if len(parts) > 3 else None
            if action:
                mode = "on" if action == "on" else "off"
                await db.set_channel_mode(cid, mode)
                await query.answer(f"Force-Sub set to {'ON' if mode == 'on' else 'OFF'}")

                # Refresh the same channel's mode view
                chat = await client.get_chat(cid)
                status = "🟢 ON" if mode == "on" else "🔴 OFF"
                new_mode = "off" if mode == "on" else "on"
                buttons = [
                    [InlineKeyboardButton(f"ʀᴇǫ ᴍᴏᴅᴇ {'OFF' if mode == 'on' else 'ON'}", callback_data=f"rfs_toggle_{cid}_{new_mode}")],
                    [InlineKeyboardButton("‹ ʙᴀᴄᴋ", callback_data="fsub_back")]
                ]
                await query.message.edit_text(
                    f"Channel: {chat.title}\nCurrent Force-Sub Mode: {status}",
                    reply_markup=InlineKeyboardMarkup(buttons)
                )

    elif data == "fsub_back":
        channels = await db.show_channels()
        buttons = []
        for cid in channels:
            try:
                chat = await client.get_chat(cid)
                mode = await db.get_channel_mode(cid)
                status = "🟢" if mode == "on" else "🔴"
                buttons.append([InlineKeyboardButton(f"{status} {chat.title}", callback_data=f"rfs_ch_{cid}")])
            except:
                continue

        await query.message.edit_text(
            "sᴇʟᴇᴄᴛ ᴀ ᴄʜᴀɴɴᴇʟ ᴛᴏ ᴛᴏɢɢʟᴇ ɪᴛs ғᴏʀᴄᴇ-sᴜʙ ᴍᴏᴅᴇ:",
            reply_markup=InlineKeyboardMarkup(buttons)
        )


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
