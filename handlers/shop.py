from aiogram import types
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

shop_kb = ReplyKeyboardMarkup(resize_keyboard=True)
shop_kb.add(
    KeyboardButton('одужды'),
    KeyboardButton('хочу зимние ботинки'),
    KeyboardButton('хочу футболки'),
)

async  def shop_start(cb: types.CallbackQuery):

    await cb.bot.send_message(
        chat_id=cb.from_user.id,
        text= "Выберите категорию из меню ниже",
        reply_markup=shop_kb
    )
