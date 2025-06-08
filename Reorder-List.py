# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        \\\
        Do not return anything, modify head in-place instead.
        \\\

        slow = head
        fast = head

        while slow and fast and fast.next:
            slow = slow.next 
            fast = fast.next.next

        secondH = slow.next 
        slow.next = None
        node = None

        while secondH:
            nextNode = secondH.next
            secondH.next = node
            node = secondH
            secondH = nextNode

        first = head
        second = node

        while first and second:
            temp1 = first.next
            temp2 = second.next

            first.next = second
            second.next = temp1

            first = temp1
            second = temp2

            







        