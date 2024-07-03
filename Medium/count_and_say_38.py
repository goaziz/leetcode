class Solution:
    def helper(self, previous_term):
        i = 0
        count = 0
        res = ''

        while i < len(previous_term):
            count = 1
            while i + 1 < len(previous_term) and previous_term[i] == previous_term[i + 1]:
                i += 1
                count += 1
            res += str(count) + previous_term[i]
            i += 1

        return res

    def countAndSay(self, n: int) -> str:
        res = '1'

        for _ in range(1, n):
            ans = self.helper(res)
            res = ans

        return res


obj = Solution()
n = 1
print(obj.countAndSay(n))
