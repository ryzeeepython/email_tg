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

@dp.message_handler(Command('start'))
async def on_start_test(message: types.Message):
    await message.answer('Привет, ' + str(message.from_user.full_name) + ', чтобы сгенерировать почту нажмите /generate', reply_markup= markup)
    