class Node:
    def __init__(self, val=0, next=None):
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

    def findMerged(self, l1, l2):
        curr1 = self.head
        curr2 = self.head

        while curr1 != curr2:
            if curr1.next == None:
                curr1 = l1
            else:
                curr1 = curr1.next
            if curr2.next == None:
                curr2 = l2
            else:
                curr2 = curr2.next

        return curr2.val


ll = LinkedList()
ll.push(2)
ll.push(3)
ll.push(4)
ll.push(5)
ll.push(6)
ll.printList()
print(ll.findMerged(3, 4))
