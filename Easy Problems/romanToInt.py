def romanToInt(s):
    roman = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }
    int_val = roman[s[0]]
    print(int_val)
    for i in range(1, len(s)):
        if roman[s[i]] > roman[s[i - 1]]:
            int_val += roman[s[i]] - 2 * roman[s[i - 1]]
        else:
            int_val += roman[s[i]]
    return int_val

print(romanToInt('XIX'))