import logging

from aiogram import Bot, Dispatcher

from handlers import user
from handlers import admin
from misc.constants import token


async def main() -> None:
    bot = Bot(token=token, parse_mode="MarkdownV2")
    dp = Dispatcher()

    logging.basicConfig(level=logging.INFO)

    dp.include_routers(user.router, admin.router)

    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)
