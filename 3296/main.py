""" [RGB Mixed """

def mix_color(c1, c2):
    """เฉลี่ยแบบปัดลง"""
    return (c1 + c2) // 2

def main():
    """[RGB Mixed"""
    r1, g1, b1 = map(int, input().split())
    r2, g2, b2 = map(int, input().split())
    r = mix_color(r1, r2)
    g = mix_color(g1, g2)
    b = mix_color(b1, b2)
    print(r, g, b)

main()
