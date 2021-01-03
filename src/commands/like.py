from vkbottle.user import Message, Blueprint
from vkbottle.rule import FromMe
from prefixs import p
from unit import edit_msg
from vkbottle import VKError
bp = Blueprint("LikesAdd")
from loguru import logger


@logger.catch()
@bp.on.message_handler(FromMe(),text=[p+"+лайк", p+"лайкнуть"])
async def function(ans: Message):
    try:
        user1 = await bp.api.users.get(user_ids=ans.reply_message.from_id, fields='photo_id')
        await bp.api.likes.add(type='photo', owner_id=ans.reply_message.from_id,
                                     item_id=user1[0].photo_id.replace(f"{ans.reply_message.from_id}_", ""))
        l = await bp.api.likes.get_list(type='photo', owner_id=ans.reply_message.from_id,
                                          item_id=user1[0].photo_id.replace(f"{ans.reply_message.from_id}_", ""),
                                          filter='likes', count=1000)
        like = l.count
        from prefixs import sticker
        u_name = user1[0].first_name
        text = f'{sticker} Лайк успешно поставлен!\nУ {u_name} стало лайков {like}'



        await edit_msg(ans, text)
    except VKError as ERR:
        error = f'Лайк не поставлен для {u_name}\nПричина: Пользователь с закрытым профилем.'
        await edit_msg(ans, error)


@bp.on.message_handler(FromMe(),text=[p+"-лайк", p+"убрать лайк"])
async def function(ans: Message):
    try:
        user1 = await bp.api.users.get(user_ids=ans.reply_message.from_id, fields='photo_id')
        like_add = await bp.api.likes.delete(type='photo', owner_id=ans.reply_message.from_id,
                                 item_id=user1[0].photo_id.replace(f"{ans.reply_message.from_id}_", ""))
        l = await bp.api.likes.get_list(type='photo', owner_id=ans.reply_message.from_id,
                                      item_id=user1[0].photo_id.replace(f"{ans.reply_message.from_id}_", ""),
                                      filter='likes', count=1000)
        like = l.count
        u_name = user1[0].first_name
        clos = user1[0].is_closed
        from prefixs import sticker
        await edit_msg(ans, f"{sticker} Лайк убран!\nУ {u_name} стало лайков: {like}")
    except VKError as ERR:
        from prefixs import error_sticker
        await edit_msg(ans, f"{error_sticker} Нет доступа. Профиль либо закрыт, либо я в ЧС.")


