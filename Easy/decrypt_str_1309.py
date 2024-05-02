class Solution:
    def freqAlphabets(self, s: str) -> str:
        letters = {
            '1': 'a',
            '2': 'b',
            '3': 'c',
            '4': 'd',
            '5': 'e',
            '6': 'f',
            '7': 'g',
            '8': 'h',
            '9': 'i',
            '10#': 'j',
            '11#': 'k',
            '12#': 'l',
            '13#': 'm',
            '14#': 'n',
            '15#': 'o',
            '16#': 'p',
            '17#': 'q',
            '18#': 'r',
            '19#': 's',
            '20#': 't',
            '21#': 'u',
            '22#': 'v',
            '23#': 'w',
            '24#': 'x',
            '25#': 'y',
            '26#': 'z'
        }

        res = ''
        j = len(s)
        i = 0

        while i < j:
            if '#' in s[i:i + 3]:
                res += letters.get(s[i:i + 3], '')
                i += 3
            else:
                res += letters.get(s[i], '')
                i += 1
        # for i in range(len(s)):
        #     if '#' in s[i:i + 3]:
        #         res += letters.get(s[i:i + 3], '')
        #     else:
        #         res += letters.get(s[i], '')

        return res

    def freqAlphabets2(self, s: str) -> str:
        res = ''

        i = 0
        while i < len(s):
            if i + 2 < len(s) and s[i + 2] == '#':
                c = chr(int(s[i:i + 2]) + ord('a') - 1)
                i += 3
            else:
                c = chr(int(s[i]) + ord('a') - 1)
                i += 1
            res += c

        return res


obj = Solution()
s = "10#11#12"
print(obj.freqAlphabets(s))
