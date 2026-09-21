# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: list[ListNode | None]) -> ListNode | None:

        if not lists:
            return None

        def mergeList(l1, l2):

            res = ListNode()
            dummy = res

            while l1 and l2:
                if l1.val < l2.val:
                    dummy.next = l1
                    l1 = l1.next

                else:
                    dummy.next = l2
                    l2 = l2.next

                dummy = dummy.next

            while l1:
                dummy.next = l1
                l1 = l1.next
                dummy = dummy.next

            while l2:
                dummy.next = l2
                l2 = l2.next
                dummy = dummy.next

            return res.next

        while len(lists) > 1:

            mergedLists = []

            for i in range(0, len(lists), 2):

                l1 = lists[i]
                l2 = lists[i + 1] if i + 1 < len(lists) else None

                mergedLists.append(mergeList(l1, l2))

            lists = mergedLists

        return lists[0]
