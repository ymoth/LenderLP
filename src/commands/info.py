from vkbottle.rule import FromMe
from vkbottle.user import Blueprint, Message
from unit import edit_msg
from vkbottle import VKError
bp = Blueprint('info')
from prefixs import p


@bp.on.message_handler(FromMe(),text=[p+"инфо",p+"информация"])
async def info(ans: Message):
    uid = ans.reply_message.from_id
    give = (await bp.api.users.get(user_ids=uid, fields='photo_id, bdate, status,domain,followers_count,domain'))[0]
    l = await bp.api.likes.get_list(type='photo', owner_id=ans.reply_message.from_id,
                                      item_id=give.photo_id.replace(f"{ans.reply_message.from_id}_", ""),
                                      filter='likes', count=1000)
    likes = l.count
    item_id = give.photo_id.replace(f"{ans.reply_message.from_id}_", "")
    user_id = give.id
    status = give.status
    if status == "":
        status = "Не указан"
    bdate = give.bdate
    if not bdate:
        bdate = "Дата рождения скрыта."
    name = give.first_name
    familya = give.last_name
    podpis = give.followers_count
    close = give.is_closed
    domain = give.domain

    sms = f"""
Информация ВК:

ID: {user_id}
ID Аватарки: {item_id}
Имя: {name}\nФамилия: {familya}
Статус пользователя: {status}
Дата рождения: {bdate}
Число подписчиков: {podpis}
Число лайков: {likes}
Короткая ссылка: vk.com/{domain} | @{domain}
Закрыт ли профиль: {close}
В ЧС ли он: Нет

Информация оконченна.
Фото профиля:"""
    try:
        await bp.api.messages.edit(peer_id=ans.peer_id,
                               message_id=ans.id,
                               message=sms,
                               attachment='photo' + str(user_id) + "_" + str(item_id),keep_forward_messages=1)
    except VKError as err:
        if err.error_code == 15:
            from prefixs import error_sticker
            await edit_msg(ans, f"{error_sticker} Нет доступа, возможные причины:\n Закрыт профиль, я В ЧС.")

