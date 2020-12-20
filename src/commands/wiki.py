import wikipedia #Модуль Википедии
wikipedia.set_lang("RU")
from vkbottle.rule import FromMe
from vkbottle.user import Message, Blueprint
bp = Blueprint("Wikipedia")
from prefixs import p
from unit import edit_msg


@bp.on.message_handler(FromMe(),text=[p+'вики <cul1>',p+'вики'],lower=True)
async def wiki(ans:Message, cul1:str):
    try:
        from prefixs import sticker
        msg = f'{sticker}Вот что я нашёл по запросу "{cul1}":\n{wikipedia.summary(cul1)}'
        await edit_msg(ans,msg)
    except wikipedia.PageError:
        from prefixs import error_sticker
        await edit_msg(ans, f'{error_sticker} Запрос "{cul1}" не найден.')
