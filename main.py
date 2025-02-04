import random #for randomizing exercises and giving only one to output then
import telebot #lib to interact with Telegram API

bot = telebot.TeleBot('YOUR_API_TOKEN') #Change this token to yor bot's token./Смените этот токен на токен вашего бота.

def tasks_suggestion(bot, chat_id, user_input):
    exercises = [
        "Поднимитесь на носки и опуститесь обратно на пятки 10 раз",
        "Пройдитесь на носках 10 шагов",
        "Пройдитесь на пятках 10 шагов",
        "Пройдитесь на внешней стороне стопы 10 шагов",
        "Пройдитесь на внутренней стороне стопы 10 шагов",
        "Сделайте круговые движения стопами по часовой стрелке 10 раз",
        "Сделайте круговые движения стопами против часовой стрелки 10 раз",
        "Соберите пальцами ног мелкие предметы с пола",
        "Сделайте массаж стоп с помощью теннисного мяча",
        "Сделайте массаж стоп с помощью массажного ролика"
    ]

    if user_input.isdigit():
        num_exercises = int(user_input)
        if 0 < num_exercises <= len(exercises):
            suggested_exercises = random.sample(exercises, num_exercises)
            bot.send_message(chat_id, "\n".join(suggested_exercises))
        else:
            bot.send_message(chat_id, "Неверное количество упражнений. Пожалуйста, введите число от 1 до 10.")
    else:
        bot.send_message(chat_id, "Пожалуйста, введите количество упражнений.")

@bot.message_handler(commands=['start'])
def send_welcome(message):
    """Sends welcome"""
    bot.send_message(message.chat.id, "Привет! Я могу предложить вам упражнения для стоп.")

check_number = lambda func: lambda message: func(message) if message.text.isdigit() else bot.send_message(message.chat.id, "Пожалуйста, введите количество упражнений.")

@bot.message_handler(func=check_number)
def suggest_exercises(message):
    chat_id = message.chat.id
    bot.reply_to(message, tasks_suggestion(bot=bot, chat_id=chat_id, user_input=message.text))
    bot.reply_to(message, "Пожалуйста, введите количество упражнений.")
bot.infinity_polling()
