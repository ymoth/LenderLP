from vkbottle.user import Blueprint, Message
from prefixs import p
from vkbottle.rule import FromMe
from unit import edit_msg
bp = Blueprint("DATA")
from tortoise import fields, run_async, Tortoise
from tortoise.models import Model
from loguru import logger

class Event(Model):
    id = fields.IntField(pk=True)
    name = fields.TextField()
    datetime = fields.DatetimeField(null=True)

    class Meta:
        table = "event"

    def __str__(self):
        return self.name

@logger.catch()
@bp.on.message_handler(FromMe(),text=p+"+бд", lower=True)
async def addusertobase():

        await Tortoise.init(db_url="sqlte://DataBase.db", modules={"models": ["__main__"]})
        await Tortoise.generate_schemas()
        a = event = await Event.create(name="Test")
        await Event.filter(id=event.id).update(name="Updated name")
        await Event(name="Test 2").save()
        print(a)
        run_async(addusertobase())