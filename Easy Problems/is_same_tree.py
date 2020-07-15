class TreeNode:
    def __init__(self, val=0, right=None, left=None):
        self.val = val
        self.right = right
        self.left = left


class Solution:
    def __init__(self):
        self.root = None

    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        if not p and not q:
            return True
        if not p or not q:
            return False
        if p.val != q.val:
            return False
        return self.isSameTree(p.right, q.right) and self.isSameTree(p.left, q.left)

    def add_child(self, val):
        if self.root == None:
            self.root = TreeNode(val)
        else:
            self.insert(val, self.root)

    def insert(self, data, node):
        if node.val > data:
            if node.left == None:
                node.left = TreeNode(data)
            else:
                self.insert(data, node.left)
        else:
            if node.right == None:
                node.right = TreeNode(data)
            else:
                self.insert(data, node.right)

    def in_order(self, node):
        if node == None:
            return
        else:
            print(node.val)
            self.in_order(node.left)
            self.in_order(node.right)


obj = Solution()
obj.add_child(4)
obj.add_child(5)
obj.add_child(7)
obj.add_child(8)
obj.add_child(8)
obj.add_child(6)
obj.add_child(8)
print('nodes')
obj.in_order(obj.root)