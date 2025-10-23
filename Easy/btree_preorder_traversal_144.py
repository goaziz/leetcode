from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        nums = []
        self.traverse(root, nums)

        return nums

    def traverse(self, node, nums):
        if not node:
            return None

        nums.append(node.val)
        self.traverse(node.left, nums)
        self.traverse(node.right, nums)


tree = TreeNode(1)
tree.right = TreeNode(2)
tree.right.left = TreeNode(3)
obj = Solution()
print(obj.preorderTraversal(tree))
