import threading
import telebot
import datetime
import asyncio


def get_menu_text(actions):
    """Текст меню"""
    text = 'Выберите действие: \n\n'
    for action in actions:
        text += "--> {}\n".format(action)
    return text


class Media_bot:
    def __init__(self):
        tg_token = ''
        self.bot = telebot.TeleBot(tg_token)
        self.menu = None

    def set_menu(self, actions):
        """Создание кнопок"""
        self.menu = telebot.types.ReplyKeyboardMarkup()
        for item in actions:
            self.menu.add(item)

    def welcome_user(self):
        @self.bot.message_handler(commands=['start'])
        def send_welcome(message):
            """Отправляет приветственное сообщение при первом диалоге"""
            text = "Добро пожаловать, {}!\nЯ проект ВШЭ.".format(message.from_user.first_name)
            self.set_menu(["Кнопка 1", "Кнопка 2"])
            self.bot.send_message(message.chat.id,
                                  text,
                                  reply_markup=self.menu)
            self.process_main_menu()


    def process_main_menu(self):
        """Обрабатывает главное меню"""
        @self.bot.message_handler(func=lambda message: True)
        def button_menu(message):
            if message.text == 'Телеграмм':
                actions = ["Общая статистика", "Статистика канала", "Управление каналами", "Назад"]
                self.set_menu(actions)
                self.bot.send_message(message.chat.id, get_menu_text(actions), reply_markup=self.menu)
            else:
                platforms = ['Телеграмм', 'ВК', "ФБ"]
                self.set_menu(platforms)
                self.bot.send_message(message.chat.id, 'Упс... К сожалению, я тебя не совсем понял.', reply_markup=self.menu)


    def execute(self):
        self.welcome_user()
        self.process_main_menu()
        # threading.Thread(target=self.set_stats).start()
        self.bot.infinity_polling(True)

def main():
    print('Бот запущен')
    med_bot = Media_bot()
    med_bot.execute()


if __name__ == "__main__":
    main()