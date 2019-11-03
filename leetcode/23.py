# Merge k sorted linked lists and return it as one sorted list. Analyze and describe its complexity.
#
# Example:
#
# Input:
# [
#   1->4->5,
#   1->3->4,
#   2->6
# ]
# Output: 1->1->2->3->4->4->5->6


# modules to consider on next iteration:
# from heapq import heappush, heappop, heapreplace, heapify

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        if len(lists) == 0 or (len(lists) == 1 and not lists[0]):
            return None
        fin_list = []
        for l in lists:
            if l:
                self.parser(l, l.val, fin_list)
        s = sorted(fin_list)
        node = [ListNode(i) for i in s]
        for i in range(len(node) - 1):
            node[i].next = node[i + 1]

        return node[0] if node else  None

    def parser(self, lists, target, fin_list):
        fin_list.append(target)
        if lists.next == None:
            return
        return self.parser(lists.next, lists.next.val, fin_list)
