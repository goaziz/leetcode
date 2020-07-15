


def plusMinus(arr):
    count_pls = 0
    count_mis = 0
    count_zer = 0
    for i in arr:
        if i > 0:
            count_pls += 1
        if i < 0:
            count_mis += 1
        if i == 0:
            count_zer += 1
    print('{:.6f}'.format(count_pls/len(arr)))
    print('{:.6f}'.format(count_mis/len(arr)))
    print('{:.6f}'.format(count_zer/len(arr)))

arr = [-4, 3, -9, 0, 4, 1]

plusMinus(arr)