from pathlib import Path
from random import choice

from aiogram import Bot, Router, F
from aiogram.filters import Command
from aiogram.types import Message, PhotoSize

from handlers import keyboards as kb
from engine.model import predict
from misc.constants import temp_dir, result_phrases, advices


router = Router()


@router.message(Command(commands=["start", "help"]))
async def help_command(message: Message):
    await message.reply(
        "Привет! Я - бот великого недопрогера @KruASe (а еще двое творят его начинку)\n\n"
        "<b>Я умею</b> предсказывать состояние собаки по ее фото!\n"
        "Просто пришли его мне!",
        reply_markup=kb.empty
    )


@router.message(F.photo[-1].as_("photo"))
async def process_photo(message: Message, bot: Bot, photo: PhotoSize):
    photo_path = Path(temp_dir, f"{photo.file_id}.jpg")

    await bot.download(photo, photo_path)

    emotion = predict(photo_path)

    await message.reply(
        f"<b>{result_phrases[emotion]}</b>\n\n{choice(advices[emotion])}"
    )
