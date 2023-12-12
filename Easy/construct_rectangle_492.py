from typing import List


class Solution:
    def constructRectangle(self, area: int) -> List[int]:
        L = None
        W = None

        for i in range(2, int(area ** 0.5) + 1):
            if area % i == 0:
                current_difference = abs(i - area // i)

                if L is None or current_difference < abs(L - W):
                    W = i
                    L = area // i

        # If no divisor is found, the number is prime
        if W is None:
            L = area
            W = 1

        return [L, W]

    def constructRectangle2(self, area: int) -> List[int]:
        for i in range(int(area ** 0.5), 0, -1):
            if area % i == 0:
                return [area // i, i]


obj = Solution()
n = 37
print(obj.constructRectangle2(n))
