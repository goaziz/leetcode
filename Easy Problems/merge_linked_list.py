class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next


class Solution:
    def mergeTwoLists(self, l1, l2):
        tmp = None
        if l1 is None:
            return l2
        if l2 is None:
            return l1

        if l1.data <= l2.data:
            tmp = l1
            tmp.next = self.mergeTwoLists(l1.next, l2)
        else:
            tmp = l2
            tmp.next = self.mergeTwoLists(l1, l2.next)
        return tmp
