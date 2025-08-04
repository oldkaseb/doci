from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

def get_reply_markup(user_id: int) -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(inline_keyboard=[
        [
            InlineKeyboardButton(text="✉️ پاسخ", callback_data=f"reply:{user_id}"),
            InlineKeyboardButton(text="⛔️ بلاک", callback_data=f"block:{user_id}")
        ]
    ])
