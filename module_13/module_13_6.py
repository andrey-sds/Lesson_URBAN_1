from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
import config_bot
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
import asyncio

api_key = config_bot.api
bot = Bot(token=api_key)
dp = Dispatcher(bot, storage=MemoryStorage())
kb = ReplyKeyboardMarkup()
kb2 = InlineKeyboardMarkup()

button = KeyboardButton(text='Рассчитать', resize_keybord=True)
button2 = KeyboardButton(text='Информация', resize_keybord=True)
kb.insert(button)
kb.insert(button2)

button3 = InlineKeyboardButton(text='Рассчитать норму калорий', callback_data='calories')
button4 = InlineKeyboardButton(text='Формулы расчёта', callback_data='formula')
kb2.insert(button3)
kb2.insert(button4)


@dp.message_handler(commands=["start"])
async def start_message(message):
    await message.answer("Привет! Я бот помогающий твоему здоровью!\n"
                         "Выберите действие:", reply_markup=kb)


@dp.message_handler(text='Информация')
async def inform(message):
    await message.answer('Бот рассчитывает суточную норму потребления калорий на основе '
                         'упрощённой формулы Миффлина - Сан Жеора (для мужчин)')


@dp.message_handler(text="Рассчитать")
async def main_menu(message):
    await message.answer("Выберите опцию", reply_markup=kb2, reply=True)


@dp.callback_query_handler(text='Рассчитать')
async def callback_data(call):
    await call.message.answer("calories")
    await call.answer()


@dp.callback_query_handler(text='formula')
async def get_formulas(call):
    await call.message.answer("для мужчин: 10 * вес (кг) + 6,25 * рост (см) – 5 * возраст (г) + 5\n"
                              "для женщин: 10 * вес (кг) + 6,25 * рост (см) – 5 * возраст (г) – 161")
    await call.answer()


@dp.callback_query_handler(text='calories')
async def set_age(call):
    await call.message.answer("Введите свой возраст")
    await UserState.age.set()


@dp.message_handler()
async def all_massage(message):
    # print("Введите команду /start, чтобы начать общение.")
    await message.answer(message.text + "\nВведите команду /start, чтобы начать общение.")


class UserState(StatesGroup):
    age = State()
    sex = State()
    growth = State()
    weight = State()


async def set_growth(message, state):
    await message.answer("Введите свой рост:")
    await UserState.growth.set()


async def set_weight(message, state):
    await message.answer("Введите свой вес:")
    await UserState.weight.set()


async def send_calories(message, state):
    data = await state.get_data()
    calories = 10 * float(data['weight'].replace(',', '.')) + 6.25 * float(data['growth'].replace(',', '.')) - 5 * float(data['age']) + 5
    await message.answer(f'Ваша суточная норма составляет {calories} калорий')


@dp.message_handler(state=UserState.growth)
async def fsm_handler(message, state):
    await state.update_data(growth=message.text)
    await set_weight(message, state)


@dp.message_handler(state=UserState.age)
async def fsm_handler(message, state):
    await state.update_data(age=message.text)
    await set_growth(message, state)
    await state.update_data(growth=message.text)


@dp.message_handler(state=UserState.weight)
async def fsm_handler(message, state):
    await state.update_data(weight=message.text)
    data = await state.get_data()
    await message.answer(f"Ваши данные {data}")
    await send_calories(message, state)
    await state.finish()


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
