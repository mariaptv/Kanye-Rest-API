from wsgiref.validate import header_re

from pandas import value_counts


class LinkedList:
    def __init__(self, val = 0, next = None):
        self.val = val
        self.next = next



def append(head, value):
    if not head:
        return LinkedList(value)
    current = head
    while current.next != None:
        current = current.next

    current.next = LinkedList(value)
    return head

def print_linked(head):
    current = head
    while current != None:
        print(current.val)
        current = current.next

def delete_node(head, value):
    if head.val == value:
        head = head.next

    before = head
    current = before.next
    while current.val != None:
        if current.val == value:
            before.next = current.next
            break
        current = current.next
        before = before.next



new_link = LinkedList(3)
append(new_link,4)
append(new_link, 9)

print_linked(new_link)

delete_node(new_link,4)
print_linked(new_link)
