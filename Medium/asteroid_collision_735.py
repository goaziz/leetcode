from typing import List


class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []

        for asteroid in asteroids:
            while stack and stack[-1] > 0 and asteroid < 0:
                if stack[-1] < abs(asteroid):
                    stack.pop()
                    continue
                elif stack[-1] > abs(asteroid):
                    break
                else:
                    stack.pop()
                    break
            else:
                stack.append(asteroid)

        return stack


obj = Solution()
asteroids = [-2, -2, 3, -2]
print(obj.asteroidCollision(asteroids))
