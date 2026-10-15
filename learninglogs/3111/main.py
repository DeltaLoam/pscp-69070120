"""school"""
from decimal import Decimal, ROUND_HALF_UP

def discount():
    """cal"""
    member = input()
    glocer = []
    for _ in range(int(input())):
        price = Decimal(input())
        glocer.append(price)

    total = sum(glocer)
    if member == "Y":
        last = total * Decimal("0.95")
    elif total >= 500:
        last = total * Decimal("0.97")
    else:
        last = total

    last = last.quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)
    print(last)

discount()
