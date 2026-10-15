"""3Distance"""

x1, y1, z1 = input().split()
x2, y2, z2 = input().split()

cal = (((int(x2) - int(x1)) ** 2) + ((int(y2) - int(y1)) ** 2) + ((int(z2) - int(z1)) ** 2)) ** 0.5
print(f"{cal:.2f}")
