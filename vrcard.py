from aiogram import Bot, Dispatcher, executor,types
from aiogram.types import ReplyKeyboardMarkup, ReplyKeyboardRemove, KeyboardButton

bot = Bot(token='5321198677:AAEP8mtEovJootwYR9Q4ERaBbrBeaxekGGw')

dp=Dispatcher(bot)
button1=KeyboardButton('Hello!')
button2=KeyboardButton('Youtube')
keyboard1=ReplyKeyboardMarkup(resize_keyboard=True,one_time_keyboard=True).add(button1).add(button2)


@dp.message_handler(commands=['start','help'])
async def welcome(message: types.Message):
    await message.reply("Hello!Im Gunther Bot,Please follow my YT channel", reply_markup=keyboard1)


@dp.message_handler()
async def kb_answer(message: types.Message):
    if message.text =='Hello!':
        await message.answer('Hi!How are you?')
    elif message.text =='Youtube':
        await message.answer('https://youtube.com/gunthersuper')
    else:
        await message.answer(f'Your message is:{message.text}')