"""pass/not"""

def cal():
    """cal"""
    mid = int(input())
    final = int(input())
    sum_ = mid + final

    if sum_ >= 50:
        print(sum_)
        print("pass")
    else:
        print(sum_)
        print("fail")

cal()
