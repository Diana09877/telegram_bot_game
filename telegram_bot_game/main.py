import telebot
import random
from local_settings import API_TOKEN

bot = telebot.TeleBot(API_TOKEN)

@bot.message_handler(commands=['help', 'start'])
def send_welcome(message):
    bot.reply_to(message, """\
Добро пожаловать в игру "камень, ножницы, бумага!" Выберите камень (к), ножницы (н), бумага(б)\
""")

@bot.message_handler(func=lambda message: True)
def play_game(message):
    user_move = message.text.lower()
    if user_move not in ['к', 'н', 'б']:
        bot.reply_to(message, "Неправильный ввод. Пожалуйста, выберите камень (к), ножницы (н) или бумагу (б).")
    else:
        computer_move = random.choice(["к", "н", "б"])
        if user_move == computer_move:
            bot.reply_to(message, "Ничья!")
        elif (user_move == 'к' and computer_move == 'н') or \
             (user_move == 'н' and computer_move == 'б') or \
             (user_move == 'б' and computer_move == 'к'):
            bot.reply_to(message, "Вы выиграли!")
        else:
            bot.reply_to(message, "Компьютер победил!")

bot.infinity_polling()


