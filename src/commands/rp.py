from vkbottle.rule import FromMe
from prefixs import p
from unit import edit_msg
from vkbottle.user import Message, Blueprint

bp = Blueprint("RolePlay")

@bp.on.message_handler(FromMe(),text=[p+"выебать",p+'трахнуть'],lower=True)
async def RolePlays2(ans:Message):
    rid = ans.reply_message.from_id
    rs = await bp.api.users.get(user_ids=rid,fields='city')
    oneusername = ans.from_id
    twouser = rs[0].first_name
    twouserid = rs[0].id
    rpcommand = "легко выебал"
    command = f"👌🏻 | @id{oneusername}(Пользователь) {rpcommand} @id{twouserid}({twouser})"

    await edit_msg(ans, command)


@bp.on.message_handler(FromMe(), text=[p + "подарить айфон", p + 'подарок'], lower=True)
async def RolePlaysw(ans: Message):
    rid = ans.reply_message.from_id
    rs = await bp.api.users.get(user_ids=rid, fields='city')
    oneusername = ans.from_id
    twouser = rs[0].first_name
    twouserid = rs[0].id
    rpcommand = "подарил айфон"
    command = f"@id{oneusername}(Пользователь) {rpcommand} @id{twouserid}({twouser})"

    await edit_msg(ans, command)


@bp.on.message_handler(FromMe(), text=[p + "поцеловать", p + 'целуй'], lower=True)
async def RolePlayse(ans: Message):
    rid = ans.reply_message.from_id
    rs = await bp.api.users.get(user_ids=rid, fields='city')
    oneusername = ans.from_id
    twouser = rs[0].first_name
    twouserid = rs[0].id
    rpcommand = "поцеловал"
    command = f"😍 | @id{oneusername}(Пользователь) {rpcommand} @id{twouserid}({twouser})"

    await edit_msg(ans, command)
