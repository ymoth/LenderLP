from vkbottle.rule import FromMe
from vkbottle.user import Blueprint, Message
from prefixs import p, sticker, error_sticker
from unit import edit_msg
bp = Blueprint("IRISCM")

@bp.on.message_handler(FromMe(),text=[p+"передать <cul>", p+"дать <cul>"],lower=True)
async def peredacha(ans:Message,cul:str):
    d = await bp.api.users.get(user_ids=ans.reply_message.from_id, fields="domain")
    user = d[0].domain
    username = d[0].first_name
    userlastname = d[0].last_name
    await bp.api.messages.send(peer_id=-174105461, message=f"передать {cul} @{user}",random_id=0)
    text = f"🍬 @{user}({username} {userlastname}) получил {cul} ирисок "
    await edit_msg(ans, text)






