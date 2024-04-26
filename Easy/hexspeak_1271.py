class Solution:
    def toHexspeak(self, num: str) -> str:
        letters = ['A', 'B', 'C', 'D', 'E', 'F', 'I', 'O']
        hex_s = hex(int(num))
        s = ''
        for i in hex_s[2:].upper():
            if i == '0':
                s += 'O'
            elif i == '1':
                s += 'I'
            elif i in letters:
                s += i
            else:
                return 'ERROR'

        return s

    def toHexspeak2(self, num: str) -> str:
        hex_s = hex(int(num))[2:].upper()
        hex_s = hex_s.replace('1', 'I')
        hex_s = hex_s.replace('0', 'O')

        for ch in hex_s:
            if ch not in 'ABCDEFIO':
                return 'ERROR'

        return hex_s


obj = Solution()
num = '3'
print(obj.toHexspeak(num))
