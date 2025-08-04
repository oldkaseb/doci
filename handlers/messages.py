from aiogram import types, Dispatcher
from utils.db import save_user, is_blocked, get_admins
from keyboards.inline import get_reply_markup
from utils.state import set_reply

async def user_message_handler(message: types.Message):
    if message.chat.type != "private":
        return

    if is_blocked(message.from_user.id):
        return

    user_data = {
        "full_name": message.from_user.full_name,
        "username": message.from_user.username,
        "start_time": message.date.strftime("%Y-%m-%d %H:%M:%S")
    }
    save_user(message.from_user.id, user_data)

    for admin_id in get_admins():
        try:
            await message.bot.send_message(
                admin_id,
                f"پیام از <b>{message.from_user.full_name}</b> (@{message.from_user.username} - {message.from_user.id}):\n{message.text}",
                reply_markup=get_reply_markup(message.from_user.id)
            )
        except:
            pass

    await message.reply("✅ پیام شما برای ادمین ارسال شد.")

def register_messages(dp: Dispatcher):
    dp.register_message_handler(user_message_handler, content_types=types.ContentType.TEXT)
