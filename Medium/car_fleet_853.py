from typing import List


class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = sorted(zip(position, speed), key=lambda x: -x[0])
        stack = []
        
        for pos, spd in cars:
            time = (target - pos) / spd
            
            if not stack or stack[-1] < time:
                stack.append(time)
        
        return len(stack)
        


obj = Solution()
target = 12
position = [10, 8, 0, 5, 3]
speed = [2, 4, 1, 1, 3]
print(obj.carFleet(target, position, speed))
