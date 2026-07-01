import asyncio 
import os
from dotenv import load_dotenv

from aiogram import Bot, Dispatcher
from middlewares.logging_middleware import Logging
from aiogram.types import BotCommand

from modules.auth.router import router as auth_router
from modules.common.router import router as common_router

from modules.common.commands import COMMANDS

load_dotenv()

TOKEN = os.getenv("TELEGRAM_TOKEN")

bot = Bot(token=TOKEN)
dp = Dispatcher()
dp.update.middleware(Logging())

dp.include_router(auth_router)
dp.include_router(common_router)

@dp.startup()
async def on_startup():
    await bot.set_my_commands(COMMANDS)

if __name__ == "__main__":
    dp.run_polling(bot)