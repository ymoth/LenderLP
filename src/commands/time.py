import time
from vkbottle.rule import FromMe
from vkbottle.user import Blueprint, Message
from unit import edit_msg
bp = Blueprint('time')
from prefixs import p
@bp.on.message_handler(FromMe(),text=[p+'тайм',p+"время"])
async def new_message(ans: Message):
    current_time = time.strftime("%H:%M,%S", time.localtime())
    text = f"⚙ Сейчас время: {current_time}"
    await edit_msg(ans,text)