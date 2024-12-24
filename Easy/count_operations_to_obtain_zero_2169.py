class Solution:
    def countOperations(self, num1: int, num2: int) -> int:
        count = 0
        while num1 != 0 and num2 != 0:
            if num1 > num2:
                num1 -= num2
            else:
                num2 -= num1
            count += 1

        return count


obj = Solution()
num1 = 22
num2 = 22
print(obj.countOperations(num1, num2))
