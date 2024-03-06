# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def gameResult(self, head: Optional[ListNode]) -> str:
        even_team = []
        odd_team = []
        curr = head

        while curr:
            if curr.val % 2 == 0:
                even_team.append(curr.val)
            else:
                odd_team.append(curr.val)

            curr = curr.next

        even_team_point = 0
        odd_team_point = 0
        for even, odd in zip(even_team, odd_team):
            if even > odd:
                even_team_point += 1
            elif odd > even:
                odd_team_point += 1

        if even_team_point > odd_team_point:
            return 'Even'
        elif odd_team_point > even_team_point:
            return 'Odd'
        else:
            return 'Tie'

    def gameResult2(self, head: Optional[ListNode]) -> str:
        even = 0
        odd = 0
        curr = head

        while curr:
            if curr.val > curr.next.val:
                even += 1
            elif curr.val < curr.next.val:
                odd += 1
            curr = curr.next.next

        if even > odd:
            return 'Even'
        elif odd > even:
            return 'Odd'
        else:
            return 'Tie'


obj = Solution()
head = ListNode(2)
head.next = ListNode(5)
head.next.next = ListNode(4)
head.next.next.next = ListNode(7)
head.next.next.next.next = ListNode(20)
head.next.next.next.next.next = ListNode(5)
print(obj.gameResult2(head))
