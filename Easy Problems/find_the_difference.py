from collections import Counter

def findTheDifference(s, t):
    return list(Counter(t) - Counter(s))[0]
