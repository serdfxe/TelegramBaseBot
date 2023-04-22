from aiogram import Bot, Dispatcher, types

from bot.models.user import User

from .. import Module


class StartModule(Module):
    async def start_cmd_handler(self, message: types.Message):
        try:
            if not User.get(id=message.from_user.id):
                User.new(id=message.from_user.id, username=message.from_user.username, first_name=message.from_user.first_name, last_name=message.from_user.last_name, role="user", banned=False)
        except Exception:
            await message.answer("Не удалось создать пользователя.")
        else:
            await message.answer("Привет!")


    def setup(self):
        self.dp.register_message_handler(self.start_cmd_handler, commands=["start"])


def setup_start_module(dp: Dispatcher):
    sm = StartModule(dp)
    sm.setup()
