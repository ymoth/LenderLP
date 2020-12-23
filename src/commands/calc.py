from vkbottle.user import Blueprint, Message
from vkbottle.rule import FromMe
from unit import edit_msg
user = Blueprint("calculator")
from prefixs import p, sticker
@user.on.chat_message(FromMe(),text=[p+'реши <cul1> + <cul2>', p+'реши <cul1>+<cul2>'],lower=True)
async def messages(ans: Message, cul1: int, cul2: int):
    await ans(f'{sticker}Решил быстро, ваш ответ:\n {int(cul1) + int(cul2)}.', reply_to=ans.conversation_message_id)


@user.on.chat_message(FromMe(),text=[p+'реши <cul1> - <cul2>', p+'реши <cul1>-<cul2>'],lower=True)
async def messages(ans: Message, cul1: int, cul2: int):
    await ans(f'{sticker}Решил быстро, ваш ответ:\n {int(cul1) - int(cul2)}.',reply_to=ans.conversation_message_id)


@user.on.chat_message(FromMe(),text=[p+'реши <cul1> * <cul2>',p+"реши <cul1>*<cul2>"],lower=True)
async def messages(ans: Message, cul1: int, cul2: int):
    await ans(f'{sticker}Решил быстро, ваш ответ:\n {int(cul1) * int(cul2)}.',reply_to=ans.conversation_message_id)

@user.on.chat_message(FromMe(),text=[p+'реши <cul1> / <cul2>',p+"реши <cul1>*<cul2>"],lower=True)
async def messages(ans: Message, cul1: int, cul2: int):
    await ans(f'{sticker}Решил быстро, ваш ответ:\n {int(cul1) / int(cul2)}.',reply_to=ans.conversation_message_id)


@user.on.message(FromMe(),text=[p+'реши <cul1> + <cul2>', p+'реши <cul1>+<cul2>'],lower=True)
async def messages(ans: Message, cul1: int, cul2: int):
    await ans(f'{sticker}Решил быстро, ваш ответ:\n {int(cul1) + int(cul2)}.', reply_to=ans.message_id)


@user.on.message(FromMe(),text=[p+'реши <cul1> - <cul2>', p+'реши <cul1>-<cul2>'],lower=True)
async def messages(ans: Message, cul1: int, cul2: int):
    await ans(f'{sticker}Решил быстро, ваш ответ:\n {int(cul1) - int(cul2)}.',reply_to=ans.message_id)


@user.on.message(FromMe(),text=[p+'реши <cul1> * <cul2>',p+"реши <cul1>*<cul2>"],lower=True)
async def messages(ans: Message, cul1: int, cul2: int):
    await ans(f'{sticker}Решил быстро, ваш ответ:\n {int(cul1) * int(cul2)}.',reply_to=ans.message_id)

@user.on.message(FromMe(),text=[p+'реши <cul1> * <cul2>',p+"реши <cul1>*<cul2>"],lower=True)
async def messages(ans: Message, cul1: int, cul2: int):
    await ans(f'{sticker}Решил быстро, ваш ответ:\n {int(cul1) / int(cul2)}.',reply_to=ans.message_id)





