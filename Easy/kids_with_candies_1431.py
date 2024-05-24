from typing import List


class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        max_n = max(candies)
        ans = []
        
        for i in range(len(candies)):
            s = candies[i] + extraCandies
            ans.append(s >= max_n)

        return ans


obj = Solution()
candies = [2, 3, 5, 1, 3]
extraCandies = 3
print(obj.kidsWithCandies(candies, extraCandies))
