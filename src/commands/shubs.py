import json
from vkbottle.rule import FromMe
from vkbottle.user import Blueprint, Message
from prefixs import p, error_sticker,sticker
from unit import edit_msg
bp = Blueprint("shubl")
from loguru import logger
import os
@logger.catch()

@bp.on.message_handler(FromMe(),
                       text=[p+"+шаб <nameshub>\n<text>",p+"+шаблон <shubname>\n<text>"], lower=True)
async def shubadd(ans:Message, nameshub:str, text:str):
    namejson = f"src/shubs/{nameshub}.json"
    with open(namejson, "w", encoding="utf-8") as i:
        json.dump(text, i, ensure_ascii=False)
    if namejson == nameshub:
        await edit_msg(ans,f"Шаблон уже есть в вашем списке")
    else:
        await edit_msg(ans, f'{sticker} Шаблон "{nameshub}" успешно создан.')


@bp.on.chat_message(FromMe(), text=[p+"шаб <nameshub>", p+"шаблон <nameshub>"],lower=True)
async def shubcheck(ans: Message, nameshub:str):
    try:
        namejson = f"src/shubs/{nameshub}.json"
        with open(namejson, encoding="utf-8") as shub:
            text = json.load(shub)
        await edit_msg(ans,text)
    except FileNotFoundError:
         await edit_msg(ans, f'{error_sticker}У вас нет шаблона под именем "{nameshub}"')


@bp.on.message_handler(FromMe(),text=[p+"-шаб <nameshub>",p+"-шаблон <nameshub>"],lower=True)
async def shabdelete(ans: Message, nameshub:str):
    try:
        namejson = f"src/shubs/{nameshub}.json"
        os.remove(namejson)
        await edit_msg(ans, f"{error_sticker}Шаблон {nameshub} успешно удалён.")
    except FileNotFoundError:
        await edit_msg(ans, f'{error_sticker}У вас нет шаблона под именем "{nameshub}"')


