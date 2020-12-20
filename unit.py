from vkbottle import Message
from vkbottle.user import Blueprint

bp = Blueprint("editmsg")


async def edit_msg(
        ans: Message,
        text1: str, ) -> object:
    await bp.api.messages.edit(peer_id=ans.peer_id,message_id=ans.id,message=text1, keep_forward_messages=1)

__author__ = "yMoth"
__version__ = "1.0.3"
__namelp__ = "Lender"

