class Solution:
    def numberOfMatches(self, n: int) -> int:
        count = 0

        while n != 1:
            if n % 2 == 0:
                match = n // 2
            else:
                match = (n - 1) // 2
                                
            count += match
            n -= match

        return count


obj = Solution()
n = 14
print(obj.numberOfMatches(n))
