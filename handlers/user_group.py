import logging
import time
from aiogram import types, Router, F
from aiogram.filters import Command
from filters.chat_types import ChatTypeFilter
from common import text_list
import random

user_group_router = Router()
user_group_router.message.filter(ChatTypeFilter(["group", "supergroup"]))
logging.basicConfig(level=logging.INFO)


@user_group_router.message(Command("about"))
async def menu_cmd(message: types.Message) -> None:
    """Что умеет бот?"""
    await message.answer(
        "Крестный отец всех ботов цитирует великих персонажей, контролирует заднеприводных и многое другое")


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
