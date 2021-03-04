import json


def checker(json_name,method):
    with open(json_name+".json", encoding="utf-8") as E:
        r = json.load(E)
    return r[method]



async def adder(method: str, value, intent: int):
    with open("Settings.json", "r", encoding="utf-8") as d:
        data = json.load(d)
    data[method] = value
    with open("Settings.json", "w", encoding="utf-8") as d:
        d.write(json.dumps(data, indent=intent, ensure_ascii=False))


def Days():
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
    return TimeInfo


async def LD(id, ld_id):
    if id == ld_id:
        return True
    else:
        False



