from collections import deque
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def is_leaf(self, node: Optional['TreeNode']) -> bool:
        return bool(node) and node.left is None and node.right is None

    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        left = root.left.val if (
            root.left and not root.left.left and not root.left.right) else 0
        return left + self.sumOfLeftLeaves(root.left) + self.sumOfLeftLeaves(root.right)

    def sumOfLeftLeaves2(self, root: Optional['TreeNode']) -> int:
        if not root:
            return 0

        q = deque([root])
        total = 0

        while q:
            node = q.popleft()

            # if the left child is a leaf, add its value
            if node.left:
                if self.is_leaf(node.left):
                    total += node.left.val
                else:
                    q.append(node.left)

            # only enqueue right if it's not a leaf (no need to visit a leaf right child)
            if node.right:
                if not self.is_leaf(node.right):
                    q.append(node.right)

        return total


root = TreeNode(3)
root.left = TreeNode(9)
root.right= TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)

obj = Solution()
print(obj.sumOfLeftLeaves2(root))
