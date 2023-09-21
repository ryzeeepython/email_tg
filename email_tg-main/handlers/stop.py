from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command
from aiogram.types import ReplyKeyboardRemove
import asyncio
from dispatcher import dp
from aiogram import types
from scripts.scripts import Main
from keyboard.inline.keyboard  import Keyboard
from aiogram.dispatcher.filters import Text

Keyboard = Keyboard()
markup = Keyboard.startmenu()
logic = Main()


@dp.message_handler(Command('stop'))
@dp.message_handler(Text(equals='🛑 Стоп'))
async def on_start_test(message: types.Message):
    await logic.stop(message=message)
    
