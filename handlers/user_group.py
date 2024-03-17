import logging
from aiogram import types, Router, F
from aiogram.filters import Command
from filters.chat_types import ChatTypeFilter

user_group_router = Router()
user_group_router.message.filter(ChatTypeFilter(["group", "supergroup"]))
logging.basicConfig(level=logging.INFO)

@user_group_router.message(Command("about"))
async def menu_cmd(message: types.Message) -> None:
    """Что умеет бот?"""
    await message.answer("Пока в процессе")


@user_group_router.message(F.text.lower() == "пидорбот пидор")
async def bot_is_pidor(message: types.Message) -> None:
    """Ответ на обзывательство бота"""
    await message.reply("Сам пидор")


@user_group_router.message(
    (F.text.lower().contains("пидор"))
    | (F.text.lower().contains("гей"))
    | (F.text.lower().contains("хуесос"))
)
async def pidor_reply(message: types.Message) -> None:
    """reply +"""
    await message.reply("+")
