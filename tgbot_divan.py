from aiogram import Bot, Dispatcher, types, executor
from aiogram.dispatcher.filters import Text
from aiogram.utils.markdown import hbold, hlink
import json
import ENV
import tgbot_functions

bot = Bot(token=ENV.API_TOKEN, parse_mode=types.ParseMode.HTML)

dp = Dispatcher(bot)
back_buttons = ['Назад']


@dp.message_handler()
async def echo(message: types.Message):
    if message.text.find('/count_divan') != -1 :
        await message.answer('processing...')
        date = message.text.replace("/count_divan_", "")
        await message.reply(tgbot_functions.count_goods('divany-i-kresla', date))
    if message.text.find('/count_krovati') != -1 :
        await message.answer('processing...')
        date = message.text.replace("/count_krovati_", "")
        await message.reply(tgbot_functions.count_goods('krovati-i-matrasy', date))

@dp.message_handler(commands='start')
async def start(message: types.Message):
    start_buttons = ['divany-i-kresla', 'krovati-i-matrasy']
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True).add(*start_buttons)
    await message.answer('Выберите категорию', reply_markup=keyboard)


@dp.message_handler(Text(equals="divany-i-kresla"))
async def start(message: types.Message):
    start_buttons = ['Кол-во Диванов', 'Кол-во товаров со скидкой 40%']
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True).add(*start_buttons)
    await message.answer('Выберите операцию', reply_markup=keyboard)


@dp.message_handler(Text(equals="Кол-во Диванов"))
async def start(message: types.Message):
    await message.answer('В процессе...')
    await message.answer(count_items())


@dp.message_handler(Text(equals="Кол-во товаров со скидкой 40%"))
async def start(message: types.Message):
    await message.answer('В процессе...')
    await message.answer(discount(45, test=False))


def count_items():
    with open('data\daily_parse\divany-i-kresla\divany-i-kresla_225846-27112022.json', 'r', encoding='utf-8') as file:
        items = json.load(file)
        return len(items)


def discount(discount_size, test):
    if not test:
        with open('data\daily_parse\divany-i-kresla\divany-i-kresla_225846-27112022.json', 'r',
                  encoding='utf-8') as file:
            items = json.load(file)
            discount_items = ''
            for item in items:
                if int(item['price']['discount']) > discount_size:
                    # print(item)
                    discount_items = discount_items + item['name'] + ' : ' + item['link'] + '\n'
            return discount_items
    else:
        discount_items = []
        discount_items.append({
            'name': 'Байвин-1 Soft Olive',
            'link': 'https://divan.ru/product/divan-uglovoj-bajvin-1-soft-olive',
            'price': '10000'
        })
        discount_items.append({
            'name': 'ХУЙ-1 Soft Olive',
            'link': 'https://divan.ru/product/divan-uglovoj-bajvin-1-soft-olive',
            'price': '12000'
        })
        discount_items.append({
            'name': 'ПИЗДА-1 Soft Olive',
            'link': 'https://divan.ru/product/divan-uglovoj-bajvin-1-soft-olive',
            'price': '15000'
        })

        my_str = ''
        for item in discount_items:
            my_str = my_str + item['name'] + ' : ' + item['link'] + '\n'

        return my_str


def main():
    executor.start_polling(dp)
    # count_items()
    # print(discount(45, test=True))


main()
