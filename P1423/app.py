def input():
    return 5

def getStep(_meter):
    _meter = float(_meter)
    step_meter = 2
    count = 0

    while _meter >= 0:
         _meter = _meter - step_meter
         step_meter = step_meter * 0.98
         count = count + 1

    return count

print(getStep(input()))

