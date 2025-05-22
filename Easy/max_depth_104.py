from collections import deque
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        level = 0
        result = []

        if not root:
            return 0

        self.traverse(root, level, result)

        return max(result) + 1

    def traverse(self, node, level, result):
        if not node:
            return

        if len(result) == level:
            result.append(level)

        self.traverse(node.left, level + 1, result)
        self.traverse(node.right, level + 1, result)

    def maxDepth2(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        return max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1

    def maxDepth3(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        depth = 0
        queue = deque([root])
        
        while queue:
            level_size = len(queue)
            
            for _ in range(level_size):
                node = queue.popleft()
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            depth += 1
        
        return depth