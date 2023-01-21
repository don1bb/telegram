from aiogram import types
from handlers.constants import START_TEXT
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


async def start_command(message: types.Message):
    await message.answer(
        text=START_TEXT.format(first_name=message.from_user.first_name))
    await message.delete()

    markup = InlineKeyboardMarkup()
    button_call_1 = InlineKeyboardButton("Магазин", callback_data="button_call_1")
    button_call_2 = InlineKeyboardButton("Наш адрес", callback_data="button_call_2")
    markup.add(button_call_1, button_call_2)
    await message.answer(message.from_user.first_name,
                           reply_markup=markup)






# start_kb = InlineKeyboardMarkup(resize_keyboard=True)
# start_kb.add(
#     InlineKeyboardButton('Магазин', callback_data='shop_start'),
#     InlineKeyboardButton('Наш адрес', callback_data='address')
# )
#     await message.answer(
#         text=START_TEXT.format(first_name=message.from_user.first_name))

#     await message.delete()
