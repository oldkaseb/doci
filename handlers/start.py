from aiogram.types import Message
from utils.db import save_user

async def start_handler(message: Message):
    save_user(message.from_user.id, message.from_user.full_name, message.from_user.username)
    await message.reply("""
سلام 👋
به ربات خوش آمدید!
پیام خود را ارسال کنید تا به ادمین‌ها منتقل شود.
""")