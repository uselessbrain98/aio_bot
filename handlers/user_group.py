import logging
import time
from aiogram import types, Router, F
from aiogram.filters import Command

from common.weather import get_weather
from filters.chat_types import ChatTypeFilter
from common import text_list
import random

from settings.db import create_user, connect_to_database

user_group_router = Router()
user_group_router.message.filter(ChatTypeFilter(["group", "supergroup"]))
logging.basicConfig(level=logging.INFO)


@user_group_router.message(Command("about"))
async def menu_cmd(message: types.Message) -> None:
    """Что умеет бот?"""
    await message.answer(
        "Крестный отец всех ботов цитирует великих персонажей, контролирует заднеприводных и многое другое")


@user_group_router.message(Command("info"))
async def info(message: types.Message) -> None:
    """Узнать инфо?"""
    user_id = message.from_user.id
    user_name = message.from_user.username
    first_name = message.from_user.first_name
    last_name = message.from_user.last_name
    chat_id = message.chat.id
    chat_title = message.chat.title
    sqlite_connection, cursor = connect_to_database()
    result = create_user(cursor, sqlite_connection, user_id, user_name, first_name, last_name, chat_id, chat_title)
    await message.answer(
        f"""
        Данные о пользователе=>
        user_id: {user_id}
        user_name: {user_name}
        first_name: {first_name}
        last_name: {last_name}
        chat_id(current): {chat_id}
        result: {result}
        """)


@user_group_router.message(Command("current_weather"))
async def current_weather(message: types.Message) -> None:
    """Узнать погоду"""
    r = get_weather('current')
    temp = r['current']['temp_c']
    feel = r['current']['feelslike_c']
    wind = r['current']['wind_kph']
    press = r['current']['pressure_mb']
    hum = r['current']['humidity']
    cond = r['current']['condition']['text']
    await message.answer(
        f"Температура за бортом: {temp} С\nОщущается как: {feel} С, нахуй\nЕбучий ветер: {wind} км/ч\nДавление: {press} мбар\nВлажность: {hum} %\nСостояние: {cond}")


@user_group_router.message(Command("whopidor"))
async def who_pidor(message: types.Message) -> None:
    """Определить пидора"""
    await message.answer("Бот определит кто пидор. Подожди чуть-чуть")
    time.sleep(2)
    await message.answer("Бот определил пидора. Это ты")


@user_group_router.message(Command("statham"))
async def statham(message: types.Message) -> None:
    """Цитируем Стэтхема"""
    await message.answer(f"{random.choice(text_list.statham_quotes)} (c)Стэтхем")


@user_group_router.message(Command("bender"))
async def statham(message: types.Message) -> None:
    """Цитируем Бендера"""
    await message.answer(f"{random.choice(text_list.bender_quotes)} (c)Бендер")


@user_group_router.message(Command("homer"))
async def statham(message: types.Message) -> None:
    """Цитируем Гомера"""
    await message.answer(f"{random.choice(text_list.homer_quotes)} (c)Гомер Симпсон")


@user_group_router.message(
    (F.text.lower().contains("botgodfather пидор")) | (F.text.lower().contains("botgodfather для пидоров")))
async def bot_is_pidor(message: types.Message) -> None:
    """Ответ на обзывательство бота"""
    await message.reply("Сам пидор")


@user_group_router.message(
    (
            (F.text.lower().contains("пидор"))
            | (F.text.lower().contains("гей"))
            | (F.text.lower().contains("хуесос"))
    )
    & ~(F.text.lower().contains("айнур"))
    & ~(F.text.lower().contains("dgtla"))
    & ~(F.text.lower().contains("а й"))
)
async def pidor_reply(message: types.Message) -> None:
    """reply +"""
    await message.reply("+")


@user_group_router.message(F.text.lower() == "курить")
async def all_smoke(message: types.Message) -> None:
    """Призыв всех покурить сигареты"""
    await message.answer("Пидоры, общий сбор в курилке через 3...2...")


@user_group_router.message(F.text.lower() == "обед")
async def all_eat(message: types.Message) -> None:
    """Обедать пора"""
    await message.reply("Роллы для лохов, пельмешки для пацанов. (с) Стетхем ")


@user_group_router.message(F.text.lower() == "да")
async def yes(message: types.Message):
    """Ответа на да"""
    await message.reply("Хуй, пизда, Джигурда")


@user_group_router.message(F.text.lower() == "нет")
async def yes(message: types.Message):
    """Ответа на нет"""
    await message.reply("Пидора ответ")
