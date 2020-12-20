from vkbottle.user import Blueprint, Message
from vkbottle.rule import FromMe
from unit import edit_msg
user = Blueprint("calculator")
from prefixs import p
@user.on.message_handler(FromMe(),text=p+'реши <cul1> + <cul2>',lower=True)
async def messages(ans: Message, cul1: int, cul2: int):
    await edit_msg(ans,f'Решил быстро, ваш ответ:\n {int(cul1) + int(cul2)}.')


@user.on.message_handler(FromMe(),text=p+'реши <cul1> - <cul2>',lower=True)
async def messages(ans: Message, cul1: int, cul2: int):
    await edit_msg(ans,f'Решил быстро, ваш ответ:\n {int(cul1) - int(cul2)}.')


@user.on.message_handler(FromMe(),text=p+'реши <cul1> * <cul2>',lower=True)
async def messages(ans: Message, cul1: int, cul2: int):
    await edit_msg(ans,f'Решил быстро, ваш ответ:\n {int(cul1) * int(cul2)}.')








