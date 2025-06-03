from Node import Node

def create_linked_list(values):
    """
       Build a linked list from a Python list.
       Returns None when `values` is empty.
    """
    if not values:  # ← guard for the empty-list case
        return None

    head = Node(values[0])
    current = head

    for val in values[1:]:
        current.next = Node(val)
        current = current.next
    return head


# Function to convert linked list back to list (for output checking)
def To_list(head):
    res = []
    while head:
        res.append(head.data)
        head = head.next
    return res

