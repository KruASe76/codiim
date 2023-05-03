from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message, ReplyKeyboardRemove


router = Router()


@router.message(Command(commands=["start", "help"]))
async def help_command(message: Message):
    await message.answer(
        "Привет\! Я \- бот великого недопрогера @KruASe \(а еще двое творят его начинку\)\n"
        "Он обещает, что вскоре я научусь что\-то предсказывать\.\.\.",
        reply_markup=ReplyKeyboardRemove()
    )


@router.message(Command(commands=["magic"]))
async def magic_command(message: Message):
    await message.answer(
        "Написано же, что пока не сделано\!",
        reply_markup=ReplyKeyboardRemove()
    )
