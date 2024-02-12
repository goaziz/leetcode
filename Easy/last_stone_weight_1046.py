from typing import List


class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        n = len(stones)
        if n == 1:
            return stones[0]

        for i in range(n - 1):
            if len(stones) > 1:
                x = max(stones)
                stones.remove(x)
                y = max(stones)

                if x == y:
                    stones.remove(y)
                else:
                    stones.remove(y)
                    diff = abs(y - x)
                    stones.append(diff)

        return 0 if len(stones) == 0 else stones[-1]


obj = Solution()
stones = [2, 7, 4, 1, 8, 1]
print(obj.lastStoneWeight(stones))
