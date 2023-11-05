from typing import List


class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:

        for i in range(len(nums) - 1):
            for j in range(i + 1, len(nums)):
                if nums[i] == nums[j] and abs(i - j) <= k:
                    return True

        return False

    def containsNearbyDuplicate2(self, nums: List[int], k: int) -> bool:
        hashmap = {}

        for i in range(len(nums)):
            if nums[i] in hashmap:
                idx = hashmap[nums[i]]
                if abs(i - idx) <= k:
                    return True
            hashmap[nums[i]] = i

        return False

    def containsNearbyDuplicate3(self, nums: List[int], k: int) -> bool:
        # not mine
        window = set()
        L = 0
        for R in range(len(nums)):
            if R - L > k:
                window.remove(nums[L])
                L += 1
            if nums[R] in window:
                return True
            window.add(nums[R])
        return False


obj = Solution()
nums = [1, 1]
k = 3
print(obj.containsNearbyDuplicate3(nums, k))
