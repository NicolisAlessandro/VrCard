from flash import request
from flash import Response
import telegram.ext
#import pandas_datareader as web

#with open("token.txt", "r") as f:
 #   TOKEN = f.read()
  #  print("il tuo token è ", TOKEN)

#TOKEN = open(r"C:\Users\311 Verona\Documents\GitHub\Ptco\esPython\telegram-bot\\token.txt", "r")
#print("il tuo token è ", TOKEN)

TOKEN = "5592675935:AAFXOB1e14hOIb2iiRdiL_KO0CaIZA0DBE4"

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
 
def tel_send_message(chat_id, text):
    url = f'https://api.telegram.org/bot{TOKEN}/sendMessage'
    payload = {
                'chat_id': chat_id,
                'text': text
                }
   
    r = request.post(url,json=payload)
    return r

def handle_message(update, context):
    update.message.reply_text(f"hai detto {update.message.text}")
    
def index():
    if request.method == 'POST':
        msg = request.get_json()
        try:
            chat_id, txt = tel_parse_message(msg)
            if txt == "inline":
               tel_send_inlinebutton(chat_id)
        except:
            print("from index-->")
 
        return Response('ok', status=200)
    else:
        return "<h1>Welcome!</h1>"
 

def tel_send_inlinebutton(chat_id):
    url = f'https://api.telegram.org/bot{TOKEN}/sendMessage'
 
    payload = {
        'chat_id': chat_id,
        'text': "What is this?",
        'reply_markup': {
            "inline_keyboard": [[
                {
                    "text": "A",
                    "callback_data": "ic_A"
                },
                {
                    "text": "B",
                    "callback_data": "ic_B"
                }]
            ]
        }
    }
    r = request.post(url, json=payload)
    return r
    
updater = telegram.ext.Updater(TOKEN, use_context=True)
disp = updater.dispatcher

disp.add_handler(telegram.ext.CommandHandler("start", start))
disp.add_handler(telegram.ext.CommandHandler("help", help))
disp.add_handler(telegram.ext.CommandHandler("context", context))
disp.add_handler(telegram.ext.CommandHandler("contact", contact))
disp.add_handler(telegram.ext.MessageHandler(telegram.ext.Filters.text , handle_message))
disp.add_handler(telegram.ext.CommandHandler("requests", tel_send_inlinebutton ))


updater.start_polling()
updater.idle()