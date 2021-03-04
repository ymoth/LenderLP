from vkbottle.user import Message, Blueprint
from unit import get_id_for_domain, edit_msg
from loguru import logger
from vkbottle.rule import FromMe
import json
from prefixs import p, sticker, error_sticker
from src.Filters.MiniBase import checker

bp = Blueprint("Doverenost")

PovtoryalkaPrefix = checker("Settings", "povtoryalka_prefix")


@bp.on.message_handler(FromMe(), text=[p + "+дов <domain>", p + "в довы <domain>"], lower=True)
async def AddDov(ans: Message, domain):
    domain__ = domain.replace("@", "")
    id = get_id_for_domain(domain__)
    returned = {"user_id": id}
    with open(f"src//dovs//{id}.json", "w", encoding="utf-8") as E:
        json.dump(returned, E, ensure_ascii=False)

    await ans(f"{sticker}Успешно сохранен доверенный пользователь. ", reply_to=ans.id)


@bp.on.message_handler(FromMe(), text=[p + "+дов", p + "в довы"], lower=True)
async def AddDov(ans: Message):
    id = ans.reply_message.from_id
    returned = {"user_id": id}
    with open(f"src//dovs//{id}.json", "w", encoding="utf-8") as E:
        json.dump(returned, E, ensure_ascii=False)

    await ans(f"{sticker}Успешно сохранен доверенный пользователь. ", reply_to=ans.id)


@bp.on.message_handler(FromMe(), text=[p + "-дов <domain>"], lower=True)
async def DelDov(ans: Message,domain):
    domain__ = domain.replace("@", "")
    id = get_id_for_domain(domain__)
    import os
    os.remove(f"src//dovs//{id}.json")
    await ans(f"{sticker}Успешно удалён доверенный пользователь.",reply_to=ans.id)

@bp.on.message_handler(FromMe(), text=[p + "-дов"], lower=True)
async def DelDov(ans: Message):
    id = ans.reply_message.from_id
    import os
    os.remove(f"src//dovs//{id}.json")
    await ans(f"{sticker}Успешно удалён доверенный пользователь.",reply_to=ans.id)


@logger.catch()
@bp.on.message_handler(text=[PovtoryalkaPrefix + "напиши <text>"], lower=True)
async def Mean(ans: Message, text):
    try:
        user_id = ans.from_id
        with open(f"src//dovs//{user_id}.json") as E:
            ld_id = json.load(E)["user_id"]

        if user_id == int(ld_id):
            await ans(f"{text}")
    except FileNotFoundError:
        user_id = ans.from_id
        username = (await bp.api.users.get(user_ids=user_id))[0].first_name
        userfamuly = (await bp.api.users.get(user_ids=user_id))[0].last_name

        from loguru import logger as lg

        text = f'''
{username} {userfamuly} пытался вам дать сигнал на повторение с текстом "{text}"

Айди чата: {ans.chat_id}
Айди сообщения: {ans.id}
Айди пользователя: {ans.from_id}
'''
        lg.info(text)


@bp.on.message_handler(FromMe(), text=[p + "сменить повторялку на <new_prefix>"])
async def NewPrefix(ans: Message, new_prefix):
    from src.Filters.MiniBase import adder
    await adder("povtoryalka_prefix", value=new_prefix, intent=3)
    await ans(f'{error_sticker}Ваш префикс повторялки успешно изменён на "{new_prefix}". ', reply_to=ans.id)
