from typing import List


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        ans = [0] * n

        for i in range(n):
            for j in range(i + 1, n):
                if temperatures[i] < temperatures[j]:
                    ans[i] = j - i
                    break

        return ans

    def dailyTemperatures2(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        ans = [0] * n
        stack = []

        for curr_day, temperature in enumerate(temperatures):

            while stack and temperatures[stack[-1]] < temperature:
                prev_day = stack.pop()
                ans[prev_day] = curr_day - prev_day

            stack.append(curr_day)

        return ans


obj = Solution()
temperatures = [73, 74, 75, 71, 69, 72, 76, 73]
print(obj.dailyTemperatures2(temperatures))
