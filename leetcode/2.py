# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
#
#
# class Solution:
#     def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
#         l1_string = ""
#         while l1:
#             l1_string = str(l1.val) + l1_string
#             l1 = l1.next
#
#         l2_string = ""
#         while l2:
#             l2_string = str(l2.val) + l2_string
#             l2 = l2.next
#
#         l_sum = str(int(l1_string) + int(l2_string))
#
#         l3 = ListNode(int(l_sum[-1]))
#         itr = l3
#
#         for numIdx in range(-2, -len(l_sum) - 1, -1):
#             itr.next = ListNode(int(l_sum[numIdx]))
#             itr = itr.next
#
#         return l3
#


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:

        if l1 and l1.next and l2:
            val1 = l1.val
            val2 = l2.val
            l1.val = val1 + val2
            if l1.val >= 10:
                l1.val = int(str(l1.val)[1])
                carry = 1
                temp = l1.next.val
                if not l2.next:
                    l2.next = ListNode(0)
                l1.next.val = temp + carry
            self.addTwoNumbers(l1.next, l2.next)
        elif l2 and l2.next and not l1.next:
            l1.next = ListNode(0)
            val1 = l1.val
            val2 = l2.val
            l1.val = val1 + val2
            if l1.val >= 10:
                l1.val = int(str(l1.val)[1])
                carry = 1
                temp = l1.next.val
                l1.next.val = temp + carry
            self.addTwoNumbers(l1.next, l2.next)

        else:
            if not l1 or not l2:
                return l1
            val1 = l1.val
            val2 = l2.val
            if (val1 + val2) >= 10:

                l1.val = int(str(val1 + val2)[1])
                carry = 1
                l1.next = ListNode(carry)
            else:
                l1.val = l1.val + l2.val
            return l1
        return l1
