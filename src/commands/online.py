from vkbottle.user import Blueprint, Message
from prefixs import p
from vkbottle.rule import FromMe
bp = Blueprint("online")
from unit import edit_msg
from vkbottle import VKError

@bp.on.message_handler(FromMe(), text=[p+"+онлайн",p+"+онл"], lower=True)
async def onlineon(ans: Message):
    await edit_msg(ans, "✅ | Вечный онлайн успешно поставлен.")
    while True:
        await bp.api.account.set_online()



@bp.on.message_handler(FromMe(), text=[p+"+оффлайн",p+"+офл"], lower=True)
async def onlineoff(ans: Message):
    await edit_msg(ans, f"✅ | Вечный оффлайн успешно поставлен.")
    while True:
        await bp.api.account.set_offline()


@bp.on.message_handler(FromMe(),text=[p+"кик",p+'кикнуть'], lower=True)
async def kick(ans:Message):
    kickmember = await bp.api.messages.remove_chat_user(user_id=ans.reply_message.from_id,chat_id=ans.chat_id)
    if kickmember:
        await edit_msg(ans,f"Пользователь исключён из беседы.")
    else:
        await edit_msg(ans,f"Нет прав. Пользователь возможно не в беседе.")

