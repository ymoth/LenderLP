from vkbottle.user import Blueprint, Message
from vkbottle.rule import FromMe
from unit import edit_msg
user = Blueprint("calculator")
from prefixs import p, sticker
@user.on.message_handler(FromMe(),text=[p+'реши <cul1> + <cul2>', p+'реши <cul1>+<cul2>'],lower=True)
async def messages(ans: Message, cul1: int, cul2: int):
    await ans(f'{sticker}Решил быстро, ваш ответ:\n {int(cul1) + int(cul2)}.')


@user.on.message_handler(FromMe(),text=[p+'реши <cul1> - <cul2>', p+'реши <cul1>-<cul2>'],lower=True)
async def messages(ans: Message, cul1: int, cul2: int):
    await ans(f'{sticker}Решил быстро, ваш ответ:\n {int(cul1) - int(cul2)}.')


@user.on.message_handler(FromMe(),text=[p+'реши <cul1> * <cul2>',p+"реши <cul1>*<cul2>"],lower=True)
async def messages(ans: Message, cul1: int, cul2: int):
    await ans(f'{sticker}Решил быстро, ваш ответ:\n {int(cul1) * int(cul2)}.',reply_to=ans.conversation_message_id)

@user.on.message_handler(FromMe(),text=[p+'реши <cul1> / <cul2>',p+"реши <cul1>/<cul2>"],lower=True)
async def messages(ans: Message, cul1: int, cul2: int):
    await ans(f'{sticker}Решил быстро, ваш ответ:\n {int(cul1) / int(cul2)}.')


class Agents:
    Agent1 = '@id361838231(Никита Тиленин)'
    Agent2 = '@id438277254(Валерий Цурков)'
    Agent3 = '@id585779970(Slava Panyukov)'
    Agent4 = '@id485060903(Юрий Громов)'
    Agent5 = '@id()'
    Agent6 = '@id()'
    Agent7 = '@id()'
    Agent8 = '@id()'


from unit import __namelp__
@user.on.message_handler(FromMe(),text=[p+"помощь", p+"агенты"], lower=True)
async def help(ans: Message):

    a = await user.api.users.get(user_ids=ans.from_id, fields="online")
    u_name = a[0].first_name
    u_fam = a[0].last_name
    txt = f"""
📖 Посмотреть команды можно тут:
vk.com/@lenderlp-cmdlp
Администрация:
@id608732541(You)

Агенты ТП {__namelp__} LP:
1. {Agents.Agent1}
2. {Agents.Agent2}
3. {Agents.Agent3}
4. {Agents.Agent4}
5. Пусто
Пользователь LLP: @id{ans.from_id}({u_name} {u_fam})
"""
    await edit_msg(ans, txt)






