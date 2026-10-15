"""num same"""

def same_check():
    """checker"""

    num1 = int(input())
    num2 = int(input())
    num3 = int(input())

    if num1 == num2 == num3:
        print("all the same")
    elif num1 == num2 or num1 == num3 or num2 == num3:
        print("neither")
    else:
        print("all different")

same_check()
