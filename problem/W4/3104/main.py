"""ticket"""

def price_cal():
    """price cal"""
    age, day = input().split()
    age = int(age)

    if age < 5:
        price = 0
    elif 5 <= age <= 18:
        price = 100
    else:
        price = 150

    if day == "Wed":
        print(int(price / 2))
    else:
        print(price)

price_cal()
