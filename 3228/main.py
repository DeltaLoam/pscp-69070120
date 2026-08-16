"""aeiou"""

text = input()
COUNT = 0

if text in text.lower():
    for i in text:
        if i in "aeiou":
            COUNT += 1

print(COUNT)
