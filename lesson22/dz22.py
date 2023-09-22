import logging
import os
from random import choice
from aiogram import Bot, Dispatcher, types, executor

API_TOKEN = '6610238403:AAH50T5dXUB6tZ6vo8YAjlOTUl5prNGdaQ0'


logging.basicConfig(level=logging.INFO)

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

IMGS_PATH = 'lesson22/img'

categories = ['фотографії' 'фотки' 'фотографии' 'малюнок' 'фото'],


answers ={
    'categories' : ['фотографії' 'фотки' 'фотографии' 'малюнок' 'фото'],
    'cat' : ['кот' 'котик' 'котяра' 'котейка' 'котя' 'котики' 'коты' 'котика' 'кота' ],
    'space' : ['космос' 'космосу' 'космоса' 'космосом' 'космосам' 'космосами' ],
    'people' : ['люди' 'людишки' 'человеки']
}

def get_photo_by_category(category):
    path = f'{IMGS_PATH}/{category}'
    files = os.listdir(path)
    img = choice(files)
    return open(f'{path}/{img}', 'rb')


@dp.message_handler(commands = ['start'])
async def send_welcome(message: types.Message):
    await message.answer(f'Привіт! Ти можеш запитати мене показати кота, людей, або космос ')
    
    
    
@dp.message_handler()
async def basic_answer(message: types.Message):
    trigger1 = False
    category = ''
    
    words = message.text.split()
    
    
    for word in words:
        if word.lower() in categories:
            trigger1 = True
            continue
        for key, value in answers.items():
            if word.lower() in value:
                category = key
                
    if trigger1 and category:
        await message.answer_photo(get_photo_by_category(category))
    else:
        await message.answer('Я тебе не зрозумів, спробуй ще раз')
        
        
if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
            