from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove

start_button = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Ariza qoldirish")
        ],
    ],
    resize_keyboard=True
)

no_phone_number = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Boshqa raqamim yo'q")
        ],
    ],
    resize_keyboard=True
)


remove_b = ReplyKeyboardRemove()

main_profession = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Haydovchi"),
            KeyboardButton(text="Call Center Operatori"),
        ],
    ],
    resize_keyboard=True
)

vehicle_type = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Avtomobil"),
            KeyboardButton(text="Velosiped"),
            KeyboardButton(text="Skuter"),
        ],
    ],

    resize_keyboard=True
)

yes_no = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Bor"),
            KeyboardButton(text="Yo'q"),
        ],
    ],
    resize_keyboard=True
)


send_button = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Yuborish"),
            KeyboardButton(text="Bekor qilish"),
        ],
    ],
    resize_keyboard=True
)


