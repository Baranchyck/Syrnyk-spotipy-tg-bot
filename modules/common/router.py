from aiogram import Router, types
from aiogram.filters import Command, CommandStart

from modules.common.commands import COMMANDS

router = Router()

@router.message(CommandStart())
async def start(message: types.Message):
    await message.answer('Привіт! Я SyrnykBot 🧀\n'
                         'Публікую твої лайкнуті треки зі Spotify в Telegram канал.\n' 
                         'Щоб почати — /login')

@router.message(Command('help'))
async def help(message: types.Message):
    text = f"\n".join(f"{i}. <code>{cmd.command}</code> — {cmd.description}" for i, cmd in enumerate(COMMANDS, 1))
    await message.answer(f'Команди: \n' \
                         f'{text}', parse_mode="HTML")
