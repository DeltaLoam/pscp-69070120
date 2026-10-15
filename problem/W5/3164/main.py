"""pair"""

def pair():
    """pair"""
    num = int(input())
    list_num = []

    for _ in range(num):
        first = int(input())
        second = int(input())

        if first > second:
            list_num.append(first)
        else:
            list_num.append(second)

    if num == 1:
        print(list_num[0])
    else:
        print(f"{' + '.join(map(str, list_num))} = {sum(list_num)}")


pair()
