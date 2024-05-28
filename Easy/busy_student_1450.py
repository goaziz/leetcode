from typing import List


class Solution:
    def busyStudent(self, startTime: List[int], endTime: List[int], queryTime: int) -> int:
        count = 0

        for start, end in zip(startTime, endTime):
            if start <= queryTime <= end:
                count += 1

        return count

    def busyStudent2(self, startTime: List[int], endTime: List[int], queryTime: int) -> int:
        count = 0

        for i in range(len(startTime)):
            if startTime[i] <= queryTime <= endTime[i]:
                count += 1

        return count


obj = Solution()
startTime = [1, 2, 3]
endTime = [3, 2, 7]
queryTime = 4
print(obj.busyStudent(startTime, endTime, queryTime))
