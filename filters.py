from dataclasses import dataclass
from aiogram.filters import BaseFilter
from aiogram.types import Message


class IsAdmin(BaseFilter):
    admins_list: list[int] = []
    def __init__(self, admins_list):
        self.admins_list = admins_list
    async def __call__(self, message: Message):
        return message.from_user.id in self.admins_list