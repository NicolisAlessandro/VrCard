#
# file: main 
#  authors: Alessandro, Simone , Michela
#  date: 27/06/2022
#  description: Main file of the project, bot implementation 
#

from email import message
from numpy import append
from telegram import bot_api_version
import telegram.ext
from telegram import *
from requests import *
from telegram.ext import *
from letturaDb import  descrizioneBot, descrizioneEngBot, posizioneBotx, posizioneBoty, restituisciOra 

nscelta= 0
frase = ""
i=0
nposti = 0
index_monument=""
nomposti = []
categ=""
categen =""
torna_alle=""
stamp_to_screen_monument=""
dizionario= {}
lista= []

luogo1 = ['NULL','NULL','NULL']
luogo2 = ['NULL','NULL','NULL']
luogo3 = ['NULL','NULL','NULL']
nvolte=0
with open("TOKEN.txt", "r") as f:
    TOKEN = f.read()
    print("Your token is: ", TOKEN)
    
TOKEN = "5592675935:AAFXOB1e14hOIb2iiRdiL_KO0CaIZA0DBE4"

def start(update, context):
    
    buttons=[
        [InlineKeyboardButton(
            "🇮🇹 Italiano",
            callback_data="🇮🇹 Italiano")
        ],
        [InlineKeyboardButton(
            "🇬🇧 / 🇺🇸 English",
            callback_data="🇬🇧 / 🇺🇸 English")
        ]
    ]
    context.bot.send_message(
        chat_id=update.effective_chat.id,
        reply_markup=InlineKeyboardMarkup(buttons),
        text="lingua:\n🇮🇹 Italiano\n🇬🇧 / 🇺🇸 English ")
    
def queryHandler(update, context):
    global luogo1, luogo2, luogo3, nvolte
    global stamp_to_screen_monument
    global torna_alle
    global categ
    global nscelta
    global index_monument
    global frase
    global nposti
    global categen
    global dizionario
    global lista
    
    query = update.callback_query.data
    update.callback_query.answer()
        
    if "🇮🇹 Italiano" in query:

        nvolte=0
        buttons=[
            [InlineKeyboardButton(
                "Quiz", 
                url="https://take.panquiz.com/0558-1914-4625")
            ],
            [InlineKeyboardButton(
                "MAPPA : Posizione della struttura selezionata",
                callback_data="Mappa")
            ],
            [InlineKeyboardButton(
                "ITINERARIO PERSONALIZZATO : Scegli tre strutture per creare un percorso",
                callback_data="Viaggio")
            ],
            [InlineKeyboardButton(
                "AFFLUENZA : Grafici di affluenza nei rispettivi anni",
                callback_data="Grafici")
            ],
            [InlineKeyboardButton(
                "Indietro",
                callback_data="Back/Indietro")
             ]
        ]
        update.callback_query.edit_message_text(
            reply_markup=InlineKeyboardMarkup(buttons),  
            text="🇮🇹 Benvenuto nel canale telegram ufficiale della VeronaCard! Che funzionalità desideri usare?"
            )

    if "🇬🇧 / 🇺🇸 English" in query:
            
        nvolte=0
        buttons=[
            [InlineKeyboardButton(
                    "Quiz",
                    url="https://take.panquiz.com/7756-4532-2726")
                 ],
                [InlineKeyboardButton(
                    "MAP : Position of the selected place",
                    callback_data="emap_")
                 ],
                [InlineKeyboardButton(
                    "PERSONALIZED PATH. Select three places to create a path",
                    callback_data="Jurney")
                 ], 
                [InlineKeyboardButton(
                    "AFFLUENCE : Affluence of people in each year for every place",
                    callback_data="Graphs")
                 ],
                [InlineKeyboardButton(
                    "Back",
                    callback_data="Back/Indietro")
                 ]
            ]
        update.callback_query.edit_message_text(
            reply_markup=InlineKeyboardMarkup(buttons),  
            text="🇬🇧 / 🇺🇸 Welcome to the official telegram bot of the Verona Card! Which feature would you like to use?"
        )
   
    if "Viaggio" in query:
        
        nscelta=2
        frase="Via_"
        buttons=[
            [InlineKeyboardButton(
                "Monumenti: quali monumenti vuoi visitare?",
                callback_data="Via__Monumenti")
             ],
            [InlineKeyboardButton(
                "Musei: Quali musei vuoi visitare? ",
                callback_data="Via__Musei ")
             ],
            [InlineKeyboardButton(
                "Chiese: Quali chiese vuoi visitare?",
                callback_data="Via__Chiese")
             ],
            [InlineKeyboardButton(
                "Back/Indietro",
                callback_data="🇮🇹 Italiano")
             ]
            ]
        update.callback_query.edit_message_text(
            reply_markup=InlineKeyboardMarkup(buttons),  
            text="Scegli tre strutture per creare un percorso")

    if "Mappa" in query:
        
        nscelta = 1
        frase = "map_"
        buttons=[
            [InlineKeyboardButton(
                "Mappa completa",
                url="http://umap.openstreetmap.fr/it/map/map_vrcard_780732")
             ],
            [InlineKeyboardButton(
                "Monumenti",
                callback_data="map__Monumenti")
             ],
            [InlineKeyboardButton(
                "Musei ",
                callback_data="map__Musei ")
             ],
            [InlineKeyboardButton(
                "Chiese",
                callback_data="map__Chiese")
             ],
            [InlineKeyboardButton(
                "Back/Indietro",
                callback_data="🇮🇹 Italiano")
             ]
            ]
        update.callback_query.edit_message_text(
            reply_markup=InlineKeyboardMarkup(buttons),  
            text="Posizione della struttura selezionata")
    
    if "Grafici" in query:
    
        nscelta = 3
        frase = "graf_"
        buttons = []
        for i in range (14,21):
            buttons.append(
                [InlineKeyboardButton(
                    "20" + str(i),
                    callback_data="graf_20" + str (i))
                ]
            )
            
        buttons.append(
            [InlineKeyboardButton(
                "Indietro",
                callback_data="scegli")
            ]
        )
        
        update.callback_query.edit_message_text(
            reply_markup=InlineKeyboardMarkup(buttons),
            text="Grafici di affluenza nei rispettivi anni")


    if "emap_" in query:

        frase="engmap_"
        nscelta = 1
        buttons=[
            [InlineKeyboardButton(
                "Complete map",
                url="http://umap.openstreetmap.fr/it/map/map_vrcard_780732")
             ],
            [InlineKeyboardButton(
                "Monuments",
                callback_data="engmap_Monuments")
             ],
            [InlineKeyboardButton(
                "Museum ",
                callback_data="engmap_Museum ")
             ],
            [InlineKeyboardButton(
                "Church",
                callback_data="engmap_Church")
             ],
            [InlineKeyboardButton(
                "Back",
                callback_data="🇬🇧 / 🇺🇸 English")
             ]
            ]
        update.callback_query.edit_message_text(
            reply_markup=InlineKeyboardMarkup(buttons),
            text="Position of the selected place.")
    
    if "Jurney" in query:

        nscelta=2
        frase="Jur_"
        buttons=[
            [InlineKeyboardButton(
                "Monuments",
                callback_data="Jur_Monuments")
             ],
            [InlineKeyboardButton(
                "Museums ",
                callback_data="Jur_Museum ")
             ],
            [InlineKeyboardButton(
                "Churchs",
                callback_data="Jur_Church")
             ],
            [InlineKeyboardButton(
                "Back",
                callback_data="🇬🇧 / 🇺🇸 English")
             ]
            ]
        update.callback_query.edit_message_text(
            reply_markup=InlineKeyboardMarkup(buttons),  
            text=" Select three places to create a path")
    
    if "Graphs" in query:

        nscelta = 3
        frase = "graph_"
        buttons = []
        for i in range (14,21):
            buttons.append(
                [InlineKeyboardButton(
                    "20" + str(i),
                    callback_data="graph_eng20" + str (i))
                ]
            )
            
        buttons.append(
            [InlineKeyboardButton(
                "back",
                callback_data="123Back")
            ]
        )
        
        update.callback_query.edit_message_text(
            reply_markup=InlineKeyboardMarkup(buttons),
            text=" Affluence of people in each year for every place.")

    if "Back/Indietro" in query:

        buttons=[
            [InlineKeyboardButton(
                "🇮🇹 Italiano",
                callback_data="🇮🇹 Italiano")
             ],
            [InlineKeyboardButton(
                "🇬🇧 / 🇺🇸 English",
                callback_data="🇬🇧 / 🇺🇸 English")
             ]
            ]
        update.callback_query.edit_message_text(
            reply_markup=InlineKeyboardMarkup(buttons),
            text="lingua:\n🇮🇹 Italiano\n🇬🇧 / 🇺🇸 English")
    
    for i in range(0,30):
        if str( "map_" + categ + str(i)) == query:
            coordX = posizioneBotx(categ)
            coordY = posizioneBoty(categ)
            context.bot.sendLocation(
                chat_id=update.effective_chat.id,
                latitude=coordX[i][0], 
                longitude=coordY[i][0]
                )
            buttons=[
                [InlineKeyboardButton(
                    "indietro",
                    callback_data="scegli")]]
            update.callback_query.edit_message_text(
                reply_markup=InlineKeyboardMarkup(buttons),
                text="clicca il pulsante per tornare indietro")
            
    for i in range(0,nposti):
        if str( "engmap_" + categen + str(i)) == query:
            coordX = posizioneBotx(categ)
            coordY = posizioneBoty(categ)
            context.bot.sendLocation(
                chat_id=update.effective_chat.id,
                latitude=coordX[i][0], 
                longitude=coordY[i][0]
                )
            buttons=[
                [InlineKeyboardButton(
                    "back",
                    callback_data="123Back")]]
            update.callback_query.edit_message_text(
                reply_markup=InlineKeyboardMarkup(buttons),
                text="click the button to go back")
   


    for i in range(0,30):
        if str( "Jur_" + categen + str(i)) == query:
            coordX = posizioneBotx(categ)
            coordY = posizioneBoty(categ)
            ora_visita = restituisciOra(categ)
            if nvolte == 0:
                luogo1[0] = coordX[i][0]
                luogo1[1] = coordY[i][0]
                luogo1[2] = ora_visita[i][0]
                nvolte+=1
            elif nvolte == 1:
                luogo2[0] = coordX[i][0]
                luogo2[1] = coordY[i][0]
                luogo2[2] = ora_visita[i][0]
                nvolte+=1
            elif nvolte == 2:
                luogo3[0] = coordX[i][0]
                luogo3[1] = coordY[i][0]
                luogo3[2] = ora_visita[i][0]
                nvolte+=1
                
                context.bot.sendLocation(
                    chat_id=update.effective_chat.id,
                    latitude=luogo1[0], 
                    longitude=luogo1[1]
                    )
                
                context.bot.send_message(
                    chat_id=update.effective_chat.id,
                    text="the times to visit is" + str(luogo1[2])
                )
                
                context.bot.sendLocation(
                    chat_id=update.effective_chat.id,
                    latitude=luogo2[0], 
                    longitude=luogo2[1]
                    )
                
                context.bot.send_message(
                    chat_id=update.effective_chat.id,
                    text="the times to visit is " + str(luogo2[2])
                )

                context.bot.sendLocation(
                    chat_id=update.effective_chat.id,
                    latitude=luogo3[0], 
                    longitude=luogo3[1]
                    )
                
                context.bot.send_message(
                    chat_id=update.effective_chat.id,
                    text="the times to visit is" + str(luogo3[2])
                )
                
                buttons=[
                [InlineKeyboardButton(
                    "Back",
                    callback_data="123Back")
                 ]
                ]
                update.callback_query.edit_message_text(
                reply_markup=InlineKeyboardMarkup(buttons),
                text="click the button to go back")
  
    for i in range(0,30):
        if str( "Via_" + categ + str(i)) in query:
            coordX = posizioneBotx(categ)
            coordY = posizioneBoty(categ)
            ora_visita = restituisciOra(categ)
            if nvolte == 0:
                luogo1[0] = coordX[i][0]
                luogo1[1] = coordY[i][0]
                luogo1[2] = ora_visita[i][0]
                nvolte+=1
            elif nvolte == 1:
                luogo2[0] = coordX[i][0]
                luogo2[1] = coordY[i][0]
                luogo2[2] = ora_visita[i][0]
                nvolte+=1
            elif nvolte == 2:
                luogo3[0] = coordX[i][0]
                luogo3[1] = coordY[i][0]
                luogo3[2] = ora_visita[i][0]
                nvolte+=1
                
                context.bot.sendLocation(
                    chat_id=update.effective_chat.id,
                    latitude=luogo1[0], 
                    longitude=luogo1[1]
                    )
                
                context.bot.send_message(
                    chat_id=update.effective_chat.id,
                    text="il tempo per visitare è " + str(luogo1[2])
                )
                
                context.bot.sendLocation(
                    chat_id=update.effective_chat.id,
                    latitude=luogo2[0], 
                    longitude=luogo2[1]
                    )
                
                context.bot.send_message(
                    chat_id=update.effective_chat.id,
                    text="il tempo per visitare è " + str(luogo2[2])
                )

                context.bot.sendLocation(
                    chat_id=update.effective_chat.id,
                    latitude=luogo3[0], 
                    longitude=luogo3[1]
                    )
                
                context.bot.send_message(
                    chat_id=update.effective_chat.id,
                    text="il tempo per visitare è " + str(luogo3[2])
                )
                
                buttons=[
                [InlineKeyboardButton(
                    "indietro",
                    callback_data="scegli")
                 ]
                ]
                update.callback_query.edit_message_text(
                reply_markup=InlineKeyboardMarkup(buttons),
                text="clicca il pulsante per tornare indietro")

    for i in range(14,21):
        if str("graf_20"+str(i)) in query:
            PHOTO_PATH= 'immagini/20'+str(i)+'.png'
            context.bot.send_photo( 
                chat_id=update.effective_chat.id,
                photo=open(PHOTO_PATH, 'rb')
            )
            buttons=[
                [InlineKeyboardButton(
                    "indietro",
                    callback_data="scegli")
                ]
            ]
            update.callback_query.edit_message_text(
                reply_markup=InlineKeyboardMarkup(buttons),
                text="clicca il pulsante per tornare indietro")
            
    for i in range(14,21):
        if str("graph_eng20"+str(i)) == query:
            PHOTO_PATH= 'immagini/eng20'+str(i)+'.png'
            context.bot.send_photo( 
                chat_id=update.effective_chat.id,
                photo=open(PHOTO_PATH, 'rb')
            )
            buttons=[
                [InlineKeyboardButton(
                    "Back",
                    callback_data="123Back")
                ]
            ]
            update.callback_query.edit_message_text(
                reply_markup=InlineKeyboardMarkup(buttons),
                text="click the button to go back")
    
    if (str(frase)+ "_Monumenti") in query:

        categ = "Monumenti"
        name_mon = descrizioneBot("Monumenti")
        buttons=[]
        nposti = 8
        for i in range (0, len(name_mon)):
            name_monument_str = name_mon[i][0]
            index_monument = str(frase)+"Monumenti"+str(i)
            buttons.append(
                [InlineKeyboardButton(
                    name_monument_str,
                    callback_data=index_monument)
                ]) 
        buttons.append(
            [InlineKeyboardButton(
                "Indietro",
                callback_data="scegli")
            ])
        update.callback_query.edit_message_text(
            reply_markup=InlineKeyboardMarkup(buttons), 
            text="Monumenti: quali monumenti vuoi visitare?")

    if (str(frase)+ "_Chiese") in query:
        
        name_mon = descrizioneBot("Chiese")
        categ = "Chiese"
        
        nposti = 5
        buttons=[]
        for i in range (0, len(name_mon)):
            name_monument_str = name_mon[i][0]
            index_monument = str(frase)+"Chiese"+str(i)
            buttons.append(
                [InlineKeyboardButton(
                    name_monument_str,
                    callback_data=index_monument)
                ]) 
            print(name_monument_str)
        buttons.append(
            [InlineKeyboardButton(
                "Indietro",
                callback_data="scegli")
            ]) 
        update.callback_query.edit_message_text(
            reply_markup=InlineKeyboardMarkup(buttons),
            text="Chiese: Quali chiese vuoi visitare?"
            )

    if str(frase+"_Musei ") == query:
        categ = "Musei "
        nposti = 15
        name_mon = descrizioneBot("Musei ")
        buttons=[]
        for i in range (0, len(name_mon)):
            name_monument_str = name_mon[i][0]
            index_monument = str(frase)+"Musei "+str(i)
            buttons.append([InlineKeyboardButton(name_monument_str,callback_data=index_monument)]) 
            print(name_monument_str)
        buttons.append(
            [InlineKeyboardButton(
                "Indietro",
                callback_data="scegli")]) 
        update.callback_query.edit_message_text(
            reply_markup=InlineKeyboardMarkup(buttons),
            text="Musei: Quali musei vuoi visitare?")

    if (str(frase)+ "Monuments") == query:
        
        categ = "Monumenti"
        categen = "Monuments"
        name_mon = descrizioneEngBot("Monumenti")
        buttons=[]
        nposti = 8
        for i in range (0, len(name_mon)):
            name_monument_str = name_mon[i][0]
            index_monument = str(frase)+"Monuments"+str(i)
            buttons.append(
                [InlineKeyboardButton(
                    name_monument_str,
                    callback_data=index_monument)
                ]
            ) 
        buttons.append(
            [InlineKeyboardButton(
                "back",
                callback_data="123Back")
            ]
        )
        update.callback_query.edit_message_text(
            reply_markup=InlineKeyboardMarkup(buttons), 
            text="which monuments do you want to visit?"
        )

    if (str(frase)+ "Church") == query:
        
        name_mon = descrizioneEngBot("Chiese")
        categ = "Chiese"
        categen = "Church"
        nposti = 5
        buttons=[]
        for i in range (0, len(name_mon)):
            name_monument_str = name_mon[i][0]
            index_monument = str(frase)+"Church"+str(i)
            buttons.append(
                [InlineKeyboardButton(
                    name_monument_str,
                    callback_data=index_monument
                    )
                ]
            ) 
            print(name_monument_str)
        buttons.append(
            [InlineKeyboardButton(
                "back",
                callback_data="123Back")
            ]
        ) 
        update.callback_query.edit_message_text(
            reply_markup=InlineKeyboardMarkup(buttons),
            text="which churches do you want to visit?"
        )

    if str(frase+"Museum ") == query:
        categ = "Musei "
        categen = "Museum"
        nposti = 15
        name_mon = descrizioneEngBot("Musei ")
        buttons=[]
        for i in range (0, len(name_mon)):
            name_monument_str = name_mon[i][0]
            index_monument = str(frase)+"Museum"+str(i)
            buttons.append(
                [InlineKeyboardButton(
                    name_monument_str,callback_data=index_monument)
                ]
            ) 
            print(name_monument_str)
        buttons.append(
            [InlineKeyboardButton(
                "back",
                callback_data="123Back")
            ]
        ) 
        update.callback_query.edit_message_text(
            reply_markup=InlineKeyboardMarkup(buttons),
            text="which museums do you want to visit?"
        )

    if "scegli" in query:
    
        if nscelta == 1:

            nscelta = 1
            frase = "map_"
            buttons = [
                [InlineKeyboardButton(
                    "Monumenti",
                    callback_data="map__Monumenti")],
                [InlineKeyboardButton(
                    "Musei ", 
                    callback_data="map__Musei ")],
                [InlineKeyboardButton(
                    "Chiese", 
                    callback_data="map__Chiese")],
                [InlineKeyboardButton(
                    "Indietro",
                    callback_data="🇮🇹 Italiano")]
            ]
            update.callback_query.edit_message_text(
                reply_markup=InlineKeyboardMarkup(buttons),
                text="Posizione della struttura selezionata"
            )

        elif nscelta == 2:

            nscelta=2
            frase="Via_"
            buttons=[
                [InlineKeyboardButton(
                    "Monumenti",
                    callback_data="Via__Monumenti")
                 ],
                [InlineKeyboardButton(
                    "Musei ",
                    callback_data="Via__Musei ")
                 ],
                [InlineKeyboardButton(
                    "Chiese",
                    callback_data="Via__Chiese")
                 ],
                [InlineKeyboardButton(
                    "Indietro",
                    callback_data="🇮🇹 Italiano")
                 ]
                ]
            update.callback_query.edit_message_text(
                reply_markup=InlineKeyboardMarkup(buttons),  
                text="scegli 3 delle possibili strutture")

        elif nscelta == 3:
        
            nscelta = 3
            frase = "graf_"
            buttons = []
            for i in range (14,21):
                buttons.append(
                    [InlineKeyboardButton(
                        "20" + str(i),
                        callback_data="graf_20" + str (i))
                    ]
                )
            
            buttons.append(
                [InlineKeyboardButton(
                    "Indietro", 
                    callback_data="🇮🇹 Italiano"
                    )
                 ]
            )
            update.callback_query.edit_message_text(
                reply_markup=InlineKeyboardMarkup(buttons),
                text="Grafici di affluenza nei rispettivi anni"
            )
    

    if "123Back" in query:
        if nscelta == 1:

            frase = "engmap_"
            nscelta = 1
            buttons = [
                [InlineKeyboardButton(
                    "Monuments", callback_data="engmap_Monuments")],
                [InlineKeyboardButton(
                    "Museum ", callback_data="engmap_Museum ")],
                [InlineKeyboardButton(
                    "Church", callback_data="engmap_Church")],
                [InlineKeyboardButton(
                    "Back", callback_data="🇬🇧 / 🇺🇸 English")]
            ]
            update.callback_query.edit_message_text(
                reply_markup=InlineKeyboardMarkup(buttons),
                text="Position of the selected place."
            )

        elif nscelta == 2:

            nscelta = 2
            frase = "Jur_"
            buttons = [
                [InlineKeyboardButton(
                    "Monuments", callback_data="Jur_Monuments")],
                [InlineKeyboardButton(
                    "Museum", callback_data="Jur_Museum ")],
                [InlineKeyboardButton(
                    "Church", callback_data="Jur_Church")],
                [InlineKeyboardButton(
                    "Back", callback_data="🇬🇧 / 🇺🇸 English")]
            ]
            update.callback_query.edit_message_text(
                reply_markup=InlineKeyboardMarkup(buttons),
                text=" Select three places to create a path"
            )

        elif nscelta == 3:

            nscelta = 3
            frase = "graph_"
            buttons = []
            for i in range (14,21):
                buttons.append(
                    [InlineKeyboardButton(
                        "20" + str(i),
                        callback_data="graph_eng20" + str (i))
                    ]
                )
            
            buttons.append(
                [InlineKeyboardButton(
                    "Back/Indietro", 
                    callback_data="🇬🇧 / 🇺🇸 English"
                    )
                 ]
            )
            update.callback_query.edit_message_text(
                reply_markup=InlineKeyboardMarkup(buttons),
                text=" Affluence of people in each year for every place"
            )
            
def help(update, context):

    update.message.reply_text("""
    📙Available commands:
    /start -> Welcome message
    /help -> This message
    /content -> Info about the bot
    /contact -> My contacts
    """)
    

updater = telegram.ext.Updater(TOKEN, use_context = True)
disp = updater.dispatcher

disp.add_handler(telegram.ext.CommandHandler("start", start))
disp.bot_data = {"lingua" : ""}
disp.add_handler(telegram.ext.CommandHandler("help", help))
disp.add_handler(CallbackQueryHandler(queryHandler))

updater.start_polling()
updater.idle()