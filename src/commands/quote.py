from PIL import Image, ImageFilter, ImageFont, ImageDraw
from vkbottle.user import Message, Blueprint
from vkbottle.rule import FromMe
from unit import edit_msg
from prefixs import p

bp = Blueprint("quote")


async def quote(name, family, text):
    img = Image.new("RGBA", (650, 350), "black")
    idraw = ImageDraw.Draw(img)
    font_ = ImageFont.truetype('arial.ttf', size=30)
    idraw.text((200, 5), text="Цитаты великих людей:", font=font_)
    idraw.text((0, 90), text=f"© {name} {family}", font=font_)
    idraw.text((200, 200), text=f"« {text} »", font=font_)
    return img


@bp.on.message_handler(FromMe(), text=p + "+цитата", lower=True)
async def loadquote(ans: Message):
    from vkbottle.api.uploader.photo import PhotoUploader
    username = (await bp.api.users.get(user_ids=ans.reply_message.from_id))[0].first_name
    userfam = (await bp.api.users.get(user_ids=ans.reply_message.from_id))[0].last_name
    quotetext = (await bp.api.messages.get_by_id(message_ids=ans.reply_message.id)).items[0].text
    image = await quote(name=username, family=userfam, text=quotetext)
    image.save("Result.png")

    photo_uploader = PhotoUploader(bp.api, generate_attachment_strings=True)
    await photo_uploader.upload_message_photo("src.Result.png")