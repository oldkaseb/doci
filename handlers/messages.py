from aiogram.types import Message, CallbackQuery, InlineKeyboardMarkup, InlineKeyboardButton
from config import ADMIN_ID
from utils.db import is_admin
from utils.state import set_reply, clear_reply
from aiogram import Bot

async def user_message_handler(message: Message):
    from_user = message.from_user
    text = message.text or "[بدون متن]"

    markup = InlineKeyboardMarkup().add(
        InlineKeyboardButton("✉️ پاسخ", callback_data=f"reply:{from_user.id}"),
        InlineKeyboardButton("⛔ بلاک", callback_data=f"block:{from_user.id}")
    )

    admin_bot = Bot.get_current()
    await admin_bot.send_message(ADMIN_ID, f"پیام از {from_user.full_name} (@{from_user.username} - {from_user.id}):\n{text}", reply_markup=markup)
    await message.reply("✅ پیام شما برای ادمین ارسال شد.")

async def admin_reply_callback(call: CallbackQuery):
    user_id = int(call.data.split(":")[1])
    set_reply(call.from_user.id, user_id)
    await call.message.answer(f"✉️ پیام خود را برای کاربر {user_id} ارسال کنید:")

async def block_user_callback(call: CallbackQuery):
    await call.message.answer("⛔ عملکرد بلاک هنوز پیاده‌سازی نشده است.")