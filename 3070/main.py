""""odd even"""

def think():
    """odd add"""
    num1 = int(input())
    num2 = int(input())
    num3 = int(input())

    num = [num1, num2, num3]

    even = 0
    odd = 0

    for i in num:
        if not i % 2:
            even += 1
        else:
            odd += 1

    print(even)
    print(odd)

think()
