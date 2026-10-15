"""password generator"""
name = input("Enter your name:")
sur = input("Enter your surname:")
age = int(input("Enter your age:"))

if len(name) >= 5 and len(sur) >= 5:
    print(f"{name[0]}{name[1]}{sur[-1]}{str(age)[-1]}")
else:
    print(f"{name[0]}{str(age)}{sur[-1]}")
