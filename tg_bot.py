from aiogram import Bot, Dispatcher, types, executor
from aiogram.dispatcher.filters import Text
from aiogram.utils.markdown import hbold, hlink
import json
import ENV

bot = Bot(token=ENV.API_TOKEN, parse_mode=types.ParseMode.HTML)

dp = Dispatcher(bot)
back_buttons = ['Назад']


@dp.message_handler(commands='start')
async def start(message: types.Message):
    start_buttons = ['Camry', 'Land Cruiser']
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True).add(*start_buttons)

    await message.answer('Выберите модель авто', reply_markup=keyboard)


@dp.message_handler(Text(equals="Camry"))
async def camry_(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True).add(*back_buttons)
    await message.answer('please wait...', reply_markup=keyboard)

    with open(f'{ENV.TG_DATA}/cars.json', 'r', encoding='utf-8') as file:
        json_data = json.load(file)

    for item in json_data:
        card = f"{hlink(item.get('name'), item.get('url'))} \n" \
                f"{hbold('Price:')} {item.get('price')}"
        await message.answer(card)

    await message.answer('go back', reply_markup=keyboard)



@dp.message_handler(Text(equals="Land Cruiser"))
async def tlc_(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True).add(*back_buttons)
    await message.answer('Выбрал Land Cruiser', reply_markup=keyboard)


@dp.message_handler(Text(equals="Назад"))
async def start(message: types.Message):
    start_buttons = ['Camry', 'Land Cruiser']
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True).add(*start_buttons)

    await message.answer('Выберите модель авто', reply_markup=keyboard)


def main():
    executor.start_polling(dp)


if __name__ == '__main__':
    main()