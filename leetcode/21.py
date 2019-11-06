# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
# Cooler solution I found:
# class Solution:
#    def mergeTwoLists(self, a, b):
#        if a and b:
#            if a.val > b.val:
#                a, b = b, a
#            a.next = self.mergeTwoLists(a.next, b)
#        return a or b

# class Solution:
#     def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
#         current = ListNode(-1) # dummy node for head
#         head = current
#         while l1 and l2:
#             if l1.val < l2.val:
#                 current.next = l1
#                 l1 = l1.next
#             else:
#                 current.next = l2
#                 l2 = l2.next
#             current = current.next
#         current.next = l1 if l1 else l2
#         return head.next

from heapq import heappush, heappop


class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if not l1 and not l2:
            return None
        if not l1: return l2
        if not l2: return l1

        h1 = []
        while l1 != None or l2 != None:
            if l1:
                heappush(h1, l1.val)
                l1 = l1.next
            if l2:
                heappush(h1, l2.val)
                l2 = l2.next

        l = [ListNode(heappop(h1)) for i in range(len(h1))]
        i = 0

        while i < len(l) - 1:
            l[i].next = l[i + 1]
            i += 1

        return l[0]

