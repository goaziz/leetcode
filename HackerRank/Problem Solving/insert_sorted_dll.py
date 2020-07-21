class Node:
    def __init__(self, val=0, next=None, prev=None):
        self.val = val
        self.next = next
        self.prev = prev


class DoublyLinkedList:
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

    def sortedInsert(self, node):
        node = Node(node)
        # tmp = self.head
        if self.head == None:
            return node
        elif node < self.head.val:
            node.next = self.head
            self.head.prev = node
            return node
        else:
            node = self.sortedInsert(node)
            self.head.next = node
            node.prev = self.head
            return self.head

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


ll = DoublyLinkedList()
ll.push(10)
ll.push(1)
ll.push(7)
ll.push(7)
ll.push(4)
ll.push(2)
# ll.sortedInsert(9)
ll.reverseList()
ll.printList()
