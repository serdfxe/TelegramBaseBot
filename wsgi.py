from aiogram import executor

import logging

from bot import create_dp


logging.basicConfig(level=logging.INFO)

dp = create_dp()

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
