from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    result = False

    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False

        if root.left is None and root.right is None:
            return root.val == targetSum

        r = targetSum - root.val

        return self.hasPathSum(root.left, r) or self.hasPathSum(root.right, r)

    def hasPathSum2(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False

        stack = [(root, targetSum - root.val)]

        while stack:
            node, r = stack.pop()

            if not node.left and not node.right and r == 0:
                return True
            if node.left:
                stack.append((node.left, r - node.left.val))
            if node.right:
                stack.append((node.right, r - node.right.val))
        
        return False
