class Solution:
    def toLowerCase(self, s: str) -> str:
        chars = {'A': 'a', 'B': 'b', 'C': 'c', 'D': 'd', 'E': 'e', 'F': 'f',
                 'G': 'g', 'H': 'h', 'I': 'i', 'J': 'j', 'K': 'k', 'L': 'l',
                 'M': 'm', 'N': 'n', 'O': 'o', 'P': 'p', 'Q': 'q', 'R': 'r',
                 'S': 's', 'T': 't', 'U': 'u', 'V': 'v', 'W': 'w', 'X': 'x',
                 'Y': 'y', 'Z': 'z'}

        res = ''
        for char in s:
            if char not in chars:
                res += char
            else:
                res += chars.get(char)

        return res

    def toLowerCase2(self, s: str) -> str:
        upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        lower = "abcdefghijklmnopqrstuvwxyz"
        h = dict(zip(upper, lower))

        return ''.join([h[x] if x in h else x for x in s])


obj = Solution()
s = "Hello World"
print(obj.toLowerCase(s))
