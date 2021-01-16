from PIL import Image, ImageFilter, ImageFont, ImageDraw
from vkbottle.user import Message, Blueprint
from vkbottle.rule import FromMe
from unit import edit_msg
from prefixs import p
import asyncio, loguru, os

bp = Blueprint("quote")


async def quote(name, family, text, photo_site):
    img = Image.new("RGBA", (650, 350), "black")
    idraw = ImageDraw.Draw(img)
    font_ = ImageFont.truetype('arial.ttf', size=30)
    idraw.text((200, 5), text="Цитаты великих людей:", font=font_)
    idraw.text((5, 50), text=f"© {name} {family}", font=font_)
    idraw.text((15, 150), text=f"« {text} »", font=ImageFont.truetype('arial.ttf', size=25))
    return img

import prefixs
@loguru.logger.catch()
@bp.on.message_handler(FromMe(), text=p + "+цитата", lower=True)
async def loadquote(ans: Message):
    from vkbottle.api.uploader.photo import PhotoUploader
    username = (await bp.api.users.get(user_ids=ans.reply_message.from_id))[0].first_name
    userfam = (await bp.api.users.get(user_ids=ans.reply_message.from_id))[0].last_name
    quotetext = (await bp.api.messages.get_by_id(message_ids=ans.reply_message.id)).items[0].text
    userphoto = (await bp.api.users.get(user_ids=ans.reply_message.from_id))[0].photo_50
    image = await quote(name=username, family=userfam, text=quotetext, photo_site=userphoto)
    image.save("Result.png")
    photo_uploader = PhotoUploader(bp.api, generate_attachment_strings=True)
    photo_id = await photo_uploader.upload_message_photo("Result.png")
    await bp.api.messages.edit(message_id=ans.id, attachment=photo_id, peer_id=ans.peer_id)
    os.remove("Result.png")
    await ans(f"{prefixs.sticker}Цитата готова.", reply_to=ans.id)
