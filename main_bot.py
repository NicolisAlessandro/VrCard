#
# file: main 
#  authors: Alessandro, Simone , Michela
#  date: 27/06/2022
#  description: Main file of the project, bot implementation 
#import pyscreenshot
from email import message
from numpy import append
from telegram import bot_api_version
import telegram.ext
from telegram import *
from requests import *
from telegram.ext import *
from letturaDb import  descrizioneBot, posizioneBotx, posizioneBoty 
nscelta=0
frase = ""
i=0
nposti = 0
index_monument=""
categ=""
torna_alle=""
stamp_to_screen_monument=""
with open("TOKEN.txt", "r") as f:
    TOKEN = f.read()
    print("Your token is: ", TOKEN)
    
#TOKEN = "5592675935:AAFXOB1e14hOIb2iiRdiL_KO0CaIZA0DBE4"

def start(update, context):
    
    buttons=[[InlineKeyboardButton("🇮🇹 Italiano", callback_data="🇮🇹 Italiano")],[InlineKeyboardButton("🇬🇧 / 🇺🇸 English",callback_data="🇬🇧 / 🇺🇸 English")]]
    context.bot.send_message(chat_id=update.effective_chat.id, reply_markup=InlineKeyboardMarkup(buttons),text="lingua:\n🇮🇹 Italiano\n🇬🇧 / 🇺🇸 English ")

def queryHandler(update, context):
    global stamp_to_screen_monument
    global torna_alle
    global categ
    global nscelta
    global index_monument
    global frase
    global nposti
    query = update.callback_query.data
    update.callback_query.answer()

    if "🇮🇹 Italiano" in query:

        buttons=[[InlineKeyboardButton("Mappa",callback_data="Mappa")],[InlineKeyboardButton("Viaggio",callback_data="Viaggio")], [InlineKeyboardButton("Grafici",callback_data="Grafici")],[InlineKeyboardButton("Back/Indietro",callback_data="Back/Indietro")]]
        update.callback_query.edit_message_text(reply_markup=InlineKeyboardMarkup(buttons),  text="🇮🇹 Benvenuto nel nostro canale Telegram, che tipo di Monumento ti piacerebbe visitare?")

    if "🇬🇧 / 🇺🇸 English" in query:

        buttons=[[InlineKeyboardButton("Map",callback_data="engmap_")],[InlineKeyboardButton("Jurney",callback_data="Jurney")], [InlineKeyboardButton("Graphs",callback_data="Graphs")],[InlineKeyboardButton("Back/Indietro",callback_data="Back/Indietro")]]
        update.callback_query.edit_message_text(reply_markup=InlineKeyboardMarkup(buttons),  text="🇬🇧 / 🇺🇸 welcome to our telegram bot,which type of structure would you like to visit today?")
   
    if "Viaggio" in query:

        nscelta=2
        frase="Via_"
        buttons=[[InlineKeyboardButton("Monumenti",callback_data="Via__Monumenti")], [InlineKeyboardButton("Musei ",callback_data="Via__Musei ")],[InlineKeyboardButton("Chiese",callback_data="Via__Chiese")],[InlineKeyboardButton("Back/Indietro",callback_data="🇮🇹 Italiano")]]
        update.callback_query.edit_message_text(reply_markup=InlineKeyboardMarkup(buttons),  text="null")

    if "Mappa" in query:

        nscelta = 1
        frase = "map_"
        buttons=[[InlineKeyboardButton("Monumenti",callback_data="map__Monumenti")], [InlineKeyboardButton("Musei ",callback_data="map__Musei ")],[InlineKeyboardButton("chiese",callback_data="map__Chiese")],[InlineKeyboardButton("Back/Indietro",callback_data="🇮🇹 Italiano")]]
        update.callback_query.edit_message_text(reply_markup=InlineKeyboardMarkup(buttons),  text="mappa")
    
    if "Grafici" in query:

        nscelta = 3
        frase = "graf_"
        buttons=[[InlineKeyboardButton("Monumenti",callback_data="graf__Monumenti")], [InlineKeyboardButton("Musei ",callback_data="graf__Musei ")],[InlineKeyboardButton("Chiese",callback_data="graf__Chiese")],[InlineKeyboardButton("Back/Indietro",callback_data="🇮🇹 Italiano")]]
        update.callback_query.edit_message_text(reply_markup=InlineKeyboardMarkup(buttons),  text="Grafici: ")

    if "engmap_" in query:

        frase="engmap_"
        nscelta = 1
        buttons=[[InlineKeyboardButton("Monuments",callback_data="engmap_Monuments")], [InlineKeyboardButton("Museum ",callback_data="engmap_Museum ")],[InlineKeyboardButton("Church",callback_data="engmap_Church")],[InlineKeyboardButton("Back/Indietro",callback_data="🇮🇹 Italiano")]]
        update.callback_query.edit_message_text(reply_markup=InlineKeyboardMarkup(buttons),  text="mappa")
    
    if "Jurney" in query:

        nscelta=2
        frase="Jur_"
        buttons=[[InlineKeyboardButton("Monuments",callback_data="Jur_Monuments")], [InlineKeyboardButton("Museum",callback_data="Jur_Museum")],[InlineKeyboardButton("Church",callback_data="Jur_Church")],[InlineKeyboardButton("Back/Indietro",callback_data="🇬🇧 / 🇺🇸 English")]]
        update.callback_query.edit_message_text(reply_markup=InlineKeyboardMarkup(buttons),  text="Where we droppin' bois?")
    
    if "Graphs" in query:

        nscelta=3
        frase="graf_"
        buttons=[[InlineKeyboardButton("Monuments",callback_data="graf_Monuments")], [InlineKeyboardButton("Museum",callback_data="graf_Museum")],[InlineKeyboardButton("Church",callback_data="graf_Church")],[InlineKeyboardButton("Back/Indietro",callback_data="🇬🇧 / 🇺🇸 English")]]
        update.callback_query.edit_message_text(reply_markup=InlineKeyboardMarkup(buttons),  text="Graphs: ")

    if "Back/Indietro" in query:

        buttons=[[InlineKeyboardButton("🇮🇹 Italiano", callback_data="🇮🇹 Italiano")],[InlineKeyboardButton("🇬🇧 / 🇺🇸 English",callback_data="🇬🇧 / 🇺🇸 English")]]
        update.callback_query.edit_message_text(reply_markup=InlineKeyboardMarkup(buttons),  text="lingua:\n🇮🇹 Italiano\n🇬🇧 / 🇺🇸 English")
    
    if "Jur_Church" in query:

        buttons=[[InlineKeyboardButton("Chu1",callback_data="Jur_Chu1")],[InlineKeyboardButton("Chu1",callback_data="Jur_Chu2")],[InlineKeyboardButton("Chu1",callback_data="Jur_Chu3")],
        [InlineKeyboardButton("Chu1",callback_data="Jur_Chu4")],[InlineKeyboardButton("Back",callback_data="eng_map")]]
        update.callback_query.edit_message_text(reply_markup=InlineKeyboardMarkup(buttons),  text="which Church?")

    for i in range(0,20):
        if str( "map_" + categ + str(i)) in query:
            coordX = posizioneBotx(categ)
            coordY = posizioneBoty(categ)
            context.bot.sendLocation(chat_id=update.effective_chat.id, latitude=coordX[i][0], longitude=coordY[i][0])
            buttons=[[InlineKeyboardButton("indietro",callback_data="scegli")]]
            update.callback_query.edit_message_text(reply_markup=InlineKeyboardMarkup(buttons),  text="clicca il pulsante per tornare indietro")
   
    for i in range(0,20):
        if str( "Via_" + categ + str(i)) in query:

            buttons=[[InlineKeyboardButton("indietro",callback_data="scegli")]]
            update.callback_query.edit_message_text(reply_markup=InlineKeyboardMarkup(buttons),  text="clicca il pulsante per tornare indietro")

    for i in range(0,20):
        if str( "graf_" + categ + str(i)) in query:
            PHOTO_PATH= 'immagini/'+categ+str(i)
            PHOTO_PATH= 'immagini/immagine.png'
            context.bot.send_photo(chat_id=update.effective_chat.id, photo=open(PHOTO_PATH, 'rb'))
            buttons=[[InlineKeyboardButton("indietro",callback_data="scegli")]]
            update.callback_query.edit_message_text(reply_markup=InlineKeyboardMarkup(buttons),  text="clicca il pulsante per tornare indietro")

    if (str(frase)+ "_Monumenti") in query:

        categ = "Monumenti"
        name_mon = descrizioneBot("Monumenti")
        buttons=[]
        nposti = 8
        for i in range (0, len(name_mon)):
            name_monument_str = name_mon[i][0]
            index_monument = str(frase)+"Monumenti"+str(i)
            buttons.append([InlineKeyboardButton(name_monument_str,callback_data=index_monument)]) 
        buttons.append([InlineKeyboardButton("Indietro",callback_data="scegli")])
        update.callback_query.edit_message_text(reply_markup=InlineKeyboardMarkup(buttons),  text="quale Monumento??")

    if (str(frase)+ "_Chiese") in query:
        
        name_mon = descrizioneBot("Chiese")
        categ = "Chiese"
        nposti = 5
        buttons=[]
        for i in range (0, len(name_mon)):
            name_monument_str = name_mon[i][0]
            index_monument = str(frase)+"Chiese"+str(i)
            buttons.append([InlineKeyboardButton(name_monument_str,callback_data=index_monument)]) 
            print(name_monument_str)
        buttons.append([InlineKeyboardButton("Indietro",callback_data="scegli")]) 
        update.callback_query.edit_message_text(reply_markup=InlineKeyboardMarkup(buttons), text="chiesa?")

    if str(frase+"_Musei") in query:
        categ = "Musei "
        nposti = 15
        name_mon = descrizioneBot("Musei ")
        buttons=[]
        for i in range (0, len(name_mon)):
            name_monument_str = name_mon[i][0]
            index_monument = str(frase)+"Musei "+str(i)
            buttons.append([InlineKeyboardButton(name_monument_str,callback_data=index_monument)]) 
            print(name_monument_str)
        buttons.append([InlineKeyboardButton("Indietro",callback_data="scegli")]) 
        update.callback_query.edit_message_text(reply_markup=InlineKeyboardMarkup(buttons), text="chiesa?")


    if "scegli" in query:

        if nscelta==1:

            buttons=[[InlineKeyboardButton("Monumenti",callback_data="map__Monumenti")], [InlineKeyboardButton("Musei ",callback_data="map__Musei ")],[InlineKeyboardButton("chiese",callback_data="map__Chiese")],[InlineKeyboardButton("Back/Indietro",callback_data="Mappa")]]
            update.callback_query.edit_message_text(reply_markup=InlineKeyboardMarkup(buttons),  text="mappa")
        
        elif nscelta == 2:

            buttons=[[InlineKeyboardButton("Monumenti",callback_data="Via__Monumenti")], [InlineKeyboardButton("Musei ",callback_data="Via__Musei ")],[InlineKeyboardButton("Chiese",callback_data="Via__Chiese")],[InlineKeyboardButton("Back/Indietro",callback_data="🇮🇹 Italiano")]]
            update.callback_query.edit_message_text(reply_markup=InlineKeyboardMarkup(buttons),  text="null")
       
        elif nscelta == 3:

            buttons=[[InlineKeyboardButton("Monumenti",callback_data="graf__Monumenti")], [InlineKeyboardButton("Musei ",callback_data="graf__Musei ")],[InlineKeyboardButton("Chiese",callback_data="graf__Chiese")],[InlineKeyboardButton("Back/Indietro",callback_data="🇮🇹 Italiano")]]
            update.callback_query.edit_message_text(reply_markup=InlineKeyboardMarkup(buttons),  text="Grafici: ")
    
    if "123Back" in query:

        if nscelta==1:

            frase="engmap_"
            nscelta = 1
            buttons=[[InlineKeyboardButton("Monuments",callback_data="map__Monuments")], [InlineKeyboardButton("Museum ",callback_data="map__Museum ")],[InlineKeyboardButton("Church",callback_data="engmap__Church")],[InlineKeyboardButton("Back/Indietro",callback_data="🇮🇹 Italiano")]]
            update.callback_query.edit_message_text(reply_markup=InlineKeyboardMarkup(buttons),  text="mappa")
        
        elif nscelta == 2:

            nscelta=2
            frase="Jur_"
            buttons=[[InlineKeyboardButton("Monuments",callback_data="Jur__Monuments")], [InlineKeyboardButton("Museum",callback_data="Jur__Museum")],[InlineKeyboardButton("Church",callback_data="Jur__Church")],[InlineKeyboardButton("Back/Indietro",callback_data="🇬🇧 / 🇺🇸 English")]]
            update.callback_query.edit_message_text(reply_markup=InlineKeyboardMarkup(buttons),  text="Where we droppin' bois?")
       
        elif nscelta == 3:
            
            nscelta=3
            frase="graf_"
            buttons=[[InlineKeyboardButton("Monuments",callback_data="graf__Monuments")], [InlineKeyboardButton("Museum",callback_data="graf__Museum")],[InlineKeyboardButton("Church",callback_data="graf__Church")],[InlineKeyboardButton("Back/Indietro",callback_data="🇬🇧 / 🇺🇸 English")]]
            update.callback_query.edit_message_text(reply_markup=InlineKeyboardMarkup(buttons),  text="Graphs: ")

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

updater.start_polling()
updater.idle()

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
