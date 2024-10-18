from typing import List


class Solution:
    def twoOutOfThree(self, nums1: List[int], nums2: List[int], nums3: List[int]) -> List[int]:

        freq = {}
        seen = set()
        result = set()

        for num1 in nums1:
            freq[num1] = freq.get(num1, 0) + 1

        for num2 in nums2:
            if num2 in freq:
                result.add(num2)
            else:
                seen.add(num2)

        for num3 in nums3:
            if num3 in freq or num3 in seen:
                result.add(num3)

        return list(result)


nums1 = [1, 2, 2]
nums2 = [4, 3, 3]
nums3 = [5]
obj = Solution()
print(obj.twoOutOfThree(nums1, nums2, nums3))
