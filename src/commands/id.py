from vkbottle.user import Blueprint, Message
from prefixs import p
from vkbottle.rule import FromMe
from unit import edit_msg

bp = Blueprint('IDS')


@bp.on.message_handler(FromMe(), text=[p + "ид", p + 'айди', p + 'айдишник'], lower=True)
async def r_info(ans: Message):
    RESPONE = await bp.api.users.get(user_ids=ans.reply_message.from_id, fields='photo_id')
    u_name = RESPONE[0].first_name
    ID = ans.reply_message.from_id
    text = f'Айди пользователя @id{ID} ({u_name}): \n💤 {ID}'
    await edit_msg(ans, text)


@bp.on.message_handler(FromMe(), text=[p + "дд <cul>"])
async def dellmsg(ans: Message):
    History = await bp.api.request("messages.getHistory", {"peer_id": ans.peer_id,
                                                           "offset": 15,
                                                           "count": 200})
    if History["items"][0]["from_id"] == ans.from_id:
        await bp.api.messages.delete(message_ids=ans.message_id)
    else:
        await ans("net")


