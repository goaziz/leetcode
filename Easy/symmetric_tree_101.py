from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return

        return self.is_symmetric(root, root)

    def is_symmetric(self, a, b):
        if not a and not b:
            return True

        if not a or not b:
            return False

        if a.val != b.val:
            return False

        return self.is_symmetric(a.left, b.right) and self.is_symmetric(a.right, b.left)
