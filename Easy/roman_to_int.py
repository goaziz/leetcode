class Solution:
    def romanToInt(self, s: str) -> int:
        roman = {
            'I': 1, 'V': 5, 'X': 10, 'L': 50,
            'C': 100, 'D': 500, 'M': 1000
        }
        value = 0
        for i in range(len(s) - 1):
            if roman[s[i]] < roman[s[i + 1]]:
                value -= roman[s[i]]
            else:
                value += roman[s[i]]

        return value + roman[s[-1]]
