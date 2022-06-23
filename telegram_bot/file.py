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

        buttons=[[InlineKeyboardButton("Monument",callback_data="map_monument1")], [InlineKeyboardButton("Monument",callback_data="map_monument2")],
        [InlineKeyboardButton("Monument",callback_data="map_monument3")],[InlineKeyboardButton("Monument",callback_data="map_monument4")],
        [InlineKeyboardButton("Monument",callback_data="map_monument5")],[InlineKeyboardButton("Monument",callback_data="map_monument6")],
        [InlineKeyboardButton("Monument",callback_data="map_monument7")],[InlineKeyboardButton("Back",callback_data="eng_map")]]
        context.bot.send_message(chat_id=update.effective_chat.id,reply_markup=InlineKeyboardMarkup(buttons), text="which monument?")

    if "map_Museum" in query:

        buttons=[[InlineKeyboardButton("Mus1",callback_data="map_Mus1")],[InlineKeyboardButton("Back",callback_data="eng_map")]]
        context.bot.send_message(chat_id=update.effective_chat.id,reply_markup=InlineKeyboardMarkup(buttons), text="which museum?")
    
    if "map_Church" in query:

        buttons=[[InlineKeyboardButton("Chu1",callback_data="map_Chu1")], [InlineKeyboardButton("Chu1",callback_data="map_Chu2")], 
        [InlineKeyboardButton("Chu1",callback_data="map_Chu3")], [InlineKeyboardButton("Chu1",callback_data="map_Chu4")],
        [InlineKeyboardButton("Back",callback_data="eng_map")]]
        context.bot.send_message(chat_id=update.effective_chat.id,reply_markup=InlineKeyboardMarkup(buttons), text="which Church?")

    if "graf_Monuments" in query:

        buttons=[[InlineKeyboardButton("Monument",callback_data="graf_monument1")], [InlineKeyboardButton("Monument",callback_data="graf_monument2")],
        [InlineKeyboardButton("Monument",callback_data="graf_monument3")],[InlineKeyboardButton("Monument",callback_data="graf_monument4")],
        [InlineKeyboardButton("Monument",callback_data="graf_monument5")],[InlineKeyboardButton("Monument",callback_data="graf_monument6")],
        [InlineKeyboardButton("Monument",callback_data="graf_monument7")],[InlineKeyboardButton("Back",callback_data="eng_map")]]
        context.bot.send_message(chat_id=update.effective_chat.id,reply_markup=InlineKeyboardMarkup(buttons), text="which monument?")

    if "graf_Museum" in query:

        buttons=[[InlineKeyboardButton("Mus1",callback_data="graf_Mus1")],[InlineKeyboardButton("Back",callback_data="eng_map")]]
        context.bot.send_message(chat_id=update.effective_chat.id,reply_markup=InlineKeyboardMarkup(buttons), text="which museum?")
    
    if "graf_Church" in query:

        buttons=[[InlineKeyboardButton("Chu1",callback_data="graf_Chu1")],[InlineKeyboardButton("Chu1",callback_data="graf_Chu2")],[InlineKeyboardButton("Chu1",callback_data="graf_Chu3")],
        [InlineKeyboardButton("Chu1",callback_data="graf_Chu4")],[InlineKeyboardButton("Back",callback_data="eng_map")]]
        context.bot.send_message(chat_id=update.effective_chat.id,reply_markup=InlineKeyboardMarkup(buttons), text="which Church?")
    
    if "Jur_Monuments" in query:

        buttons=[[InlineKeyboardButton("Monument",callback_data="Jur_monument1")], [InlineKeyboardButton("Monument",callback_data="Jur_monument2")],
        [InlineKeyboardButton("Monument",callback_data="Jur_monument3")],[InlineKeyboardButton("Monument",callback_data="Jur_monument4")],
        [InlineKeyboardButton("Monument",callback_data="Jur_monument5")],[InlineKeyboardButton("Monument",callback_data="Jur_monument6")],
        [InlineKeyboardButton("Monument",callback_data="Jur_monument7")],[InlineKeyboardButton("Back",callback_data="eng_map")]]
        context.bot.send_message(chat_id=update.effective_chat.id,reply_markup=InlineKeyboardMarkup(buttons), text="which monument?")

    if "Jur_Museum" in query:

        buttons=[[InlineKeyboardButton("Mus1",callback_data="Jur_Mus1")],[InlineKeyboardButton("Back",callback_data="eng_map")]]
        context.bot.send_message(chat_id=update.effective_chat.id,reply_markup=InlineKeyboardMarkup(buttons), text="which museum?")
    
    if "Jur_Church" in query:

        buttons=[[InlineKeyboardButton("Chu1",callback_data="Jur_Chu1")],[InlineKeyboardButton("Chu1",callback_data="Jur_Chu2")],[InlineKeyboardButton("Chu1",callback_data="Jur_Chu3")],
        [InlineKeyboardButton("Chu1",callback_data="Jur_Chu4")],[InlineKeyboardButton("Back",callback_data="eng_map")]]
        context.bot.send_message(chat_id=update.effective_chat.id,reply_markup=InlineKeyboardMarkup(buttons), text="which Church?")

    if "map_Monumenti" in query:

        buttons=[[InlineKeyboardButton("Monument",callback_data="map_monumento1")], [InlineKeyboardButton("Monument",callback_data="map_monumento2")],
        [InlineKeyboardButton("Monument",callback_data="map_monumento3")],[InlineKeyboardButton("Monument",callback_data="map_monumento4")],
        [InlineKeyboardButton("Monument",callback_data="map_monumento5")],[InlineKeyboardButton("Monument",callback_data="map_monumento6")],
        [InlineKeyboardButton("Monument",callback_data="map_monumento7")],[InlineKeyboardButton("Back",callback_data="🇮🇹 Italiano")]]
        context.bot.send_message(chat_id=update.effective_chat.id,reply_markup=InlineKeyboardMarkup(buttons), text="quale monumento??")

    if "map_Musei" in query:

        buttons=[[InlineKeyboardButton("Mus1",callback_data="map_Museo1")],[InlineKeyboardButton("Indietro",callback_data="🇮🇹 Italiano")]]
        context.bot.send_message(chat_id=update.effective_chat.id,reply_markup=InlineKeyboardMarkup(buttons), text="quali musei?")
    
    if "map_Chiese" in query:

        buttons=[[InlineKeyboardButton("Chiesa1",callback_data="map_Chi1")],[InlineKeyboardButton("Chiesa1",callback_data="map_Chi2")],[InlineKeyboardButton("Chiesa1",callback_data="map_Chi3")],
        [InlineKeyboardButton("Chiesa1",callback_data="map_Chi4")],[InlineKeyboardButton("Indietro",callback_data="🇮🇹 Italiano")]]
        context.bot.send_message(chat_id=update.effective_chat.id,reply_markup=InlineKeyboardMarkup(buttons), text="quali chiesa?")
    
    if "graf_Monumenti" in query:

        buttons=[[InlineKeyboardButton("Monument",callback_data="graf_monumento1")], [InlineKeyboardButton("Monument",callback_data="graf_monumento2")],
        [InlineKeyboardButton("Monument",callback_data="graf_monumento3")],[InlineKeyboardButton("Monument",callback_data="graf_monumento4")],
        [InlineKeyboardButton("Monument",callback_data="graf_monumento5")],[InlineKeyboardButton("Monument",callback_data="graf_monumento6")],
        [InlineKeyboardButton("Monument",callback_data="graf_monumento7")],[InlineKeyboardButton("Back",callback_data="🇮🇹 Italiano")]]
        context.bot.send_message(chat_id=update.effective_chat.id,reply_markup=InlineKeyboardMarkup(buttons), text="quale monumento??")

    if "graf_Musei" in query:

        buttons=[[InlineKeyboardButton("Mus1",callback_data="graf_Museo1")],[InlineKeyboardButton("Indietro",callback_data="🇮🇹 Italiano")]]
        context.bot.send_message(chat_id=update.effective_chat.id,reply_markup=InlineKeyboardMarkup(buttons), text="quali musei?")
    
    if "graf_Chiese" in query:

        buttons=[[InlineKeyboardButton("Chiesa1",callback_data="graf_Chi1")],[InlineKeyboardButton("Chiesa1",callback_data="graf_Chi2")],[InlineKeyboardButton("Chiesa1",callback_data="graf_Chi3")],
        [InlineKeyboardButton("Chiesa1",callback_data="graf_Chi4")],[InlineKeyboardButton("Indietro",callback_data="🇮🇹 Italiano")]]
        context.bot.send_message(chat_id=update.effective_chat.id,reply_markup=InlineKeyboardMarkup(buttons), text="quale chiesa?")

    if "Via_Monumenti" in query:

        buttons=[[InlineKeyboardButton("Monument",callback_data="Via_monumento1")], [InlineKeyboardButton("Monument",callback_data="Via_monumento2")],
        [InlineKeyboardButton("Monument",callback_data="Via_monumento3")],[InlineKeyboardButton("Monument",callback_data="Via_monumento4")],
        [InlineKeyboardButton("Monument",callback_data="Via_monumento5")],[InlineKeyboardButton("Monument",callback_data="Via_monumento6")],
        [InlineKeyboardButton("Monument",callback_data="Via_monumento7")],[InlineKeyboardButton("Back",callback_data="🇮🇹 Italiano")]]
        context.bot.send_message(chat_id=update.effective_chat.id,reply_markup=InlineKeyboardMarkup(buttons), text="quale monumento??")

    if "Via_Musei" in query:

        buttons=[[InlineKeyboardButton("Mus1",callback_data="Via_Museo1")],[InlineKeyboardButton("Indietro",callback_data="🇮🇹 Italiano")]]
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
        context.bot.send_message(chat_id=update.effective_chat.id,reply_markup=InlineKeyboardMarkup(buttons), text="🇮🇹 Benvenuto nel nostro canale Telegram, che tipo di monumento ti piacerebbe visitare?")

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
disp.add_handler(telegram.ext.CommandHandler("content", content))
disp.add_handler(telegram.ext.CommandHandler("contact", contact))
disp.add_handler(CallbackQueryHandler(queryHandler))


updater.start_polling()
updater.idle()
