# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: ListNode | None) -> ListNode | None:

        prev = None

        while head:
            nextNode = head.next
            head.next = prev
            prev = head
            head = nextNode

        return prev
