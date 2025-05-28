from CreateLinkedList import create_linked_list
from PrintLinkedList import print_linked_list

# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.next = None


class Solution:
    def swap_kth_node(self, head, k):

        if k == 0:
            return head

        k_head_begin_final = None

        k_head_end = head
        k_head_begin = head
        k_begin_counter = 1
        while k_head_begin.next:
            if k_begin_counter == k:
                k_head_begin_final = k_head_begin
            k_head_begin = k_head_begin.next
            k_begin_counter += 1

        if k_begin_counter < k:
            return head

        k_end_counter = 1

        if k_begin_counter == k:
            k_head_begin_final = k_head_begin

        while k_end_counter < (k_begin_counter + 1 - k):
            k_head_end = k_head_end.next
            k_end_counter += 1

        swap_holder = k_head_begin_final.data
        k_head_begin_final.data = k_head_end.data
        k_head_end.data = swap_holder

        return head

    """SOLUTION 2nd
            if k == 0 or not head:
            return False
        
        size = 0
        temp_head = head
        while temp_head:
            size += 1
            temp_head = temp_head.next
        
        if k > size or k == size - k + 1:
            return head
            
        prevX = None
        currX = head
        for _ in range(k-1):
            prevX = currX
            currX = currX.next
        
        prevY = None
        currY = head
        for _ in range(size-k):
            prevY = currY
            currY = currY.next
            
        if prevX:
            prevX.next = currY
        else:
            head = currY
            
        if prevY:
            prevY.next = currX
        else:
            head = currX        
            
        
        currX.next, currY.next = currY.next, currX.next
            
        return head
    
    """


test = create_linked_list(list(range(1, 5)))
print_linked_list(test)
print(Solution().swap_kth_node(test, 1))
print_linked_list(test)
