import random
import telebot

bot = telebot.TeleBot('7021467106:AAG_4O56OhdLROlfnElq4bzaO0JgHptjPBo') #Change this token to yor bot's token./Смените этот токен на токен вашего бота.

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
    @bot.message_handler(func=lambda message: True)
    def kk(message):
        chat_id = message.chat.id
        bot.send_message(chat_id, "Неверное количество упражнений. Пожалуйста, введите число от 1 до 10.")
    if user_input.isdigit():
        num_exercises = int(user_input)
        if num_exercises > 0 and num_exercises <= len(exercises):
            suggested_exercises = random.sample(exercises, num_exercises)
            for exercise in suggested_exercises:
                bot.send_message(chat_id, exercise)
            bot.send_message(chat_id, "Пожалуйста, введите количество упражнений.")
        else:
            kk(chat_id)
    else:
        bot.send_message(chat_id, "Пожалуйста, введите количество упражнений.")

@bot.message_handler(commands=['start'])
def send_welcome(message):
    """sumary_line"""
    bot.reply_to(message, "Привет! Я могу предложить вам упражнения для стоп.")

def check_number(func):
    def wrapper(message):
        if message.text.isdigit():
            return func(message)
        else:
            bot.send_message(message.chat.id, "Пожалуйста, введите количество упражнений.")
    return wrapper

@bot.message_handler(func=check_number)
def echo_all(message):
    #Lol, it doesn't do echo. It calls a function that suggest exercises.
    #Btw, I'm too lazy to rename this function.
    chat_id = message.chat.id
    bot.reply_to(message, tasks_suggestion(bot=bot, chat_id=chat_id, user_input=message.text))
    bot.reply_to(message, "Пожалуйста, введите количество упражнений.")
bot.infinity_polling()
