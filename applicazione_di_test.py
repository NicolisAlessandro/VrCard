#
# file: main 
#  authors: Alessandro, Simone , Michela
#  date: 27/06/2022
#  description: Main file of the project, bot implementation 

import telegram.ext
from telegram import *
from requests import *
from telegram.ext import CallbackQueryHandler
from letturaDb import  descrizioneBot, posizioneBotx, posizioneBoty
#from geopy.geocoders import Nominatim   libreria 
frase = ""
i=0
nposti = 0
index_monument=""
categ=""
with open("TOKEN.txt", "r") as f:
    TOKEN = f.read()
    print("Your token is: ", TOKEN)
    
#TOKEN = "5592675935:AAFXOB1e14hOIb2iiRdiL_KO0CaIZA0DBE4"

def start(update, context):
    buttons=[[InlineKeyboardButton("🇮🇹 Italiano", callback_data="🇮🇹 Italiano")],[InlineKeyboardButton("🇬🇧 / 🇺🇸 English",callback_data="🇬🇧 / 🇺🇸 English")]]
    context.bot.send_message(chat_id=update.effective_chat.id, reply_markup=InlineKeyboardMarkup(buttons),text="lingua:\n🇮🇹 Italiano\n🇬🇧 / 🇺🇸 English ")

def queryHandler(update, context):
    global categ
    global index_monument
    global frase
    global nposti
    query = update.callback_query.data
    update.callback_query.answer()

    if "Viaggio" in query:

        frase="Via_"
        buttons=[[InlineKeyboardButton("Monumenti",callback_data="Via_Monumenti")], [InlineKeyboardButton("Musei",callback_data="Via_Musei")],[InlineKeyboardButton("Chiese",callback_data="Via_Chiese")],[InlineKeyboardButton("Back/Indietro",callback_data="🇮🇹 Italiano")]]
        context.bot.send_message(chat_id=update.effective_chat.id,reply_markup=InlineKeyboardMarkup(buttons), text="null")

    if "Mappa" in query:

        frase = "map_"
        buttons=[[InlineKeyboardButton("Monumenti",callback_data="map_Monumenti")], [InlineKeyboardButton("Musei",callback_data="map_Musei")],[InlineKeyboardButton("chiese",callback_data="map_Chiese")],[InlineKeyboardButton("Back/Indietro",callback_data="🇮🇹 Italiano")]]
        context.bot.send_message(chat_id=update.effective_chat.id,reply_markup=InlineKeyboardMarkup(buttons), text="mappa")
    
    if "Grafici" in query:

        frase = "graf_"
        buttons=[[InlineKeyboardButton("Monumenti",callback_data="graf_Monumenti")], [InlineKeyboardButton("Musei",callback_data="graf_Musei")],[InlineKeyboardButton("Chiese",callback_data="graf_Chiese")],[InlineKeyboardButton("Back/Indietro",callback_data="🇮🇹 Italiano")]]
        context.bot.send_message(chat_id=update.effective_chat.id,reply_markup=InlineKeyboardMarkup(buttons), text="Grafici: ")

    if "eng_map" in query:

        frase="engmap_"
        buttons=[[InlineKeyboardButton("Monuments",callback_data="map_Monuments")], [InlineKeyboardButton("Museum",callback_data="map_Museum")],[InlineKeyboardButton("Church",callback_data="Jur_Church")],[InlineKeyboardButton("Back/Indietro",callback_data="🇬🇧 / 🇺🇸 English")]]
        context.bot.send_message(chat_id=update.effective_chat.id,reply_markup=InlineKeyboardMarkup(buttons), text="map for what?")   
    
    if "Jurney" in query:

        frase="Jur_"
        buttons=[[InlineKeyboardButton("Monuments",callback_data="Jur_Monuments")], [InlineKeyboardButton("Museum",callback_data="Jur_Museum")],[InlineKeyboardButton("Church",callback_data="Jur_Church")],[InlineKeyboardButton("Back/Indietro",callback_data="🇬🇧 / 🇺🇸 English")]]
        context.bot.send_message(chat_id=update.effective_chat.id,reply_markup=InlineKeyboardMarkup(buttons), text="Where we droppin' bois?")
    
    if "Graphs" in query:

        frase="graf_"
        buttons=[[InlineKeyboardButton("Monuments",callback_data="graf_Monuments")], [InlineKeyboardButton("Museum",callback_data="graf_Museum")],[InlineKeyboardButton("Church",callback_data="graf_Church")],[InlineKeyboardButton("Back/Indietro",callback_data="🇬🇧 / 🇺🇸 English")]]
        context.bot.send_message(chat_id=update.effective_chat.id,reply_markup=InlineKeyboardMarkup(buttons), text="Graphs: ")

    if "Back/Indietro" in query:

        start(update, context)

    if "map_Monuments" in query:
    
        buttons=[[InlineKeyboardButton("Funicolare di Castel San Pietro",callback_data="map_Monument1")], [InlineKeyboardButton("Teatro Romano",callback_data="map_Monument2")],
        [InlineKeyboardButton("Arena",callback_data="map_Monument3")],[InlineKeyboardButton("Castelvecchio",callback_data="map_Monument4")],
        [InlineKeyboardButton("Arche Scaligere",callback_data="map_Monument5")],[InlineKeyboardButton("Torre dei Lamberti",callback_data="map_Monument6")],
        [InlineKeyboardButton("Monument",callback_data="map_Monument7")],[InlineKeyboardButton("Back",callback_data="eng_map")]]
        context.bot.send_message(chat_id=update.effective_chat.id,reply_markup=InlineKeyboardMarkup(buttons), text="which Monument?")

    if "map_Museum" in query:

        buttons=[[InlineKeyboardButton("Mus1",callback_data="map_Mus1")],[InlineKeyboardButton("Mus2",callback_data="map_Mus2")],
        [InlineKeyboardButton("Mus3",callback_data="map_Mus3")],[InlineKeyboardButton("Mus4",callback_data="map_Mus4")],[InlineKeyboardButton("Mus5",callback_data="map_Mus5")],
        [InlineKeyboardButton("Mus6",callback_data="map_Mus6")],[InlineKeyboardButton("Mus7",callback_data="map_Mus7")],[InlineKeyboardButton("Mus8",callback_data="map_Mus8")],
        [InlineKeyboardButton("Mus9",callback_data="map_Mus9")],[InlineKeyboardButton("Mus10",callback_data="map_Mus10")],[InlineKeyboardButton("Mus11",callback_data="map_Mus11")],
        [InlineKeyboardButton("Mus12",callback_data="map_Mus12")],[InlineKeyboardButton("Mus13",callback_data="map_Mus13")],
        [InlineKeyboardButton("Mus14",callback_data="map_Mus14")],[InlineKeyboardButton("Back",callback_data="eng_map")]]
        context.bot.send_message(chat_id=update.effective_chat.id,reply_markup=InlineKeyboardMarkup(buttons), text="which museum?")
    
    if "map_Church" in query:

        buttons=[[InlineKeyboardButton("Chu1",callback_data="map_Chu1")], [InlineKeyboardButton("Chu1",callback_data="map_Chu2")], 
        [InlineKeyboardButton("Chu1",callback_data="map_Chu3")], [InlineKeyboardButton("Chu1",callback_data="map_Chu4")],
        [InlineKeyboardButton("Back",callback_data="eng_map")]]
        context.bot.send_message(chat_id=update.effective_chat.id,reply_markup=InlineKeyboardMarkup(buttons), text="which Church?")

    if "graf_Monuments" in query:

        buttons=[[InlineKeyboardButton("Monument",callback_data="graf_Monument1")], [InlineKeyboardButton("Monument",callback_data="graf_Monument2")],
        [InlineKeyboardButton("Monument",callback_data="graf_Monument3")],[InlineKeyboardButton("Monument",callback_data="graf_Monument4")],
        [InlineKeyboardButton("Monument",callback_data="graf_Monument5")],[InlineKeyboardButton("Monument",callback_data="graf_Monument6")],
        [InlineKeyboardButton("Monument",callback_data="graf_Monument7")],[InlineKeyboardButton("Back",callback_data="eng_map")]]
        context.bot.send_message(chat_id=update.effective_chat.id,reply_markup=InlineKeyboardMarkup(buttons), text="which Monument?")

    if "graf_Museum" in query:

        buttons=[[InlineKeyboardButton("Mus1",callback_data="graf_Mus1")],[InlineKeyboardButton("Mus2",callback_data="graf_Mus2")],
        [InlineKeyboardButton("Mus3",callback_data="graf_Mus3")],[InlineKeyboardButton("Mus4",callback_data="graf_Mus4")],[InlineKeyboardButton("Mus5",callback_data="graf_Mus5")],
        [InlineKeyboardButton("Mus6",callback_data="graf_Mus6")],[InlineKeyboardButton("Mus7",callback_data="graf_Mus7")],[InlineKeyboardButton("Mus8",callback_data="graf_Mus8")],
        [InlineKeyboardButton("Mus9",callback_data="graf_Mus9")],[InlineKeyboardButton("Mus10",callback_data="graf_Mus10")],[InlineKeyboardButton("Mus11",callback_data="graf_Mus11")],
        [InlineKeyboardButton("Mus12",callback_data="graf_Mus12")],[InlineKeyboardButton("Mus13",callback_data="graf_Mus13")],
        [InlineKeyboardButton("Mus14",callback_data="graf_Mus14")],[InlineKeyboardButton("Back",callback_data="eng_map")]]
        context.bot.send_message(chat_id=update.effective_chat.id,reply_markup=InlineKeyboardMarkup(buttons), text="which museum?")
    
    if "graf_Church" in query:

        buttons=[[InlineKeyboardButton("Chu1",callback_data="graf_Chu1")],[InlineKeyboardButton("Chu1",callback_data="graf_Chu2")],[InlineKeyboardButton("Chu1",callback_data="graf_Chu3")],
        [InlineKeyboardButton("Chu1",callback_data="graf_Chu4")],[InlineKeyboardButton("Back",callback_data="eng_map")]]
        context.bot.send_message(chat_id=update.effective_chat.id,reply_markup=InlineKeyboardMarkup(buttons), text="which Church?")
    
    if "Jur_Monuments" in query:

        buttons=[[InlineKeyboardButton("Monument",callback_data="Jur_Monument1")], [InlineKeyboardButton("Monument",callback_data="Jur_Monument2")],
        [InlineKeyboardButton("Monument",callback_data="Jur_Monument3")],[InlineKeyboardButton("Monument",callback_data="Jur_Monument4")],
        [InlineKeyboardButton("Monument",callback_data="Jur_Monument5")],[InlineKeyboardButton("Monument",callback_data="Jur_Monument6")],
        [InlineKeyboardButton("Monument",callback_data="Jur_Monument7")],[InlineKeyboardButton("Back",callback_data="eng_map")]]
        context.bot.send_message(chat_id=update.effective_chat.id,reply_markup=InlineKeyboardMarkup(buttons), text="which Monument?")

    if "Jur_Museum" in query:

        buttons=[[InlineKeyboardButton("Mus1",callback_data="Jur_Mus1")],[InlineKeyboardButton("Mus2",callback_data="Jur_Mus2")],
        [InlineKeyboardButton("Mus3",callback_data="Jur_Mus3")],[InlineKeyboardButton("Mus4",callback_data="Jur_Mus4")],[InlineKeyboardButton("Mus5",callback_data="Jur_Mus5")],
        [InlineKeyboardButton("Mus6",callback_data="Jur_Mus6")],[InlineKeyboardButton("Mus7",callback_data="Jur_Mus7")],[InlineKeyboardButton("Mus8",callback_data="Jur_Mus8")],
        [InlineKeyboardButton("Mus9",callback_data="Jur_Mus9")],[InlineKeyboardButton("Mus10",callback_data="Jur_Mus10")],[InlineKeyboardButton("Mus11",callback_data="Jur_Mus11")],
        [InlineKeyboardButton("Mus12",callback_data="Jur_Mus12")],[InlineKeyboardButton("Mus13",callback_data="Jur_Mus13")],
        [InlineKeyboardButton("Mus14",callback_data="Jur_Mus14")],[InlineKeyboardButton("Back",callback_data="eng_map")]]
        context.bot.send_message(chat_id=update.effective_chat.id,reply_markup=InlineKeyboardMarkup(buttons), text="which museum?")
    
    if "Jur_Church" in query:

        buttons=[[InlineKeyboardButton("Chu1",callback_data="Jur_Chu1")],[InlineKeyboardButton("Chu1",callback_data="Jur_Chu2")],[InlineKeyboardButton("Chu1",callback_data="Jur_Chu3")],
        [InlineKeyboardButton("Chu1",callback_data="Jur_Chu4")],[InlineKeyboardButton("Back",callback_data="eng_map")]]
        context.bot.send_message(chat_id=update.effective_chat.id,reply_markup=InlineKeyboardMarkup(buttons), text="which Church?")

    if (str(frase)+ "Monumento") in query:

        categ = "Monumenti"
        name_mon = descrizioneBot("Monumenti")
        buttons=[]
        nposti = 8
        for i in range (0, len(name_mon)):
            name_monument_str = name_mon[i][0]
            index_monument = str(frase)+"Monumento"+str(i)
            buttons.append([InlineKeyboardButton(name_monument_str,callback_data=index_monument)]) 
            print(name_monument_str)

        context.bot.send_message(chat_id=update.effective_chat.id,reply_markup=InlineKeyboardMarkup(buttons), text="quale Monumento??")

    if (str(frase)+ "Chiese") in query:
        
        name_mon = descrizioneBot("Chiese")
        categ = "Chiese"
        nposti = 5
        buttons=[]
        for i in range (0, len(name_mon)):
            name_monument_str = name_mon[i][0]
            index_monument = str(frase)+"Chiesa"+str(i)
            buttons.append([InlineKeyboardButton(name_monument_str,callback_data=index_monument)]) 
            print(name_monument_str)

        context.bot.send_message(chat_id=update.effective_chat.id,reply_markup=InlineKeyboardMarkup(buttons), text="quale Chiesa??")

    if str(frase+"Musei") in query:
        categ = "Musei"
        nposti = 15
        name_mon = descrizioneBot("Musei")
        buttons=[]
        for i in range (0, len(name_mon)):
            name_monument_str = name_mon[i][0]
            index_monument = str(frase)+"Musei"+str(i)
            buttons.append([InlineKeyboardButton(name_monument_str,callback_data=index_monument)]) 
            print(name_monument_str)
        
        context.bot.send_message(chat_id=update.effective_chat.id,reply_markup=InlineKeyboardMarkup(buttons), text="quale Museo??")

    if "🇬🇧 / 🇺🇸 English" in query:
        buttons=[[InlineKeyboardButton("Map",callback_data="eng_map")],[InlineKeyboardButton("Jurney",callback_data="Jurney")], [InlineKeyboardButton("Graphs",callback_data="Graphs")],[InlineKeyboardButton("Back/Indietro",callback_data="Back/Indietro")]]
        context.bot.send_message(chat_id=update.effective_chat.id,reply_markup=InlineKeyboardMarkup(buttons), text="🇮🇹 welcome to our telegram bot,which type of structure would you like to visit today?")

    if "🇮🇹 Italiano" in query:

        buttons=[[InlineKeyboardButton("Mappa",callback_data="Mappa")],[InlineKeyboardButton("Viaggio",callback_data="Viaggio")], [InlineKeyboardButton("Grafici",callback_data="Grafici")],[InlineKeyboardButton("Back/Indietro",callback_data="Back/Indietro")]]
        context.bot.send_message(chat_id=update.effective_chat.id,reply_markup=InlineKeyboardMarkup(buttons), text="🇮🇹 Benvenuto nel nostro canale Telegram, che tipo di Monumento ti piacerebbe visitare?")

    for i in range(0,15):
        if str("map_"+ categ + str(i)) in query:

            descr_it = descrizioneBot(categ)
            stamp_to_screen_monument = "Nome monumento: "+ descr_it[i][0]
            stamp_to_screen_monument += "\n\n\nIndirizzo monumento: "+ descr_it[i][2]
            stamp_to_screen_monument += "\n\n\nDescrizione monumento: "+ descr_it[i][1]
            context.bot.send_message(chat_id=update.effective_chat.id, text = stamp_to_screen_monument)

   
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
