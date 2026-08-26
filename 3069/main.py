"""zodiac"""

def zodiac():
    """thinker"""
    day = int(input())
    month = int(input())

    signs = [
        "capricorn", "aquarius", "pisces", "aries",
        "taurus", "gemini", "cancer", "leo",
        "virgo", "libra", "scorpio", "sagittarius"
    ]

    cut = [20, 19, 21, 20, 21, 22, 23, 23, 23, 24, 22, 22]

    if day < cut[month - 1]:
        print(signs[month - 1])
    else:
        print(signs[month % 12])

zodiac()
