from aiogram.types import Message, CallbackQuery
from aiogram import types
from utils.db import get_users, is_admin
from utils.state import set_reply, get_reply, clear_reply
from keyboards.inline import get_reply_markup

async def user_message_handler(message: Message):
    if is_admin(message.from_user.id):
        return  # ادمین پیام نفرسته به خودش

    user_id = str(message.from_user.id)
    full_name = message.from_user.full_name
    username = message.from_user.username or "ندارد"
    text = message.text

    from config import ADMIN_ID
    from utils.db import get_admins

    # ارسال پیام برای همه ادمین‌ها
    for admin in get_admins():
        await message.bot.send_message(
            admin,
            f"پیام از {full_name} (@{username} - {user_id}):\n{text}",
            reply_markup=get_reply_markup(user_id),
        )

async def admin_reply_callback(callback: CallbackQuery):
    user_id = callback.data.split(":")[1]
    set_reply(callback.from_user.id, int(user_id))
    await callback.message.answer("✉️ لطفاً پیام خود را برای پاسخ بنویسید.")
    await callback.answer()

async def block_user_callback(callback: CallbackQuery):
    user_id = callback.data.split(":")[1]
    from utils.db import block_user
    block_user(int(user_id))
    await callback.message.answer("⛔️ کاربر بلاک شد.")
    await callback.answer()
