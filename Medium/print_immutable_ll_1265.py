class ImmutableListNode:
    def __init__(self, value, next=None):
        self._value = value
        self._next = next

    def printValue(self) -> None:
        print(self._value)

    def getNext(self) -> 'ImmutableListNode':
        return self._next


class Solution:
    def printLinkedListInReverse(self, head: ImmutableListNode) -> None:

        if head is not None:
            self.printLinkedListInReverse(head.getNext())
            head.printValue()

    def printLinkedListInReverse2(self, head: ImmutableListNode) -> None:
        stack = []
        
        while head:
            stack.append(head)
            head = head.getNext()
        
        while stack:
            node = stack.pop()
            node.printValue()
        

node3 = ImmutableListNode(3)
node2 = ImmutableListNode(2, node3)
node1 = ImmutableListNode(1, node2)
obj = Solution()
obj.printLinkedListInReverse2(node1)
