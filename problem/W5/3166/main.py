"""grade"""

def avg():
    """average"""
    num = int(input())
    subjects = []
    passed = True

    for _ in range(num):
        score = int(input())
        subjects.append(score)

        if score < 50:
            passed = False

    average = sum(subjects) / num
    print(f"{average:.1f}")

    if average >= 60 and passed:
        print("PASS")
    else:
        print("FAIL")

avg()
