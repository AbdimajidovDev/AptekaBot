import os

from dotenv import load_dotenv

#
# from aiogram import Bot, Dispatcher, types
# from aiogram.enums import ParseMode
# from aiogram.fsm.storage.memory import MemoryStorage
# from aiogram.client.default import DefaultBotProperties
#
#
# TOKEN = os.getenv("TOKEN")

load_dotenv()
ADMIN_ID = int(os.getenv("ADMIN_ID"))
#
# if not TOKEN:
#     raise ValueError("❌ BOT_TOKEN .env faylda topilmadi!")
#
#
# bot = Bot(
#     token=TOKEN,
#     default=DefaultBotProperties(parse_mode=ParseMode.HTML)
# )
# dp = Dispatcher(storage=MemoryStorage())