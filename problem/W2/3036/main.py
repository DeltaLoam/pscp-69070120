"""prasart"""
import math

def main():
    """Function"""
    n_room = int(input())

    if n_room == 1:
        r = 1
    else:
        r = math.isqrt(n_room - 1) + 1

    k = n_room - (r - 1) ** 2

    if k % 2 == 1:
        walls = 2 * (r - 1)
    else:
        walls = 2 * (r - 1) - 1

    print(walls)

main()
