"""coke"""

price = int(input())
pro_cap = int(input())
pro_price = int(input())
buy = int(input())

print(((buy // pro_cap) * pro_price) + ((buy - (buy // pro_cap)) * price))
