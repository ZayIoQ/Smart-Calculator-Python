import telebot


TOKEN = '8206212961:AAEUvYbJGKTUnoSmtMHJYMfo2rYjL3t1bOU'


bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def welcome(message):
    bot.send_message(message.chat.id, "Что сегодня учишь?")

@bot.message_handler(func=lambda message: True)
def answer(message):
    if message.text.lower().strip() == "python":
        bot.send_message(message.chat.id, "Круто! Иди учи декораторы!")
    elif message.text.lower().strip() == "математика":
        bot.send_message(message.chat.id, "Круто! Пойди поучи логарифмы!")

    else:
        bot.send_message(message.chat.id, "Не понимаю что вы написали, но иди поучи Python")

bot.infinity_polling()


