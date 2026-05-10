# Problem: Reverse a Linked List
# A linked list is like a chain: 1→2→3→4→5
# Reversed: 5→4→3→2→1

class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

def reverse_linked_list(head):
    prev = None
    current = head

    while current:
        next_node = current.next
        current.next = prev
        prev = current
        current = next_node

    return prev

# Build list: 1→2→3→4→5
head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
head.next.next.next = Node(4)
head.next.next.next.next = Node(5)

# Reverse it
new_head = reverse_linked_list(head)

# Print result
current = new_head
while current:
    print(current.val, end=" → ")
    current = current.next
# Output: 5 → 4 → 3 → 2 → 1 →