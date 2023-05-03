from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


admin = InlineKeyboardMarkup(
    row_width=1,
    inline_keyboard=[
        [
            InlineKeyboardButton(
                text="Спать! ⛔️",
                callback_data="shutdown"
            )
        ]
    ]
)
