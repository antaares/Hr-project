from aiogram.dispatcher.filters.state import StatesGroup, State




class UserForm(StatesGroup):
    full_name = State()
    year = State()
    phone_number = State()
    phone_number2 = State()
    photo = State()
    profession = State()
    Driver = State()
    Rider = State()
    Operator = State()
    sales = State()
    where = State()
    send = State()
