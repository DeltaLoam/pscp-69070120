"""summer"""

def summer():
    """morty"""
    much = int(input())
    sums = 0

    while True:
        num = int(input())

        if num == -1:
            break

        sums += num

        if sums == much:
            break

    print(sums)

summer()
