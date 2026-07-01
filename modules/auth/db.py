import aiosqlite
import os
from dotenv import load_dotenv
from modules.auth.schemas import User

load_dotenv()
DB_PATH = os.getenv('DB_PATH')

async def db_init():
    async with aiosqlite.connect(DB_PATH) as db:
        await db.execute('CREATE TABLE IF NOT EXISTS users(id INTEGER PRIMARY KEY, telegram_id TEXT, spotify_id TEXT, access_token TEXT, refresh_token TEXT, expires_at DATETIME, scopes TEXT)')
        await db.commit()

async def db_check_user_status(telegram_id : int) -> bool:
    async with aiosqlite.connect(DB_PATH) as db:
        cursor = await db.execute('SELECT telegram_id FROM users WHERE telegram_id = ?', (telegram_id,))
        rows = await cursor.fetchall()
        return rows
    
async def db_add_user(user: User):
    async with aiosqlite.connect(DB_PATH) as db:
        await db.execute('INSERT INTO users (telegram_id, spotify_id, access_token, refresh_token, expires_at, scopes) VALUES(?, ?, ?, ?, ?, ?)', 
                         (user.telegram_id, user.spotify_id, user.access_token, user.refresh_token, user.expires_at, user.scopes, ))
        await db.commit()

async def db_get_user(telegram_id: int):
    async with aiosqlite.connect(DB_PATH) as db:
        cursor = await db.execute('SELECT telegram_id, spotify_id, access_token, refresh_token, expires_at, scopes FROM users WHERE telegram_id = ?', (telegram_id,))
        user = await cursor.fetchone()
        return user
    
async def db_delete_user(telegram_id: int):
    async with aiosqlite.connect(DB_PATH) as db:
        await db.execute('DELETE FROM users WHERE telegram_id = ?', (telegram_id,))
        await db.commit()