class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def add_child(self, data):
        if self.data == data:
            return
        if data < self.data:
            if self.left:
                self.left.add_child(data)
            else:
                self.left = TreeNode(data)
        else:
            if self.right:
                self.right.add_child(data)
            else:
                self.right = TreeNode(data)

    def in_order_traversal(self):
        arr = []

        if self.left:
            arr += self.left.in_order_traversal()

        arr.append(self.data)

        if self.right:
            arr += self.right.in_order_traversal()

        return arr

    def search(self, val):
        if self.data == val:
            return True

        if val < self.data:
            if self.left:
                return self.left.search(val)
            return False

        if val > self.data:
            if self.right:
                return self.right.search(val)
            return False

    def find_min(self):
        if self.left is None:
            return self.data
        return self.left.find_min()

    def find_max(self):
        if self.right is None:
            return self.data
        return self.right.find_max()

    def calculate_sum(self):
        left_sum = self.left.calculate_sum() if self.left else 0
        right_sum = self.right.calculate_sum() if self.right else 0
        return self.data + left_sum + right_sum


def build_tree(arr):
    root = TreeNode(arr[0])

    for i in range(1, len(arr)):
        root.add_child(arr[i])

    return root


if __name__ == '__main__':
    num = [17, 1, 4, 20, 5, 8, 7, 25, 25]
    num_tree = build_tree(num)
    print(num_tree.in_order_traversal())
    # print(num_tree.search(2))
    print(num_tree.calculate_sum())
