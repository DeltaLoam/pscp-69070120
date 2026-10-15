"""aeiou"""

def squid():
    """aeiou count for loop"""
    amount = int(input())
    count = 0

    for _ in range(amount):
        char = input()
        if char in "AEIOU":
            count += 1
    print(count)

squid()
