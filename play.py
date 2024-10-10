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

def mergeTwoLists( list1, list2):
    """
    :type list1: Optional[ListNode]
    :type list2: Optional[ListNode]
    :rtype: Optional[ListNode]
    """


    current1 = list1
    current2 = list2
    while current1.next != None and current2.next != None:
        if current1 == None:
            current1.next = current2
        elif current1.val > current2.val:
            temp = current1
            current1
            current2 = current2.next
        elif current2.val > current1.val:
            result.next = current1
            current1 = current1.next
        result = result.next

    print_linked(result)
    return result

new_link = LinkedList(3)
append(new_link,4)
append(new_link, 9)



new_link1 = LinkedList(5)
append(new_link1,6)
append(new_link1, 10)

print(mergeTwoLists(new_link, new_link1))


class Node:
    def __init__(self, data):
        self.data = data  # The value of the node
        self.next = None  # Pointer to the next node

    # Method to create a linked list from an array (this method is part of Node class)
    @staticmethod
    def create_linked_list(arr):
        if not arr:
            return None

        head = Node(arr[0])  # Create the head node
        current = head
        for item in arr[1:]:
            current.next = Node(item)  # Create and link the next node
            current = current.next
        return head  # Return the head of the newly created linked list

    # Method to reverse the linked list (this method works on a linked list)
    def reverse(self):
        previous = None
        current = self
        while current:
            next_node = current.next  # Store the next node
            current.next = previous   # Reverse the current node's pointer
            previous = current        # Move previous to this node
            current = next_node       # Move to the next node
        return previous  # Return the new head of the reversed linked list

    # Method to print the linked list
    def print_list(self):
        current = self
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

# Example usage:
if __name__ == "__main__":
    arr = [1, 2, 12, 4]  # Given array

    # Create the linked list using the create_linked_list method
    head = Node.create_linked_list(arr)

    print("Original Linked List:")
    head.print_list()

    # Reverse the linked list using the reverse method
    reversed_head = head.reverse()

    print("Reversed Linked List:")
    reversed_head.print_list()
