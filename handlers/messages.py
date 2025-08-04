from aiogram.types import Message, CallbackQuery
from config import ADMIN_ID
from utils.db import is_admin, save_user, get_users
from utils.state import set_reply
from keyboards.inline import get_reply_markup

async def user_message_handler(message: Message):
    # ❗️ نذاریم پیام ادمین‌ها به عنوان پیام کاربر پردازش بشه
    if is_admin(message.from_user.id):
        return

    user_id = message.from_user.id
    full_name = message.from_user.full_name
    username = message.from_user.username or "ندارد"
    start_time = message.date.strftime("%Y-%m-%d %H:%M:%S")

    # ذخیره اطلاعات کاربر
    save_user(user_id, full_name, username, start_time)

    # ارسال پیام به همه ادمین‌ها
    from utils.db import load_json
    admins = load_json("admins.json")
    for admin_id in admins:
        try:
            await message.bot.send_message(
                int(admin_id),
                f"پیام از:\n👤 {full_name} (@{username}) - {user_id}\n\n{message.text}",
                reply_markup=get_reply_markup(user_id)
            )
        except:
            pass

    await message.reply("پیام شما برای ادمین ارسال شد ✅")
