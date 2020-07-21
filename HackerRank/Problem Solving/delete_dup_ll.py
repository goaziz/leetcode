class Node:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next


class LinkedList:
    def __init__(self):
        self.head = None

    def push(self, node):
        new_node = Node(node, self.head)
        self.head = new_node

    def printList(self):
        tmp = self.head
        arr = ''
        while tmp:
            arr += str(tmp.val) + '-->'
            tmp = tmp.next
        print(arr)

    def removeDuplicate(self):
        tmp = self.head
        if tmp is None:
            return tmp

        curr = tmp.next
        prev = tmp

        while curr != None:
            if curr.val == prev.val:
                prev.next = curr.next
                curr = curr.next
            else:
                curr = curr.next
                prev = prev.next
        return tmp

ll = LinkedList()
ll.push(1)
ll.push(2)
ll.push(2)
ll.push(3)
ll.push(4)
ll.printList()
ll.removeDuplicate()
ll.printList()