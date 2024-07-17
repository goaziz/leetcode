class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:

    def __init__(self) -> None:
        self.head = None

    def append(self, data: int, head: ListNode) -> ListNode:
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

    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        a_count = 0
        previous = None
        current = list1
        end = None

        while current:

            if a_count == a:
                for _ in range(a, b + 1):
                    current = current.next

                previous.next = list2
                end = current
                break

            a_count += 1
            previous = current
            current = current.next

        while list2.next:
            list2 = list2.next

        list2.next = end

        return list1

    def mergeInBetween2(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        start = None
        end = list1
        
        for idx in range(b):
            if idx == a - 1:
                start = end
            end = end.next
        
        start.next = list2
        
        while list2.next:
            list2 = list2.next
        list2.next = end.next
        end.next = None
        
        return list1

    def print_list(self, head):
        while head:
            print(str(head.val), end=' --> ')
            head = head.next


obj = Solution()
head = None
head = obj.append(10, head)
head = obj.append(1, head)
head = obj.append(13, head)
head = obj.append(6, head)
head = obj.append(9, head)
head = obj.append(5, head)
head2 = None
head2 = obj.append(1000, head2)
head2 = obj.append(1002, head2)
head2 = obj.append(1003, head2)

head = obj.mergeInBetween(head, 3, 4, head2)
obj.print_list(head)
