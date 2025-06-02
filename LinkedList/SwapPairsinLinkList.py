from LinkedList.CreateLinkedList import create_linked_list, To_list


def pairwiseSwap(head):
    # code here

    if head is None or head.next is None:
        return head

    prev = None
    current = head
    head = current.next

    while current and current.next:
        second_node = current.next
        third_node = second_node.next

        second_node.next = current
        current.next = third_node

        if prev:
            prev.next = second_node

        prev = current
        current = third_node

    return head



head = create_linked_list([1, 2, 3, 4, 5, 6, 7])
swapped = pairwiseSwap(head)
print("Test 1:", To_list(swapped))  # Expected: [2, 1, 4, 3, 6, 5, 7]

head = create_linked_list([1, 2, 3, 4, 5, 6])
swapped = pairwiseSwap(head)
print("Test 2:", To_list(swapped))  # Expected: [2, 1, 4, 3, 6, 5]

head = create_linked_list([10, 20])
swapped = pairwiseSwap(head)
print("Test 3:", To_list(swapped))  # Expected: [20, 10]


head = create_linked_list([99])
swapped = pairwiseSwap(head)
print("Test 4:", To_list(swapped))  # Expected: [99]

head = None
swapped = pairwiseSwap(head)
print("Test 5:", To_list(swapped))  # Expected: []
