import sqlite3
import datetime

class BotDB:

    def __init__(self):
        self.conn = sqlite3.connect('./scripts/db.db')
        self.cursor = self.conn.cursor()

    def get_email(self, user_id):
        questions = self.cursor.execute(f"SELECT `email` FROM `users` WHERE user_id = {user_id}")
        return questions.fetchall()

    def save_email(self, user_id, email):
        date = datetime.datetime.now()
        self.cursor.execute(f"REPLACE INTO `users` (`user_id`, `email`, `date`) VALUES (?, ?, ?)", (user_id, email, date))
        return self.conn.commit()

    def delete_email(self, user_id): 
        self.cursor.execute(f"DELETE FROM `users` WHERE `user_id` = {user_id}")
        return self.conn.commit()

    def close(self):
        """Закрываем соединение с БД"""
        self.connection.close()