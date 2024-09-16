import os
import telebot
from telebot import types
from dotenv import load_dotenv

# Загрузка переменных окружения из .env файла
load_dotenv()

# Токен вашего бота
TOKEN = os.getenv('YOUR_BOT_TOKEN')

bot = telebot.TeleBot(TOKEN)

# Очередь для поиска собеседников
waiting_users = []

# Словарь для хранения пар собеседников
chats = {}

# Создаем кнопку "Поиск собеседника"
def get_main_markup():
    return types.ReplyKeyboardMarkup(resize_keyboard=True).add(types.KeyboardButton('Поиск собеседника'))

# Обработка команды /start
@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, "Нажми 'Поиск собеседника', чтобы начать чат", reply_markup=get_main_markup())

# Обработка нажатия на кнопку "Поиск собеседника"
@bot.message_handler(func=lambda message: message.text == "Поиск собеседника")
def search_for_companion(message):
    user_id = message.from_user.id

    # Проверка, есть ли пользователь уже в поиске
    if user_id in waiting_users:
        bot.send_message(message.chat.id, "Вы уже в поиске собеседника!")
        return

    # Если есть кто-то в очереди, соединяем
    if waiting_users:
        companion_id = waiting_users.pop(0)
        chats[user_id] = companion_id
        chats[companion_id] = user_id

        bot.send_message(message.chat.id, "Собеседник найден! Можете начать общаться.")
        bot.send_message(companion_id, "Собеседник найден! Можете начать общаться.")
    else:
        # Добавляем пользователя в очередь
        waiting_users.append(user_id)
        bot.send_message(message.chat.id, "Ищем собеседника...")

# Пересылка сообщений между пользователями
@bot.message_handler(func=lambda message: message.from_user.id in chats, content_types=['text', 'voice'])
def relay_message(message):
    user_id = message.from_user.id
    companion_id = chats[user_id]

    try:
        if message.content_type == 'text':
            # Пересылаем текстовое сообщение собеседнику
            bot.send_message(companion_id, message.text)
        elif message.content_type == 'voice':
            # Пересылаем голосовое сообщение собеседнику
            bot.send_voice(companion_id, message.voice.file_id)
    except Exception as e:
        bot.send_message(message.chat.id, "Не удалось отправить сообщение.")
        print(e)

# Запуск бота
bot.polling(none_stop=True)
