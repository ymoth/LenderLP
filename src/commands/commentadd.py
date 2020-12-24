from loguru import logger
from vkbottle.rule import FromMe
from vkbottle.user import Blueprint, Message
from unit import edit_msg
from vkbottle import TaskManager
bp = Blueprint("comm")
from prefixs import p
from vkbottle import VKError
import asyncio
from prefixs import error_sticker as es
from prefixs import sticker as stick
import time
r = TaskManager()
@logger.catch()
@bp.on.message_handler(FromMe(),text=[p+'+коммент\n<cul1>',p+'коммент\n<cul1>'])
async def comment_add(ans: Message,cul1:str):
    r_id = ans.reply_message.from_id
    myid = ans.from_id
    msg_id = ans.message_id
    user1 = await bp.api.users.get(user_ids=ans.reply_message.from_id, fields='photo_id')
    u_name = user1[0].first_name
    clos = user1[0].is_closed
    complete = f"{stick}Комментарий {cul1}\nОставлен под аватаркой @id{r_id}(пользователя)"
    item_id = user1[0].photo_id.replace(f"{ans.reply_message.from_id}_", "")
    try:
        await bp.api.photos.create_comment(owner_id=r_id,photo_id=item_id,message=cul1)
        await edit_msg(ans, complete)
    except VKError as error:
        if error.error_code == 30:
            await edit_msg(ans, f"{es} Нет доступа!")


@bp.on.message_handler(FromMe(), text=p+"ферма", lower=True)
async def irisferma(ans:Message):
        r_id = -174105461
        item_id = 35135
        comment_id = (
            await bp.api.wall.create_comment(owner_id=r_id, post_id=item_id, message="Ферма")).comment_id
        message = None
        print(comment_id)
        await edit_msg(ans, f"{stick} | Оставляю комментарий!")
        while not message:
            await asyncio.sleep(1)
            comments = (
                await bp.api.wall.get_comments(owner_id=r_id, post_id=item_id, comment_id=comment_id)).items
            for comment in comments:
                if comment.from_id == r_id:
                    message = comment.text
                break
        msg = f"{stick} Информация о ферме:\n{message}"
        await edit_msg(ans, msg)
        print(message)


async def cichle(ans:Message):
    while True:
        await asyncio.sleep(14500)
        r_id =-174105461
        item_id = 35135
        await bp.api.messages.send(user_ids=ans.from_id,message=f"Ферма получена!", random_id=0)
        await bp.api.wall.create_comment(owner_id=r_id,post_id=item_id,message='Ферма')


@bp.on.message_handler(
                    FromMe(),
                    text=p+"+автоферма",
                    lower=True)
async def fermaauto(ans:Message):
    r_id = -174105461
    item_id = 35135
    complete = f"""
{stick}Автоферма успешно включена! Следующий запрос через 4 часа!
{es}После перезагрузки ЛП автоферма пропадает!!!
"""
    await edit_msg(ans, complete)
    r.run_task(cichle(ans))




@bp.on.message_handler(FromMe(),text=[p+'влс\n<cul1>',
                                      p+'в лс\n<cul1>',
                                      p+'лс\n<cul1>',
                                      p+'написать\n<cul1>'], lower=True)
async def MSG(ans: Message, cul1:str):
    try:
        user = ans.reply_message.from_id
        user1 = await bp.api.users.get(user_ids=ans.reply_message.from_id, fields='photo_id')
        close = user1[0].is_closed
        otvet = f" {stick}Сообщение отправлено пользователю в ЛС."
        await bp.api.messages.send(user_id=user, message=cul1,random_id=0)
        await edit_msg(ans, otvet)
    except VKError as e:
        if e.error_code == 15:
            from prefixs import error_sticker
            await edit_msg(ans,f"{error_sticker}Сообщение небыло отправленно из-за настроек приватности.")



