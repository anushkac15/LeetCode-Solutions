# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        res = ListNode()
        dummy = res

        carry =0

        while l1 or l2 or carry:

            l1Val = l1.val if l1 else 0
            l2Val = l2.val if l2 else 0

            sum = l1Val+l2Val+carry
            carry=sum//10
            digit =sum%10

            res.next = ListNode(digit)
            res=res.next

            if l1: l1 = l1.next
            if l2:  l2=l2.next

        return dummy.next