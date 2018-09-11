count = 0
inputStr = """290 
230 
280 
200 
300 
170 
330 
50 
90 
80 
200 
60"""

def input():
    global count
    returnStr = inputStr.split('\n')[count]
    count += 1
    return returnStr

# get monthly save and left money
def left_money(leave, spend):
    leftMount = leave - spend
    if leftMount < 0:
        return [0, leftMount]
    else:
        return [leftMount // 100 * 100, leftMount % 100]


leaveMoney = 0
totalAmount = 0
flag = True
overflow = 0

# add to total
def add_money(monthAdd, monthLeave):
    global leaveMoney
    global totalAmount
    leaveMoney = monthLeave
    totalAmount += monthAdd


# get total money yearly
def get_total():
    return int(totalAmount * 1.2 + leaveMoney)


for item in range(0, 12):
    spendMoney = int(input())
    [save, left] = left_money(300 + leaveMoney, spendMoney)
    if left < 0:
        flag = False
        overflow = -(item + 1)
        break
    else:
        add_money(save, left)

if flag == False:
    print(overflow)
else:
    print(get_total())