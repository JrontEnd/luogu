inputStr = '''57
2 2
50 30
30 27'''
count = -1

def input():
    global count
    count += 1
    splitArr = inputStr.split('\n')
    return splitArr[count]

import math

lowestAmount = 0
total = -1

def getAmount(price, count):
    global total,lowestAmount
    bundle_count = math.ceil(float(total)/float(count))
    amount = bundle_count * price
    if (total == -1 or amount < total):
        total = amount

def set_total(buy_total):
    global total
    total = buy_total

set_total(input())
[penPrice, penCount] = input().split()
getAmount(penPrice, penCount)
[penPrice, penCount] = input().split()
getAmount(penPrice, penCount)
[penPrice, penCount] = input().split()
getAmount(penPrice, penCount)

print(total)
