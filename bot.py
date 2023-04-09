import logging
import aiogram
from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import InlineKeyboardButton,InlineKeyboardMarkup
from config import API_TOKEN

button1 = InlineKeyboardButton(text='Rektorat',callback_data='Rektor')
button2 = InlineKeyboardButton(text='Fakultetlar',callback_data='Fakultet')
keyboard_inline = InlineKeyboardMarkup().add(button1,button2)
button3 = InlineKeyboardButton(text='Universitet rektori',callback_data='universitet rektori')
button4 = InlineKeyboardButton(text='O`quv ishlari bo`yicha prorektor',callback_data='prorektor')
button5 = InlineKeyboardButton(text='Yoshlar masalalari bo`yicha prorektor',callback_data='yoshlarprorektor')
button6 = InlineKeyboardButton(text='Moliya va iqtisod ishlari bo`yicha prorektor',callback_data='moliyaprorektor')
button7 = InlineKeyboardButton(text='Ilmiy ishlar va innovatsiyalar bo`yicha prorektor',callback_data='ilmiyprorektor')
button8 = InlineKeyboardButton(text='Axborot texnologiyalar bo`yicha prorektor',callback_data='axborotprorektor')
button9 = InlineKeyboardButton(text='Asosiy menyuga qaytish',callback_data='back')
keyboard_inline1 = InlineKeyboardMarkup().add(button3).add(button4).add(button5).add(button6).add(button7).add(button8).add(button9)
# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    await message.reply("Assalomu alaykum! ADU rahbariyati bilan tanishish botiga xush kelibsiz",reply_markup=keyboard_inline)
    print(message.from_user.id)
    
@dp.callback_query_handler(text=['Rektor','Fakultet'])
async def random_value(call: types.CallbackQuery):
    if call.data == 'Rektor':
        await call.message.reply(text='Rektorat',reply_markup=keyboard_inline1)
    if call.data == 'Fakultet':
       await call.message.answer(text='Fizika-matematika fakulteti,\nFilologiya fakulteti,\nTabiiy fanlar fakulteti,\nTarix fakulteti,\nIjtimoiy-iqtisodiyot fakulteti,\nPedagogika fakulteti,\nMaktabgacha ta’lim fakulteti,\nSan’atshunoslik fakulteti,\nXorijiy tillar fakulteti,\nJismoniy madaniyat fakulteti,\nAxborot texnologiyalari va kompyuter injiniringi fakulteti')
        
@dp.callback_query_handler(text=['universitet rektori','prorektor','yoshlarprorektor','moliyaprorektor','ilmiyprorektor','axborotprorektor','back'])
async def random_value(call: types.CallbackQuery):
    if call.data == 'universitet rektori':
        await bot.send_photo(chat_id=call.from_user.id,photo=open(f"pictures/rektor.jpg","rb"),caption='YULDASHEV AKRAMJON SULTANMURADOVICH \n Rektor. Biologiya fanlari doktori, professor.')
    if call.data == 'prorektor':
        await bot.send_photo(chat_id=call.from_user.id,photo=open(f"pictures/prorek.jpg","rb"),caption='MULLAJONOV RUSTAMJON VAHOBJONOVICH \n O`quv ishlar bo`yicha prorektor. Fizika-matematika fanlari nomzodi, dotsent')
    if call.data == 'yoshlarprorektor':
        await bot.send_photo(chat_id=call.from_user.id,photo=open(f"pictures/yoshlar.jpg","rb"),caption="HAMRAQULOV A'ZAMJON SHERMUHAMMADOVICH \n Yoshlar masalalari va ma'naviy-ma'rifiy ishlar bo`yicha prorektor. Filologiya fanlari nomzodi")
    if call.data == 'moliyaprorektor':
        await bot.send_photo(chat_id=call.from_user.id,photo=open(f"pictures/moliya.jpg","rb"),caption="SOBIROV SHOYADBEK QURBONALIYEVICH\n Moliya va iqtisod ishlari bo`yicha prorektor")
    if call.data == 'ilmiyprorektor':
        await bot.send_photo(chat_id=call.from_user.id,photo=open(f"pictures/ilm.jpg","rb"),caption="KARIMJANOV IKBOLJON ABDULAZIZOVICH\n Ilmiy ishlar va innovatsiyalar bo'yicha prorektor. ")
    if call.data == 'axborotprorektor':
        await bot.send_photo(chat_id=call.from_user.id,photo=open(f"pictures/axborot.jpg","rb"),caption="MAXKAMOV MADAMINJON KOMILOVICH\n Axborot texnologiyalari bo`yicha prorektor")
    if call.data == 'back':
        await call.message.reply(text="Assalomu alaykum! ADU rahbariyati bilan tanishish botiga xush kelibsiz",reply_markup=keyboard_inline)
executor.start_polling(dp)