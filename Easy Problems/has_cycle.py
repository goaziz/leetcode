class Node:
    def __init__(self, x=None, next=None):
        self.val = x
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

    def hasCysle(self):
        head = self.head
        if head == None or head.next == None:
            return False

        slow = head
        fast = head.next

        while slow != fast:
            if fast == None or fast.next == None:
                return False
            slow = slow.next
            fast = fast.next.next
        return True

ll = LinkedList()

ll.push(2)
ll.push(3)
ll.push(4)
ll.printList()
print(ll.hasCysle())