""" Right Arrow """

def main():
    """Right Arrow"""
    k = int(input())
    n = int(input())
    mid = n // 2
    for row in range(n):
        indent = mid - abs(row - mid)
        print(" " * indent + "*" * k)

main()
