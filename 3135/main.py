"""circle game"""

def game():
    """circle thief"""
    stop ,step ,thief = map(int,input().split())
    pos = 1
    count = 1

    if thief == 1:
        print(1)
    else:
        while True:
            pos = (pos + step - 1) % stop + 1

            if pos == 1:
                break

            count += 1

            if pos == thief:
                break

        print(count)

game()
