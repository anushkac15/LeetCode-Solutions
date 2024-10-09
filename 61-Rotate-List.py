# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or not head.next or k == 0:
            return head

        stack = []
        current = head
        
        while current:
            stack.append(current.val)
            current = current.next
        
        length = len(stack)
        k = k % length
        
        if k == 0:
            return head
        
        new_head_values = stack[-k:] + stack[:-k]
        
        new_head = ListNode(new_head_values[0])
        current = new_head
        
        for val in new_head_values[1:]:
            current.next = ListNode(val)
            current = current.next
        
        return new_head
