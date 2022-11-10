import math


def season(month):
    if month in (1, 2, 12):
        return "Зима"
    elif month in (3, 4, 5):
        return "Весна"
    elif month in (6, 7, 8):
        return "Лето"
    elif month in (6, 7, 8):
        return "Лето"
    else:
        return 'Нет такого месяца'


s = season(3)
print(s)