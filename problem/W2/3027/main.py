"""housing"""
length, width, step = input().split()
price = int(input())

print((int(length) * 2 + int(width) * 2) * int(step))
print((int(length) * 2 + int(width) * 2) * int(step) * price)
