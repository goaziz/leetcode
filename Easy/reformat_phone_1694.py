class Solution:
    def reformatNumber(self, number: str) -> str:
        number = number.replace('-', '').replace(' ', '')
        n = len(number)
        if n <= 2:
            return number

        primary, carry = divmod(n, 3)
        if carry == 0:
            primary = primary * 3
        elif carry == 1:
            primary = (primary - 1) * 3
            carry = (carry + 1) * 2
        elif carry == 2:
            primary = primary * 3

        count = 0
        res = ""
        for num in range(primary):
            if count == 3:
                res += '-' + number[num]
                count = 1
            else:
                res += number[num]
                count += 1

        if carry > 0:
            count = 0
            res += '-' if res else ''
            for num in number[primary:]:
                if count == 2:
                    res += '-' + num
                    count = 0
                else:
                    res += num
                    count += 1

        return res

    def reformatNumber2(self, number: str) -> str:
        number = number.replace('-', '').replace(' ', '')
        n = len(number)
        if n <= 2:
            return number

        res = ''
        count = 0
        primary, carry = divmod(n, 3)

        if carry in [0, 2]:
            primary *= 3
        else:
            primary = (primary - 1) * 3
            carry = 4

        for i in range(primary):
            if count == 3:
                res += '-' + number[i]
                count = 1
            else:
                res += number[i]
                count += 1

        if carry == 2:
            res += '-' + number[-2:]
        elif carry == 4:
            temp = number[-4:-2] + '-' + number[-2:]
            res += '-' if res else ''
            res += temp

        return res

    def reformatNumber3(self, number: str) -> str:
        number = number.replace('-', '').replace(' ', '')
        n = len(number)
        res = []

        for i in range(0, n, 3):
            if n - i != 4:
                res.append(number[i: i + 3])
            else:
                res += [number[i: i + 2], number[i + 2:]]
                break

        return '-'.join(res)


obj = Solution()
number = "123 4-5678"
print(obj.reformatNumber3(number))
