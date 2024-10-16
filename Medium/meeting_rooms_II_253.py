import heapq
from typing import List


class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: x[0])

        end_times = []
        heapq.heappush(end_times, intervals[0][1])

        for interval in intervals[1:]:
            if end_times[0] <= interval[0]:
                heapq.heappop(end_times)
            heapq.heappush(end_times, interval[1])

        return len(end_times)


obj = Solution()
intervals = [[9, 10], [4, 9], [4, 17]]
print(obj.minMeetingRooms(intervals))
