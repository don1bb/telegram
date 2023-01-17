from aiogram import Bot, Dispatcher, executor, types
from aiogram.dispatcher.filters import Text
from dotenv import load_dotenv
from os import getenv
import logging
from handlers.constants import HELP_TEXT, START_TEXT
from handlers.start import start_command
from handlers.help import help_command
from handlers.pictures import image_sender
from handlers.shop import shop_start
from handlers.all_messages import echo
from handlers.shop_categories import show_clothes

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    load_dotenv()
    bot = Bot(getenv('BOT_TOKEN'))
    dp = Dispatcher(bot)

    dp.register_message_handler(start_command, commands=['start'])
    dp.register_message_handler(help_command, commands=['help'])
    dp.register_message_handler(image_sender, commands=['picture'])
    dp.register_callback_query_handler(shop_start, text=['shop_start'])
    dp.register_message_handler(show_clothes, Text(equals='одежды'))
    dp.register_message_handler(echo)
    executor.start_polling(dp, skip_updates=True)



