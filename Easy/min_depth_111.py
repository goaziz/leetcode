from collections import deque
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # def minDepth(self, root: Optional[TreeNode]) -> int:
    #     if not root:
    #         return 0

    #     queue = deque([(root, 1)])

    #     while queue:
    #         node, depth = queue.popleft()

    #         if not node.left and not node.right:
    #             return depth
    #         if node.left:
    #             queue.append((node.left, depth + 1))
    #         if node.right:
    #             queue.append((node.right, depth + 1))

    #     return 0

    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        min_depth = 1
        queue = deque([root])

        while queue:
            level_size = len(queue)

            for _ in range(level_size):
                node = queue.popleft()

                if not node.left and not node.right:
                    return min_depth

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            min_depth += 1

        return min_depth
