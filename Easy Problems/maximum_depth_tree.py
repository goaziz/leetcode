class TreeNode:
    def __init__(self, val=0, right=None, left=None):
        self.val = val
        self.right = right
        self.left = left


class Solution:
    def __init__(self):
        self.root = None

    def insert(self, val):
        if self.root == None:
            self.root = TreeNode(val)
        else:
            self._insert(val, self.root)

    def _insert(self, val, node):
        if node.val > val:
            if node.left == None:
                node.left = TreeNode(val)
            else:
                self._insert(val, node.left)
        else:
            if node.right == None:
                node.right = TreeNode(val)
            else:
                self._insert(val, node.right)

    def maxDepth(self, node):
        if node == None:
            return 0
        leftDepth = self.maxDepth(node.left)
        rightDepth = self.maxDepth(node.right)

        if leftDepth > rightDepth:
            return leftDepth + 1
        return rightDepth + 1

    def print_in_order(self, node):
        if node == None:
            return
        self.print_in_order(node.left)
        print(node.val)
        self.print_in_order(node.right)


tree = Solution()
tree.insert(4)
tree.insert(3)
tree.insert(6)
tree.insert(5)
tree.insert(7)
# tree.print_in_order(tree.root)
print(tree.maxDepth(tree.root))
