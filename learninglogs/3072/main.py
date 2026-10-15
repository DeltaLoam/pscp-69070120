"""aeiou"""

def counter():
    """checker"""
    word = input().lower()
    array = {"a": 0, "e": 0, "i": 0, "o": 0, "u": 0}

    for i in word:
        if i in "aeiou":
            array[i] += 1

    for vowel, count in array.items():
        if count > 0:
            print(f"{vowel} : {count}")

counter()
