"""stats"""

def stat():
    """statistic calculation"""
    amount = int(input())
    max_num = float("-inf")
    min_num = float("inf")
    sum_num = 0
    for _ in range(amount):
        num = int(input())
        sum_num += num
        if num > max_num:
            max_num = num
        if num < min_num:
            min_num = num
    avg_num = sum_num / amount

    print(f"MIN: {min_num:.3f}")
    print(f"MAX: {max_num:.3f}")
    print(f"AVG: {avg_num:.3f}")

stat()
