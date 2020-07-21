def getMoneySpent(keyboards, drives, b):
    sum = -1
    for i in range(len(keyboards)):
        for j in range(len(drives)):
            if keyboards[i] + drives[j] <= b and keyboards[i] + drives[j]  > sum:
                sum = keyboards[i] + drives[j]
    return sum