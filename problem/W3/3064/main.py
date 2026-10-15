"""Birth Day"""
import datetime

year_1 = int(input())
month_1 = int(input())
day_1 = int(input())
year_2 = int(input())
month_2 = int(input())
day_2 = int(input())

date1 = datetime.date(year_1, month_1, day_1)
date2 = datetime.date(year_2, month_2, day_2)

difference = abs((date1 - date2).days)

if difference <= 7:
    print("0")
elif date1 < date2:
    print("1")
else:
    print("2")
