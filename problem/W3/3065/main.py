"""roman"""

def roman_num():
    """roman number"""
    num = int(input())
    roman_dict = {
        1: "I",
        2: "II",
        3: "III",
        4: "IV",
        5: "V",
        6: "VI",
        7: "VII",
        8: "VIII",
        9: "IX",
    }

    if 1 <= num <= 9:
        print(roman_dict[num])
    elif num > 9 or not num:
        print("Error : Out of range")
    elif num < 0:
        print("Error : Please input positive number")

roman_num()
