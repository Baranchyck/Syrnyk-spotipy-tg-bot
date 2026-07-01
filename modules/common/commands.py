from aiogram.types import BotCommand

COMMANDS = [BotCommand(command="/start", description="запустити бота"),
            BotCommand(command="/help", description="список команд"),
            BotCommand(command="/login", description="підключити Spotify"),
            BotCommand(command="/status", description="перевірити авторизацію"),]
