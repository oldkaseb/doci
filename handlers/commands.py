from aiogram import types, Dispatcher
from utils.db import get_users, add_admin, remove_admin, is_admin
from config import ADMIN_ID

async def stats_command(message: types.Message):
    if not is_admin(message.from_user.id):
        return
    users = get_users()
    text = f"📊 تعداد کاربران: {len(users)}\n\n"
    for uid, data in users.items():
        text += f"👤 {data['full_name']} | @{data['username']} | {uid} | {data['start_time']}\n"
    await message.reply(text or "کاربری یافت نشد.")

async def forall_command(message: types.Message):
    if not is_admin(message.from_user.id): return
    await message.reply("✉️ لطفاً پیام همگانی را فوروارد یا ارسال کنید.")

async def admin_command(message: types.Message):
    if not is_admin(message.from_user.id): return
    try:
        parts = message.text.split()
        if len(parts) != 3:
            raise Exception()
        action, user_id = parts[1], int(parts[2])
        if action == "add":
            add_admin(user_id)
            await message.reply(f"✅ ادمین {user_id} اضافه شد.")
        elif action == "remove":
            remove_admin(user_id)
            await message.reply(f"✅ ادمین {user_id} حذف شد.")
        else:
            raise Exception()
    except:
        await message.reply("❌ فرمت درست: /admin add 123456 یا /admin remove 123456")

def register_commands(dp: Dispatcher):
    dp.register_message_handler(stats_command, commands=["stats"])
    dp.register_message_handler(forall_command, commands=["forall"])
    dp.register_message_handler(admin_command, commands=["admin"])
