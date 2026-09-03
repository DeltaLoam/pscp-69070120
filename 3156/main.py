"""conan"""

def decoder():
    """conan"""
    code = input()
    decode_num = int(input())
    decoded = ""
    char = "abcdefghijklmnopqrstuvwxyz"

    for _, letter in enumerate(code):
        decoded += char[(char.index(letter) + decode_num) % 26]

    print(decoded)

decoder()
