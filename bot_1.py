from aiogram import Bot, Dispatcher
from aiogram.filters import Command
from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.types import Message, InputFile, InlineKeyboardButton
from aiogram import types

API_TOKEN: str = '6214808173:AAHmqWl1LL-9ytJ7T5MY9mTnfkvRADIOpv0'
bot: Bot = Bot(token=API_TOKEN)
dp: Dispatcher = Dispatcher()

@dp.message(Command(commands = ['start']))
async def start(message: Message):
    await message.answer("Я бот для домашнего задания")
    await message.answer("напиши /write, чтобы записать домашнее задание")
    await message.answer("напиши /read, чтобы посмотреть домашнее задание")
    keyboard = InlineKeyboardBuilder()
    keyboard.add(InlineKeyboardButton(text="Оставить дз", callback_data="1"))
    keyboard.add(InlineKeyboardButton(text="Посмотреть дз", callback_data="2"))
    await message.answer("Или воспользуйся кнопками:", reply_markup=keyboard.as_markup())

@dp.callback_query()
async def answer(callback: types.CallbackQuery):
    if callback.data == '1':
        await callback.message.answer("Отправь сообщение с дз, которое ты хочешь оставить для одноклассников")
        @dp.message()
        async def answer1(message: Message):
            global dz
            dz = message.text
    if callback.data == '2':
        await callback.message.answer(dz)

@dp.message(Command(commands = ['write']))
async def write(message: Message):
    await message.answer("Отправь сообщение с дз, которое ты хочешь оставить для одноклассников")
    @dp.message()
    async def write1(message: Message):
        global dz
        dz = message.text

@dp.message(Command(commands=['read']))
async def read(message: Message):
    await message.answer(dz)

if __name__ == '__main__':
    dp.run_polling(bot)