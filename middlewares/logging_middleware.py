from aiogram import BaseMiddleware

from datetime import datetime

class Logging(BaseMiddleware):
    async def __call__(self, handler, event, data):
        message = event.message
        if message is None:
            return await handler(event, data)

        user_name = message.from_user.username
        id        = message.from_user.id
        text      = message.text if message.text is not None else "[non-text content]"
        date      = datetime.now().strftime("%d/%m/%Y, %H:%M:%S")
    
        print(f'[ [{date}] User: @{user_name} ({id}): {text} ]')

        return await handler(event, data)