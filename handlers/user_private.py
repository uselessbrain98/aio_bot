import logging
from aiogram import types, Router, F
from aiogram.filters import CommandStart, Command
from filters.chat_types import ChatTypeFilter


user_private_router = Router()
user_private_router.message.filter(ChatTypeFilter(["private"]))


logging.basicConfig(level=logging.INFO)


@user_private_router.message(CommandStart())
async def start_cmd(message: types.Message) -> None:
    """Команда старта"""
    await message.answer(
        f"Вечер в хату, {message.from_user.full_name}. Определитель петуха здесь"
    )


@user_private_router.message(Command("about"))
async def menu_cmd(message: types.Message) -> None:
    """Что умеет бот?"""
    await message.answer("Пока в процессе")


@user_private_router.message((F.text.lower().contains('пидорбот пидор')) | (F.text.lower().contains('пидорбот для пидоров')))
async def bot_is_pidor(message: types.Message) -> None:
    """Ответ на обзывательство бота"""
    await message.answer("Сам пидор")


@user_private_router.message(
    (F.text.lower().contains("пидор")) | (F.text.lower().contains("гей"))
)
async def pidor_reply(message: types.Message) -> None:
    """reply +"""
    await message.reply("+")


@user_private_router.message()
async def all(message: types.Message) -> None:
    await message.answer('Напиши что-нибудь разумное, кожаный ублюдок')
