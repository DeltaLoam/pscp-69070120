"""score"""

def calculate():
    """score cal"""
    prob = int(input())
    mid = int(input())
    final = int(input())

    if prob >= 5 and mid >= 20 and final >= 25:
        print("pass")
    else:
        print("fail")

calculate()
