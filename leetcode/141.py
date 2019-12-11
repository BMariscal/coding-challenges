# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        fast_runner = head
        slow_runner = head

        while fast_runner != None and fast_runner.next != None:
            fast_runner = fast_runner.next.next
            slow_runner = slow_runner.next

            if slow_runner is fast_runner:
                return True

        return False

    