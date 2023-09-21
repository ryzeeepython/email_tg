from . import db
from aiogram.types import ReplyKeyboardRemove
from dispatcher import dp
from aiogram import types
import asyncio
import requests 
from . import db

BotDB = db.BotDB()

class Main:

    async def get_mail(self): 
        domain = requests.get('https://www.1secmail.com/api/v1/?action=genRandomMailbox&count=1').json()
        return domain[0]

    async def check_messages(self, mail):
        mail = mail.split('@') 
        messages  = requests.get(f'https://www.1secmail.com/api/v1/?action=getMessages&login={mail[0]}&domain={mail[1]}').json()
        return messages

    async def get_message(self, message, message_id, mail): 
        mail = mail.split('@') 
        data  = requests.get(f'https://www.1secmail.com/api/v1/?action=readMessage&login={mail[0]}&domain={mail[1]}&id={message_id}').json()
        await message.answer(f"От: {data['from']}\nТема: {data['subject']}\nТекст: {data['textBody']}")

    async def delete_mail(self, mail):
        url = 'https://www.1secmail.com/mailbox'
        data = {
            'action': 'deleteMailbox',
            'login': mail.split('@')[0],
            'domain': mail.split('@')[1]
        }

        r = requests.post(url, data=data)


    async def main(self, message): 
        try: 
            mail = await self.get_mail()
            messages = await self.check_messages(mail)
            BotDB.save_email(user_id= message.from_user.id, email = mail)
            await message.answer('Новая почта сгенерирована: ' + mail + '\nВсе сообщения приходящие на эту почту будут присылаться вам прямо в чат! ')
            old_len = 0
            while True:
                mail = BotDB.get_email(user_id=message.from_user.id)
                if mail: 
                    messages = await self.check_messages(mail[0][0]) 
                    if len(messages) != old_len:
                        await self.get_message(message_id = messages[0]["id"], mail = mail[0][0], message = message)
                        old_len = len(messages)
                    else: 
                        pass
                    await asyncio.sleep(1)
                else: 
                    break
        except Exception as err:
            print(err)

    async def stop(self, message):
        mail = BotDB.get_email(user_id=message.from_user.id)
        if mail:
            await self.delete_mail(mail[0][0])
            BotDB.delete_email(user_id= message.from_user.id)
            await message.answer('Эта почта удалена, с нее больше не будут приходить сообщения')
        else:
            await message.answer('У вас нет активных почт')
