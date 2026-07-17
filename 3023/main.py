"""calculator"""

num = int(input())
result = "1"

if num > 1:
    for i in range(2, num):
        result = result + "+" + str(i + 1)
    result = result + "="
    print(result)
    print(len(result))
elif num == 1:
    print(result)
