from aiogram.types import BotCommand

private = [
    BotCommand(command="start", description="Запустить бота"),
    BotCommand(command="about", description="Что умеет бот?"),
]

group = [
    BotCommand(command="whopidor", description="Распознать пидора"),
    BotCommand(command="about", description="Что умеет бот?"),
    BotCommand(command="statham", description="Цитаты Стэтхема"),
    BotCommand(command="bender", description="Цитаты Бендера"),
    BotCommand(command="homer", description="Цитаты Гомера"),
]
