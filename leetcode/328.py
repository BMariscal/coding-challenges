# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        # O(n) time complexity
        even = []
        odd = []
        index = 0
        temp_list = head
        while head != None:
            val = head.val
            if index % 2 == 0:
                odd.append(val)
            else:
                even.append(val)
            index += 1
            temp = head.next
            head = temp
        even_i = 0
        odd_i = 0
        head = temp_list
        len_even = len(even)
        len_odd = len(odd)
        fin = temp_list
        while head != None:
            if odd_i < len_odd:
                odd_val = odd[odd_i]
                head.val = odd_val
                odd_i += 1
            elif even_i < len_even:
                even_val = even[even_i]
                head.val = even_val
                even_i += 1
            temp = head.next
            head = temp
        return fin



