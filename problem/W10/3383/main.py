""" Difference """


def main():
    """Difference"""
    n = int(input())
    m = int(input())
    a = set()
    for _ in range(n):
        a.add(int(input()))
    b = set()
    for _ in range(m):
        b.add(int(input()))
    ans = sorted(a - b)
    print(*ans)


main()
