"""BrickBridge"""

def build():
    """building"""
    small_bricks = int(input())
    big_bricks = int(input())
    goal_length = int(input())

    big_used = min(big_bricks, goal_length // 5)
    remain_length = goal_length - big_used * 5

    if remain_length <= small_bricks:
        print(remain_length)
    else:
        print(-1)

build()
