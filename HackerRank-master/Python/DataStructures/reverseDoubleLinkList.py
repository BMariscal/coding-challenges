
##Reverse a doubly linked list




class DoublyLinkedListNode:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


def reverse(head):
    temp = head.next
    head.next = head.prev
    head.prev = temp
    if temp == None:
        return head
    return reverse(temp)


one = DoublyLinkedListNode(1)
two = DoublyLinkedListNode(2)
three = DoublyLinkedListNode(3)
four = DoublyLinkedListNode(4)

one.next = two
two.prev = one
two.next = three

three.prev = two
three.next = four

four.prev = three


print(reverse(one))

