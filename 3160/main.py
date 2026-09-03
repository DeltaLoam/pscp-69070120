"""prime"""
def prime():
    """rick"""
    start, stop = map(int, input().split())

    primes = []

    for num in range(start, stop + 1):
        if num < 2:
            continue

        is_prime = True

        for i in range(2, int(num ** 0.5) + 1):
            if not num % i:
                is_prime = False
                break

        if is_prime:
            primes.append(str(num))

    if primes:
        print(" ".join(primes))

    print(f"Total primes: {len(primes)}")

prime()
