from abc import ABC, abstractclassmethod

from aiogram import Bot, Dispatcher, types



class Module(ABC):
    def __init__(self, dp: Dispatcher):
        self.dp: Dispatcher = dp
        self.bot: Bot = dp.bot


    @abstractclassmethod
    def setup(dp: Dispatcher):
        ...
