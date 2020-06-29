def strStr(haystack, needle):

    for i in haystack:
        if needle in haystack:
            index = haystack.index(needle)
            return index
        else:
            return -1

    if haystack == '' and needle != '':
        return -1
    else:
        return 0


h = 'hello'
n = 'll'

print(strStr(h, n))