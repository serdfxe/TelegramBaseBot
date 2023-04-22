from aiogram import Bot, Dispatcher, types

from aiogram.contrib.fsm_storage.memory import MemoryStorage


from .modules.setup import setup_modules

from .filters import init_filters

from .config import TOKEN


def create_dp():
    bot = Bot(token=TOKEN)

    storage = MemoryStorage()

    dp = Dispatcher(bot, storage=storage)

    dp.message_handlers.once = True 

    init_filters(dp)

    setup_modules(dp)

    return dp