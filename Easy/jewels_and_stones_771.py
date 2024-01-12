from typing import Counter


class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        c = Counter(stones)
        count = 0
        for jewel in jewels:
            if jewel in c:
                count += c.get(jewel)

        return count


obj = Solution()
jewels = "z"
stones = "ZZ"
print(obj.numJewelsInStones(jewels, stones))
