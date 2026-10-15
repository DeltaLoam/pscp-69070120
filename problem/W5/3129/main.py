"""cafe"""

def sell():
    """selling"""
    days = int(input())
    income_logs = []

    for _ in range(days):
        income = int(input())
        income_logs.append(income)

    print(sum(income_logs))
    print(max(income_logs))
    print(min(income_logs))
    print(f"{(sum(income_logs) / len(income_logs)):.1f}")

sell()
