from typing import List


class Solution:
    def countGoodRectangles(self, rectangles: List[List[int]]) -> int:
        max_len = 0
        count = 0

        for rectangle in rectangles:
            square = min(rectangle)
            if max_len < square:
                count = 1
                max_len = square
            elif max_len == square:
                count += 1

        return count

    def countGoodRectangles2(self, rectangles: List[List[int]]) -> int:
        length = []

        for rectangle in rectangles:
            length.append(min(rectangle))

        max_len = max(length)
        return length.count(max_len)


obj = Solution()
rectangles = [[5, 8], [3, 9], [5, 12], [16, 5]]
print(obj.countGoodRectangles(rectangles))
