class Solution:

    def sum_of_digits(self, n):
        s = 0

        while n != 0:
            digit = n % 10
            s += digit
            n //= 10

        return s

    def countLargestGroup(self, n: int) -> int:
        hashmap = {}

        for i in range(1, n + 1):
            sum_digt = self.sum_of_digits(i)
            if sum_digt in hashmap:
                hashmap[sum_digt].append(i)
            else:
                hashmap[sum_digt] = [i]
        max_length = max(hashmap.values(), key=len)
        largest_groups = [group for group in hashmap.values() if len(
            group) == len(max_length)]

        return len(largest_groups)

    def countLargestGroup(self, n: int) -> int:
        dp = {0: 0}
        counts = [0] * (4 * 9)
        for i in range(1, n + 1):
            quotient, reminder = divmod(i, 10)
            dp[i] = reminder + dp[quotient]
            counts[dp[i] - 1] += 1

        return counts.count(max(counts))


obj = Solution()
n = 2642
print(obj.countLargestGroup(n))
