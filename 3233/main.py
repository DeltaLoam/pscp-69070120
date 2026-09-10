"""lotto"""

def checker():
    """prize"""
    prize_str, prize_num = input().split()
    buy_str, buy_num = input().split()

    if buy_str == prize_str and buy_num == prize_num:
        money = 1000000
    elif buy_num == prize_num:
        money = 100000
    elif buy_str == prize_str and buy_num[-3:] == prize_num[-3:]:
        money = 2000
    elif buy_str == prize_str and buy_num[-2:] == prize_num[-2:]:
        money = 1000
    elif buy_num[-3:] == prize_num[-3:]:
        money = 200
    elif buy_num[-2:] == prize_num[-2:]:
        money = 100
    elif buy_str == prize_str:
        money = 20
    else:
        money = 0

    print(money)

checker()
