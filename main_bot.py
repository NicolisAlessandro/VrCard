from telegram import ReplyKeyboardMarkup
import telegram.ext

with open("token.txt", "r") as f:
    TOKEN = f.read()
    print("Your token is: ", TOKEN)



def start(update, context):
    # Create buttons to slect language:
    keyboard = [['🇮🇹', '🇬🇧 / 🇺🇸']]

    # Create initial message:
    message = "🇮🇹  Benvenuto ...... \n 🇬🇧 / 🇺🇸  Welcome to our bot ......"
    text = ReplyKeyboardMarkup(keyboard, one_time_keyboard=True, resize_keyboard=True)
    update.message.reply_text(message, reply_markup=text)


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

def handle_message(update, context):
    update.message.reply_text("You texted: {message.text}")

updater = telegram.ext.Updater(TOKEN, use_context = True)
disp = updater.dispatcher

disp.add_handler(telegram.ext.CommandHandler("start", start))
disp.add_handler(telegram.ext.CommandHandler("help", help))
disp.add_handler(telegram.ext.CommandHandler("content", content))
disp.add_handler(telegram.ext.CommandHandler("contact", contact))
disp.add_handler(telegram.ext.MessageHandler(telegram.ext.Filters.text, handle_message))


updater.start_polling()
updater.idle()
