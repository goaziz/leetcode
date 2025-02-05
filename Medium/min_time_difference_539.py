from collections import Counter
from typing import List


class Solution:

    def get_difference(self, time1, time2):
        h1, m1 = map(int, time1.split(':'))
        h2, m2 = map(int, time2.split(':'))
        min_in_day = 24 * 60

        minutes1 = h1 * 60 + m1
        minutes2 = h2 * 60 + m2

        diff1 = abs(minutes2 - minutes1)
        diff2 = min_in_day - diff1

        return min(diff1, diff2)

    def findMinDifference(self, timePoints: List[str]) -> int:
        timePoints.sort()
        result = float('inf')
        first_time = last_time = None

        for i in range(len(timePoints)):
            if i == 0:
                first_time = timePoints[i]
            else:
                diff = self.get_difference(timePoints[i - 1], timePoints[i])
                result = min(result, diff)

            last_time = timePoints[i]

        wrap_diff = self.get_difference(first_time, last_time)

        return min(result, wrap_diff)


obj = Solution()
timePoints = ["00:00", "23:59", "00:00"]
print(obj.findMinDifference(timePoints))
