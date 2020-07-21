def diognalDifference(arr):
    diag = [arr[i][i] for i in range(len(arr))]
    print(diag)
    diag_r = sum([row[i] for i, row in enumerate(arr)])
    diag_l = sum([row[-i - 1] for i, row in enumerate(arr)])
    return abs(diag_r - diag_l)

