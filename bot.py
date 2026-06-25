import asyncio 
import os
from dotenv import load_dotenv

from aiogram import Bot, Dispatcher
from modules.auth.router import router as auth_router

load_dotenv()

TOKEN = os.getenv("TELEGRAM_TOKEN")

bot = Bot(token=TOKEN)
dp = Dispatcher()

dp.include_router(auth_router)


async def main():
    await dp.run_polling(bot)

if __name__ == "__main__":
    dp.run_polling(bot)