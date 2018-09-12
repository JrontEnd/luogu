def input():
    return '3 10'

DAY_SPPED = 150 + 100

def total_distance(_start_day, _total_day):
    current_day = 0
    current_week_day = _start_day
    total_distance = 0

    while current_day < _total_day:
        if 1 <= current_week_day <= 5:
            total_distance = total_distance + DAY_SPPED

        if current_week_day == 7:
            current_week_day = 1
        else:
            current_week_day = current_week_day + 1

        current_day = current_day + 1

    return total_distance

inputStr = input().split()
print(total_distance(float(inputStr[0]), float(inputStr[1])))
