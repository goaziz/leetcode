class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def __init__(self) -> None:
        self.head = None

    def append(self, data, head):
        new_node = ListNode(data)

        if head is None:
            new_node.next = head
            head = new_node
        else:
            current = head
            while current.next:
                current = current.next

            current.next = new_node

        return head

    def deleteDuplicatesUnsorted(self, head: ListNode) -> ListNode:
        freq = {}
        current = head

        while current:
            val = current.val
            freq[val] = freq.get(val, 0) + 1

            current = current.next

        sentinel = ListNode(0)
        tail = sentinel

        for key, value in freq.items():
            if value == 1:
                new_node = ListNode(key)
                tail.next = new_node
                tail = new_node

        return sentinel.next

    def print_list(self, head):
        current = head
        while current:
            print(str(current.val), end=' --> ')
            current = current.next


obj = Solution()
head = None
head = obj.append(2, head)
head = obj.append(1, head)
head = obj.append(2, head)
head = obj.append(2, head)
# obj.print_list(head)
head = obj.deleteDuplicatesUnsorted(head)
# print()
obj.print_list(head)
