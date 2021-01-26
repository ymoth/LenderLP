from vkbottle import Message
from vkbottle.user import Blueprint
from prefixs import p

bp = Blueprint("editmsg")


async def edit_msg(
        ans: Message,
        text1: str, ) -> object:
    await bp.api.messages.edit(peer_id=ans.peer_id, message_id=ans.id, message=text1, keep_forward_messages=1)

async def get_user(user_id):
    username = (await bp.api.users.get(user_ids=user_id))[0].first_name
    userfamuly = (await bp.api.users.get(user_ids=user_id))[0].last_name

    Info = {
        "user_name" : f"{username}",
        "user_family" : f"{userfamuly}"
    }
    return Info

__author__ = "yMoth"
__version__ = "1.0.8"
__namelp__ = "Lender"

__updates__ = f"Добавлена команда {p}пин/закреп, анпин."


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


def randomizer(a_, b_):
    import random
    try:
        a_ == int
        b_ == int
        return random.uniform(a_, b_)
    except ValueError:
        return f"{ValueError}"





