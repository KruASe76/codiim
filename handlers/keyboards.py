from aiogram.types import (
    InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardRemove
)


empty = ReplyKeyboardRemove()

admin = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(
                text="Спать! ⛔️",
                callback_data="shutdown"
            )
        ]
    ]
)
