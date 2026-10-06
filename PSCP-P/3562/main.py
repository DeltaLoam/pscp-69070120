"""str count"""

def count():
    """counter"""
    message = input()
    upper = 0
    lower = 0
    number = 0

    for i in message:
        if i.isupper():
            upper += 1
        elif i.islower():
            lower += 1
        elif i.isdigit():
            number += 1

    print(f"{upper} {lower} {number}")

count()
