"""power of 2"""

def power():
    """powerer"""
    num = int(input())
    number = int(0)

    for i in range(num + 1):
        number += i ** 2
    print(number)

power()
