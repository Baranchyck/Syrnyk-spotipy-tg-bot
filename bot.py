import asyncio 
import os
from dotenv import load_dotenv

from aiogram import Bot, Dispatcher
from modules.auth.router import router as auth_router
from middlewares.logging_middleware import Logging

load_dotenv()

TOKEN = os.getenv("TELEGRAM_TOKEN")

bot = Bot(token=TOKEN)
dp = Dispatcher()
dp.update.middleware(Logging())
# dp.message.middleware(Logging())

dp.include_router(auth_router)

if __name__ == "__main__":
    dp.run_polling(bot)