from typing import List


class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        result = []

        for i in nums1:
            next_greater = -1
            idx = nums2.index(i)
            for j in nums2[idx:]:
                if i < j:
                    next_greater = j
                    break
                else:
                    next_greater = -1

            result.append(next_greater)

        return result

    def nextGreaterElement2(self, nums1: List[int], nums2: List[int]) -> List[int]:
        hashmap = {}
        stack = []

        for i in nums2:
            while stack and i > stack[-1]:
                hashmap[stack.pop()] = i
            stack.append(i)

        while stack:
            hashmap[stack.pop()] = -1

        result = [hashmap.get(num, -1) for num in nums1]

        return result


obj = Solution()
nums1 = [2, 4]
nums2 = [1, 2, 3, 4]
print(obj.nextGreaterElement2(nums1, nums2))
