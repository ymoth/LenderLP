from vkbottle.rule import FromMe
from vkbottle.user import Message, Blueprint
from unit import edit_msg, get_id_for_domain
from prefixs import error_sticker, p, sticker
import json, loguru
import prefixs as PREFIX
from unit import __author__, __version__, __namelp__

bp = Blueprint("Audio_Translate")


@loguru.logger.catch()
@bp.on.message_handler(FromMe(), text=p + "гс", lower=True)
async def VoiceTranslate(ans: Message):
    aud = ans.reply_message.attachments[0]["audio_message"]
    if aud["transcript"] == '':
        Transcript = "Пустой ответ. Сообщение не распозноно."
    else:
        Transcript = aud["transcript"]

    await ans(f"""
VoiceLLP 
{sticker}@id{ans.reply_message.from_id}(Пользователь) сказал в голосовое сообщение:
{Transcript}

""", reply_to=ans.reply_message.id)