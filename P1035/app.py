def input():
    return '1'

def min_count(number):
    number = int(number)
    total = 0
    i = 0
    while number >= total:
        i = i + 1
        total = total + (float(1) / i)
    print(i)

min_count(input())