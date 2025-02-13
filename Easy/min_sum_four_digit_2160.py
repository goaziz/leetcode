class Solution:
    def minimumSum(self, num: int) -> int:
        x = list(map(str, str(num)))
        x.sort()
        num1 = int(x[0] + x[2])
        num2 = int(x[1] + x[3])

        return num1 + num2


obj = Solution()
num = 4009
print(obj.minimumSum(num))
