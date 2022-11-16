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
    start_buttons = ['divany-i-kresla', 'krovati-i-matrasy']
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True).add(*start_buttons)
    await message.answer('Выберите категорию', reply_markup=keyboard)


def main():
    executor.start_polling(dp)



main()
