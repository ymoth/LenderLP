from vkbottle.rule import FromMe
from vkbottle.user import Blueprint, Message
from unit import edit_msg

bp = Blueprint("addfriends")
from prefixs import p
from loguru import logger
from vkbottle import VKError
from prefixs import sticker, error_sticker


@logger.catch()
@bp.on.message_handler(FromMe(), text=[p + 'вдр', p + '+др', p + '+друзья'])
async def friend_add(ans: Message):
    try:
        RESPONSE = await bp.api.request("friends.add", {"user_id": ans.reply_message.from_id})
        if RESPONSE == 1:
            await edit_msg(ans, f"{sticker}Заявка в друзья отправлена @id{ans.reply_message.from_id}(пользователю)")
        elif RESPONSE == 2:
            await edit_msg(ans, f"{sticker}@id{ans.reply_message.from_id}(Пользователь) добавлен в друзья!")
    except VKError as e:
        if e.error_code == 175:
            await edit_msg(ans,
                           f"{error_sticker}Невозможно добавить в друзья @id{ans.reply_message.from_id}(пользователя), который занес Вас в свой черный список.")
        elif e.error_code == 176:
            await edit_msg(ans,
                           f"{error_sticker}Невозможно добавить в друзья @id{ans.reply_message.from_id}(пользователя), который занесен в Ваш черный список.")

@bp.on.message_handler(FromMe(), text=[p + 'вдр <domain>', p + '+др <domain>', p + '+друзья <domain>'])
async def friend_add(ans: Message, domain):
    try:
        from unit import get_id_for_domain
        domain = domain.replace("@", "")
        id = get_id_for_domain(domain_=domain)
        RESPONSE = await bp.api.request("friends.add", {"user_id": id})
        if RESPONSE == 1:
            await edit_msg(ans, f"{sticker}Заявка в друзья отправлена @id{id}(пользователю)")
        elif RESPONSE == 2:
            await edit_msg(ans, f"{sticker}@id{id}(Пользователь) добавлен в друзья!")
    except VKError as e:
        if e.error_code == 175:
            await edit_msg(ans,
                           f"{error_sticker}Невозможно добавить в друзья @id{id}(пользователя), который занес Вас в свой черный список.")
        elif e.error_code == 176:
            await edit_msg(ans,
                           f"{error_sticker}Невозможно добавить в друзья @id{id}(пользователя), который занесен в Ваш черный список.")


@bp.on.message_handler(FromMe(), text=[p + 'издр', p + '-др', p + '-друзья'])
async def friend_del(ans: Message):
    await bp.api.friends.delete(user_id=ans.reply_message.from_id)
    message = f'{sticker}@id{ans.reply_message.from_id} (Пользователь) успешно удалён из друзей.'
    await edit_msg(ans, message)

@bp.on.message_handler(FromMe(), text=[p + 'издр <domain>', p + '-др <domain>', p + '-друзья <domain>'])
async def friend_del(ans: Message, domain):
    from unit import get_id_for_domain
    domain__ = domain.replace("@", "")
    id = get_id_for_domain(domain__)
    await bp.api.friends.delete(user_id=id)
    message = f'{sticker}@id{id} (Пользователь) успешно удалён из друзей.'
    await edit_msg(ans, message)





@bp.on.message_handler(FromMe(), text=[p + "+чс", p + "вчс"], lower=True)
async def blacklistadd(ans: Message):
    me = await bp.api.account.ban(owner_id=ans.reply_message.from_id)
    try:
        if me == 1:
            await edit_msg(ans, f"{sticker} @id{ans.reply_message.from_idв}(Пользователь) успешно добавлен в ЧС.")

    except VKError as err:
        if err.error_code == 15:
            await edit_msg(ans, f"{error_sticker} Ошибка! Пользователь уже в чс.")


@bp.on.message_handler(FromMe(), text=[p + "+чс <domain>", p + "вчс <domain>"], lower=True)
async def blacklistadd(ans: Message, domain):
    from unit import get_id_for_domain
    domain = domain.replace("@", "")
    id = get_id_for_domain(domain)
    me = await bp.api.account.ban(owner_id=id)
    try:
        if me == 1:
            await edit_msg(ans, f"{sticker} @id{id}(Пользователь) успешно добавлен в ЧС.")

    except VKError as err:
        if err.error_code == 15:
            await edit_msg(ans, f"{error_sticker} Ошибка! Пользователь уже в чс.")


@bp.on.message_handler(FromMe(), text=[p + "-чс", p + "изчс"], lower=True)
async def blacklistdl(ans: Message):
    me = await bp.api.account.unban(owner_id=ans.reply_message.from_id)
    if me == 1:
        await edit_msg(ans, f"{sticker} @id{ans.reply_message.from_id}(Пользователь) успешно удалён с ЧС.")
    else:
        await edit_msg(ans, f"Ошибка! Пользователь уже разблокирован из чс.")


@bp.on.message_handler(FromMe(), text=[p + "повтори", p + "повтор", p + "повторить"])
async def povtorichat(ans: Message):
    text_id = ans.reply_message.id
    a = await bp.api.messages.get_by_id(message_ids=text_id)
    text = a.items[0].text
    await edit_msg(ans, text)


@bp.on.message_handler(FromMe(), text=[p + "п", p + "пинг", p + "пг"], lower=True)
async def proverka(ans: Message):
    try:
        from prefixs import sticker as STICKERLP
        import time
        ping = round(time.time() - ans.date, 2)
        obrabotka = 0, 1

        if ping < 0:
            ping = 0.0
        text = f"""
PING LLP:
{sticker}Ваш пинг равен: {ping}
Обработка заняла: {obrabotka}"""
        if ping > 5:
            text = f"""
PING LLP:
{sticker}Ваш пинг равен: {ping}
Обработка заняла: {obrabotka}
{error_sticker}У вас высокий пинг!"""
        await ans(text,reply_to=ans.id)
    except UnboundLocalError:
        await ans(f"{error_sticker} Не дам пинг! Попробуй запрос ещё раз.", reply_to=ans.id)

