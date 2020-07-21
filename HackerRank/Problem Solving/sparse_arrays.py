def matchingStrings(strings, queries):
    return [strings.count(q) for q in queries]

st = ['aba', 'baba', 'aba', 'xzxb']
qu = ['aba', 'xzxb', 'ab']
print(matchingStrings(st, qu))