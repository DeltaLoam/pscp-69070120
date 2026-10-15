"""triangle"""
a = float(input())
b = float(input())
c = float(input())

if a > 0 and b > 0 and c > 0:
    s = (a + b + c) / 2
    area = (s * (s - a) * (s - b) * (s - c)) ** 0.5
    print(f"{area:.3f}")
