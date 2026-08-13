def parse_time(s):
    """แปลง 'H.MM' -> นาทีรวม (int) หรือ None ถ้าไม่ถูกต้อง"""
    if s is None:
        return None
    s = s.strip()
    if s == "":
        return None

    if '.' not in s:
        h_str, m_str = s, "0"
    else:
        parts = s.split('.')
        if len(parts) != 2:
            return None
        h_str, m_str = parts

    if not h_str.lstrip('-').isdigit() or not m_str.isdigit():
        return None

    h = int(h_str)
    m = int(m_str)

    if h < 0 or h > 23:
        return None
    if m < 0 or m > 59:
        return None

    return h * 60 + m


def calc_rate(hours):
    rates = {1: 25, 2: 50, 3: 80, 4: 110, 5: 145, 6: 180}
    if hours in rates:
        return rates[hours]
    elif 7 <= hours <= 24:
        return 250
    else:
        return None


def main():
    t_in = input()
    t_out = input()

    entry = parse_time(t_in)
    exit_ = parse_time(t_out)

    if entry is None or exit_ is None:
        print("ERROR")
        return

    duration = exit_ - entry
    if duration < 0:
        duration += 24 * 60  # ข้ามเที่ยงคืน

    if duration <= 15:
        print("FREE")
        return

    hours = (duration + 59) // 60  # ceil division
    rate = calc_rate(hours)

    if rate is None:
        print("ERROR")
    else:
        print(rate)


main()