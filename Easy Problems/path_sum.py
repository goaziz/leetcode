class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __init__(self):
        self.root = None

    def hasPathSum(self, node, sum):
        if not node:
            return False
        if not node.left and not node.right and node.val == sum:
            return True

        sum -= node.val
        return self.hasPathSum(node.left, sum) or self.hasPathSum(node.right, sum)


