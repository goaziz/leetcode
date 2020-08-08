import collections

class TreeNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, val):
        new_node = TreeNode(val, self.head)
        self.head = new_node

    def isPalindrome(self):
        queue = collections.deque([])
        current = self.head
        while current != None:
            queue.append(current)
            current = current.next

        while len(queue) >= 2:
            if queue.popleft().val != queue.pop().val:
                return False
        return True

    def printList(self):
        tmp = self.head
        arr = ''
        while tmp:
            arr += str(tmp.val) + '-->'
            tmp = tmp.next
        print(arr)

list = LinkedList()
list.insert(0)
list.insert(0)
list.printList()
print(list.isPalindrome())