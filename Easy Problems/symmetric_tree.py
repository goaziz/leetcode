class Node:
    def __init__(self, val=0, right=None, left=None):
        self.val = val
        self.right = right
        self.left = left


class Tree:
    def __init__(self):
        self.root = None

    def insert(self, val):
        if self.root == None:
            self.root = Node(val)
        else:
            self._insert(val, self.root)

    def _insert(self, val, node):
        if node.val > val:
            if node.left == None:
                node.left = Node(val)
            else:
                self._insert(val, node.left)
        else:
            if node.right == None:
                node.right = Node(val)
            else:
                self._insert(val, node.right)

    def isSymmetric(self, node) -> bool:
        return self.isMirror(node, node)

    def isMirror(self, t1, t2):
        if not t1 and not t2: return True
        if not t1 or not t2: return False
        return t1.val == t2.val and self.isMirror(t1.right, t2.left) and self.isMirror(t1.left, t2.right)

    def search(self, data):
        if self.root != None:
            return self._search(data, self.root)
        else:
            return None

    def _search(self, val, node):
        # if val == node.val:
        #     return node
        # if val < node.val:
        #     if node.left:
        #         return self._search(val, node.left)
        #     else:
        #         return None
        # else:
        #     if node.right:
        #         return self._search(val, node.right)
        #     else:
        #         return None

        # alternative
        # if node == None or node.val == val:
        #     return node
        # if val < node.val:
        #     return self._search(val, node.left)
        # if val > node.val:
        #     return self._search(val, node.right)

        while node != None:
            if val == node.val:
                return node
            if val < node.val:
                node = node.left
            if val > node.val:
                node = node.right
        return node

    def in_order(self, node):
        if node == None:
            return
        else:
            print(node.val)
            self.in_order(node.right)
            self.in_order(node.left)


tree = Tree()
tree.insert(1)
tree.insert(2)
tree.insert(2)
tree.insert(3)
tree.insert(4)
tree.insert(4)
tree.insert(3)
# tree.in_order(tree.root)
print('Found value ', tree.search(3).val)
# print(tree.search(4).val)
