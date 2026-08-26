""""range mod"""

def modder():
    """moddest"""
    start = int(input())
    end = int(input())
    div = int(input())
    mod = int(input())
    count = 0

    for i in range(start, end + 1):
        if i % div == mod:
            count += 1

    print(count)

modder()
