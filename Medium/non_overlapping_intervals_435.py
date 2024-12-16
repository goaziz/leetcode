from typing import List


class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: x[1])
        overlap_count = 0
        prev_end = float('-inf')
        
        for start, end in intervals:
            if start >= prev_end:
                prev_end = end
            else:
                overlap_count += 1

        return overlap_count


obj = Solution()
intervals = [[1, 100], [11, 22], [1, 11], [2, 12]]
print(obj.eraseOverlapIntervals(intervals))
