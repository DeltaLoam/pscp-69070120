"""temp_changer"""

def temp_changer():
    """Main_function"""
    temp = float(input())
    base_temp = input()
    result_temp = input()

    celsius = 0.0
    result = 0.0

    if base_temp == "C":
        celsius = temp
    elif base_temp == "F":
        celsius = (temp - 32) * 5 / 9
    elif base_temp == "K":
        celsius = temp - 273.15
    elif base_temp == "R":
        celsius = (temp - 491.67) * 5 / 9

    if result_temp == "C":
        result = celsius
    elif result_temp == "F":
        result = celsius * 9 / 5 + 32
    elif result_temp == "K":
        result = celsius + 273.15
    elif result_temp == "R":
        result = (celsius + 273.15) * 9 / 5

    print(f"{result:.2f}")

temp_changer()
