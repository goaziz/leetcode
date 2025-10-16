from collections import deque
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        return self.is_balanced(root) != float('-inf')

    def is_balanced(self, node):
        if not node:
            return -1

        height = float('-inf')

        left_height = self.is_balanced(node.left)
        if left_height == height:
            return height

        right_height = self.is_balanced(node.right)
        if right_height == height:
            return height

        if abs(left_height - right_height) > 1:
            return height

        return max(left_height, right_height) + 1
