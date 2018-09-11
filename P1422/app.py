def input():
    return '267'


energyUsed = int(input())

# define price
seg1 = 0.4463
seg2 = 0.4663
seg3 = 0.5663

# calculate segment amount
amount = 0
if energyUsed <= 150:
    amount = energyUsed * seg1
elif energyUsed <= 400:
    amount = 150 * seg1 + (energyUsed - 150) * seg2
else:
    amount = 150 * seg1 + 250 * seg2 + (energyUsed - 400) * seg3

# print result
print(round(amount, 1))
