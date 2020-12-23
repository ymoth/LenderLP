from vkbottle.rule import FromMe
from vkbottle.user import Message, Blueprint
from unit import edit_msg
from prefixs import error_sticker,p,sticker
import json
import prefixs as PREFIX
from unit import __author__,__version__,__namelp__
bp = Blueprint("Signals")


@bp.on.message_handler(FromMe(),
                       text=[p+"нрп",p+"новое рп"],lower=True
                       )
async def myrptext(ans:Message):
    text = f"""Что-бы создать свою РП-Команду, пишите так:
{p}+нрп (название рп)
Смайлик действие

Пример:
{p}+нрп ударить
👊 ударил(а)"""
    await edit_msg(ans, text)


@bp.on.message_handler(FromMe(),
                       text=[p+"+нрп <namerp>\n<sticker> <value>",p+"новое рп <namerp>\n<sticker> <value>"],lower=True
                       )
async def rpadd(ans:Message, namerp:str, sticker:str, value:str):
    namejson = f"src/meroleplays/{namerp}.json"

    text = {"namerp": namerp,
            "sticker": sticker,
            "value": value}

    with open(namejson, "w", encoding="utf-8") as i:
        json.dump(dict(text), i, ensure_ascii=False)

    complete = f'{PREFIX.sticker} Успешно создана RP-Команда "{namerp}"'
    await edit_msg(ans, complete)



@bp.on.message_handler(FromMe(),text=[p+"помощь", p+"агенты"], lower=True)
async def help(ans: Message):

    a = await bp.api.users.get(user_ids=ans.from_id, fields="online")
    u_name = a[0].first_name
    u_fam = a[0].last_name
    txt = f"""
📖 Посмотреть команды можно тут:
vk.com/@lenderlp-cmdlp
Администрация:
@id608732541 (You)

Агенты ТП LednerLP:
1.@id485060903 (Александр Юшманов)
2.@id361838231 (Никита Тилетин)
3.@id538274893 (Ян)

Пользователь LLP: @id{ans.from_id}({u_name} {u_fam})
"""
    await edit_msg(ans, txt)


@bp.on.message_handler(FromMe(),text=p+"рп <namerp>", lower=True)
async def RolePlay(ans:Message, namerp:str):
    try:
        namejson = f"src/meroleplays/{namerp}.json"
        with open(namejson, encoding="utf-8") as RP:
            text = json.load(RP)
        sticker, value = text["sticker"], text["value"]
        respone = await bp.api.users.get(user_ids=ans.from_id)
        respone2 = await bp.api.users.get(user_ids=ans.reply_message.from_id)
        from_user, user, from_user_id, user_id = respone[0].first_name, respone2[0].first_name, respone[0].id, respone2[0].id
        textlower = f"{sticker} | @id{from_user_id} ({from_user}) {value} @id{user_id}({user})"
        await edit_msg(ans, textlower)
    except FileNotFoundError:
        await edit_msg(ans, f"{error_sticker}У Вас нету РП-Команды {namerp}")

@bp.on.message_handler(FromMe(),text=[p+"-нрп <namerp>",p+"-рп <namerp>"],lower=True)
async def shabdelete(ans: Message, namerp:str):
    try:
        import os
        namejson = f"src/meroleplays/{namerp}.json"
        os.remove(namejson)
        await edit_msg(ans, f'{sticker}РП-Команда "{namerp}" успешно удалёна.')
    except:
        await edit_msg(ans, f"{error_sticker}У Вас нету РП-Команды {namerp}")

@bp.on.message_handler(FromMe(),text=[p+"инфолп", p+"лп инфо"],lower=True)
async def shabdelete(ans: Message):
    y = "✅"
    n = "❌"
    from prefixs import stickerforstart, error_stickerforstart
    a= await bp.api.users.get(user_ids=ans.from_id)
    username = a[0].first_name
    lastname = a[0].last_name
    text = f"""
📘 {__namelp__} LP
📕 Версия LP: {__version__}
📙 Автор: {__author__}

Присутсвие токенов: {y}
Ваш стикер: {stickerforstart}
Ваш стикер при ошибке" {error_stickerforstart}
Ваш префикс: {p}
Пользователь: @id{ans.from_id}({username} {lastname})
"""
    return await edit_msg(ans, text)

@bp.on.message_handler(FromMe(), text=[p+"конв",p+"перевод"], lower=True)
async def perevod(ans: Message):
    rus = "ё!\"№;%:?йцукенгшщзхъфывапролджэячсмитьбю.ЙЦУКЕНГШЩЗХЪФЫВАПРОЛДЖЭ/ЯЧСМИТЬБЮ,"
    eng = "~!@#$%^&qwertyuiop[]asdfghjkl;'zxcvbnm,./QWERTYUIOP{}ASDFGHJKL:\"|ZXCVBNM<>?"
    message_id = ans.reply_message.id
    dadadadada = await bp.api.messages.get_by_id(message_ids=message_id)
    message = dadadadada.items[0].text
    msg = message.translate(message.maketrans(eng, rus))
    await edit_msg(ans, msg)

from loguru import logger
@logger.catch()
@bp.on.chat_message(FromMe(),text=[p+"чат инфо", p+"инфо о чате"])
async def chatinfo(ans:Message):
    CHATRESPONE = await bp.api.request('messages.getChat', {'chat_id': ans.chat_id})
    namechat = CHATRESPONE['title']
    adminchat = CHATRESPONE['admin_id']
    RESPONE = await bp.api.users.get(user_ids=adminchat)
    name, fam = RESPONE[0].first_name, RESPONE[0].last_name
    memberscul = CHATRESPONE['members_count']
    chat_id = CHATRESPONE['id']
    photo = CHATRESPONE['photo_50']
    if not photo:
        photo = "Не установлена фотография"

    message = f"""
{sticker}Информация о чате:
Название беседы: {namechat}
Администратор беседы: @id{adminchat}({name} {fam}) 
Количество участников: {memberscul}
Мой айди чата: {chat_id}

Аватарка чата: {photo}"""

    await edit_msg(ans, message)

import asyncio
@logger.catch()
@bp.on.message_handler(FromMe(), text=[p+"спам <cul>\n<txt>", p+"+спам <cul>\n<txt>"], lower=True)
async def spam(ans:Message, cul:str, txt:str):
    net = int(cul)
    print(type(net))
    for i in range(net):
        await asyncio.sleep(0.5)
        await ans(txt)


