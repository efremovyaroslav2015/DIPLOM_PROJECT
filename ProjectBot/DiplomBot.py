import asyncio
import logging
import sys
import pickle

from aiogram import Bot, Dispatcher, Router, types, F
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart, Command
from aiogram.types import Message, CallbackQuery
from aiogram.utils.markdown import hbold
from aiogram.fsm.state import StatesGroup, State
from aiogram.fsm.context import FSMContext
from aiogram.types import ContentType
from handler import router


TOKEN = "7051789408:AAFzWmd5H1j4nmo4alk5lEY4S1IvK279oBU"
bot = Bot(token=TOKEN)
dp = Dispatcher()


async def main():  # -> None
    # Initialize Bot instance with a default parse mode which will be passed to all API calls
    # bot = Bot(TOKEN, parse_mode=ParseMode.HTML)
    # And the run events dispatching
    dp.include_router(router)
    await dp.start_polling(bot)

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print('Exit')
