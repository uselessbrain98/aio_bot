from aiogram import types, Router, F
from aiogram.filters import CommandStart, Command
import logging

user_group_router = Router()
user_group_router.message.filter(ChatTypeFilter(['group', 'supergroup']))
