import random

from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from decouple import config
import logging

TOKEN = config('TOKEN')

bot = Bot(TOKEN)
dp = Dispatcher(bot=bot)

@dp.message_handler(commands=['start'])
async def start_handler(message: types.Message):
    await bot.send_message(chat_id=message.from_user.id,
                           text=f' привет епт {message.from_user.first_name}')
    await message.answer('это метод вопрос')
    await message.reply('reply method')

@dp.message_handler(commands=['quiz'])
async def quiz(message: types.Message):
    markup = InlineKeyboardMarkup()
    button_call = InlineKeyboardButton('next ', callback_data='button_call')
    markup.add(button_call)
    question = '3*3'
    answers = [
        '4',
        '3',
        '2',
        '5',
        '9',

    ]

    await bot.send_poll(
        chat_id=message.from_user.id,
        question=question,
        options=answers,
        is_anonymous=False,
        type='quiz',
        correct_option_id=4,
        explanation='ну ты ппень',
        open_period=10,
        reply_markup=markup,
    )

@dp.callback_query_handler(text='button_call')
async def quiz_1(call: types.CallbackQuery):
    question = 'мем смешон или нет '
    answers = [
        'yes',
        'no',
        'so/so',
    ]

    photo = open('media/scale_1200.webp', 'rb')
    await bot.send_photo(call.from_user.id, photo=photo)

    await bot.send_poll(
        chat_id=call.from_user.id,
        question=question,
        options=answers,
        is_anonymous=False,
        type='quiz',
        correct_option_id=1,
        explanation='ну ты ппень',
        open_period=10,
    )

@dp.message_handler(commands=['mem'])
async def mem (message: types.Message):
    photo = ['media/images.jpg',
             'media/img_20201125_173213_491_jpg'
]

    photo = open(random.choice(photo), 'rb')
    await bot.send_photo(message.chat.id, photo)



@dp.message_handler()
async def exo(message: types.Message):
    try:
        if int(message.text):
            await message.answer(int(message.text) ** 2)
    except:
        await bot.send_message(chat_id=message.from_user.id, text=message.text)


if __name__  ==  '__main__' :
    logging.basicConfig(level=logging.INFO)
    executor.start_polling(dp, skip_updates=True)

