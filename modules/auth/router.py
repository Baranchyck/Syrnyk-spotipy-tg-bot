from aiogram import Router
from aiogram import types
from aiogram.filters import Command, CommandStart

router = Router()

@router.message(Command("login"))
async def login(message: types.Message):
    await message.answer("Авторизація через Spotify")