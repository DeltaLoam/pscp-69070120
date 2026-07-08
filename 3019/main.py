"""safePassword"""
guess_str = input()
guess_int = int(input())

if guess_str == "H" and guess_int == 4567:
    print("safe unlocked")
elif guess_str != "H" and guess_int == 4567:
    print("safe locked - change char")
elif guess_str == "H" and guess_int != 4567:
    print("safe locked - change digit")
elif guess_str != "H" and guess_int != 4567:
    print("safe locked")
