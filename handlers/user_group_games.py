import logging
import time
from aiogram import types, Router, F
from aiogram.filters import Command

from filters.chat_types import ChatTypeFilter
import random

from settings.db import create_user, connect_to_database

user_group_router = Router()
user_group_router.message.filter(ChatTypeFilter(["group", "supergroup"]))
logging.basicConfig(level=logging.INFO)

@user_group_router.message(Command("finddick"))
async def find_dick(message: types.Message) -> None:
    """Игра finddick"""
    await message.answer(
        "Крестный отец всех ботов цитирует великих персонажей, контролирует заднеприводных и многое другое")
