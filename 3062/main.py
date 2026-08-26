"""price"""

def price():
    """price"""
    age = int(input())
    status = input().lower()

    if 0 <= age < 18 or status == "s":
        print("20")
    else:
        print("50")

price()
