from aiogram import types, Router, F
from aiogram.filters import CommandStart, Command
import logging

user_private_router = Router()
logging.basicConfig(level=logging.INFO)


@user_private_router.message(CommandStart())
async def start_cmd(message: types.Message) -> None:
    await message.answer(f"Hello, {message.from_user.full_name}")


@user_private_router.message(Command('about'))
async def menu_cmd(message: types.Message) -> None:
    await message.answer("Пока в процессе")


@user_private_router.message(F.text.lower() == 'пидор')
async def pidor(message: types.Message) -> None:
    await message.answer("Сам пидор")


@user_private_router.message(F.text.lower().contains('пидор'))
async def pidor(message: types.Message) -> None:
    await message.answer("Сам пидор")

