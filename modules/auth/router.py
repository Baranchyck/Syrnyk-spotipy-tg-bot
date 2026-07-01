from aiogram import Router
from aiogram import types
from aiogram.filters import Command, CommandStart

router = Router()

@router.message(Command("login"))
async def login(message: types.Message):
    await message.answer("Авторизація через Spotify")

@router.message(Command('status'))
async def status(message: types.Message):
    await message.answer("⏳ Авторизація ще не підключена")