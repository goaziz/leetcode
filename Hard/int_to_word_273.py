import math


class Solution:
    def numberToWords(self, num: int) -> str:
        nums_map = {
            0: "Zero", 1: "One", 2: "Two", 3: "Three",
            4: "Four", 5: "Five", 6: "Six", 7: "Seven",
            8: "Eight", 9: "Nine", 10: "Ten", 11: "Eleven",
            12: "Twelve", 13: "Thirteen", 14: "Fourteen", 15: "Fifteen",
            16: "Sixteen", 17: "Seventeen", 18: "Eighteen", 19: "Nineteen",
            100: "Hundred", 1000: "Thousand", 1000000: "Million", 1000000000: "Billion"
        }
        groups = ["", "Thousand", "Million", "Billion"]
        result = ""
        group = 0
        
        multiple_of_ten = ['', '', 'Twenty', 'Thirty', 'Forty', 'Fifty', 'Sixty', 'Seventy', 'Eighty', 'Ninety']

        while num > 0:
            if num % 1000 != 0:
                n = num % 1000
                temp = ""

                if n >= 100:
                    temp += nums_map[n // 100] + " Hundred "
                    n %= 100

                if n >= 20:
                    temp += multiple_of_ten[n // 10] + ' '
                    n %= 10

                if n > 0:
                    temp += nums_map[n] + ' '
                temp += groups[group] + ' '
                result = temp + result

            num //= 1000
            group += 1

        return result.strip()


obj = Solution()
num = 320
print(obj.numberToWords(num))
