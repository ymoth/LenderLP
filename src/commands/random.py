from vkbottle.rule import FromMe
from vkbottle.user import Blueprint,Message
from prefixs import p
import random
from unit import edit_msg
from loguru import logger
bp = Blueprint("RANDOM")


@bp.on.message_handler(FromMe(),text=[p+'рандом <cul1> или <cul2>',p+"выбери <cul1> или <cul2>"],lower=True)
async def Leand(ans:Message, cul1:str,cul2:str):
    spisok = [cul1, cul2]
    await ans(f'Хм, я выбираю: {spisok[random.randint(0,1)]}',reply_to=ans.id)


@bp.on.message_handler(text=[
        p+"вероятность того что <thing",
        p+"вероятность что <thing",
        p+"вероятность <thing>"
        ],lower=True)
async def probability(ans: Message, thing: str):
    await edit_msg(
        ans, f"Вероятность того, что {thing} равна {round(random.uniform(0.0, 1.0) * 100, 2)}%"
    )
@logger.catch()
@bp.on.chat_message(FromMe(),text=p+'кто <cul1>',lower=True)
async def RandomChat(ans:Message, cul1:str):
    chat = await bp.api.request("messages.getChat", {"chat_id":ans.chat_id})
    userschat = chat['users']
    randomid = random.choice(userschat)
    user = await bp.api.users.get(user_ids=randomid)
    msg = f"""
Ух-ты, {cul1} это у нас 
❗ | @id{user[0].id}({user[0].first_name} {user[0].last_name})
"""
    await edit_msg(ans,msg)
