"""elo"""
ra = float(input("Ra:"))
rb = float(input("Rb:"))
choice = input("A or B?").upper()

if choice == "A":
    ea = 1 / (1 + 10 ** ((rb - ra) / 400))
    print(f"{ea:.2f}")
elif choice == "B":
    eb = 1 / (1 + 10 ** ((ra - rb) / 400))
    print(f"{eb:.2f}")
