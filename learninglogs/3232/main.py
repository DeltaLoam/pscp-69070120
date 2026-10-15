"""frog"""

def jump():
    """jumper"""
    boost, goal = map(int, input().split())

    total = 0
    count = 0

    while boost > 0:
        total += boost
        count += 1

        if total >= goal:
            print(count)
            return

        boost -= 2

    print(-1)

jump()
