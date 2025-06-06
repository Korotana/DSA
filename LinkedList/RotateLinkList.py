
class Solution:

    # Function to rotate a linked list.
    def rotate(self, head, k):
        # code here

        if not head or k == 0:
            return head


        size = 1
        tail = head
        while tail.next:
            size +=1
            tail = tail.next

        k %= size
        if k == 0:
            return head

        curr = head
        for _ in range( k -1):
            curr = curr.next

        new_head = curr.next
        curr.next = None

        tail.next = head

        return new_head
