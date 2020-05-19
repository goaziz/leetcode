def longestCommonPrefix(strs):
    ch = ''
    if len(strs) == 0:
        return ''
    strs = sorted(strs)
    for x in strs[0]:
        if strs[-1].startswith(ch + x):
            ch += x
        else:
            break
    return ch
