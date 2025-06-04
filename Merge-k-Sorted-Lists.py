# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:

        def TwoSortedLists(list1, list2):

            dummy = ListNode()
            res = dummy
            while list1 and list2:
                if list1.val <list2.val:
                    res.next = list1
                    list1= list1.next

                else:
                    res.next = list2
                    list2=list2.next

                res = res.next

            if list1:
                res.next = list1
            if list2:
                res.next = list2

            return dummy.next

            
        if not lists or len(lists) == 0:
            return None
        
        while len(lists) > 1:
            temp = []
            for i in range(0, len(lists), 2):
                l1 = lists[i]
                l2 = lists[i+1] if i + 1 < len(lists) else None
                temp.append(TwoSortedLists(l1, l2))
            lists = temp
        
        return lists[0]

        