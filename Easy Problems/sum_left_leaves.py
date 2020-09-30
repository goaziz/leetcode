class Node:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        self.children = []


class Tree:
    def __init__(self):
        self.root = None

    def insert(self, val):
        if self.root is None:
            self.root = Node(val)
        else:
            self._insert(val, self.root)

    def _insert(self, val, node):
        if node.val > val:
            if node.left is None:
                node.left = Node(val)
            else:
                self._insert(val, node.left)
        else:
            if node.right is None:
                node.right = Node(val)
            else:
                self._insert(val, node.right)

    def isLeaf(self, node):
        if node == None:
            return False
        if node.left == None and node.right == None:
            return True
        return False

    def sumLeftLeafNodes(self, node):
        sum = 0
        if node != None:
            if self.isLeaf(node.left):
                sum += node.left.val
            else:
                sum += self.sumLeftLeafNodes(node.left)
            sum += self.sumLeftLeafNodes(node.right)
        return sum

    def in_order(self, node):
        if node is None:
            return
        print(node.val)
        self.in_order(node.right)
        self.in_order(node.left)


tree = Tree()
tree.insert(1)
tree.insert(3)
tree.insert(4)
tree.insert(5)
tree.insert(8)
tree.insert(6)
tree.insert(9)
# print(tree.sumLeftLeafNodes(tree.root))
# print(tree.similar_leaf(tree.root, tree.root))
print(tree.sumLeftLeafNodes(tree.root))
