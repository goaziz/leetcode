from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def insert(self, nums, start, end):
        if start > end:
            return None

        mid = (end + start) // 2
        root = TreeNode(nums[mid])

        root.left = self.insert(nums, start, mid - 1)
        root.right = self.insert(nums, mid + 1, end)

        return root

    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        return self.insert(nums, 0, len(nums) - 1)

    def sortedArrayToBST2(self, nums: List[int]) -> Optional[TreeNode]:
        if not nums:
            return None

        mid = len(nums) // 2
        root = TreeNode(nums[mid])
        root.left = self.sortedArrayToBST(nums[:mid])
        root.right = self.sortedArrayToBST(nums[mid + 1:])

        return root


obj = Solution()
nums = [-10, -3, 0, 5, 9]
root = obj.sortedArrayToBST(nums)
