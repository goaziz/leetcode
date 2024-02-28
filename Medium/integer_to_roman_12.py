class Solution:
    def intToRoman(self, num: int) -> str:
        romans = {
            1: 'I',
            4: 'IV',
            5: 'V',
            9: 'IX',
            10: 'X',
            40: 'XL',
            50: 'L',
            90: 'XC',
            100: 'C',
            400: 'CD',
            500: 'D',
            900: 'CM',
            1000: 'M'
        }
        ans = []

        for key, val in reversed(romans.items()):
            if num == 0:
                break
            count, num = divmod(num, key)
            ans.append(val * count)

        return ''.join(ans)


obj = Solution()
num = 304
print(obj.intToRoman(num))
