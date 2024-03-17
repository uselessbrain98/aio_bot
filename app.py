import asyncio
from aiogram import Bot, Dispatcher
from aiogram.types import BotCommandScopeAllPrivateChats, BotCommandScopeAllGroupChats

from common.cmd_list import private, group
from handlers.user_private import user_private_router
from settings import BOT_TOKEN

dp = Dispatcher()
dp.include_routers(user_private_router)
ALLOWED_UPDATES = ['message, edited_message']


async def main() -> None:
    bot = Bot(BOT_TOKEN)
    await bot.set_my_commands(commands=private, scope=BotCommandScopeAllPrivateChats())
    await bot.set_my_commands(commands=group, scope=BotCommandScopeAllGroupChats())
    await dp.start_polling(bot, allowed_updates=ALLOWED_UPDATES)


if __name__ == "__main__":
    asyncio.run(main())
