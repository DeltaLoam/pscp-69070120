"""point"""

def points():
    """game"""
    base = int(input())
    bonus = int(input())
    days = int(input())
    multiplier = 1

    if days > 3:
        multiplier = 1.5

    sum_points = int((base + bonus) * multiplier)

    if sum_points >= 1500:
        rank = 5
    elif sum_points >= 1000:
        rank = 4
    elif sum_points >= 500:
        rank = 3
    elif sum_points >= 200:
        rank = 2
    else:
        rank = 1

    if rank == 5 and days >= 7:
        badge = 99
    elif rank == 4 and bonus > 300:
        badge = 88
    else:
        badge = 0

    print(sum_points)
    print(rank)
    print(badge)

points()
