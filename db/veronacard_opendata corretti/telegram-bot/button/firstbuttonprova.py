import telebot

bot = telebot.Telebot("5592675935:AAFXOB1e14hOIb2iiRdiL_KO0CaIZA0DBE4")

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "sparo a caso perché non è inglese lo :)", reply_markup = inline_keyboard())

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    # bot.reply_to(message, message.txt)
    m = message
    if m.txt == "salom":
        bot.send_message(m.chat.id, "sparo a caso perc")
    if m.text == "secsi alessandro":
        bot.send_message(m.chat.id, "non è english, forza ucraina")
    if m.text == "hello":
        bot.send_message(m.chat.id, "Good Morning")

bot.polling()