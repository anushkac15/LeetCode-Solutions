# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        st = []

        while head != None:
            st.append(head.val)
            head = head.next

        for i in range(len(st)//2):
            if st[i]!=st[len(st)-1-i]:
                return False
        return True
        
        