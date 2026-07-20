a = float(input())
b = float(input())

min_score = max(0, a - 2*b)

if b - min_score > 2:
    print("Surprising")
else:
    print("Not surprising")
