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

lowestAmount = -1
total = 0

def getAmount(price, count):
    price = float(price)
    count = float(count)
    global total,lowestAmount
    bundle_count = math.ceil(float(total)/float(count))
    amount = int(bundle_count * price)
    if (lowestAmount == -1 or amount < lowestAmount):
        lowestAmount = amount

def set_total(buy_total):
    global total
    total = buy_total

set_total(input())
[penCount, penPrice] = input().split()
getAmount(penPrice, penCount)
[penCount, penPrice] = input().split()
getAmount(penPrice, penCount)
[penCount, penPrice] = input().split()
getAmount(penPrice, penCount)

print(lowestAmount)
