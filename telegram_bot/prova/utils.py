from distutils.command.config import config
import os

config = {
    "API_ID" : "",
    "API_HASH" : "",
    "SESSION_NAME" : "",
    "BOT_TOKEN" : "",
    "CHAT_ID" : "",
}

os.environ.setdefault("API_ID" , config['API_ID'])
os.environ.setdefault("API_HASH" , config['API_HASH'])
os.environ.setdefault("SESSION_NAME" , config['SESSION_NAME'])
os.environ.setdefault("BOT_TOKEN" , config['BOT_TOKEN'])
os.environ.setdefault("CHAT_ID" , config['CHAT_ID'])