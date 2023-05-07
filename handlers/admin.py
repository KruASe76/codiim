from sys import exit

from aiogram import Router
from aiogram.filters import Command, Text
from aiogram.types import Message, CallbackQuery

from handlers.filters import BotAdminMessageFilter, BotAdminCallbackFilter
from handlers import keyboards as kb


router = Router()


@router.message(Command(commands=["god"]), BotAdminMessageFilter())
async def admin_panel_command(message: Message):
    await message.answer("Здравствуй, Господи!", reply_markup=kb.admin)


@router.callback_query(Text(text="shutdown"), BotAdminCallbackFilter())
async def shutdown_query(callback: CallbackQuery):
    await callback.answer()
    await callback.message.answer("Бот уходит в закат...")

    exit()
