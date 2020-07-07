class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def __init__(self):
        self.head = None

    def push(self, data):
        new_node = ListNode(data)
        new_node.next = self.head
        self.head = new_node

    def addTwoNumbers(self, l1, l2, c=0):
        val = l1.val + l2.val + c
        c = val // 10
        res = ListNode(val % 10)

        if (l1.next != None or l2.next != None or c != 0):
            if l1.next == None:
                l1.next = ListNode(0)
            if l2.next == None:
                l2.next = ListNode(0)
            res.next = self.addTwoNumbers(l1.next, l2.next, c)
        return res

    def printList(self):
        tmp = self.head
        arrow = ''
        while tmp:
            arrow += str(tmp.val) + '-->'
            tmp = tmp.next
        print(arrow)


l1 = Solution()
l2 = Solution()

l1.push(2)
l1.push(3)
l1.push(5)
print(l1.printList())

l2.push(4)
l2.push(3)
l2.push(8)
print(l2.printList())

res = Solution()
res.addTwoNumbers(l1.head, l2.head)
print(res.printList())
