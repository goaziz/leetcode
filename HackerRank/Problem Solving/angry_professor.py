def angryProfessor(k, a):
    print("YES" if sum([1 for x in a if x <= 0]) < k else "NO")
    res = [i for i in a if i <= 0]
    if len(res) >= k:
        return 'NO'
    else:
        return 'YES'


a = [13, 91, 56, -62, 96, 5, -84, 36, 46, 13]
k = 7
print(angryProfessor(k, a))

# 10 7
# 26 94 -95 34 67 -97 17 52 1 86
# 10 2
# 19 29 -17 -71 -75 -27 -56 -53 65 83
# 10 10
# -32 -3 -70 8 -40 -96 -18 -46 -21 -79
# 10 9
# -50 0 64 14 -56 -91 -65 -36 51 -28
# 10 6
# -58 -29 -35 -18 43 -28 -76 43 -13 6
# 10 1
# 88 -17 -96 43 83 99 25 90 -39 86
# YES
# NO
# YES
# YES
# NO
# NO
