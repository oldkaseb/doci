from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

def get_reply_markup(user_id):
    return InlineKeyboardMarkup().add(
        InlineKeyboardButton("✉️ پاسخ", callback_data=f"reply:{user_id}"),
        InlineKeyboardButton("⛔ بلاک", callback_data=f"block:{user_id}")
    )
