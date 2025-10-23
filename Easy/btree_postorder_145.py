from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        nums = []
        self.traverse(root, nums)

        return nums

    def traverse(self, node, nums):
        if not node:
            return None

        self.traverse(node.left, nums)
        self.traverse(node.right, nums)
        nums.append(node.val)
