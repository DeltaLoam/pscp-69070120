"""price"""
price = int(input())

if price * 0.10 <= 50:
    print(f"{(((price + 50) * 0.07) + (price + 50)):.2f}")
elif 50 < price * 0.10 <= 1000:
    print(f"{((price + price * 0.10) * 0.07) + (price + price * 0.10):.2f}")
elif price * 0.10 > 1000:
    print(f"{(((price + 1000) * 0.07) + (price + 1000)):.2f}")
