class Solution:
    def clumsy(self, n: int) -> int:
        arr = []
        oper_count = 0

        for i in range(n, 0, -1):
            if oper_count == 0:
                oper = '*'
                oper_count += 1
            elif oper_count == 1:
                oper = '//'
                oper_count += 1
            elif oper_count == 2:
                oper = '+'
                oper_count += 1
            else:
                oper = '-'
                oper_count = 0

            arr.append(str(i))
            arr.append(oper)

        s = ''.join(arr[:-1])
        return eval(s)

    def clumsy2(self, n: int) -> int:
        k = 0
        stack = [n]

        for i in range(n - 1, 0, -1):
            if k == 0:
                stack.append(stack.pop() * i)
            elif k == 1:
                stack.append(stack.pop() // i)
            elif k == 2:
                stack.append(i)
            else:
                stack.append(-i)
            k = (k + 1) % 4

        return sum(stack)


obj = Solution()
n = 10
print(obj.clumsy(n))
