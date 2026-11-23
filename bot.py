
import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.filters import CommandStart, Command

TOKEN = "BOT_TOKEN"

dp = Dispatcher()


@dp.message(CommandStart())
async def start(message: types.Message):
    await message.answer("Salom! Botga xush kelibsiz!")


@dp.message(Command("help"))
async def help_command(message: types.Message):
    await message.answer("Bu oddiy Telegram bot.")


@dp.message()
async def echo(message: types.Message):
    if message.text:
        await message.answer(message.text)


async def main():
    bot = Bot(token=TOKEN)
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
