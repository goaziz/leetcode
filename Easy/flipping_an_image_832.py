from typing import List


class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        for row in range(len(image)):
            for col in range(len(image[row])):
                if image[row][col] == 0:
                    image[row][col] = 1
                else:
                    image[row][col] = 0

            image[col] = image[row][::-1]

        return image

    def flipAndInvertImage2(self, image: List[List[int]]) -> List[List[int]]:
        for idx, val in enumerate(image):
            val.reverse()
            image[idx] = [abs(i - 1) for i in val]
            
        return image


obj = Solution()
image = [[1, 1, 0, 0], [1, 0, 0, 1], [0, 1, 1, 1], [1, 0, 1, 0]]
print(obj.flipAndInvertImage2(image))
