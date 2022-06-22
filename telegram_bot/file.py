import telegram.ext
from telegram import*
from requests import*
from telegram.ext import CallbackQueryHandler
import sqlite3

from prova import creaBottonibot, descrizioneBot

with open("token.txt", "r") as f:
    TOKEN = f.read()
    print("Your token is: ", TOKEN)

TOKEN = "5592675935:AAFXOB1e14hOIb2iiRdiL_KO0CaIZA0DBE4"

def start(update, context):

    #csv_read()

    buttons=[[KeyboardButton("🇮🇹 Italiano")],[KeyboardButton("🇬🇧 / 🇺🇸 English")]]
    context.bot.send_message(chat_id=update.effective_chat.id, text=" 🇮🇹 Scegli la lingua \n 🇬🇧 / 🇺🇸 Choose the language",
    reply_markup=ReplyKeyboardMarkup(buttons, one_time_keyboard=True))

def csv_read():
    list = []
    Dup = []
    reader = sqlite3.connect('veronacard.db')
    c = reader.cursor()
    c.execute('SELECT name_id FROM site_info')
    for row in reader: 
        if list.__contains__(row[3]) == False:
            list.add(row[3])
    print(list)
    
def handle_message(update, context):
    if "Chiese" in update.message.text:
       
        btn=[[InlineKeyboardButton("chiesa1",callback_data="chiesa1")], [InlineKeyboardButton("chiesa2",callback_data="chiesa2")], [InlineKeyboardButton("chiesa3",callback_data="chiesa3")], [InlineKeyboardButton("chiesa3",callback_data="chiesa4")], [InlineKeyboardButton("indietro",callback_data="indietro")]]
        context.bot.send_message(chat_id=update.effective_chat.id, reply_markup=InlineKeyboardMarkup(btn),text="ecco la lista delle chiese: ")
        descrizioneBot("Chiese")

    if "Back/Indietro" in update.message.text:

        buttons=[[KeyboardButton("🇮🇹 Italiano")],[KeyboardButton("🇬🇧 / 🇺🇸 English")]]
        context.bot.send_message(chat_id=update.effective_chat.id, text=" 🇮🇹 Scegli la lingua \n 🇬🇧 / 🇺🇸 Choose the language",
        reply_markup=ReplyKeyboardMarkup(buttons, one_time_keyboard=True))

    if "musei" in update.message.text:

        btn=[[InlineKeyboardButton("museo1",callback_data="museo1")], [InlineKeyboardButton("museo2",callback_data="museo2")], [InlineKeyboardButton("museo3",callback_data="museo3")], [InlineKeyboardButton("indietro",callback_data="indietro")]]
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
    
    if "chiesa" in query:
        context.bot.send_message(chat_id=update.effective_chat.id, text="chiese")

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

def content(update, context):

    update.message.reply_text("The bot's content will be added soon... 👀")

def contact(update, context):

    update.message.reply_text("  📧 Contact me on adrian20032010@gmail.com \n 📱 Discord: konksz#6398")

updater = telegram.ext.Updater(TOKEN, use_context = True)
disp = updater.dispatcher

disp.add_handler(telegram.ext.CommandHandler("start", start))
disp.add_handler(telegram.ext.CommandHandler("help", help))
disp.add_handler(telegram.ext.CommandHandler("csv_read", csv_read))
disp.add_handler(telegram.ext.CommandHandler("content", content))
disp.add_handler(telegram.ext.CommandHandler("contact", contact))
disp.add_handler(CallbackQueryHandler(queryHandler))
disp.add_handler(telegram.ext.MessageHandler(telegram.ext.Filters.text, handle_message))
#disp.add_handler(telegram.ext.MessageHandler(telegram.ext.Filters.text, creaBottoni))

updater.start_polling()
updater.idle()
