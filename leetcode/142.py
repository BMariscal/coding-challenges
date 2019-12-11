# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        if head == None: return None
        if head.next == None: return None
        visited = {}
        visited[head] = True
        first = head.next

        while first:
            if first in visited:
                return first

            visited[first] = True
            first = first.next

        return None