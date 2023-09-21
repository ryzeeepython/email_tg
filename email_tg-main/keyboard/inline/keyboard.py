#from aiogram.types import ReplyKeyboardMarkup
from aiogram import types
from scripts.scripts import Main


class Keyboard:

    def startmenu(self):
        list_button_name = ['🆕Новая Почта', '🚨 Инфо', '🛑 Стоп']
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard= True)
        keyboard.add(*list_button_name)

        return keyboard

