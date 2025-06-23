import asyncio
import logging

from aiogram.types import Message, BotCommand
from aiogram.filters import CommandStart
from dotenv import load_dotenv

import os

from aiogram import Bot, Dispatcher, types
from aiogram.enums import ParseMode
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.client.default import DefaultBotProperties

from app.handlers.user import user_router
from app.handlers.admin import admin_router

from app.config import ADMIN_ID

load_dotenv()

logging.basicConfig(level=logging.INFO)

TOKEN = os.getenv("TOKEN")
# ADMIN_ID = os.getenv("ADMIN_ID")

if not TOKEN:
    raise ValueError("❌ BOT_TOKEN .env faylda topilmadi!")

bot = Bot(
    token=TOKEN,
    default=DefaultBotProperties(parse_mode=ParseMode.HTML)
)
dp = Dispatcher(storage=MemoryStorage())


dp.include_router(admin_router)
dp.include_router(user_router)

async def startup_answer(bot: Bot):
    await bot.send_message(ADMIN_ID, "Bot ishga tushdi! ✅")


async def shutdown_answer(bot: Bot):
    await bot.send_message(ADMIN_ID, "Bot ishdan to'xtadi! ❌")


@dp.message(CommandStart())
async def start_handler(message: Message):
    await message.answer("Assalomu alaykum! Botimizga xush kelibsiz!")

    await bot.set_my_commands([
        BotCommand(command='/start', description='Botni ishga tushirish!'),
    ])

async def main():
    dp.startup.register(startup_answer)


    dp.shutdown.register(shutdown_answer)

    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
