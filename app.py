import asyncio
from aiogram import Bot, Dispatcher
from aiogram.types import BotCommandScopeAllPrivateChats, BotCommandScopeAllGroupChats

from common.cmd_list import private, group
from handlers.user_private import user_private_router
from handlers.user_group import user_group_router
from settings import BOT_TOKEN


dp = Dispatcher()
dp.include_routers(user_private_router)
dp.include_routers(user_group_router)
ALLOWED_UPDATES = ["message, edited_message"]


async def main() -> None:
    """Запуск и настройка бота"""
    bot = Bot(BOT_TOKEN)
    await bot.delete_webhook(drop_pending_updates=True)
    await bot.set_my_commands(commands=private, scope=BotCommandScopeAllPrivateChats())
    await bot.set_my_commands(commands=group, scope=BotCommandScopeAllGroupChats())
    await dp.start_polling(bot, allowed_updates=ALLOWED_UPDATES)


if __name__ == "__main__":
    asyncio.run(main())
