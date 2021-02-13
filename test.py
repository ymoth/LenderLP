import time as tm

t = tm

TimeInfo = [*t.localtime()]
if TimeInfo[1] == 1:
    TimeInfo[1] = ["Январь",1]
elif TimeInfo[1] == 2:
    TimeInfo[1] = ["Февраль",2]
elif TimeInfo[1] == 3:
    TimeInfo[1] = ["Март",3]
elif TimeInfo[1] == 4:
    TimeInfo[1] = ["Апрель",4]
elif TimeInfo[1] == 5:
    TimeInfo[1] = ["Май",5]
elif TimeInfo[1] == 6:
    TimeInfo[1] = ["Июнь",6]
elif TimeInfo[1] == 7:
    TimeInfo[1] = ["Июль",7]
elif TimeInfo[1] == 8:
    TimeInfo[1] = ["Август",8]
elif TimeInfo[1] == 9:
    TimeInfo[1] = ["Сентябрь",9]
elif TimeInfo[1] == 10:
    TimeInfo[1] = ["Октябрь",10]
elif TimeInfo[1] == 11:
    TimeInfo[1] = ["Ноябрь",11]
elif TimeInfo[1] == 12:
    TimeInfo[1] = ["Декабрь",12]

Text = f"""
Месяц: {TimeInfo[1][0]}, {TimeInfo[1][1]} месяц по счёту.
Полная дата: {TimeInfo[0]}.{TimeInfo[1][1]}.{TimeInfo[2]} Время: {TimeInfo[3]}.{TimeInfo[4]}.{TimeInfo[5]}
"""
