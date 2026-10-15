"""swapper"""
num = input()
swap_num = num[1] + num[0]
operator = input()

if operator == "+":
    print(f"{int(num)} + {int(swap_num)} = {int(num) + int(swap_num)}")
elif operator == "*":
    print(f"{int(num)} * {int(swap_num)} = {int(num) * int(swap_num)}")
