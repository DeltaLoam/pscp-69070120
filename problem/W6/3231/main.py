"""gambling"""

def toy():
    """cube"""

    guess = int(input())
    real = int(input())

    if not 1 <= guess <= 6 or not 1 <= real <= 6:
        print("Invalid")
    elif guess == real:
        print("Correct!")
    else:
        print("Wrong!")

toy()
