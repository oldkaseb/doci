from aiogram.types import Message
from config import ADMIN_ID
from utils.db import get_users, add_admin, remove_admin, is_admin
from utils.state import get_reply, clear_reply

async def stats_handler(message: Message):
    if not is_admin(message.from_user.id): return
    users = get_users()
    text = f"📊 تعداد کاربران: {len(users)}\n\n"
    for uid, data in users.items():
        text += f"👤 {data['full_name']} | @{data['username']} | {uid} | {data['start_time']}\n"

    await message.reply(text or "کاربری یافت نشد.")

async def forall_handler(message: Message):
    if not is_admin(message.from_user.id): return
    await message.reply("✉️ لطفاً پیام همگانی را فوروارد یا ارسال کنید.")

async def add_admin_handler(message: Message):
    if not is_admin(message.from_user.id): return
    try:
        admin_id = int(message.text.split()[2])
        add_admin(admin_id)
        await message.reply(f"✅ ادمین با آیدی {admin_id} افزوده شد.")
    except:
        await message.reply("❌ فرمت دستور نادرست است. مثال: افزودن ادمین 123456789")

async def remove_admin_handler(message: Message):
    if not is_admin(message.from_user.id): return
    try:
        admin_id = int(message.text.split()[2])
        remove_admin(admin_id)
        await message.reply(f"✅ ادمین با آیدی {admin_id} حذف شد.")
    except:
        await message.reply("❌ فرمت دستور نادرست است. مثال: حذف ادمین 123456789")

async def reply_handler(message: Message):
    user_id = get_reply(message.from_user.id)
    if user_id:
        try:
            await message.bot.send_message(user_id, f"✉️ پاسخ ادمین: {message.text}")
            await message.reply("✅ پیام ارسال شد.")
        except:
            await message.reply("❌ ارسال پیام به کاربر ناموفق بود.")
        clear_reply(message.from_user.id)
