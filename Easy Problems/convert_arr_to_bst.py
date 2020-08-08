class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __init__(self):
        self.root = None

    def insert(self, val):
        if self.root == None:
            self.root = TreeNode(val, self.root)
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

    def sortedArrayToBST(self, nums):
        if not nums:
            return None
        mid = len(nums) // 2
        root = TreeNode(nums[mid])
        root.left = self.sortedArrayToBST(nums[:mid])
        root.right = self.sortedArrayToBST(nums[mid + 1:])
        return root

    def printList(self, node):
        if node == None:
            return
        else:
            print(node.val)
            self.printList(node.left)
            self.printList(node.right)


tree = Solution()
arr = [1, 2, 3, 4, 5, 6, 7]
root = tree.sortedArrayToBST(arr)
tree.printList(root)
