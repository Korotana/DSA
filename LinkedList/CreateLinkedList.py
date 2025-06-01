from Node import Node

def create_linked_list(values):
    head = Node(values[0])
    current = head

    for val in values[1:]:
        current.next = Node(val)
        current = current.next
    return head


