"""multiply"""

def multipler():
    """multi"""
    num = str(input())
    num_list = []
    total = 1

    for i in num:
        if i != "0":
            num_list.append(int(i))

    if not num_list:
        print(0)
        return

    for i in num_list:
        total *= i

    print(total)

multipler()
