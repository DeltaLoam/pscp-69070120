"""555"""

def five():
    """555"""
    num = int(input())

    for i in range(1, num+1):
        if not i % 5:
            print("X", end="")
        else:
            print("*", end="")

five()
