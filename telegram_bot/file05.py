import telegram.ext
from telegram import*
from requests import*
from telegram.ext import CallbackQueryHandler
import csv
import sqlite3

lan = None
with open("TOKEN.txt", "r") as f:
    TOKEN = f.read()
    print("Your token is: ", TOKEN)

def start(update, context):

    #csv_read()

    buttons=[[InlineKeyboardButton("🇮🇹 Italiano", callback_data="🇮🇹 Italiano")],[InlineKeyboardButton("🇬🇧 / 🇺🇸 English",callback_data="🇬🇧 / 🇺🇸 English")]]
    context.bot.send_message(chat_id=update.effective_chat.id, reply_markup=InlineKeyboardMarkup(buttons),text="lingua:\n🇮🇹 Italiano\n🇬🇧 / 🇺🇸 English ")

#def handle_message(update, context):
def queryHandler(update, context):

    query = update.callback_query.data
    update.callback_query.answer()

    if "Viaggio" in query:

        buttons=[[InlineKeyboardButton("Monumenti",callback_data="Via_Monumenti")], [InlineKeyboardButton("Musei",callback_data="Via_Musei")],[InlineKeyboardButton("Chiese",callback_data="Via_Chiese")],[InlineKeyboardButton("Back/Indietro",callback_data="🇮🇹 Italiano")]]
        context.bot.send_message(chat_id=update.effective_chat.id,reply_markup=InlineKeyboardMarkup(buttons), text="null")

    if "Mappa" in query:

        buttons=[[InlineKeyboardButton("Monumenti",callback_data="map_Monumenti")], [InlineKeyboardButton("Musei",callback_data="map_Musei")],[InlineKeyboardButton("chiese",callback_data="map_Chiese")],[InlineKeyboardButton("Back/Indietro",callback_data="🇮🇹 Italiano")]]
        context.bot.send_message(chat_id=update.effective_chat.id,reply_markup=InlineKeyboardMarkup(buttons), text="mappa")
    
    if "Grafici" in query:

        buttons=[[InlineKeyboardButton("Monumenti",callback_data="graf_Monumenti")], [InlineKeyboardButton("Musei",callback_data="graf_Musei")],[InlineKeyboardButton("Chiese",callback_data="graf_Chiese")],[InlineKeyboardButton("Back/Indietro",callback_data="🇮🇹 Italiano")]]
        context.bot.send_message(chat_id=update.effective_chat.id,reply_markup=InlineKeyboardMarkup(buttons), text="Grafici: ")

    if "eng_map" in query:

        buttons=[[InlineKeyboardButton("Monuments",callback_data="map_Monuments")], [InlineKeyboardButton("Museum",callback_data="map_Museum")],[InlineKeyboardButton("Church",callback_data="Jur_Church")],[InlineKeyboardButton("Back/Indietro",callback_data="🇬🇧 / 🇺🇸 English")]]
        context.bot.send_message(chat_id=update.effective_chat.id,reply_markup=InlineKeyboardMarkup(buttons), text="map for what?")   
    
    if "Jurney" in query:

        buttons=[[InlineKeyboardButton("Monuments",callback_data="Jur_Monuments")], [InlineKeyboardButton("Museum",callback_data="Jur_Museum")],[InlineKeyboardButton("Church",callback_data="Jur_Church")],[InlineKeyboardButton("Back/Indietro",callback_data="🇬🇧 / 🇺🇸 English")]]
        context.bot.send_message(chat_id=update.effective_chat.id,reply_markup=InlineKeyboardMarkup(buttons), text="Where we droppin' bois?")
    
    if "Graphs" in query:

        buttons=[[InlineKeyboardButton("Monuments",callback_data="graf_Monuments")], [InlineKeyboardButton("Museum",callback_data="graf_Museum")],[InlineKeyboardButton("Church",callback_data="graf_Church")],[InlineKeyboardButton("Back/Indietro",callback_data="🇬🇧 / 🇺🇸 English")]]
        context.bot.send_message(chat_id=update.effective_chat.id,reply_markup=InlineKeyboardMarkup(buttons), text="Graphs: ")

    if "Back/Indietro" in query:

        start(update, context)

    if "map_Monuments" in query:
    
        buttons=[[InlineKeyboardButton("Monument",callback_data="map_Monument1")], [InlineKeyboardButton("Monument",callback_data="map_Monument2")],
        [InlineKeyboardButton("Monument",callback_data="map_Monument3")],[InlineKeyboardButton("Monument",callback_data="map_Monument4")],
        [InlineKeyboardButton("Monument",callback_data="map_Monument5")],[InlineKeyboardButton("Monument",callback_data="map_Monument6")],
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

    if "map_Monumenti" in query:

<<<<<<< HEAD
        buttons=[[InlineKeyboardButton("Monument",callback_data="map_Monumento1")], [InlineKeyboardButton("Monument",callback_data="map_Monumento2")],
        [InlineKeyboardButton("Monument",callback_data="map_Monumento3")],[InlineKeyboardButton("Monument",callback_data="map_Monumento4")],
        [InlineKeyboardButton("Monument",callback_data="map_Monumento5")],[InlineKeyboardButton("Monument",callback_data="map_Monumento6")],
        [InlineKeyboardButton("Monument",callback_data="map_Monumento7")],[InlineKeyboardButton("Back",callback_data="🇮🇹 Italiano")]]
        context.bot.send_message(chat_id=update.effective_chat.id,reply_markup=InlineKeyboardMarkup(buttons), text="quale Monumento??")

    if "map_Musei" in query:

        buttons=[[InlineKeyboardButton("Mus1",callback_data="map_Museo1")],[InlineKeyboardButton("Mus2",callback_data="map_Museo2")],[InlineKeyboardButton("Mus3",callback_data="map_Museo3")],
=======
        buttons=[[InlineKeyboardButton("Monument",callback_data="map_monumento1")], [InlineKeyboardButton("Monument",callback_data="map_monumento2")],
        [InlineKeyboardButton("Monument",callback_data="map_monumento3")],[InlineKeyboardButton("Monument",callback_data="map_monumento4")],
        [InlineKeyboardButton("Monument",callback_data="map_monumento5")],[InlineKeyboardButton("Monument",callback_data="map_monumento6")],
        [InlineKeyboardButton("Monument",callback_data="map_monumento7")],[InlineKeyboardButton("Back",callback_data="🇮🇹 Italiano")]]
        context.bot.send_message(chat_id=update.effective_chat.id,reply_markup=InlineKeyboardMarkup(buttons), text="quale monumento??")

    if "map_Musei" in query:

        buttons=[[InlineKeyboardButton("Mus1",callback_data="map_Museo1")],[InlineKeyboardButton("Mus1",callback_data="map_Museo1")],
        [InlineKeyboardButton("Mus1",callback_data="map_Museo1")],[InlineKeyboardButton("Mus2",callback_data="map_Museo2")],[InlineKeyboardButton("Mus3",callback_data="map_Museo3")],
>>>>>>> 3ebc1069e8e09088d70132664bf535f7c6a58c15
        [InlineKeyboardButton("Mus4",callback_data="map_Museo4")],[InlineKeyboardButton("Mus5",callback_data="map_Museo5")],[InlineKeyboardButton("Mus6",callback_data="map_Museo6")],
        [InlineKeyboardButton("Mus7",callback_data="map_Museo7")],[InlineKeyboardButton("Mus8",callback_data="map_Museo8")],[InlineKeyboardButton("Mus9",callback_data="map_Museo9")],
        [InlineKeyboardButton("Mus10",callback_data="map_Museo10")],[InlineKeyboardButton("Mus11",callback_data="map_Museo11")],[InlineKeyboardButton("Mus12",callback_data="map_Museo12")],
        [InlineKeyboardButton("Mus13",callback_data="map_Museo13")],[InlineKeyboardButton("Mus14",callback_data="map_Museo14")],[InlineKeyboardButton("Indietro",callback_data="🇮🇹 Italiano")]]
        context.bot.send_message(chat_id=update.effective_chat.id,reply_markup=InlineKeyboardMarkup(buttons), text="quali musei?")
    
    if "map_Chiese" in query:

        buttons=[[InlineKeyboardButton("Chiesa1",callback_data="map_Chi1")],[InlineKeyboardButton("Chiesa1",callback_data="map_Chi2")],[InlineKeyboardButton("Chiesa1",callback_data="map_Chi3")],
        [InlineKeyboardButton("Chiesa1",callback_data="map_Chi4")],[InlineKeyboardButton("Indietro",callback_data="🇮🇹 Italiano")]]
        context.bot.send_message(chat_id=update.effective_chat.id,reply_markup=InlineKeyboardMarkup(buttons), text="quali chiesa?")
    
    if "graf_Monumenti" in query:

        buttons=[[InlineKeyboardButton("Monument",callback_data="graf_Monumento1")], [InlineKeyboardButton("Monument",callback_data="graf_Monumento2")],
        [InlineKeyboardButton("Monument",callback_data="graf_Monumento3")],[InlineKeyboardButton("Monument",callback_data="graf_Monumento4")],
        [InlineKeyboardButton("Monument",callback_data="graf_Monumento5")],[InlineKeyboardButton("Monument",callback_data="graf_Monumento6")],
        [InlineKeyboardButton("Monument",callback_data="graf_Monumento7")],[InlineKeyboardButton("Back",callback_data="🇮🇹 Italiano")]]
        context.bot.send_message(chat_id=update.effective_chat.id,reply_markup=InlineKeyboardMarkup(buttons), text="quale Monumento??")

    if "graf_Musei" in query:

        buttons=[[InlineKeyboardButton("Mus1",callback_data="graf_Museo1")],[InlineKeyboardButton("Mus1",callback_data="graf_Museo1")],
        [InlineKeyboardButton("Mus1",callback_data="graf_Museo1")],[InlineKeyboardButton("Mus2",callback_data="graf_Museo2")],[InlineKeyboardButton("Mus3",callback_data="graf_Museo3")],
        [InlineKeyboardButton("Mus4",callback_data="graf_Museo4")],[InlineKeyboardButton("Mus5",callback_data="graf_Museo5")],[InlineKeyboardButton("Mus6",callback_data="graf_Museo6")],
        [InlineKeyboardButton("Mus7",callback_data="graf_Museo7")],[InlineKeyboardButton("Mus8",callback_data="graf_Museo8")],[InlineKeyboardButton("Mus9",callback_data="graf_Museo9")],
        [InlineKeyboardButton("Mus10",callback_data="graf_Museo10")],[InlineKeyboardButton("Mus11",callback_data="graf_Museo11")],[InlineKeyboardButton("Mus12",callback_data="graf_Museo12")],
        [InlineKeyboardButton("Mus13",callback_data="graf_Museo13")],[InlineKeyboardButton("Mus14",callback_data="graf_Museo14")],[InlineKeyboardButton("Indietro",callback_data="🇮🇹 Italiano")]]
        context.bot.send_message(chat_id=update.effective_chat.id,reply_markup=InlineKeyboardMarkup(buttons), text="quali musei?")
    
    if "graf_Chiese" in query:

        buttons=[[InlineKeyboardButton("Chiesa1",callback_data="graf_Chi1")],[InlineKeyboardButton("Chiesa1",callback_data="graf_Chi2")],[InlineKeyboardButton("Chiesa1",callback_data="graf_Chi3")],
        [InlineKeyboardButton("Chiesa1",callback_data="graf_Chi4")],[InlineKeyboardButton("Indietro",callback_data="🇮🇹 Italiano")]]
        context.bot.send_message(chat_id=update.effective_chat.id,reply_markup=InlineKeyboardMarkup(buttons), text="quale chiesa?")

    if "Via_Monumenti" in query:

        buttons=[[InlineKeyboardButton("Monumento",callback_data="Via_Monumento1")], [InlineKeyboardButton("Monumento",callback_data="Via_Monumento2")],
        [InlineKeyboardButton("Monument",callback_data="Via_Monumento3")],[InlineKeyboardButton("Monument",callback_data="Via_Monumento4")],
        [InlineKeyboardButton("Monument",callback_data="Via_Monumento5")],[InlineKeyboardButton("Monument",callback_data="Via_Monumento6")],
        [InlineKeyboardButton("Monument",callback_data="Via_Monumento7")],[InlineKeyboardButton("Back",callback_data="🇮🇹 Italiano")]]
        context.bot.send_message(chat_id=update.effective_chat.id,reply_markup=InlineKeyboardMarkup(buttons), text="quale Monumento??")

    if "Via_Musei" in query:

<<<<<<< HEAD
        buttons=[[InlineKeyboardButton("Mus1",callback_data="via_Museo1")],[InlineKeyboardButton("Mus2",callback_data="via_Museo2")],[InlineKeyboardButton("Mus3",callback_data="via_Museo3")],
=======
        buttons=[[InlineKeyboardButton("Mus1",callback_data="via_Museo1")],[InlineKeyboardButton("Mus1",callback_data="via_Museo1")],
        [InlineKeyboardButton("Mus1",callback_data="via_Museo1")],[InlineKeyboardButton("Mus2",callback_data="via_Museo2")],[InlineKeyboardButton("Mus3",callback_data="via_Museo3")],
>>>>>>> 3ebc1069e8e09088d70132664bf535f7c6a58c15
        [InlineKeyboardButton("Mus4",callback_data="via_Museo4")],[InlineKeyboardButton("Mus5",callback_data="via_Museo5")],[InlineKeyboardButton("Mus6",callback_data="via_Museo6")],
        [InlineKeyboardButton("Mus7",callback_data="via_Museo7")],[InlineKeyboardButton("Mus8",callback_data="via_Museo8")],[InlineKeyboardButton("Mus9",callback_data="via_Museo9")],
        [InlineKeyboardButton("Mus10",callback_data="via_Museo10")],[InlineKeyboardButton("Mus11",callback_data="via_Museo11")],[InlineKeyboardButton("Mus12",callback_data="via_Museo12")],
        [InlineKeyboardButton("Mus13",callback_data="via_Museo13")],[InlineKeyboardButton("Mus14",callback_data="via_Museo14")],[InlineKeyboardButton("Indietro",callback_data="🇮🇹 Italiano")]]
        context.bot.send_message(chat_id=update.effective_chat.id,reply_markup=InlineKeyboardMarkup(buttons), text="quali museo?")
    
    if "Via_Chiese" in query:

        buttons=[[InlineKeyboardButton("Chiesa1",callback_data="Via_Chi1")],[InlineKeyboardButton("Chiesa1",callback_data="Via_Chi2")],[InlineKeyboardButton("Chiesa1",callback_data="Via_Chi3")],
        [InlineKeyboardButton("Chiesa1",callback_data="Via_Chi4")],[InlineKeyboardButton("Indietro",callback_data="🇮🇹 Italiano")]]
        context.bot.send_message(chat_id=update.effective_chat.id,reply_markup=InlineKeyboardMarkup(buttons), text="quale chiesa?")


    if "🇬🇧 / 🇺🇸 English" in query:
        buttons=[[InlineKeyboardButton("Map",callback_data="eng_map")],[InlineKeyboardButton("Jurney",callback_data="Jurney")], [InlineKeyboardButton("Graphs",callback_data="Graphs")],[InlineKeyboardButton("Back/Indietro",callback_data="Back/Indietro")]]
        context.bot.send_message(chat_id=update.effective_chat.id,reply_markup=InlineKeyboardMarkup(buttons), text="🇮🇹 welcome to our telegram bot,which type of structure would you like to visit today?")

    if "🇮🇹 Italiano" in query:

        buttons=[[InlineKeyboardButton("Mappa",callback_data="Mappa")],[InlineKeyboardButton("Viaggio",callback_data="Viaggio")], [InlineKeyboardButton("Grafici",callback_data="Grafici")],[InlineKeyboardButton("Back/Indietro",callback_data="Back/Indietro")]]
        context.bot.send_message(chat_id=update.effective_chat.id,reply_markup=InlineKeyboardMarkup(buttons), text="🇮🇹 Benvenuto nel nostro canale Telegram, che tipo di Monumento ti piacerebbe visitare?")

    if "via_Church1" in query:
        descr_it = descrizioneBot("Chiese")
        list = posizioneBot("Chiese")
        context.bot.send_message(chat_id=update.effective_chat.id, text = descr_it[0])
        context.bot.send_message(chat_id=update.effective_chat.id, text = list[0])
        
    if "via_Church2" in query:
        descr_it = descrizioneBot("Chiese")
        list = posizioneBot("Chiese")
        context.bot.send_message(chat_id=update.effective_chat.id, text = descr_it[1])
        context.bot.send_message(chat_id=update.effective_chat.id, text = list[1])
        
    if "via_Church3" in query:
        descr_it = descrizioneBot("Chiese")
        list = posizioneBot("Chiese")
        context.bot.send_message(chat_id=update.effective_chat.id, text = descr_it[2])
        context.bot.send_message(chat_id=update.effective_chat.id, text = list[2])
        
    if "via_Church4" in query:
        descr_it = descrizioneBot("Chiese")
        list = posizioneBot("Chiese")
        context.bot.send_message(chat_id=update.effective_chat.id, text = descr_it[3])
        context.bot.send_message(chat_id=update.effective_chat.id, text = list[3])
    
    if "via_Monument1" in query:
        list = posizioneBot("Monumenti")
        descr_it = descrizioneBot("Monumenti")
        context.bot.send_message(chat_id=update.effective_chat.id, text = descr_it[0])
        context.bot.send_message(chat_id=update.effective_chat.id, text = list[0])
    
    if "via_Monument2" in query:
        list = posizioneBot("Monumenti")
        descr_it = descrizioneBot("Monumenti")
        context.bot.send_message(chat_id=update.effective_chat.id, text = descr_it[1])
        context.bot.send_message(chat_id=update.effective_chat.id, text = list[1])
        
    if "via_Monument3" in query:
        list = posizioneBot("Monumenti")
        descr_it = descrizioneBot("Monumenti")
        context.bot.send_message(chat_id=update.effective_chat.id, text = descr_it[2])
        context.bot.send_message(chat_id=update.effective_chat.id, text = list[2])
        
    if "via_Monument4" in query:
        list = posizioneBot("Monumenti")
        descr_it = descrizioneBot("Monumenti")
        context.bot.send_message(chat_id=update.effective_chat.id, text = descr_it[3])
        context.bot.send_message(chat_id=update.effective_chat.id, text = list[3])
        
    if "via_Monument5" in query:
        list = posizioneBot("Monumenti")
        descr_it = descrizioneBot("Monumenti")
        context.bot.send_message(chat_id=update.effective_chat.id, text = descr_it[4])
        context.bot.send_message(chat_id=update.effective_chat.id, text = list[4])
        
    if "via_Monument6" in query:
        list = posizioneBot("Monumenti")
        descr_it = descrizioneBot("Monumenti")
        context.bot.send_message(chat_id=update.effective_chat.id, text = descr_it[5])
        context.bot.send_message(chat_id=update.effective_chat.id, text = list[5])
        
    if "via_Monument7" in query:
        list = posizioneBot("Monumenti")
        descr_it = descrizioneBot("Monumenti")
        context.bot.send_message(chat_id=update.effective_chat.id, text = descr_it[6])
        context.bot.send_message(chat_id=update.effective_chat.id, text = list[6])
        
    if "via_Museum1" in query:
        list = posizioneBot("Musei")
        descr_it = descrizioneBot("Musei")
        context.bot.send_message(chat_id=update.effective_chat.id, text = descr_it[0])
        context.bot.send_message(chat_id=update.effective_chat.id, text = list[0])
    
    if "via_Museum2" in query:
        list = posizioneBot("Monumenti")
        descr_it = descrizioneBot("Monumenti")
        context.bot.send_message(chat_id=update.effective_chat.id, text = descr_it[1])
        context.bot.send_message(chat_id=update.effective_chat.id, text = list[1])
        
    if "via_Museum3" in query:
        list = posizioneBot("Monumenti")
        descr_it = descrizioneBot("Monumenti")
        context.bot.send_message(chat_id=update.effective_chat.id, text = descr_it[2])
        context.bot.send_message(chat_id=update.effective_chat.id, text = list[2])
        
    if "via_Museum4" in query:
        list = posizioneBot("Monumenti")
        descr_it = descrizioneBot("Monumenti")
        context.bot.send_message(chat_id=update.effective_chat.id, text = descr_it[3])
        context.bot.send_message(chat_id=update.effective_chat.id, text = list[3])
        
    if "via_Museum5" in query:
        list = posizioneBot("Monumenti")
        descr_it = descrizioneBot("Monumenti")
        context.bot.send_message(chat_id=update.effective_chat.id, text = descr_it[4])
        context.bot.send_message(chat_id=update.effective_chat.id, text = list[4])
        
    if "via_Museum6" in query:
        list = posizioneBot("Monumenti")
        descr_it = descrizioneBot("Monumenti")
        context.bot.send_message(chat_id=update.effective_chat.id, text = descr_it[5])
        context.bot.send_message(chat_id=update.effective_chat.id, text = list[5])
        
    if "via_Museum7" in query:
        list = posizioneBot("Monumenti")
        descr_it = descrizioneBot("Monumenti")
        context.bot.send_message(chat_id=update.effective_chat.id, text = descr_it[6])
        context.bot.send_message(chat_id=update.effective_chat.id, text = list[6])
        
    if "via_Museum8" in query:
        list = posizioneBot("Monumenti")
        descr_it = descrizioneBot("Monumenti")
        context.bot.send_message(chat_id=update.effective_chat.id, text = descr_it[7])
        context.bot.send_message(chat_id=update.effective_chat.id, text = list[7])
    
    if "via_Museum9" in query:
        list = posizioneBot("Monumenti")
        descr_it = descrizioneBot("Monumenti")
        context.bot.send_message(chat_id=update.effective_chat.id, text = descr_it[8])
        context.bot.send_message(chat_id=update.effective_chat.id, text = list[8])
        
    if "via_Museum10" in query:
        list = posizioneBot("Monumenti")
        descr_it = descrizioneBot("Monumenti")
        context.bot.send_message(chat_id=update.effective_chat.id, text = descr_it[9])
        context.bot.send_message(chat_id=update.effective_chat.id, text = list[9])
        
    if "via_Museum11" in query:
        list = posizioneBot("Monumenti")
        descr_it = descrizioneBot("Monumenti")
        context.bot.send_message(chat_id=update.effective_chat.id, text = descr_it[10])
        context.bot.send_message(chat_id=update.effective_chat.id, text = list[10])
        
    if "via_Museum12" in query:
        list = posizioneBot("Monumenti")
        descr_it = descrizioneBot("Monumenti")
        context.bot.send_message(chat_id=update.effective_chat.id, text = descr_it[11])
        context.bot.send_message(chat_id=update.effective_chat.id, text = list[11])
        
    if "via_Museum13" in query:
        list = posizioneBot("Monumenti")
        descr_it = descrizioneBot("Monumenti")
        context.bot.send_message(chat_id=update.effective_chat.id, text = descr_it[12])
        context.bot.send_message(chat_id=update.effective_chat.id, text = list[12])
        
    if "via_Museum14" in query:
        list = posizioneBot("Monumenti")
        descr_it = descrizioneBot("Monumenti")
        context.bot.send_message(chat_id=update.effective_chat.id, text = descr_it[13])
        context.bot.send_message(chat_id=update.effective_chat.id, text = list[13])
    
    if "via_Chiese1" in query:
        descr_it = descrizioneBot("Chiese")
        list = posizioneBot("Chiese")
        context.bot.send_message(chat_id=update.effective_chat.id, text = descr_it[0])
        context.bot.send_message(chat_id=update.effective_chat.id, text = list[0])
        
    if "via_Chiese2" in query:
        descr_it = descrizioneBot("Chiese")
        list = posizioneBot("Chiese")
        context.bot.send_message(chat_id=update.effective_chat.id, text = descr_it[1])
        context.bot.send_message(chat_id=update.effective_chat.id, text = list[1])
        
    if "via_Chiese3" in query:
        descr_it = descrizioneBot("Chiese")
        list = posizioneBot("Chiese")
        context.bot.send_message(chat_id=update.effective_chat.id, text = descr_it[2])
        context.bot.send_message(chat_id=update.effective_chat.id, text = list[2])
        
    if "via_Chiese4" in query:
        descr_it = descrizioneBot("Chiese")
        list = posizioneBot("Chiese")
        context.bot.send_message(chat_id=update.effective_chat.id, text = descr_it[3])
        context.bot.send_message(chat_id=update.effective_chat.id, text = list[3])
    
    if "via_Monumento1" in query:
        list = posizioneBot("Monumenti")
        descr_it = descrizioneBot("Monumenti")
        context.bot.send_message(chat_id=update.effective_chat.id, text = descr_it[0])
        context.bot.send_message(chat_id=update.effective_chat.id, text = list[0])
    
    if "via_Monumento2" in query:
        list = posizioneBot("Monumenti")
        descr_it = descrizioneBot("Monumenti")
        context.bot.send_message(chat_id=update.effective_chat.id, text = descr_it[1])
        context.bot.send_message(chat_id=update.effective_chat.id, text = list[1])
        
    if "via_Monumento3" in query:
        list = posizioneBot("Monumenti")
        descr_it = descrizioneBot("Monumenti")
        context.bot.send_message(chat_id=update.effective_chat.id, text = descr_it[2])
        context.bot.send_message(chat_id=update.effective_chat.id, text = list[2])
        
    if "via_Monumento4" in query:
        list = posizioneBot("Monumenti")
        descr_it = descrizioneBot("Monumenti")
        context.bot.send_message(chat_id=update.effective_chat.id, text = descr_it[3])
        context.bot.send_message(chat_id=update.effective_chat.id, text = list[3])
        
    if "via_Monumento5" in query:
        list = posizioneBot("Monumenti")
        descr_it = descrizioneBot("Monumenti")
        context.bot.send_message(chat_id=update.effective_chat.id, text = descr_it[4])
        context.bot.send_message(chat_id=update.effective_chat.id, text = list[4])
        
    if "via_Monumento6" in query:
        list = posizioneBot("Monumenti")
        descr_it = descrizioneBot("Monumenti")
        context.bot.send_message(chat_id=update.effective_chat.id, text = descr_it[5])
        context.bot.send_message(chat_id=update.effective_chat.id, text = list[5])
        
    if "via_Monumento7" in query:
        list = posizioneBot("Monumenti")
        descr_it = descrizioneBot("Monumenti")
        context.bot.send_message(chat_id=update.effective_chat.id, text = descr_it[6])
        context.bot.send_message(chat_id=update.effective_chat.id, text = list[6])
        
    if "via_Museo1" in query:
        list = posizioneBot("Monumenti")
        descr_it = descrizioneBot("Monumenti")
        context.bot.send_message(chat_id=update.effective_chat.id, text = descr_it[0])
        context.bot.send_message(chat_id=update.effective_chat.id, text = list[0])
    
    if "via_Museo2" in query:
        list = posizioneBot("Monumenti")
        descr_it = descrizioneBot("Monumenti")
        context.bot.send_message(chat_id=update.effective_chat.id, text = descr_it[1])
        context.bot.send_message(chat_id=update.effective_chat.id, text = list[1])
        
    if "via_Museo3" in query:
        list = posizioneBot("Monumenti")
        descr_it = descrizioneBot("Monumenti")
        context.bot.send_message(chat_id=update.effective_chat.id, text = descr_it[2])
        context.bot.send_message(chat_id=update.effective_chat.id, text = list[2])
        
    if "via_Museo4" in query:
        list = posizioneBot("Monumenti")
        descr_it = descrizioneBot("Monumenti")
        context.bot.send_message(chat_id=update.effective_chat.id, text = descr_it[3])
        context.bot.send_message(chat_id=update.effective_chat.id, text = list[3])
        
    if "via_Museo5" in query:
        list = posizioneBot("Monumenti")
        descr_it = descrizioneBot("Monumenti")
        context.bot.send_message(chat_id=update.effective_chat.id, text = descr_it[4])
        context.bot.send_message(chat_id=update.effective_chat.id, text = list[4])
        
    if "via_Museo6" in query:
        list = posizioneBot("Monumenti")
        descr_it = descrizioneBot("Monumenti")
        context.bot.send_message(chat_id=update.effective_chat.id, text = descr_it[5])
        context.bot.send_message(chat_id=update.effective_chat.id, text = list[5])
        
    if "via_Museo7" in query:
        list = posizioneBot("Monumenti")
        descr_it = descrizioneBot("Monumenti")
        context.bot.send_message(chat_id=update.effective_chat.id, text = descr_it[6])
        context.bot.send_message(chat_id=update.effective_chat.id, text = list[6])
        
    if "via_Museo8" in query:
        list = posizioneBot("Monumenti")
        descr_it = descrizioneBot("Monumenti")
        context.bot.send_message(chat_id=update.effective_chat.id, text = descr_it[7])
        context.bot.send_message(chat_id=update.effective_chat.id, text = list[7])
    
    if "via_Museo9" in query:
        list = posizioneBot("Monumenti")
        descr_it = descrizioneBot("Monumenti")
        context.bot.send_message(chat_id=update.effective_chat.id, text = descr_it[8])
        context.bot.send_message(chat_id=update.effective_chat.id, text = list[8])
        
    if "via_Museo10" in query:
        list = posizioneBot("Monumenti")
        descr_it = descrizioneBot("Monumenti")
        context.bot.send_message(chat_id=update.effective_chat.id, text = descr_it[9])
        context.bot.send_message(chat_id=update.effective_chat.id, text = list[9])
        
    if "via_Museo11" in query:
        list = posizioneBot("Monumenti")
        descr_it = descrizioneBot("Monumenti")
        context.bot.send_message(chat_id=update.effective_chat.id, text = descr_it[10])
        context.bot.send_message(chat_id=update.effective_chat.id, text = list[10])
        
    if "via_Museo12" in query:
        list = posizioneBot("Monumenti")
        descr_it = descrizioneBot("Monumenti")
        context.bot.send_message(chat_id=update.effective_chat.id, text = descr_it[11])
        context.bot.send_message(chat_id=update.effective_chat.id, text = list[11])
        
    if "via_Museo13" in query:
        list = posizioneBot("Monumenti")
        descr_it = descrizioneBot("Monumenti")
        context.bot.send_message(chat_id=update.effective_chat.id, text = descr_it[12])
        context.bot.send_message(chat_id=update.effective_chat.id, text = list[12])
        
    if "via_Museo14" in query:
        list = posizioneBot("Monumenti")
        descr_it = descrizioneBot("Monumenti")
        context.bot.send_message(chat_id=update.effective_chat.id, text = descr_it[13])
        context.bot.send_message(chat_id=update.effective_chat.id, text = list[13])

    if "museo" in query:
        context.bot.send_message(chat_id=update.effective_chat.id, text="musei")
    
    if "chiesa" in query:
        context.bot.send_message(chat_id=update.effective_chat.id, text="chiese")

    if "monumento" in query:
        context.bot.send_message(chat_id=update.effective_chat.id, text="monumenti")
    
    if "museum" in query:
        context.bot.send_message(chat_id=update.effective_chat.id, text="museum")
    
<<<<<<< HEAD
    if "map_Museum2" in query:
        list = posizioneBot("Monumenti")
        descr_it = descrizioneBot("Monumenti")
        context.bot.send_message(chat_id=update.effective_chat.id, text = descr_it[1])
        context.bot.send_message(chat_id=update.effective_chat.id, text = list[1])
        
    if "map_Museum3" in query:
        list = posizioneBot("Monumenti")
        descr_it = descrizioneBot("Monumenti")
        context.bot.send_message(chat_id=update.effective_chat.id, text = descr_it[2])
        context.bot.send_message(chat_id=update.effective_chat.id, text = list[2])
        
    if "map_Museum4" in query:
        list = posizioneBot("Monumenti")
        descr_it = descrizioneBot("Monumenti")
        context.bot.send_message(chat_id=update.effective_chat.id, text = descr_it[3])
        context.bot.send_message(chat_id=update.effective_chat.id, text = list[3])
        
    if "map_Museum5" in query:
        list = posizioneBot("Monumenti")
        descr_it = descrizioneBot("Monumenti")
        context.bot.send_message(chat_id=update.effective_chat.id, text = descr_it[4])
        context.bot.send_message(chat_id=update.effective_chat.id, text = list[4])
        
    if "map_Museum6" in query:
        list = posizioneBot("Monumenti")
        descr_it = descrizioneBot("Monumenti")
        context.bot.send_message(chat_id=update.effective_chat.id, text = descr_it[5])
        context.bot.send_message(chat_id=update.effective_chat.id, text = list[5])
        
    if "map_Museum7" in query:
        list = posizioneBot("Monumenti")
        descr_it = descrizioneBot("Monumenti")
        context.bot.send_message(chat_id=update.effective_chat.id, text = descr_it[6])
        context.bot.send_message(chat_id=update.effective_chat.id, text = list[6])
        
    if "map_Museum8" in query:
        list = posizioneBot("Monumenti")
        descr_it = descrizioneBot("Monumenti")
        context.bot.send_message(chat_id=update.effective_chat.id, text = descr_it[7])
        context.bot.send_message(chat_id=update.effective_chat.id, text = list[7])
    
    if "map_Museum9" in query:
        list = posizioneBot("Monumenti")
        descr_it = descrizioneBot("Monumenti")
        context.bot.send_message(chat_id=update.effective_chat.id, text = descr_it[8])
        context.bot.send_message(chat_id=update.effective_chat.id, text = list[8])
        
    if "map_Museum10" in query:
        list = posizioneBot("Monumenti")
        descr_it = descrizioneBot("Monumenti")
        context.bot.send_message(chat_id=update.effective_chat.id, text = descr_it[9])
        context.bot.send_message(chat_id=update.effective_chat.id, text = list[9])
        
    if "map_Museum11" in query:
        list = posizioneBot("Monumenti")
        descr_it = descrizioneBot("Monumenti")
        context.bot.send_message(chat_id=update.effective_chat.id, text = descr_it[10])
        context.bot.send_message(chat_id=update.effective_chat.id, text = list[10])
        
    if "map_Museum12" in query:
        list = posizioneBot("Monumenti")
        descr_it = descrizioneBot("Monumenti")
        context.bot.send_message(chat_id=update.effective_chat.id, text = descr_it[11])
        context.bot.send_message(chat_id=update.effective_chat.id, text = list[11])
        
    if "map_Museum13" in query:
        list = posizioneBot("Monumenti")
        descr_it = descrizioneBot("Monumenti")
        context.bot.send_message(chat_id=update.effective_chat.id, text = descr_it[12])
        context.bot.send_message(chat_id=update.effective_chat.id, text = list[12])
        
    if "map_Museum14" in query:
        list = posizioneBot("Monumenti")
        descr_it = descrizioneBot("Monumenti")
        context.bot.send_message(chat_id=update.effective_chat.id, text = descr_it[13])
        context.bot.send_message(chat_id=update.effective_chat.id, text = list[13])
    
    if "mapp_Chiese1" in query:
        descr_it = descrizioneBot("Chiese")
        list = posizioneBot("Chiese")
        context.bot.send_message(chat_id=update.effective_chat.id, text = descr_it[0])
        context.bot.send_message(chat_id=update.effective_chat.id, text = list[0])
        
    if "mapp_Chiese2" in query:
        descr_it = descrizioneBot("Chiese")
        list = posizioneBot("Chiese")
        context.bot.send_message(chat_id=update.effective_chat.id, text = descr_it[1])
        context.bot.send_message(chat_id=update.effective_chat.id, text = list[1])
        
    if "mapp_Chiese3" in query:
        descr_it = descrizioneBot("Chiese")
        list = posizioneBot("Chiese")
        context.bot.send_message(chat_id=update.effective_chat.id, text = descr_it[2])
        context.bot.send_message(chat_id=update.effective_chat.id, text = list[2])
        
    if "mapp_Chiese4" in query:
        descr_it = descrizioneBot("Chiese")
        list = posizioneBot("Chiese")
        context.bot.send_message(chat_id=update.effective_chat.id, text = descr_it[3])
        context.bot.send_message(chat_id=update.effective_chat.id, text = list[3])
    
    if "map_Monumento1" in query:
        list = posizioneBot("Monumenti")
        descr_it = descrizioneBot("Monumenti")
        context.bot.send_message(chat_id=update.effective_chat.id, text = descr_it[0])
        context.bot.send_message(chat_id=update.effective_chat.id, text = list[0])
    
    if "map_Monumento2" in query:
        list = posizioneBot("Monumenti")
        descr_it = descrizioneBot("Monumenti")
        context.bot.send_message(chat_id=update.effective_chat.id, text = descr_it[1])
        context.bot.send_message(chat_id=update.effective_chat.id, text = list[1])
        
    if "map_Monumento3" in query:
        list = posizioneBot("Monumenti")
        descr_it = descrizioneBot("Monumenti")
        context.bot.send_message(chat_id=update.effective_chat.id, text = descr_it[2])
        context.bot.send_message(chat_id=update.effective_chat.id, text = list[2])
        
    if "map_Monumento4" in query:
        list = posizioneBot("Monumenti")
        descr_it = descrizioneBot("Monumenti")
        context.bot.send_message(chat_id=update.effective_chat.id, text = descr_it[3])
        context.bot.send_message(chat_id=update.effective_chat.id, text = list[3])
        
    if "map_Monumento5" in query:
        list = posizioneBot("Monumenti")
        descr_it = descrizioneBot("Monumenti")
        context.bot.send_message(chat_id=update.effective_chat.id, text = descr_it[4])
        context.bot.send_message(chat_id=update.effective_chat.id, text = list[4])
        
    if "map_Monumento6" in query:
        list = posizioneBot("Monumenti")
        descr_it = descrizioneBot("Monumenti")
        context.bot.send_message(chat_id=update.effective_chat.id, text = descr_it[5])
        context.bot.send_message(chat_id=update.effective_chat.id, text = list[5])
        
    if "map_Monumento7" in query:
        list = posizioneBot("Monumenti")
        descr_it = descrizioneBot("Monumenti")
        context.bot.send_message(chat_id=update.effective_chat.id, text = descr_it[6])
        context.bot.send_message(chat_id=update.effective_chat.id, text = list[6])
        
    if "map_Museo1" in query:
        list = posizioneBot("Monumenti")
        descr_it = descrizioneBot("Monumenti")
        context.bot.send_message(chat_id=update.effective_chat.id, text = descr_it[0])
        context.bot.send_message(chat_id=update.effective_chat.id, text = list[0])
    
    if "map_Museo2" in query:
        list = posizioneBot("Monumenti")
        descr_it = descrizioneBot("Monumenti")
        context.bot.send_message(chat_id=update.effective_chat.id, text = descr_it[1])
        context.bot.send_message(chat_id=update.effective_chat.id, text = list[1])
        
    if "map_Museo3" in query:
        list = posizioneBot("Monumenti")
        descr_it = descrizioneBot("Monumenti")
        context.bot.send_message(chat_id=update.effective_chat.id, text = descr_it[2])
        context.bot.send_message(chat_id=update.effective_chat.id, text = list[2])
        
    if "map_Museo4" in query:
        list = posizioneBot("Monumenti")
        descr_it = descrizioneBot("Monumenti")
        context.bot.send_message(chat_id=update.effective_chat.id, text = descr_it[3])
        context.bot.send_message(chat_id=update.effective_chat.id, text = list[3])
        
    if "map_Museo5" in query:
        list = posizioneBot("Monumenti")
        descr_it = descrizioneBot("Monumenti")
        context.bot.send_message(chat_id=update.effective_chat.id, text = descr_it[4])
        context.bot.send_message(chat_id=update.effective_chat.id, text = list[4])
        
    if "map_Museo6" in query:
        list = posizioneBot("Monumenti")
        descr_it = descrizioneBot("Monumenti")
        context.bot.send_message(chat_id=update.effective_chat.id, text = descr_it[5])
        context.bot.send_message(chat_id=update.effective_chat.id, text = list[5])
        
    if "map_Museo7" in query:
        list = posizioneBot("Monumenti")
        descr_it = descrizioneBot("Monumenti")
        context.bot.send_message(chat_id=update.effective_chat.id, text = descr_it[6])
        context.bot.send_message(chat_id=update.effective_chat.id, text = list[6])
        
    if "map_Museo8" in query:
        list = posizioneBot("Monumenti")
        descr_it = descrizioneBot("Monumenti")
        context.bot.send_message(chat_id=update.effective_chat.id, text = descr_it[7])
        context.bot.send_message(chat_id=update.effective_chat.id, text = list[7])
    
    if "map_Museo9" in query:
        list = posizioneBot("Monumenti")
        descr_it = descrizioneBot("Monumenti")
        context.bot.send_message(chat_id=update.effective_chat.id, text = descr_it[8])
        context.bot.send_message(chat_id=update.effective_chat.id, text = list[8])
        
    if "map_Museo10" in query:
        list = posizioneBot("Monumenti")
        descr_it = descrizioneBot("Monumenti")
        context.bot.send_message(chat_id=update.effective_chat.id, text = descr_it[9])
        context.bot.send_message(chat_id=update.effective_chat.id, text = list[9])
        
    if "map_Museo11" in query:
        list = posizioneBot("Monumenti")
        descr_it = descrizioneBot("Monumenti")
        context.bot.send_message(chat_id=update.effective_chat.id, text = descr_it[10])
        context.bot.send_message(chat_id=update.effective_chat.id, text = list[10])
        
    if "map_Museo12" in query:
        list = posizioneBot("Monumenti")
        descr_it = descrizioneBot("Monumenti")
        context.bot.send_message(chat_id=update.effective_chat.id, text = descr_it[11])
        context.bot.send_message(chat_id=update.effective_chat.id, text = list[11])
        
    if "map_Museo13" in query:
        list = posizioneBot("Monumenti")
        descr_it = descrizioneBot("Monumenti")
        context.bot.send_message(chat_id=update.effective_chat.id, text = descr_it[12])
        context.bot.send_message(chat_id=update.effective_chat.id, text = list[12])
        
    if "map_Museo14" in query:
        list = posizioneBot("Monumenti")
        descr_it = descrizioneBot("Monumenti")
        context.bot.send_message(chat_id=update.effective_chat.id, text = descr_it[13])
        context.bot.send_message(chat_id=update.effective_chat.id, text = list[13])
        
    if "graf_Church1" in query:
        descr_it = descrizioneBot("Chiese")
        list = posizioneBot("Chiese")
        context.bot.send_message(chat_id=update.effective_chat.id, text = descr_it[0])
        context.bot.send_message(chat_id=update.effective_chat.id, text = list[0])
        
    if "graf_Church2" in query:
        descr_it = descrizioneBot("Chiese")
        list = posizioneBot("Chiese")
        context.bot.send_message(chat_id=update.effective_chat.id, text = descr_it[1])
        context.bot.send_message(chat_id=update.effective_chat.id, text = list[1])
        
    if "graf_Church3" in query:
        descr_it = descrizioneBot("Chiese")
        list = posizioneBot("Chiese")
        context.bot.send_message(chat_id=update.effective_chat.id, text = descr_it[2])
        context.bot.send_message(chat_id=update.effective_chat.id, text = list[2])
        
    if "graf_Church4" in query:
        descr_it = descrizioneBot("Chiese")
        list = posizioneBot("Chiese")
        context.bot.send_message(chat_id=update.effective_chat.id, text = descr_it[3])
        context.bot.send_message(chat_id=update.effective_chat.id, text = list[3])
    
    if "graf_Monument1" in query:
        list = posizioneBot("Monumenti")
        descr_it = descrizioneBot("Monumenti")
        context.bot.send_message(chat_id=update.effective_chat.id, text = descr_it[0])
        context.bot.send_message(chat_id=update.effective_chat.id, text = list[0])
    
    if "graf_Monument2" in query:
        list = posizioneBot("Monumenti")
        descr_it = descrizioneBot("Monumenti")
        context.bot.send_message(chat_id=update.effective_chat.id, text = descr_it[1])
        context.bot.send_message(chat_id=update.effective_chat.id, text = list[1])
        
    if "graf_Monument3" in query:
        list = posizioneBot("Monumenti")
        descr_it = descrizioneBot("Monumenti")
        context.bot.send_message(chat_id=update.effective_chat.id, text = descr_it[2])
        context.bot.send_message(chat_id=update.effective_chat.id, text = list[2])
        
    if "graf_Monument4" in query:
        list = posizioneBot("Monumenti")
        descr_it = descrizioneBot("Monumenti")
        context.bot.send_message(chat_id=update.effective_chat.id, text = descr_it[3])
        context.bot.send_message(chat_id=update.effective_chat.id, text = list[3])
        
    if "graf_Monument5" in query:
        list = posizioneBot("Monumenti")
        descr_it = descrizioneBot("Monumenti")
        context.bot.send_message(chat_id=update.effective_chat.id, text = descr_it[4])
        context.bot.send_message(chat_id=update.effective_chat.id, text = list[4])
        
    if "graf_Monument6" in query:
        list = posizioneBot("Monumenti")
        descr_it = descrizioneBot("Monumenti")
        context.bot.send_message(chat_id=update.effective_chat.id, text = descr_it[5])
        context.bot.send_message(chat_id=update.effective_chat.id, text = list[5])
        
    if "graf_Monument7" in query:
        list = posizioneBot("Monumenti")
        descr_it = descrizioneBot("Monumenti")
        context.bot.send_message(chat_id=update.effective_chat.id, text = descr_it[6])
        context.bot.send_message(chat_id=update.effective_chat.id, text = list[6])
        
    if "graf_Museum1" in query:
        list = posizioneBot("Monumenti")
        descr_it = descrizioneBot("Monumenti")
        context.bot.send_message(chat_id=update.effective_chat.id, text = descr_it[0])
        context.bot.send_message(chat_id=update.effective_chat.id, text = list[0])
    
    if "graf_Museum2" in query:
        list = posizioneBot("Monumenti")
        descr_it = descrizioneBot("Monumenti")
        context.bot.send_message(chat_id=update.effective_chat.id, text = descr_it[1])
        context.bot.send_message(chat_id=update.effective_chat.id, text = list[1])
        
    if "graf_Museum3" in query:
        list = posizioneBot("Monumenti")
        descr_it = descrizioneBot("Monumenti")
        context.bot.send_message(chat_id=update.effective_chat.id, text = descr_it[2])
        context.bot.send_message(chat_id=update.effective_chat.id, text = list[2])
        
    if "graf_Museum4" in query:
        list = posizioneBot("Monumenti")
        descr_it = descrizioneBot("Monumenti")
        context.bot.send_message(chat_id=update.effective_chat.id, text = descr_it[3])
        context.bot.send_message(chat_id=update.effective_chat.id, text = list[3])
        
    if "graf_Museum5" in query:
        list = posizioneBot("Monumenti")
        descr_it = descrizioneBot("Monumenti")
        context.bot.send_message(chat_id=update.effective_chat.id, text = descr_it[4])
        context.bot.send_message(chat_id=update.effective_chat.id, text = list[4])
        
    if "graf_Museum6" in query:
        list = posizioneBot("Monumenti")
        descr_it = descrizioneBot("Monumenti")
        context.bot.send_message(chat_id=update.effective_chat.id, text = descr_it[5])
        context.bot.send_message(chat_id=update.effective_chat.id, text = list[5])
        
    if "graf_Museum7" in query:
        list = posizioneBot("Monumenti")
        descr_it = descrizioneBot("Monumenti")
        context.bot.send_message(chat_id=update.effective_chat.id, text = descr_it[6])
        context.bot.send_message(chat_id=update.effective_chat.id, text = list[6])
        
    if "graf_Museum8" in query:
        list = posizioneBot("Monumenti")
        descr_it = descrizioneBot("Monumenti")
        context.bot.send_message(chat_id=update.effective_chat.id, text = descr_it[7])
        context.bot.send_message(chat_id=update.effective_chat.id, text = list[7])
    
    if "graf_Museum9" in query:
        list = posizioneBot("Monumenti")
        descr_it = descrizioneBot("Monumenti")
        context.bot.send_message(chat_id=update.effective_chat.id, text = descr_it[8])
        context.bot.send_message(chat_id=update.effective_chat.id, text = list[8])
        
    if "graf_Museum10" in query:
        list = posizioneBot("Monumenti")
        descr_it = descrizioneBot("Monumenti")
        context.bot.send_message(chat_id=update.effective_chat.id, text = descr_it[9])
        context.bot.send_message(chat_id=update.effective_chat.id, text = list[9])
        
    if "graf_Museum11" in query:
        list = posizioneBot("Monumenti")
        descr_it = descrizioneBot("Monumenti")
        context.bot.send_message(chat_id=update.effective_chat.id, text = descr_it[10])
        context.bot.send_message(chat_id=update.effective_chat.id, text = list[10])
        
    if "graf_Museum12" in query:
        list = posizioneBot("Monumenti")
        descr_it = descrizioneBot("Monumenti")
        context.bot.send_message(chat_id=update.effective_chat.id, text = descr_it[11])
        context.bot.send_message(chat_id=update.effective_chat.id, text = list[11])
        
    if "graf_Museum13" in query:
        list = posizioneBot("Monumenti")
        descr_it = descrizioneBot("Monumenti")
        context.bot.send_message(chat_id=update.effective_chat.id, text = descr_it[12])
        context.bot.send_message(chat_id=update.effective_chat.id, text = list[12])
        
    if "graf_Museum14" in query:
        list = posizioneBot("Monumenti")
        descr_it = descrizioneBot("Monumenti")
        context.bot.send_message(chat_id=update.effective_chat.id, text = descr_it[13])
        context.bot.send_message(chat_id=update.effective_chat.id, text = list[13])
    
    if "graf_Chiese1" in query:
        descr_it = descrizioneBot("Chiese")
        list = posizioneBot("Chiese")
        context.bot.send_message(chat_id=update.effective_chat.id, text = descr_it[0])
        context.bot.send_message(chat_id=update.effective_chat.id, text = list[0])
        
    if "graf_Chiese2" in query:
        descr_it = descrizioneBot("Chiese")
        list = posizioneBot("Chiese")
        context.bot.send_message(chat_id=update.effective_chat.id, text = descr_it[1])
        context.bot.send_message(chat_id=update.effective_chat.id, text = list[1])
        
    if "graf_Chiese3" in query:
        descr_it = descrizioneBot("Chiese")
        list = posizioneBot("Chiese")
        context.bot.send_message(chat_id=update.effective_chat.id, text = descr_it[2])
        context.bot.send_message(chat_id=update.effective_chat.id, text = list[2])
        
    if "graf_Chiese4" in query:
        descr_it = descrizioneBot("Chiese")
        list = posizioneBot("Chiese")
        context.bot.send_message(chat_id=update.effective_chat.id, text = descr_it[3])
        context.bot.send_message(chat_id=update.effective_chat.id, text = list[3])
    
    if "graf_Monumento1" in query:
        list = posizioneBot("Monumenti")
        descr_it = descrizioneBot("Monumenti")
        context.bot.send_message(chat_id=update.effective_chat.id, text = descr_it[0])
        context.bot.send_message(chat_id=update.effective_chat.id, text = list[0])
    
    if "graf_Monumento2" in query:
        list = posizioneBot("Monumenti")
        descr_it = descrizioneBot("Monumenti")
        context.bot.send_message(chat_id=update.effective_chat.id, text = descr_it[1])
        context.bot.send_message(chat_id=update.effective_chat.id, text = list[1])
        
    if "graf_Monumento3" in query:
        list = posizioneBot("Monumenti")
        descr_it = descrizioneBot("Monumenti")
        context.bot.send_message(chat_id=update.effective_chat.id, text = descr_it[2])
        context.bot.send_message(chat_id=update.effective_chat.id, text = list[2])
        
    if "graf_Monumento4" in query:
        list = posizioneBot("Monumenti")
        descr_it = descrizioneBot("Monumenti")
        context.bot.send_message(chat_id=update.effective_chat.id, text = descr_it[3])
        context.bot.send_message(chat_id=update.effective_chat.id, text = list[3])
        
    if "graf_Monumento5" in query:
        list = posizioneBot("Monumenti")
        descr_it = descrizioneBot("Monumenti")
        context.bot.send_message(chat_id=update.effective_chat.id, text = descr_it[4])
        context.bot.send_message(chat_id=update.effective_chat.id, text = list[4])
        
    if "graf_Monumento6" in query:
        list = posizioneBot("Monumenti")
        descr_it = descrizioneBot("Monumenti")
        context.bot.send_message(chat_id=update.effective_chat.id, text = descr_it[5])
        context.bot.send_message(chat_id=update.effective_chat.id, text = list[5])
        
    if "graf_Monumento7" in query:
        list = posizioneBot("Monumenti")
        descr_it = descrizioneBot("Monumenti")
        context.bot.send_message(chat_id=update.effective_chat.id, text = descr_it[6])
        context.bot.send_message(chat_id=update.effective_chat.id, text = list[6])
        
    if "graf_Museo1" in query:
        list = posizioneBot("Monumenti")
        descr_it = descrizioneBot("Monumenti")
        context.bot.send_message(chat_id=update.effective_chat.id, text = descr_it[0])
        context.bot.send_message(chat_id=update.effective_chat.id, text = list[0])
    
    if "graf_Museo2" in query:
        list = posizioneBot("Monumenti")
        descr_it = descrizioneBot("Monumenti")
        context.bot.send_message(chat_id=update.effective_chat.id, text = descr_it[1])
        context.bot.send_message(chat_id=update.effective_chat.id, text = list[1])
        
    if "graf_Museo3" in query:
        list = posizioneBot("Monumenti")
        descr_it = descrizioneBot("Monumenti")
        context.bot.send_message(chat_id=update.effective_chat.id, text = descr_it[2])
        context.bot.send_message(chat_id=update.effective_chat.id, text = list[2])
        
    if "graf_Museo4" in query:
        list = posizioneBot("Monumenti")
        descr_it = descrizioneBot("Monumenti")
        context.bot.send_message(chat_id=update.effective_chat.id, text = descr_it[3])
        context.bot.send_message(chat_id=update.effective_chat.id, text = list[3])
        
    if "graf_Museo5" in query:
        list = posizioneBot("Monumenti")
        descr_it = descrizioneBot("Monumenti")
        context.bot.send_message(chat_id=update.effective_chat.id, text = descr_it[4])
        context.bot.send_message(chat_id=update.effective_chat.id, text = list[4])
        
    if "graf_Museo6" in query:
        list = posizioneBot("Monumenti")
        descr_it = descrizioneBot("Monumenti")
        context.bot.send_message(chat_id=update.effective_chat.id, text = descr_it[5])
        context.bot.send_message(chat_id=update.effective_chat.id, text = list[5])
        
    if "graf_Museo7" in query:
        list = posizioneBot("Monumenti")
        descr_it = descrizioneBot("Monumenti")
        context.bot.send_message(chat_id=update.effective_chat.id, text = descr_it[6])
        context.bot.send_message(chat_id=update.effective_chat.id, text = list[6])
        
    if "graf_Museo8" in query:
        list = posizioneBot("Monumenti")
        descr_it = descrizioneBot("Monumenti")
        context.bot.send_message(chat_id=update.effective_chat.id, text = descr_it[7])
        context.bot.send_message(chat_id=update.effective_chat.id, text = list[7])
    
    if "graf_Museo9" in query:
        list = posizioneBot("Monumenti")
        descr_it = descrizioneBot("Monumenti")
        context.bot.send_message(chat_id=update.effective_chat.id, text = descr_it[8])
        context.bot.send_message(chat_id=update.effective_chat.id, text = list[8])
        
    if "graf_Museo10" in query:
        list = posizioneBot("Monumenti")
        descr_it = descrizioneBot("Monumenti")
        context.bot.send_message(chat_id=update.effective_chat.id, text = descr_it[9])
        context.bot.send_message(chat_id=update.effective_chat.id, text = list[9])
        
    if "graf_Museo11" in query:
        list = posizioneBot("Monumenti")
        descr_it = descrizioneBot("Monumenti")
        context.bot.send_message(chat_id=update.effective_chat.id, text = descr_it[10])
        context.bot.send_message(chat_id=update.effective_chat.id, text = list[10])
        
    if "graf_Museo12" in query:
        list = posizioneBot("Monumenti")
        descr_it = descrizioneBot("Monumenti")
        context.bot.send_message(chat_id=update.effective_chat.id, text = descr_it[11])
        context.bot.send_message(chat_id=update.effective_chat.id, text = list[11])
        
    if "graf_Museo13" in query:
        list = posizioneBot("Monumenti")
        descr_it = descrizioneBot("Monumenti")
        context.bot.send_message(chat_id=update.effective_chat.id, text = descr_it[12])
        context.bot.send_message(chat_id=update.effective_chat.id, text = list[12])
        
    if "graf_Museo14" in query:
        list = posizioneBot("Monumenti")
        descr_it = descrizioneBot("Monumenti")
        context.bot.send_message(chat_id=update.effective_chat.id, text = descr_it[13])
        context.bot.send_message(chat_id=update.effective_chat.id, text = list[13])
=======
    if "church" in query:
        context.bot.send_message(chat_id=update.effective_chat.id, text="church")

    if "monuments" in query:
        context.bot.send_message(chat_id=update.effective_chat.id, text="monuments")
>>>>>>> 3ebc1069e8e09088d70132664bf535f7c6a58c15

    
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
