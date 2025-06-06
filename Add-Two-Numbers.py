# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        temp = ListNode()
        res = temp

        carry =0

        while l1 or l2 or carry:

            l1Val = l1.val if l1 else 0
            l2Val = l2.val if l2 else 0

            total = l1Val+l2Val+ carry
            carry = total//10
            digit = total%10

            temp.next = ListNode(digit)
            temp = temp.next

            if l1: l1=l1.next
            if l2 : l2 = l2.next

        return res.next