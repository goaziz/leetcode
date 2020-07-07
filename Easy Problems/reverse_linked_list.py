class Node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None


    def push(self, data):
        new_node = Node(data, self.head)
        self.head = new_node

    def printList(self):
        tmp = self.head
        arr = ''
        while tmp:
            arr += str(tmp.val) + '-->'
            tmp = tmp.next
        print(arr)

    def reverseList(self):
        prev = None
        current = self.head

        while current != None:
            next = current.next
            current.next = prev
            prev = current
            current = next
        self.head = prev
        return prev

ll = LinkedList()
ll.push(2)
ll.push(3)
ll.push(4)
ll.push(5)
ll.printList()
ll.reverseList()
ll.printList()