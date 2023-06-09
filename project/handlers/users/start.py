from aiogram import types
from aiogram.dispatcher.filters import Text

from aiogram.dispatcher import FSMContext

from loader import dp, bot
from data.config import owner


from states.user_form import UserForm


from keyboards.default.all_buttons import start_button, main_profession, vehicle_type, yes_no, remove_b, send_button, no_phone_number


@dp.message_handler(commands=['start'], chat_type="private",state="*")
async def start(message: types.Message, state: FSMContext):
    await state.finish()
    await message.answer(f"Assalomu alaykum {message.from_user.full_name}!\n \"Ariza qoldirish\" tugmasini bosing va arizangizni qoldiring."\
                         "Arizani bekor qilish uchun /start buyrug'ini bosing.",
                         reply_markup=start_button)
    

    





@dp.message_handler(Text(equals="Ariza qoldirish"),chat_type="private",state="*")
async def get_text_messages(message: types.Message, state: FSMContext):
    await state.finish()
    await message.answer("To‘liq ismingizni kiriting:", reply_markup=remove_b)
    await UserForm.full_name.set()




@dp.message_handler(state=UserForm.full_name)
async def get_full_name(message: types.Message, state: FSMContext):
    full_name = message.text
    await state.update_data(full_name=full_name)
    await message.answer("Telefon raqamingizni kiriting:")
    await UserForm.phone_number.set()


@dp.message_handler(state=UserForm.phone_number)
async def get_phone_number(message: types.Message, state: FSMContext):
    phone_number = message.text
    await state.update_data(phone_number=phone_number)
    await message.answer("Boshqa telefon raqamingizni ham kiriting:", reply_markup=no_phone_number)
    await UserForm.phone_number2.set()



@dp.message_handler(state=UserForm.phone_number2)
async def get_phone_number2(message: types.Message, state: FSMContext):
    phone_number2 = message.text
    if phone_number2 == "Boshqa raqamim yo'q":
        phone_number2 = None
    await state.update_data(phone_number2=phone_number2)
    await message.answer("Yoshingizni kiriting:", reply_markup=remove_b)
    await UserForm.year.set()
    



@dp.message_handler(state=UserForm.year)
async def get_year(message: types.Message, state: FSMContext):
    year = message.text
    await state.update_data(year=year)
    await message.answer("Bizga yuzingiz va gavdangiz aniq ko'ringan bitta rasm yuboring!")
    await UserForm.photo.set()



@dp.message_handler(content_types=['photo'], state=UserForm.photo)
async def get_photo(message: types.Message, state: FSMContext):
    photo = message.photo[-1].file_id
    await state.update_data(photo=photo)
    await message.answer("Siz bizda qaysi yo'nalishda ishlamoqchisiz?",
                         reply_markup=main_profession)
    await UserForm.profession.set()

@dp.message_handler(state=UserForm.profession)
async def get_profession(message: types.Message, state: FSMContext):
    profession = message.text
    if profession == "Haydovchi":
        await state.update_data(profession=profession)
        await message.answer("Qaysi turdagi transport vositasini boshqarishni xohlaysiz?",
                             reply_markup=vehicle_type)
        await UserForm.Driver.set()
    elif profession == "Call Center Operatori":
        await state.update_data(profession=profession)
        await message.answer("Bizda qancha oylik maoshga ishlamoqchisiz?", reply_markup=remove_b)
        await UserForm.sales.set()


@dp.message_handler(state=UserForm.Driver)
async def get_Driver(message: types.Message, state: FSMContext):
    text = message.text
    if text == "Avtomobil":
        await state.update_data(vehicle=text)
        await message.answer("Sizni avtomobilingiz bormi?", reply_markup=yes_no)

    elif text == "Velosiped":
        await state.update_data(vehicle=text)
        await message.answer("Sizni velosipedingiz bormi?", reply_markup=yes_no)
        
    elif text == "Skuter":
        await state.update_data(vehicle=text)
        await message.answer("Sizni skuteringiz bormi?", reply_markup=yes_no)
    await UserForm.Rider.set()





@dp.message_handler(state=UserForm.Rider)
async def get_Rider(message: types.Message, state: FSMContext):
    rider = message.text
    await state.update_data(rider=rider)
    await message.answer("Bizda qancha oylik maoshga ishlamoqchisiz?", reply_markup=remove_b)
    await UserForm.sales.set()


@dp.message_handler(state=UserForm.sales)
async def get_sales(message: types.Message, state: FSMContext):
    sales = message.text
    await state.update_data(sales=sales)
    await message.answer("Siz bizga qayerdan murojaat qildingiz?\nreklamani qayerda ko'rdingiz?", reply_markup=remove_b)
    await UserForm.where.set()


@dp.message_handler(state=UserForm.where)
async def get_where(message: types.Message, state: FSMContext):
    where = message.text
    await state.update_data(where=where)
    data = await state.get_data()
    full_name = data.get("full_name")
    phone_number = data.get("phone_number")
    phone_number2 = data.get("phone_number2")
    year = data.get("year")
    photo = data.get("photo")
    profession = data.get("profession")
    vehicle = data.get("vehicle")
    rider = data.get("rider")
    sales = data.get("sales")
    where = data.get("where")
    text = f"👤 Ism: {full_name}\n"\
        f"📞 Telefon raqam: {phone_number}\n"\
        f"📞 Telefon raqam: {phone_number2}\n"\
        f"👨‍👩‍👧‍👦 Yosh: {year}\n"\
        f"👨‍💼 Kasb: {profession}\n"
    if profession == "Haydovchi":
        text += f"🚗 Transport turi: {vehicle}\n"
        text += f"🚲 Transporti: {rider}\n"
    text += f"💰 Maosh: {sales}\n"
    text += f"📍 Qayerdan: {where}"


    await message.answer_photo(photo=photo, caption=text)






    await message.answer("Ma'lumotlaringizni tekshirib yuborish uchun \"Yuborish\" tugmasini bosing.",
                         reply_markup=send_button)
    await UserForm.send.set()



@dp.message_handler(state=UserForm.send)
async def send(message: types.Message, state: FSMContext):
    if message.text == "Bekor qilish":
        await message.answer("Ma'lumotlaringizni o'zgartirish uchun /start ni bosing.")
        await state.finish()
    data = await state.get_data()
    full_name = data.get("full_name")
    phone_number = data.get("phone_number")
    phone_number2 = data.get("phone_number2")
    year = data.get("year")
    photo = data.get("photo")
    profession = data.get("profession")
    vehicle = data.get("vehicle")
    rider = data.get("rider")
    sales = data.get("sales")
    where = data.get("where")
    text = f"👤 Ism: {full_name}\n"\
        f"📞 Telefon raqam: {phone_number}\n"\
        f"📞 Telefon raqam: {phone_number2}\n"\
        f"👨‍👩‍👧‍👦 Yosh: {year}\n"\
        f"👨‍💼 Kasb: {profession}\n"
    if profession == "Haydovchi":
        text += f"🚗 Transport turi: {vehicle}\n"
        text += f"🚲 Transporti: {rider}\n"
    text += f"💰 Maosh: {sales}\n"
    text += f"📍 Qayerdan: {where}"

    await bot.send_photo(chat_id=owner, photo=photo, caption=text)
    await message.answer("Ma'lumotlaringiz muvaffaqiyatli yuborildi!", reply_markup=remove_b)
    await state.reset_state()
    await state.finish()
    await message.answer(f"Assalomu alaykum {message.from_user.full_name}!\n \"Ariza qoldirish\" tugmasini bosing va arizangizni qoldiring."\
                         "Arizani bekor qilish uchun /start buyrug'ini bosing.",
                         reply_markup=start_button)
