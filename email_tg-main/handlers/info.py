from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command
from aiogram.types import ReplyKeyboardRemove

from dispatcher import dp
from aiogram import types
from scripts.scripts import Main
from keyboard.inline.keyboard  import Keyboard
import asyncio
from aiogram.dispatcher.filters import Text

Keyboard = Keyboard()
markup = Keyboard.startmenu()
logic = Main()

@dp.message_handler(Command('info'))
@dp.message_handler(Text(equals='🚨 Инфо'))
async def on_start_test(message: types.Message):
    await message.answer('По всем вопросам: @s_ryzeee')

    