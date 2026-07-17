"""money exchange"""

money = int(input())

money_10 = money // 10
money_5 = (money % 10) // 5
money_2 = (money % 10) % 5 // 2
money_1 = (money % 10) % 5 % 2

print(f"10 = {money_10}")
print(f"5 = {money_5}")
print(f"2 = {money_2}")
print(f"1 = {money_1}")
