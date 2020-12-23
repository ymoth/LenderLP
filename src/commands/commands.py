from vkbottle.rule import FromMe
from vkbottle.user import Blueprint, Message
bp = Blueprint("COMMANDS")
from prefixs import p
from unit import edit_msg
@bp.on.message_handler(FromMe(), text=[p+'команды', p+'кмд'], lower=True)
async def cms(ans:Message):
    from unit import __updates__
    text = f"""
Команды можно узнать тут:
vk.com/@lenderlp-cmdlp
Обновления:
-{__updates__}
"""
    await edit_msg(ans, text)

@bp.on.message_handler(FromMe(), text=[p+'обновления', p+'обновы'], lower=True)
async def update(ans:Message):
    from unit import __updates__
    txt = f"""
Обновление:
{__updates__}"""
    await edit_msg(ans, txt)