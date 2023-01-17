from aiogram import types
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

buy_istem_kb = InlineKeyboardMarkup()
buy_istem_kb.add(
    InlineKeyboardButton('купить', callback_data='buy_istem_kb')
)
async def show_clothes(message: types.Message):
    await message.answer(text='тут все что у нас есть)')
    await message.answer(text='кросcовки', reply_markup=buy_istem_kb)
    await message.answer(text='зимние', reply_markup=buy_istem_kb)
    await message.answer(text='одежды', reply_markup=buy_istem_kb)