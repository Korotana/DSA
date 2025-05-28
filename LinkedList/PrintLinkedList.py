def print_linked_list(head):
    while head:
        print(head.data, end=" -> " if head.next else "") #if head.next has any value then replace newline character in the end with -> otherwise ""
        head = head.next
    print()