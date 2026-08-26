"""bubble tea"""
def cal():
    """cal"""
    bubble, gram = input().split()
    tea, sweet, cc = input().split()

    gram = float(gram)
    sweet = int(sweet)
    cc = float(cc)

    if bubble == "H":
        bubble_cal = gram * 5
    elif bubble == "O":
        bubble_cal = gram * 3
    else:
        bubble_cal = gram * 2

    if tea == "R":
        tea_cal = [0, 12, 18, 25]
    elif tea == "T":
        tea_cal = [0, 15, 20, 30]
    else:
        tea_cal = [0, 10, 15, 20]

    total = bubble_cal + tea_cal[sweet] * cc

    print(f"{total:g}")

cal()
