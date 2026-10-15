"""luknam"""

def luknam():
    """luk nam"""
    num = str(input())
    number = ""

    for i, digit in enumerate(num):
        if i > 0 and not (len(num) - i) % 3:
            number += ","
        number += digit

    print(number)

luknam()
