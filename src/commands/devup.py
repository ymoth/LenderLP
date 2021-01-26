from vkbottle.rule import FromMe
from vkbottle.user import Message, Blueprint
from unit import edit_msg
from prefixs import error_sticker, p, sticker
import json
import prefixs as PREFIX
from unit import __author__, __version__, __namelp__

bp = Blueprint("dev_up")


async def dev_up_check():
    with open("dev_up.json", encoding="utf-8") as Dev_Up:
        token_dvup = json.load(Dev_Up)

    if len(token_dvup) > 33:
        return False
    else:
        return True


@bp.on.message_handler(FromMe(), text=[p + "подключить dev up <dev_up_token>", p + "подключить дев ап <dev_up_token>"],
                       lower=True)
async def dev_up_add(ans: Message, dev_up_token: str):
    if len(dev_up_token) > 100:
        await edit_msg(ans, f"{error_sticker}Указан неверный токен DEV-UP\nУкажите правильный токен.")
    else:
        data = {
            "dev_up_token": f"{dev_up_token}"
        }
        with open("dev_up.json", "w", encoding="utf-8") as token_:
            token_.write(json.dumps(data, indent=1))
        await edit_msg(ans, f"{sticker}Успешно сохранен токен DEV-UP")


@bp.on.message_handler(FromMe(), text=[p + "стикеры", p + "паки"], lower=True)
async def get_stickers(ans: Message):
    import dev_up, unit
    if await dev_up_check() == True:
        def stickers_get():
            with open("dev_up.json", encoding="utf-8") as Dev_Up:
                token_dvup = json.load(Dev_Up)["dev_up_token"]
            DevApi = dev_up.DevUpAPI(token=token_dvup)
            Response = dict(DevApi.vk.get_stickers(user_id=ans.reply_message.from_id).response.stickers)
            Stickers_count = Response["count"]
            Stickers_Info = Response["packs_name"]
            StickerInformation = {
                "count": f"{Stickers_count}",
                "stickers": f"{Stickers_Info}",
            }
            return StickerInformation

        count = stickers_get()["count"]
        func_stick = stickers_get()["stickers"][1:-1]
        Info = await unit.get_user(ans.reply_message.from_id)

        user_name = Info["user_name"]
        user_fam = Info["user_family"]
        if count == 0:
            text = f"{error_sticker}@id{ans.reply_message.from_id} ({user_name} {user_fam}) не имеет стикерпаков."
        text = f"""
{sticker}Пользователь @id{ans.reply_message.from_id}({user_name} {user_fam}) имеет {count} стикеров.

{func_stick.replace("'", "")}
"""
        await ans(text, reply_to=ans.id)
