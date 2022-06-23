import telegram.ext
from telegram import*
from requests import*
from telegram.ext import CallbackQueryHandler
from prova import posizioneBot, descrizioneBot

with open("token.txt", "r") as f:
    TOKEN = f.read()
    print("Your token is: ", TOKEN)

TOKEN = "5592675935:AAFXOB1e14hOIb2iiRdiL_KO0CaIZA0DBE4"

def start(update, context):
    buttons=[[KeyboardButton("🇮🇹 Italiano")],[KeyboardButton("🇬🇧 / 🇺🇸 English")]]
    context.bot.send_message(chat_id=update.effective_chat.id, text=" 🇮🇹 Scegli la lingua \n 🇬🇧 / 🇺🇸 Choose the language",
    reply_markup=ReplyKeyboardMarkup(buttons, one_time_keyboard=True))


    
def handle_message(update, context):
    if "Chiese" in update.message.text:
       
        btn=[[InlineKeyboardButton("Complesso del Duomo",callback_data="chiesa1")], [InlineKeyboardButton("Basilica di Santa Anastasia",callback_data="chiesa2")], [InlineKeyboardButton("Chiesa di San Fermo",callback_data="chiesa3")], [InlineKeyboardButton("Basilica di San Zeno",callback_data="chiesa4")], [InlineKeyboardButton("indietro",callback_data="indietro")]]
        context.bot.send_message(chat_id=update.effective_chat.id, reply_markup=InlineKeyboardMarkup(btn),text="ecco la lista delle chiese: ")
        
    if "Back/Indietro" in update.message.text:

        buttons=[[KeyboardButton("🇮🇹 Italiano")],[KeyboardButton("🇬🇧 / 🇺🇸 English")]]
        context.bot.send_message(chat_id=update.effective_chat.id, text=" 🇮🇹 Scegli la lingua \n 🇬🇧 / 🇺🇸 Choose the language",
        reply_markup=ReplyKeyboardMarkup(buttons, one_time_keyboard=True))

    if "musei" in update.message.text:

        btn=[[InlineKeyboardButton("Museo Africano",callback_data="museo1")], [InlineKeyboardButton("Museo di Storia Naturale",callback_data="museo2")], [InlineKeyboardButton("Museo degli Affreschi G.B. Cavalcaselle alla Tomba di Giulietta",callback_data="museo3")],[InlineKeyboardButton("museo3",callback_data="museo3")],[InlineKeyboardButton("museo3",callback_data="museo3")],[InlineKeyboardButton("museo3",callback_data="museo3")],[InlineKeyboardButton("museo3",callback_data="museo3")],[InlineKeyboardButton("museo3",callback_data="museo3")], [InlineKeyboardButton("indietro",callback_data="indietro")]]
        context.bot.send_message(chat_id=update.effective_chat.id, reply_markup=InlineKeyboardMarkup(btn),text="ecco la lista dei musei: ")

    if "monumenti" in update.message.text:

        btn=[[InlineKeyboardButton("monumento1",callback_data="monumento1")], [InlineKeyboardButton("monumento2",callback_data="monumento2")], [InlineKeyboardButton("monumento3",callback_data="monumento3")], [InlineKeyboardButton("indietro",callback_data="indietro")]]
        context.bot.send_message(chat_id=update.effective_chat.id, reply_markup=InlineKeyboardMarkup(btn),text="ecco la lista dei monumenti: ")

    if "Church" in update.message.text:

        btn=[[InlineKeyboardButton("church1",callback_data="church1")], [InlineKeyboardButton("church2",callback_data="church2")], [InlineKeyboardButton("church3",callback_data="church3")], [InlineKeyboardButton("Back",callback_data="Back")]]
        context.bot.send_message(chat_id=update.effective_chat.id, reply_markup=InlineKeyboardMarkup(btn),text="list of all churches: ")

    if "graphs" in update.message.text:

        buttons=[[KeyboardButton("Church")],[KeyboardButton("museum")], [KeyboardButton("monuments")],[KeyboardButton("Go Back")]]
        context.bot.send_message(chat_id=update.effective_chat.id, text="flow graphs:",
        reply_markup=ReplyKeyboardMarkup(buttons, one_time_keyboard=True))

    if "grafici" in update.message.text:

        buttons=[[KeyboardButton("Chiese")],[KeyboardButton("musei")], [KeyboardButton("monumenti")],[KeyboardButton("Torna Indietro")]]
        context.bot.send_message(chat_id=update.effective_chat.id, text="grafici di flusso",
        reply_markup=ReplyKeyboardMarkup(buttons, one_time_keyboard=True))

    if "museum" in update.message.text:
        
        btn=[[InlineKeyboardButton("museum1",callback_data="museum1")], [InlineKeyboardButton("museum2",callback_data="museum2")], [InlineKeyboardButton("museum3",callback_data="museum3")], [InlineKeyboardButton("Back",callback_data="Back")]]
        context.bot.send_message(chat_id=update.effective_chat.id, reply_markup=InlineKeyboardMarkup(btn),text="list of all museums: ")

    if "monuments" in update.message.text:

        btn=[[InlineKeyboardButton("monuments1",callback_data="monuments1")], [InlineKeyboardButton("monuments2",callback_data="monuments2")], [InlineKeyboardButton("monuments3",callback_data="monuments3")], [InlineKeyboardButton("Back",callback_data="Back")]]
        context.bot.send_message(chat_id=update.effective_chat.id, reply_markup=InlineKeyboardMarkup(btn),text="list of all monuements: ")

    if "Maps" in update.message.text:

        buttons=[[KeyboardButton("Church")],[KeyboardButton("museum")], [KeyboardButton("monuments")],[KeyboardButton("Go Back")]]
        context.bot.send_message(chat_id=update.effective_chat.id, text="*map*",
        reply_markup=ReplyKeyboardMarkup(buttons, one_time_keyboard=True))
    
    if "jurney" in update.message.text:

        buttons=[[KeyboardButton("Church")],[KeyboardButton("museum")], [KeyboardButton("monuments")],[KeyboardButton("Go Back")]]
        context.bot.send_message(chat_id=update.effective_chat.id, text="select the tyupe of monuments you want to visit",
        reply_markup=ReplyKeyboardMarkup(buttons, one_time_keyboard=True))

    if "Viaggio" in update.message.text:

        buttons=[[KeyboardButton("Chiese")],[KeyboardButton("musei")], [KeyboardButton("monumenti")],[KeyboardButton("Torna Indietro")]]
        context.bot.send_message(chat_id=update.effective_chat.id, text="scegli quale tipo di struttura vuoi",
        reply_markup=ReplyKeyboardMarkup(buttons, one_time_keyboard=True))

    if "Mappa" in update.message.text:

        i = 1
        buttons=[[KeyboardButton("Chiese")],[KeyboardButton("musei")], [KeyboardButton("monumenti")],[KeyboardButton("Torna Indietro")]]
        context.bot.send_message(chat_id=update.effective_chat.id, text="*mappa*",
        reply_markup=ReplyKeyboardMarkup(buttons, one_time_keyboard=True))
    
    if "Torna Indietro" in update.message.text:

        buttons=[[KeyboardButton("Mappa")],[KeyboardButton("Viaggio")], [KeyboardButton("grafici")],[KeyboardButton("Back/Indietro")]]
        context.bot.send_message(chat_id=update.effective_chat.id, text="🇮🇹 Benvenuto nel nostro canale Telegram, che tipo di monumento ti piacerebbe visitare?",
        reply_markup=ReplyKeyboardMarkup(buttons, one_time_keyboard=True))

    if "Go Back" in update.message.text:

        buttons=[[KeyboardButton("Maps")],[KeyboardButton("journey")], [KeyboardButton("graphs")],[KeyboardButton("Back/Indietro")]]
        context.bot.send_message(chat_id=update.effective_chat.id, text="🇬🇧 / 🇺🇸 Welcome to our bot",
        reply_markup=ReplyKeyboardMarkup(buttons, one_time_keyboard=True))

    if "🇮🇹 Italiano" in update.message.text:
        
        buttons=[[KeyboardButton("Mappa")],[KeyboardButton("Viaggio")], [KeyboardButton("grafici")],[KeyboardButton("Back/Indietro")]]
        context.bot.send_message(chat_id=update.effective_chat.id, text="🇮🇹 Benvenuto nel nostro canale Telegram, che tipo di monumento ti piacerebbe visitare?",
        reply_markup=ReplyKeyboardMarkup(buttons, one_time_keyboard=True))

    if "🇬🇧 / 🇺🇸 English" in update.message.text:

        buttons=[[KeyboardButton("Maps")],[KeyboardButton("journey")], [KeyboardButton("graphs")],[KeyboardButton("Back/Indietro")]]
        context.bot.send_message(chat_id=update.effective_chat.id, text="🇬🇧 / 🇺🇸 Welcome to our bot",
        reply_markup=ReplyKeyboardMarkup(buttons, one_time_keyboard=True))


name_id = []
descr_it = [] 
descr_it = descrizioneBot("Chiese")
#descr_eng = []
list = []
list = posizioneBot("Chiese")

def queryHandler(update, context):

    query = update.callback_query.data
    update.callback_query.answer()

    if "indietro" in query:
        buttons=[[KeyboardButton("Chiese")],[KeyboardButton("musei")], [KeyboardButton("monumenti")],[KeyboardButton("Back/Indietro")]]
        context.bot.send_message(chat_id=update.effective_chat.id, text="scegli quale tipo di struttura vuoi",
        reply_markup=ReplyKeyboardMarkup(buttons, one_time_keyboard=True))
    
    if "Back" in query:
        buttons=[[KeyboardButton("Church")],[KeyboardButton("museum")], [KeyboardButton("monuments")],[KeyboardButton("Back/Indietro")]]
        context.bot.send_message(chat_id=update.effective_chat.id, text="select the tyupe of monuments you want to visit",
        reply_markup=ReplyKeyboardMarkup(buttons, one_time_keyboard=True))

    if "museo" in query:
        context.bot.send_message(chat_id=update.effective_chat.id, text="musei")
    
    if "chiesa1" in query:
        context.bot.send_message(chat_id=update.effective_chat.id, text = descr_it[0])
        context.bot.send_message(chat_id=update.effective_chat.id, text = list[0])
        
        
    if "chiesa2" in query:
        context.bot.send_message(chat_id=update.effective_chat.id, text = descr_it[1])
        context.bot.send_message(chat_id=update.effective_chat.id, text = list[1])
        
    if "chiesa3" in query:
        context.bot.send_message(chat_id=update.effective_chat.id, text = descr_it[2])
        context.bot.send_message(chat_id=update.effective_chat.id, text = list[2])
            
    if "chiesa4" in query:
        context.bot.send_message(chat_id=update.effective_chat.id, text = descr_it[3])
        context.bot.send_message(chat_id=update.effective_chat.id, text = list[3])

    if "monumento" in query:
        context.bot.send_message(chat_id=update.effective_chat.id, text="monumenti")
    
    if "museum" in query:
        context.bot.send_message(chat_id=update.effective_chat.id, text="museum")
    
    if "church" in query:
        context.bot.send_message(chat_id=update.effective_chat.id, text="church")

    if "monuments" in query:
        context.bot.send_message(chat_id=update.effective_chat.id, text="monuments")

def help(update, context):

    update.message.reply_text("""
    📙Available commands:
    /start -> Welcome message
    /help -> This message
    /content -> Info about the bot
    /contact -> My contacts
    """)

def contact(update, context):

    update.message.reply_text("  📧 Contact me on adrian20032010@gmail.com \n 📱 Discord: konksz#6398")

updater = telegram.ext.Updater(TOKEN, use_context = True)
disp = updater.dispatcher

disp.add_handler(telegram.ext.CommandHandler("start", start))
disp.add_handler(telegram.ext.CommandHandler("help", help))
disp.add_handler(telegram.ext.CommandHandler("contact", contact))
disp.add_handler(CallbackQueryHandler(queryHandler))
disp.add_handler(telegram.ext.MessageHandler(telegram.ext.Filters.text, handle_message))
updater.start_polling()
updater.idle()
