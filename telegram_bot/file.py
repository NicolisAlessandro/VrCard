import math as m
import telegram.ext
from random import randint
from aiogram import Bot, Dispatcher, types
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

TOKEN = "5592675935:AAFXOB1e14hOIb2iiRdiL_KO0CaIZA0DBE4"
bot=Bot( token= "5592675935:AAFXOB1e14hOIb2iiRdiL_KO0CaIZA0DBE4" )
dp= Dispatcher(bot)





@dp.callback_query_handler(text = ["randomvalue10" , "randomvalue100"])
def random_value(call: types.CallbackQuery):
    if call.data == "randomvalue10":
        call.message.answer(randint(1,10))
    if call.data == "randomvalue100":
        call.message.answer(randint(1,100))
    call.answer()
    

def start(update, context):
    update.message.reply_text("Ciao bevenuto nel bot")
    
def help(update, context):
    update.message.reply_text("""
    Sono disponibili i seguenti comandi:

    /start --> Messaggio di benvenuto
    /help --> Questo messaggio
    /context --> Informazioni riguardo al corso
    /contact --> I miei contatti
    """)
    
def context(update, context):
    update.message.reply_text("il nostro contenuto")
    
def contact(update, context):
    update.message.reply_text("i miei contatti")

#def stock( update , context):
#    ticker = context.args[0]
#    data = web.DataReader(ticker,'ciao')
#    price = data.iloc[-1]['close']
#    update.message.reply_text(f"the current price of {ticker} is {price:.2f}$!")

def tel_parse_message(message):
    print("message-->",message)
    chat_id = message['message']['chat']['id']
    txt = message['message']['text']
    print("chat_id-->", chat_id)
    print("txt-->", txt)
    return chat_id,txt

@bot.message_handler(func=lambda m: "python" in m.text)
def fun2(message):
    markup = InlineKeyboardMarkup()
    markup.row_width = 2
    markup.add(InlineKeyboardButton("Azione 1", callback_data="id_azione_1"),
               InlineKeyboardButton("Azione 2", callback_data="id_azione_2"))

    bot.send_message(message.chat.id, "CIAO RAGAZZI", reply_markup=markup)

m = 0   # assegnare le variabili dal csv
coord_x = 0
coord_y = 0
nome = ""

def dist(lat1,lon1, lat2, lon2):
    return 6371 * 2 * m.asin(m.sqrt(m.pow(m.sin((m.radians(lat2) - m.radians(lat1)) / 2), 2) + m.cos(lat1) * m.cos(lat2) * m.pow(m.sin((m.radians(lon2) - m.radians(lon1)) / 2), 2)))

def distanza(update, context) -> None:
    try:
        lat1 = update.message.location.latitude
        lon1 = update.message.location.longitude
        d = []
        for i in range(0,len(coord_x)):
            d.append(dist(lat1,lon1,coord_x[i],coord_y[i]))
        e = d[:]
        d.sort()
        ind = 0
        for i in range(0,len(d)):
            if d[0]==e[i]:
                ind = i
                break
        testo = "La scuola più vicina è: " + nome[ind]
        testo_dist = "\nDistanza: " + str(round(d[0],2)) + " km"
        context.bot.send_message(chat_id=update.effective_chat.id, text=testo+testo_dist)
        update.message.reply_location(coord_x[ind], coord_y[ind])
        testo = "Per trovare nuovamente la scuola più vicina invia la tua posizione."
        context.bot.send_message(chat_id=update.effective_chat.id, text=testo)
    except:
        testo_try = "Attenzione!!!\nInviare solo la posizione attuale.\nInterrompere la condivisione della posizione in tempo reale."
        context.bot.send_message(chat_id=update.effective_chat.id, text=testo_try) 

def handle_message(update, context):
    update.message.reply_text(f"hai detto {update.message.text}")
    
    
updater = telegram.ext.Updater(TOKEN, use_context=True)
disp = updater.dispatcher

disp.add_handler(telegram.ext.CommandHandler("start", start))
disp.add_handler(telegram.ext.CommandHandler("help", help))
disp.add_handler(telegram.ext.CommandHandler("context", context))
disp.add_handler(telegram.ext.CommandHandler("contact", contact))
disp.add_handler(telegram.ext.CommandHandler("distanza", distanza))
disp.add_handler(telegram.ext.MessageHandler(telegram.ext.Filters.text , handle_message))
#disp.add_handler(telegram.ext.CommandHandler("random", random_answer))


updater.start_polling()
updater.idle()







#codice 2




import telegram.ext
from telegram import*
from requests import*
from telegram.ext import CallbackQueryHandler
import csv
import sqlite3

luoghi = []
with open("TOKEN.txt", "r") as f:
    TOKEN = f.read()
    print("Your token is: ", TOKEN)

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

        btn=[[InlineKeyboardButton("chiesa1",callback_data="chiesa1")], [InlineKeyboardButton("chiesa2",callback_data="chiesa2")], [InlineKeyboardButton("chiesa3",callback_data="chiesa3")], [InlineKeyboardButton("indietro",callback_data="indietro")]]
        context.bot.send_message(chat_id=update.effective_chat.id, reply_markup=InlineKeyboardMarkup(btn),text="ecco la lista delle chiese: ")

    if "musei" in update.message.text:

        btn=[[InlineKeyboardButton("museo1",callback_data="museo1")], [InlineKeyboardButton("museo2",callback_data="museo2")], [InlineKeyboardButton("museo3",callback_data="museo3")], [InlineKeyboardButton("indietro",callback_data="indietro")]]
        context.bot.send_message(chat_id=update.effective_chat.id, reply_markup=InlineKeyboardMarkup(btn),text="ecco la lista dei musei: ")

    if "monumenti" in update.message.text:

        btn=[[InlineKeyboardButton("monumento1",callback_data="monumento1")], [InlineKeyboardButton("monumento2",callback_data="monumento2")], [InlineKeyboardButton("monumento3",callback_data="monumento3")], [InlineKeyboardButton("indietro",callback_data="indietro")]]
        context.bot.send_message(chat_id=update.effective_chat.id, reply_markup=InlineKeyboardMarkup(btn),text="ecco la lista dei monumenti: ")

    if "Church" in update.message.text:

        btn=[[InlineKeyboardButton("church1",callback_data="church1")], [InlineKeyboardButton("church2",callback_data="church2")], [InlineKeyboardButton("church3",callback_data="church3")], [InlineKeyboardButton("Back",callback_data="Back")]]
        context.bot.send_message(chat_id=update.effective_chat.id, reply_markup=InlineKeyboardMarkup(btn),text="list of all churches: ")

    if "museum" in update.message.text:
        
        btn=[[InlineKeyboardButton("museum1",callback_data="museum1")], [InlineKeyboardButton("museum2",callback_data="museum2")], [InlineKeyboardButton("museum3",callback_data="museum3")], [InlineKeyboardButton("Back",callback_data="Back")]]
        context.bot.send_message(chat_id=update.effective_chat.id, reply_markup=InlineKeyboardMarkup(btn),text="list of all museums: ")

    if "monuments" in update.message.text:

        btn=[[InlineKeyboardButton("monuments1",callback_data="monuments1")], [InlineKeyboardButton("monuments2",callback_data="monuments2")], [InlineKeyboardButton("monuments3",callback_data="monuments3")], [InlineKeyboardButton("Back",callback_data="Back")]]
        context.bot.send_message(chat_id=update.effective_chat.id, reply_markup=InlineKeyboardMarkup(btn),text="list of all monuements: ")
    
    if "Back/Indietro" in update.message.text:

        buttons=[[KeyboardButton("🇮🇹 Italiano")],[KeyboardButton("🇬🇧 / 🇺🇸 English")]]
        context.bot.send_message(chat_id=update.effective_chat.id, text=" 🇮🇹 Scegli la lingua \n 🇬🇧 / 🇺🇸 Choose the language",
        reply_markup=ReplyKeyboardMarkup(buttons, one_time_keyboard=True))

    if "🇮🇹 Italiano" in update.message.text:
        
        i=1
        buttons=[[KeyboardButton("Chiese")],[KeyboardButton("musei")], [KeyboardButton("monumenti")],[KeyboardButton("Back/Indietro")]]
        context.bot.send_message(chat_id=update.effective_chat.id, text="🇮🇹 Benvenuto nel nostro canale Telegram, che tipo di monumento ti piacerebbe visitare?",
        reply_markup=ReplyKeyboardMarkup(buttons, one_time_keyboard=True))

    if "🇬🇧 / 🇺🇸 English" in update.message.text:

        buttons=[[KeyboardButton("Church")],[KeyboardButton("museum")], [KeyboardButton("monuments")],[KeyboardButton("Back/Indietro")]]
        context.bot.send_message(chat_id=update.effective_chat.id, text="🇬🇧 / 🇺🇸 Welcome to our bot, select the type of monument you want to visit?",
        reply_markup=ReplyKeyboardMarkup(buttons, one_time_keyboard=True))

def queryHandler(update, context):

    query = update.callback_query.data
    update.callback_query.answer()

    if "indietro" in query:
        buttons=[[KeyboardButton("Chiese")],[KeyboardButton("musei")], [KeyboardButton("monumenti")],[KeyboardButton("Back/Indietro")]]
        context.bot.send_message(chat_id=update.effective_chat.id, text="🇮🇹 Benvenuto nel nostro canale Telegram, che tipo di monumento ti piacerebbe visitare?",
        reply_markup=ReplyKeyboardMarkup(buttons, one_time_keyboard=True))
    
    if "Back" in query:
        buttons=[[KeyboardButton("Church")],[KeyboardButton("museum")], [KeyboardButton("monuments")],[KeyboardButton("Back/Indietro")]]
        context.bot.send_message(chat_id=update.effective_chat.id, text="🇬🇧 / 🇺🇸 Welcome to our bot, select the type of monument you want to visit?",
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




updater.start_polling()
updater.idle()
