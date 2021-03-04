import json
from vkbottle.rule import FromMe
from vkbottle.user import Blueprint, Message
from prefixs import p, error_sticker, sticker, stickerforstart,error_stickerforstart
from unit import edit_msg, get_user
from src.Filters import adder, checker, Days
bp = Blueprint("Settings")

@bp.on.message_handler(FromMe(),text="нл", lower=True)
async def SettingsInformation(ans:Message):
    y = "✅"
    n = "❌"
    import time as t
    TimeInfo = [*t.localtime()]
    if TimeInfo[1] == 1:
        TimeInfo[1] = ["Январь", 1]
    elif TimeInfo[1] == 2:
        TimeInfo[1] = ["Февраль", 2]
    elif TimeInfo[1] == 3:
        TimeInfo[1] = ["Март", 3]
    elif TimeInfo[1] == 4:
        TimeInfo[1] = ["Апрель", 4]
    elif TimeInfo[1] == 5:
        TimeInfo[1] = ["Май", 5]
    elif TimeInfo[1] == 6:
        TimeInfo[1] = ["Июнь", 6]
    elif TimeInfo[1] == 7:
        TimeInfo[1] = ["Июль", 7]
    elif TimeInfo[1] == 8:
        TimeInfo[1] = ["Август", 8]
    elif TimeInfo[1] == 9:
        TimeInfo[1] = ["Сентябрь", 9]
    elif TimeInfo[1] == 10:
        TimeInfo[1] = ["Октябрь", 10]
    elif TimeInfo[1] == 11:
        TimeInfo[1] = ["Ноябрь", 11]
    elif TimeInfo[1] == 12:
        TimeInfo[1] = ["Декабрь", 12]


    with open("Settings.json", encoding="utf-8") as Info:
        ResponseSettings = json.load(Info)

    UserRespone = await get_user(ans.from_id)

    if ResponseSettings["AutoFerma"] == True:
        AutoFerma = y + " Включена"
    else:
        AutoFerma = n + " Выключена"

    StartTime = ResponseSettings["StartTime"]
    if StartTime == '':
        StartTime = f"{error_sticker}Не указано"

    DevUp = ResponseSettings["DevUp"]
    if DevUp == False:
        DevUp = n
    else:
        DevUp = y

    VKME = ResponseSettings["VK_ME_TOKEN"]
    if VKME == False:
        VKME = n
    else:
        VKME = y

    import os, time
    path = "src//shubs//"
    path2 = "src//meroleplays//"
    path3 = "src//dovs//"
    RPCmd = int(len(os.listdir(path2)))
    SHB = int(len(os.listdir(path)))
    dovs = int(len(os.listdir(path3)))
    povtoryalka_prefix = checker("Settings", "povtoryalka_prefix")
    text = f"""
{sticker}Пользователь @id{ans.from_id}({UserRespone["user_name"]} {UserRespone["user_family"]})
Ваш стикер при ошибке: {error_stickerforstart}
Ваш стикер: {stickerforstart}
Ваш префикс: {p}
Ваш префикс повторялки: {povtoryalka_prefix}

Автоферма: {AutoFerma}
Запуск LLP состоялся: {StartTime}

Присутсвие Dev-Up ключа: {DevUp}
Присутсвие токена KateMobile: {y}
Присутсвие токена VK ME: {VKME}

Месяц: {TimeInfo[1][0]}: {TimeInfo[1][1]} по счёту.
Время: {TimeInfo[3]}:{TimeInfo[4]}.{TimeInfo[5]} 🕑
Полная дата: {TimeInfo[2]}.{TimeInfo[1][1]}.{TimeInfo[0]} 📅

Доверенных пользователей: {dovs}
Кол-во РП-Команд: {RPCmd+1}
Кол-во шаблонов: {SHB+1}

Ваш пинг: {round(time.time() - ans.date, 2)}
Обработка сообщения долгая из-за проверки JSON формата.
"""
    await ans(text, reply_to=ans.id)

