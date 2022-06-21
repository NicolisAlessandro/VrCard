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