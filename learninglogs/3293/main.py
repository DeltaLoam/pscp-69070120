""" BigFrame """

def main():
    """BigFrame"""
    lines = [input().rstrip() for _ in range(5)]
    width = max(len(s) for s in lines)
    border = "*" * (width + 4)
    print(border)
    for s in lines:
        print("* " + s.ljust(width) + " *")
    print(border)

main()
