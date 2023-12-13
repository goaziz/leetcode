from typing import List


class Solution:
    def findPoisonedDuration(self, timeSeries: List[int], duration: int) -> int:
        n = len(timeSeries)
        if n == 0:
            return 0

        poisoned_time = 0

        for i in range(n - 1):
            difference = min(duration, abs(timeSeries[i] - timeSeries[i+1]))
            poisoned_time += difference

        return poisoned_time + duration


obj = Solution()
timeSeries = [1, 2, 3, 4, 5, 6, 7, 8, 9]
duration = 0
print(obj.findPoisonedDuration(timeSeries, duration))
