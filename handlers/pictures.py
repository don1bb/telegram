from aiogram import types


async def image_sender(message: types.Message):
	"""
		Функция ответа пользователю картинкой
	"""
	await message.answer_photo(
        open('image/gg.jpg', 'rb'),
        caption="кроссовки"
    )
	await message.delete()