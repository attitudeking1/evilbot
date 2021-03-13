from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
import os
import sys
from threading import Thread
from pyrogram import idle, filters
from pyrogram.handlers import MessageHandler
from helpers.wrappers import errors, admins_only


@Client.on_message(
    filters.command("repo")
    & filters.group
    & ~ filters.edited
)
async def start(client: Client, message: Message):
    await message.reply_text(
        "**ELITES MUSIC:** IF YOU WANT TO LISTEN MUSIC IN VOICE CHAT THEN ADD THIS BOT AND @ELITES_MASTER TO GROUP",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "💙 SUPPORT 💙", url="https://t.me/ELITES_SUPPORT"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "💚 MY MASTER 💚", url="https://t.me/VEDIC_MATHS_OWNER"
                    ),
                    InlineKeyboardButton(
                        "💜OFFICIAL CHANNEL💜", url="https://t.me/THE_ELITES_NETWORK"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "❌ Close ❌", callback_data="close"
                    )
                ]
            ]
        )
    )
    
@Client.on_message(
    filters.command("repo")
    & filters.private
    & ~ filters.edited
)
async def start_(client: Client, message: Message):
    await message.reply_text(
       "**ELITES MUSIC:** IF YOU WANT TO LISTEN MUSIC IN VOICE CHAT THEN ADD THIS BOT AND @ELITES_MASTER TO GROUP",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "💙 SUPPORT 💙", url="https://t.me/ELITES_SUPPORT"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "💚 MY MASTER 💚", url="https://t.me/VEDIC_MATHS_OWNER"
                    ),
                    InlineKeyboardButton(
                        "💜OFFICIAL CHANNEL💜", url="https://t.me/THE_ELITES_NETWORK"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "❌ Close ❌", callback_data="close"
                    )
                ]
            ]
        )
    )
