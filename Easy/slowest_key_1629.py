from typing import List


class Solution:
    def slowestKey(self, releaseTimes: List[int], keysPressed: str) -> str:
        max_difference = releaseTimes[0]
        ans = keysPressed[0]

        for i in range(1, len(releaseTimes)):
            current_time = releaseTimes[i]
            prev_time = releaseTimes[i - 1]
            difference = abs(prev_time - current_time)

            if difference > max_difference or (max_difference == difference and keysPressed[i] > ans):
                max_difference = difference
                ans = keysPressed[i]

        return ans


obj = Solution()
releaseTimes = [12, 23, 36, 46, 62]
keysPressed = "spuda"
print(obj.slowestKey(releaseTimes, keysPressed))
