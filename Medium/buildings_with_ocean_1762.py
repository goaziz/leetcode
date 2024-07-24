from typing import List


class Solution:
    def findBuildings(self, heights: List[int]) -> List[int]:
        stack = []

        for i in range(len(heights)):
            while stack and heights[stack[-1]] <= heights[i]:
                stack.pop()

            stack.append(i)

        return stack

    def findBuildings2(self, heights: List[int]) -> List[int]:
        n = len(heights)
        res = []
        stack = []

        for i in reversed(range(n)):
            while stack and heights[stack[-1]] < heights[i]:
                stack.pop()

            if not stack:
                res.append(i)

            stack.append(i)
        res.reverse()

        return res

    def findBuildings3(self, heights: List[int]) -> List[int]:
        max_height = -1
        res = []
        
        for i in reversed(range(len(heights))):
            
            if max_height < heights[i]:
                res.append(i)
                
                max_height = heights[i]
        res.reverse()
        return res

obj = Solution()
heights = [1, 3, 2, 4]
print(obj.findBuildings3(heights))
