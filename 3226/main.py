"""a"""
def main():
    """a"""
    price = int(float(input()) * 100)
    time = int(input())
    inflation_rate = 381
    for _ in range(time):
        price += (price * inflation_rate) // 10000
    print(f"{price // 100}.{price % 100:02d}")
main()
