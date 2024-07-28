import random

list = []

#testing stuff
for i in range (0, 10):
    x = random.randrange(1, 11)
    list.append(x)

blist = [1, 2, 2, 3, 3, 5, 5, 5]

def average(list):
    total = 0
    listLen = len(list)
    for i in range(0, listLen):
        total += list[i]
    return (total / listLen)

def mode(list):
    listLen = len(list)
    list.sort()
    modes = []
    highest = 0
    curr = 1
    for i in range(0, listLen):
        temp = list[i]
        if i == (listLen - 1):
            print("Reached End")
        elif temp == list[i+1]:
            curr += 1
            if curr == highest:
                modes.append(list[i])
                highest = curr
            if curr > highest:
                modes = []
                modes.append(list[i])
                highest = curr
        else:
            curr = 1
    return modes, highest

avg = average(list)
modeList, modeAmount = mode(list)

print("The average was",avg)

if len(modeList) > 1:
    print("The mode was tied between:",modeList,"with each appearing",modeAmount,"times") 
elif len(modeList) == 0:
    print("No mode, every element only appeared once")
else:
    print("The mode was",modeList[0],"which appeared",modeAmount,"times")
