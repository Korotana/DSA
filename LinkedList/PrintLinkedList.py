def print_linked_list(head):
    if not head:
        print("∅")
        return
    cur = head
    while cur:
        print(cur.data, end=" -> ")
        cur = cur.next
    print("None")