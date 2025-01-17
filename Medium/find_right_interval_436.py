from typing import List


class Solution:

    def binary_search(self, target, nums):
        right = len(nums)
        left = 0

        while left < right:
            mid = (right + left) // 2

            if nums[mid] < target:
                left = mid + 1
            else:
                right = mid

        return left

    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        if len(intervals) == 1:
            return [-1]

        indexed_intervals = [(start, end, i)
                             for i, (start, end) in enumerate(intervals)]
        indexed_intervals.sort()

        start_times = [start for start, _, _ in indexed_intervals]
        result = []
        for start, end in intervals:
            idx = self.binary_search(end, start_times)
            if idx < len(start_times):
                result.append(indexed_intervals[idx][2])
            else:
                result.append(-1)

        return result


obj = Solution()
intervals = [[3, 4], [2, 3], [1, 2]]
print(obj.findRightInterval(intervals))
