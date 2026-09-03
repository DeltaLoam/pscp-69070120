"""stock"""

def stock():
    """stocking"""
    alls = int(input())
    sums = 0
    even = 0
    odd = 0

    for _ in range(alls):
        num = int(input())

        sums += num
        if not num % 2:
            even += 1
        else:
            odd += 1

    print(f"SUM {sums}")
    print(f"EVEN {even}")
    print(f"ODD {odd}")

stock()
