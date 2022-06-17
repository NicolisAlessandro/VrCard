import telegram.ext

with open("token.txt", "r") as f:
    TOKEN = f.read()
    print("Il tuo token è: ", TOKEN)


def start(update, context):
    update.message.reply_text("Ciao! Benvenuto nel bot")


def help(update, context):
    update.message.reply_text("""
    Sono disponibili i seguenti comandi:
    /start --> Messaggio di benvenuto
    /help --> Questo messaggio
    /content --> Informazioni riguardo al corso
    /contact --> I miei contatti
    """)


def content(update, context):
    update.message.reply_text("Il nostro contenuto")


def contact(update, context):
    update.message.reply_text("I miei contatti")


updater = telegram.ext.Updater(TOKEN, use_context=True)
disp = updater.dispatcher

disp.add_handler(telegram.ext.CommandHandler("start", start))
disp.add_handler(telegram.ext.CommandHandler("help", help))
disp.add_handler(telegram.ext.CommandHandler("content", content))
disp.add_handler(telegram.ext.CommandHandler("contact", contact))

updater.start_polling()
updater.idle()
