from vkbottle.user import User
import json
import json
with open('config.json', encoding="utf-8") as RP:
    tokenss = json.load(RP)
tokens = tokenss['tokens']
token1 = tokenss['tokens'][0]

user = User(tokens=tokens, mobile=True)


from src.commands import iris,id,signals,time, like, calc,wiki,msgdel,addfriends,commentadd,info,random,online,commands,shubs
import unit
from requests import get as rget
from unit import __version__, __author__, __namelp__
user.set_blueprints(time.bp,unit.bp,like.bp,
calc.user,wiki.bp,msgdel.bp,
addfriends.bp,info.bp,commentadd.bp,
random.bp,online.bp,commands.bp,shubs.bp,signals.bp, id.bp,iris.bp)
user_id = (rget(f'https://api.vk.com/method/users.get?&v=5.52&access_token={token1}').json())['response'][0]['id']
async def start():
    text = f"""
📘 {__namelp__} LP запущен.
📕 Версия LP: {__version__}
📙 Автор: {__author__}
    """
    await user.api.messages.send(peer_id=user_id, message=text, random_id=0)

user.run_polling(on_startup=start)

