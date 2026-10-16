"""shorten"""


def main():
    """shorten"""
    numbers = []

    while True:
        try:
            number = int(input())
        except EOFError:
            break

        if number == -1:
            break

        numbers.append(number)

    if not numbers:
        return

    start = numbers[0]
    end = start
    result = []

    for number in numbers[1:]:
        if number == end + 1:
            end = number
        else:
            if start == end:
                result.append(str(start))
            else:
                result.append(f"{start}-{end}")

            start = number
            end = number

    if start == end:
        result.append(str(start))
    else:
        result.append(f"{start}-{end}")

    print(", ".join(result))

main()
