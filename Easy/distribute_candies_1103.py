from typing import List


class Solution:
    def distributeCandies(self, candies: int, num_people: int) -> List[int]:
        ans = [0] * num_people
        i = 0
        while candies >= 0:
            ans[i % num_people] += min(i + 1, candies)
            i += 1
            candies -= i

        return ans


obj = Solution()
candies = 10
num_people = 3
print(obj.distributeCandies(candies, num_people))
