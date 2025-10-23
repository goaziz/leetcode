from collections import deque
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        count = 0

        if not root:
            return count

        queue = deque([root])

        while queue:
            node = queue.popleft()
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

            count += 1

        return count

    def countNodes2(self, root: Optional[TreeNode]) -> int:
        return self.dfs(root)

    def dfs(self, node):
        if not node:
            return 0

        return 1 + self.dfs(node.left) + self.dfs(node.right)


root = TreeNode(1)
root.left = TreeNode(2)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right = TreeNode(3)
root.right.left = TreeNode(6)

obj = Solution()
print(obj.countNodes2(root))
