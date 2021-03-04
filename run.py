from vkbottle.user import User
from loguru import logger
from loguru import logger as lg
import re, json
from vkbottle.user import Message

with open("config.json", 'r',encoding="utf-8") as tok:
    data = json.load(tok)
    token = data['token']

if len(token) < 85:
    logger.catch()
    lglvl = lg.level("[TokensINFO]", no=38, color="<red>")
    lg.log("[TokensINFO]", "\nДля начала работы бота, введите ваш токен: ")
    token = input("")
    while not (re.sub('[^A-Za-z0-9]', '', token) == token and len(token) == 85):
        lg.log("[TokensINFO]", "\nНе похоже на токен, укажи правильный токен: ")
        token = input("")

    data['token'] = token
    with open("config.json", "w", encoding="utf-8") as token_:
        token_.write(json.dumps(data, indent=4))

user = User(data['token'], mobile=True)

from src.commands import dovs,settings, voicetranslate,iris, id, signals, time, like, calc, wiki, msgdel, addfriends, commentadd, info, random, online, commands, shubs, devup
import unit

from requests import get as rget
from unit import __version__, __author__, __namelp__

user.set_blueprints(dovs.bp,settings.bp,time.bp, unit.bp, like.bp,
                    calc.user, wiki.bp, msgdel.bp,
                    addfriends.bp, info.bp, commentadd.bp,
                    random.bp, online.bp, commands.bp, shubs.bp, signals.bp, id.bp, iris.bp, devup.bp, voicetranslate.bp)
# user_id = (rget(f'https://api.vk.com/method/users.get?&v=5.52&access_token={token}').json())['response'][0]['id']


async def start():
    from src.Filters.MiniBase import Days, adder, checker
    await adder("StartTime", value=f"{Days()[1][0]}: {Days()[1][1]}, {Days()[3]}:{Days()[4]}.{Days()[5]}", intent=1)

    if checker("config","VK_ME token") == "":
        with open("config.json", "r", encoding="utf-8") as d:
            data = json.load(d)
        data["VK_ME token"] = False
        with open("config.json", "w", encoding="utf-8") as d:
            d.write(json.dumps(data, indent=5, ensure_ascii=False))

    if checker("Settings", "AutoFerma") == False:
        pass
    else:
        import src.commands.commentadd
        await src.commands.commentadd.cichle(ans=Message)

    from unit import __author__, __version__, __namelp__
    from prefixs import p, stickerforstart
    text = f"""
Успешно запущен LLP.
{stickerforstart} Имя ЛП: {__namelp__}
📕 Версия LP: {__version__}
Агенты: {p} помощь
    """
    # await user.api.messages.send(peer_id=user_id, message=text, random_id=0)
    from loguru import logger as lg
    from prefixs import p, sticker
    from prefixs import stickerforstart, error_stickerforstart
    from unit import __version__, __author__

    red = lg.level("[LenderLP]", no=38, color="<yellow>")
    text = f"""
          -----------------
              {__namelp__} LP           
        → Запуск с параметрами:\n
        → Ваш префикс в LP: {p}
        → Ваши эмодзи: {stickerforstart}, {error_stickerforstart}
        → Версия лп: {__version__}
        ♔ Автор юзербота: {__author__}
        → Информация: нл
        → Информация получена, LP готово к запуску.
        PS убрано оповещение что LLP запущен.
          ------------------"""

    lg.log("[LenderLP]", text)
    ellow = lg.level("[LenderLР]", color="<yellow>", no=40)
    lg.log("[LenderLР]", "\nИдёт запуск бота!")


user.run_polling(on_startup=start)
