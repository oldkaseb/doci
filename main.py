import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor
from config import BOT_TOKEN
from handlers.commands import register_commands
from handlers.messages import register_messages

bot = Bot(token=BOT_TOKEN, parse_mode=types.ParseMode.HTML)
dp = Dispatcher(bot)

register_commands(dp)
register_messages(dp)

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
