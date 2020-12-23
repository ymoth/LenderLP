from vkbottle import Message
from vkbottle.user import Blueprint
from prefixs import p
bp = Blueprint("editmsg")


async def edit_msg(
        ans: Message,
        text1: str, ) -> object:
    await bp.api.messages.edit(peer_id=ans.peer_id,message_id=ans.id,message=text1, keep_forward_messages=1)

__author__ = "yMoth"
__version__ = "1.0.6"
__namelp__ = "Lender"

__updates__ = f"Смена префиксов, стикеров, еррор стикеров.\n Команда {p}спам число [enter] текст спама"

class colors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


