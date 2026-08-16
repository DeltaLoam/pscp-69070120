"""triangle"""
def main():
    """triangle"""
    n = int(input())
    for i in range(n):
        line = ""
        for j in range(i + 1):
            if not j or j == i or i == n - 1:
                line += "0"
            else:
                line += "1"
        print(line)
main()
