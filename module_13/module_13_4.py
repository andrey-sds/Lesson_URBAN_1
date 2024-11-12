from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage

import config_bot
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext
import asyncio

api_key = config_bot.api
bot = Bot(token=api_key)
dp = Dispatcher(bot, storage=MemoryStorage())


@dp.message_handler(commands=["start"])
async def start_message(message):
    await message.answer("Привет! Я бот помогающий твоему здоровью!\n"
                         "Введите команду /Calories для подсчёта нормы калорий")


@dp.message_handler(commands=["Calories"])
async def set_age(message):
    await message.answer("Введите свой возраст")
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
    calories = 10 * float(data['weight']) + 6.25 * float(data['growth']) - 5 * float(data['age']) + 5
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
