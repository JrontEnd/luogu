count = 0
inputStr = """5 3
6 2
7 2
5 3
5 4
0 4
0 6"""

def input():
    returnStr = inputStr.split('\\n')[count]
    count += 1
    return returnStr


# find unhappy day
unhappy = 0
maxHours = 0
for index in range(0, 7):
    studyTime = input().split()
    totalHours = int(studyTime[0]) + int(studyTime[1])
    if totalHours >= 8 and totalHours > maxHours:
        # if matched, set unhappy day and max hour
        unhappy = index + 1
        maxHours = totalHours

# print result
print(unhappy)
