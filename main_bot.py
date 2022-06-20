import telegram.ext
from telegram import*
from requests import*
from telegram.ext import CallbackQueryHandler

with open("token.txt", "r") as f:
    TOKEN = f.read()
    print("Your token is: ", TOKEN)

def start(update, context):
# Create buttons to slect language:
#     keyboard = [['🇮🇹', '🇬🇧 / 🇺🇸']]

    buttons=[[KeyboardButton("🇮🇹 Italiano")],[KeyboardButton("🇬🇧 / 🇺🇸 English")]]
    context.bot.send_message(chat_id=update.effective_chat.id, text=" 🇮🇹 Scegli la lingua \n 🇬🇧 / 🇺🇸 Choose the language",
    reply_markup=ReplyKeyboardMarkup(buttons, one_time_keyboard=True))

def handle_message(update, context):
    if "🇮🇹 Italiano" in update.message.text:
        update.message.reply_text("🇮🇹 Benvenuto nel nostro canale Telegram .... \n ......... \n ........")
        btn=[[InlineKeyboardButton("chiese",callback_data="church")], [InlineKeyboardButton("musei",callback_data="museums")]]
        context.bot.send_message(chat_id=update.effective_chat.id, reply_markup=InlineKeyboardMarkup(btn), text="asdasd")
    if "🇬🇧 / 🇺🇸 English" in update.message.text:
        update.message.reply_text("🇬🇧 / 🇺🇸 Welcome to our Telegram channel .... \n ......... \n ........")

def queryHandler(update, context):
    query = update.callback_query.data
    update.callback_query.answer()

    if "museums" in query:
        context.bot.send_message(chat_id=update.effective_chat.id, text="musei")
    
    if "church" in query:
        context.bot.send_message(chat_id=update.effective_chat.id, text="chiese")

def help(update, context):
    update.message.reply_text("""
    📙Available commands:

    /start -> Welcome message
    /help -> This message
    /content -> Info about the bot
    /contact -> My contacts
    """)

def content(update, context):
    update.message.reply_text("The bot's content will be added soon... 👀")

def contact(update, context):
    update.message.reply_text("  📧 Contact me on adrian20032010@gmail.com \n 📱 Discord: konksz#6398")

updater = telegram.ext.Updater(TOKEN, use_context = True)
disp = updater.dispatcher

disp.add_handler(telegram.ext.CommandHandler("start", start))
disp.add_handler(telegram.ext.CommandHandler("help", help))
disp.add_handler(telegram.ext.CommandHandler("content", content))
disp.add_handler(telegram.ext.CommandHandler("contact", contact))
disp.add_handler(CallbackQueryHandler(queryHandler))
disp.add_handler(telegram.ext.MessageHandler(telegram.ext.Filters.text, handle_message))




updater.start_polling()
updater.idle()
