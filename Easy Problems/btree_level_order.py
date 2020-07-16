class TreeNode:
    def __init__(self, val=0, right=None, left=None):
        self.val = val
        self.left = left
        self.right = right

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


    def levelOrderBottom(self, node):
        if node == None:
            return
        else:
            self.levelOrderBottom(node.left)
            self.levelOrderBottom(node.right)
            print(node.val)

    def levelOrderBottom2(self, node):
        stack = [(node, 0)]
        res = []
        while stack:
            node, level = stack.pop()
            if node:
                if len(res) < level + 1:
                    res.insert(0, [])
                res[-(level+1)].append(node.val)
                stack.append((node.right, level+1))
                stack.append((node.left, level+1))

        return res

tree = Solution()
tree.insert(3)
tree.insert(9)
tree.insert(20)
tree.insert(15)
tree.insert(7)
print(tree.levelOrderBottom(tree.root))
print(tree.levelOrderBottom2(tree.root))