def input():
    return '12 50 19 10'


# get date
dateDuration = input().split()
startMonth = int(dateDuration[0])
startMinute = int(dateDuration[1])
endMonth = int(dateDuration[2])
endMinute = int(dateDuration[3])

# calculate duration
durationMinute = (endMonth - startMonth) * 60 + (endMinute - startMinute)

# get result
monthResult = durationMinute // 60
minuteResult = durationMinute % 60

# print result
print(str(monthResult) + ' ' + str(minuteResult))