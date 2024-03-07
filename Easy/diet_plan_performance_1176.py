from typing import List


class Solution:
    def dietPlanPerformance(self, calories: List[int], k: int, lower: int, upper: int) -> int:
        points = 0
        s = sum(calories[:k])

        if s > upper:
            points += 1
        elif s < lower:
            points -= 1

        for i in range(k, len(calories)):
            s = s - calories[i - k] + calories[i]

            if s > upper:
                points += 1
            elif s < lower:
                points -= 1

        return points


obj = Solution()
calories = [6, 13, 8, 7, 10, 1, 12, 11]
k = 6
lower = 5
upper = 37
print(obj.dietPlanPerformance(calories, k, lower, upper))
