# Node for linked list:

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Solution:
    def addTwoLists(self, num1, num2):

        reverse_num1 = reverse_list(num1)
        reverse_num2 = reverse_list(num2)

        carry = 0
        result_head = None

        reverse_result_list = []
        while reverse_num1 or reverse_num2 or carry:
            value1 = reverse_num1.data if reverse_num1 else 0
            value2 = reverse_num2.data if reverse_num2 else 0

            total = value1 + value2 + carry

            carry = total // 10
            digit = total % 10

            new_node = Node(digit)

            if not result_head:
                result_head = new_node
                current = new_node
            else:
                current.next = new_node
                current = new_node

            if reverse_num1:
                reverse_num1 = reverse_num1.next
            if reverse_num2:
                reverse_num2 = reverse_num2.next

        result_head = reverse_list(result_head)

        while result_head and result_head.data == 0 and result_head.next:
            result_head = result_head.next

        return result_head


def reverse_list(head):
    prev = None
    current = head

    while current:
        next_node = current.next
        current.next = prev
        prev = current
        current = next_node

    return prev

