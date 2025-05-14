from collections import deque
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not q and not p:
            return True
        if not p or not q:
            return False

        p_queue = deque([p])
        q_queue = deque([q])

        while p_queue and q_queue:
            p_node = p_queue.popleft()
            q_node = q_queue.popleft()

            if p_node.val != q_node.val:
                return False

            if bool(p_node.left) != bool(q_node.left):
                return False
            if bool(p_node.right) != bool(q_node.right):
                return False

            if p_node.left:
                p_queue.append(p_node.left)
            if q_node.left:
                q_queue.append(q_node.left)

            if p_node.right:
                p_queue.append(p_node.right)
            if q_node.right:
                q_queue.append(q_node.right)

        return not p_queue and not q_queue

    def isSameTree2(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not q and not p:
            return True

        if not p or not q:
            return False

        if p.val != q.val:
            return False

        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
